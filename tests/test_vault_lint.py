"""Tests for maintenance/vault-lint.py (stdlib unittest; run: python3 -m unittest discover tests)."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

LINT = Path(__file__).resolve().parent.parent / "maintenance" / "vault-lint.py"


def run_lint(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(LINT), "--root", str(root), "--out-dir", str(root / "out"), *extra],
        capture_output=True, text=True,
    )


class VaultLintTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "ok.md").write_text("Last reviewed: 2999-01-01\n", encoding="utf-8")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def write(self, name: str, body: str) -> None:
        (self.root / name).write_text("Last reviewed: 2999-01-01\n\n" + body, encoding="utf-8")

    def test_valid_links_pass(self) -> None:
        self.write("a.md", "[ok](ok.md) [anchor](ok.md#x) [title](ok.md \"t\") [angle](<ok.md>) [web](https://e.x)\n")
        res = run_lint(self.root, "--fail-on-broken")
        self.assertEqual(res.returncode, 0, res.stdout)
        self.assertIn("broken_links=0 ", res.stdout)

    def test_broken_link_is_reported_and_fails_when_asked(self) -> None:
        self.write("a.md", "[gone](missing.md)\n")
        self.assertEqual(run_lint(self.root).returncode, 0)  # default: report only
        res = run_lint(self.root, "--fail-on-broken")
        self.assertEqual(res.returncode, 1)
        self.assertIn("missing.md", res.stdout)

    def test_links_inside_code_are_ignored(self) -> None:
        self.write("a.md", "Use `[x](nope.md)` inline.\n\n```\n[y](nope.md)\n```\n\n~~~md\n[z](nope.md)\n~~~\n")
        res = run_lint(self.root, "--fail-on-broken")
        self.assertEqual(res.returncode, 0, res.stdout)

    def test_stale_and_missing_markers(self) -> None:
        (self.root / "old.md").write_text("Last reviewed: 2000-01-01\n", encoding="utf-8")
        (self.root / "none.md").write_text("# no marker\n", encoding="utf-8")
        res = run_lint(self.root)
        self.assertIn("stale=1 ", res.stdout)
        self.assertIn("missing_marker=1 ", res.stdout)

    def test_not_a_git_repo_is_reported_not_crashed(self) -> None:
        res = run_lint(self.root)
        self.assertEqual(res.returncode, 0)
        self.assertIn("commits_7d=not-a-git-repo", res.stdout)


if __name__ == "__main__":
    unittest.main()
