#!/usr/bin/env python3
"""Portable vault lint for a canon-os knowledge tree.

Read-only. Scans a Markdown knowledge tree and writes one report. No agent, no
network, standard library + git only — so it runs the same under cron, launchd,
a systemd timer, CI, or an agent runtime (see playbooks/self-maintenance-loop.md).

Checks:
  1. Broken relative Markdown links.
  2. Files whose freshness marker (default ``Last reviewed:``) is stale or missing.
  3. (optional) Recent activity in a separate raw vault vs. commits in the tree,
     to catch "raw grew but compiled did not" drift.

Everything is a CLI flag; there are no hardcoded paths or project-specific rules.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FILENAME_DATE_RE = re.compile(r"(20\d{2}-\d{2}-\d{2})")


@dataclass(frozen=True)
class Config:
    root: Path
    vault_dir: Path | None
    out_dir: Path
    stale_days: int
    marker_re: re.Pattern[str]
    exclude_prefixes: tuple[str, ...]
    today: dt.date
    now: dt.datetime

    @property
    def since(self) -> dt.datetime:
        return self.now - dt.timedelta(days=7)


def check_links(cfg: Config) -> list[str]:
    broken: list[str] = []
    for md in sorted(cfg.root.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in MD_LINK_RE.finditer(text):
            target = m.group(1).strip()
            if not target or target.startswith(("#", "~", "/")) or "://" in target or target.startswith("mailto:"):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            if not (md.parent / path_part).resolve().exists():
                rel = md.relative_to(cfg.root).as_posix()
                broken.append(f"- `{rel}` -> `{target}`")
    return broken


def is_excluded(md: Path, cfg: Config) -> bool:
    rel = md.relative_to(cfg.root).as_posix()
    return any(rel.startswith(p) for p in cfg.exclude_prefixes)


def stale_markers(cfg: Config) -> tuple[list[str], list[str]]:
    stale: list[str] = []
    missing: list[str] = []
    cutoff = cfg.today - dt.timedelta(days=cfg.stale_days)
    for md in sorted(cfg.root.rglob("*.md")):
        if is_excluded(md, cfg):
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        m = cfg.marker_re.search(text[:1000])
        rel = md.relative_to(cfg.root).as_posix()
        if not m:
            missing.append(f"- `{rel}`")
            continue
        try:
            d = dt.date.fromisoformat(m.group(1))
        except (ValueError, IndexError):
            missing.append(f"- `{rel}` (invalid date)")
            continue
        if d < cutoff:
            stale.append(f"- `{rel}` — {d} ({(cfg.today - d).days} days ago)")
    return stale, missing


def recent_vault_changes(cfg: Config) -> tuple[int, list[str]]:
    if cfg.vault_dir is None or not cfg.vault_dir.exists():
        return 0, []
    updated = 0
    examples: list[str] = []
    for p in cfg.vault_dir.rglob("*.md"):
        try:
            mtime = dt.datetime.fromtimestamp(p.stat().st_mtime)
        except FileNotFoundError:
            continue
        if mtime >= cfg.since:
            updated += 1
            if len(examples) < 20:
                examples.append(f"- `{p.name}` — mtime {mtime:%Y-%m-%d %H:%M}")
    return updated, examples


def git_commit_count(cfg: Config) -> tuple[str, str]:
    if not (cfg.root / ".git").exists():
        return "not-a-git-repo", f"`{cfg.root}` is not a git repository; commit count unavailable."
    try:
        out = subprocess.check_output(
            ["git", "-C", str(cfg.root), "rev-list", "--count", "--since=7 days ago", "HEAD"],
            text=True, stderr=subprocess.STDOUT, timeout=20,
        ).strip()
        return out or "0", ""
    except Exception as e:  # noqa: BLE001 - report any git failure, don't crash the lint
        return "error", f"git commit count failed: {type(e).__name__}: {e}"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Portable read-only lint for a canon-os knowledge tree.")
    p.add_argument("--root", type=Path, default=Path.cwd(),
                   help="Knowledge tree to scan (read-only). Default: current directory.")
    p.add_argument("--vault-dir", type=Path, default=None,
                   help="Optional separate raw vault to check for recent activity / drift.")
    p.add_argument("--out-dir", type=Path, default=None,
                   help="Report output directory. Default: <root>/maintenance.")
    p.add_argument("--stale-days", type=int, default=90,
                   help="Age threshold in days for a stale freshness marker. Default: 90.")
    p.add_argument("--marker", default=r"Last reviewed:\s*(\d{4}-\d{2}-\d{2})",
                   help=r"Regex for the freshness marker; group 1 is an ISO date. "
                        r"Default: 'Last reviewed:\s*(\d{4}-\d{2}-\d{2})'.")
    p.add_argument("--exclude", nargs="*", default=["templates/", "decisions/"],
                   help="Path prefixes (relative to root) exempt from marker checks. "
                        "Default: templates/ decisions/.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    now = dt.datetime.now()
    root = args.root.expanduser().resolve()
    cfg = Config(
        root=root,
        vault_dir=args.vault_dir.expanduser() if args.vault_dir else None,
        out_dir=(args.out_dir.expanduser() if args.out_dir else root / "maintenance"),
        stale_days=args.stale_days,
        marker_re=re.compile(args.marker),
        exclude_prefixes=tuple(args.exclude),
        today=now.date(),
        now=now,
    )
    cfg.out_dir.mkdir(parents=True, exist_ok=True)

    broken = check_links(cfg)
    stale, missing = stale_markers(cfg)
    vault_updated, vault_examples = recent_vault_changes(cfg)
    commit_count, git_note = git_commit_count(cfg)

    warnings: list[str] = []
    if cfg.vault_dir is not None and vault_updated > 0 and commit_count in {"0", "not-a-git-repo", "error"}:
        warnings.append("raw vault changed in the last 7 days, but tree commit activity is zero/unmeasurable")

    report = cfg.out_dir / f"vault-lint-{cfg.today.isoformat()}.md"
    lines = [
        f"# Vault lint — {cfg.today.isoformat()}",
        "",
        f"- Generated: {cfg.now:%Y-%m-%d %H:%M:%S}",
        f"- Root: `{cfg.root}`",
        "- Mode: read-only; report-only output",
        "",
        "## Summary",
        "",
        f"- Broken relative Markdown links: {len(broken)}",
        f"- Files with a marker older than {cfg.stale_days} days: {len(stale)}",
        f"- Files missing/invalid the freshness marker: {len(missing)}",
        f"- Tree git commits in last 7 days: {commit_count}",
    ]
    if cfg.vault_dir is not None:
        lines.append(f"- Raw vault `.md` files touched in last 7 days: {vault_updated}")
    if git_note:
        lines.append(f"- Git note: {git_note}")
    if warnings:
        lines += ["", "## Early warnings", ""] + [f"- {w}" for w in warnings]
    lines += ["", "## Broken relative Markdown links", ""] + (broken or ["- None"])
    lines += ["", f"## Marker older than {cfg.stale_days} days", ""] + (stale or ["- None"])
    lines += ["", "## Missing/invalid freshness marker", ""] + (missing or ["- None"])
    if cfg.vault_dir is not None:
        lines += ["", "## Recent raw vault changes (first 20)", ""] + (vault_examples or ["- None"])
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"vault lint wrote {report}")
    print(
        f"broken_links={len(broken)} stale={len(stale)} missing_marker={len(missing)} "
        f"commits_7d={commit_count} vault_updated_7d={vault_updated}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
