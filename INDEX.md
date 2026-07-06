# canon-os — INDEX

Last reviewed: 2026-07-06

canon-os is a thin kernel plus indexed playbooks, so any agent — any model, any tool — works from the same
norms, behavior, and templates. Always-loaded: `kernel/` only. Everything else is read on demand, through
this index — never by sweeping a whole directory (Constitution Article 7).

See [README.md](README.md) for the thesis, and [INSTALL.md](INSTALL.md) to wire this into your tool.

## Canon hierarchy

1. Your host tool's own built-in norms (e.g. a coding agent's system instructions) — highest.
2. This project's constitution ([kernel/constitution.md](kernel/constitution.md)) — extends, never
   replaces, #1.
3. The rest of `kernel/` — authoritative for day-to-day reference once installed.
4. Each project's own agent file (CLAUDE.md / AGENTS.md) — authoritative for that project's specifics.

Whoever finds a contradiction between documents doesn't silently fix it — they report it and ask for a
ruling (Constitution Article 8).

## kernel (always loaded — 100 lines each, max)

| File | Contents |
|---|---|
| [kernel/constitution.md](kernel/constitution.md) | Ten-article agent constitution (5 engineering-discipline + 5 OS extensions) |
| [kernel/delegation-policy.md](kernel/delegation-policy.md) | Model-tier routing table + design→implementation continuation rule |
| [kernel/security-floor.md](kernel/security-floor.md) | Secrets / internal-sensitive / PII / vocabulary floor + pre-publish checklist |
| [kernel/vault-policy.md](kernel/vault-policy.md) | Knowledge-vault discipline (raw/compiled layers, 4 writing rules, source-receipts, frozen entities) |

## behavior

| File | Contents |
|---|---|
| [behavior/operating-style.md](behavior/operating-style.md) | The driving discipline (conclusion-first, act, verify, re-land) — install as your tool's output style |
| [behavior/subagent-preamble.md](behavior/subagent-preamble.md) | Copy-paste block that injects the style into sub-agents (styles don't reach them) |

## playbooks

| File | When to use |
|---|---|
| [playbooks/project-launch.md](playbooks/project-launch.md) | A new project's Phase 0-8 (the common launch procedure) |
| [playbooks/unknown-unknown-protocol.md](playbooks/unknown-unknown-protocol.md) | Before quoting, before contract, before starting, before a major pivot (UUDP) |
| [playbooks/kickoff.md](playbooks/kickoff.md) | Starting a new project so a mid-tier model reproduces top-tier behavior (copy-paste kickoff prompt) |
| [playbooks/project-audit.md](playbooks/project-audit.md) | A point-in-time audit of a single repository (copy-paste audit prompt) |
| [playbooks/maintenance-review.md](playbooks/maintenance-review.md) | Monthly-light / quarterly-deep self-maintenance |

## checklists

| File | When to use |
|---|---|
| [checklists/value-gate.md](checklists/value-gate.md) | Phase 0's Go/No-Go call (the value gate) |

## templates (copy into a new project)

| File | Purpose |
|---|---|
| [templates/project-agent-file.template.md](templates/project-agent-file.template.md) | A project's agent file (CLAUDE.md / AGENTS.md), ≤100 lines |
| [templates/implementation-notes.template.md](templates/implementation-notes.template.md) | Implementation records (coded-task / non-coded-task entry forms) |
| [templates/PROGRESS.template.md](templates/PROGRESS.template.md) | Progress file (current phase / recently completed / next session) |
| [templates/handoff.template.md](templates/handoff.template.md) | Design handoff (D-numbered decisions / H-numbered matrix / won't-build list / addendum) |
| [templates/charter.template.md](templates/charter.template.md) | One-page charter + unknowns-register (K-ledger) |
| [templates/decision.template.md](templates/decision.template.md) | Decision-log entry (4-field lightweight form — vault-policy.md §6) |

## maintenance

| File | Contents |
|---|---|
| [maintenance/deprecation-rules.md](maintenance/deprecation-rules.md) | Update / deprecate / delete / anti-bloat rules |
| [maintenance/review-log.md](maintenance/review-log.md) | Maintenance-review record (starter, with one illustrative entry) |
| [maintenance/backlog.md](maintenance/backlog.md) | Single ledger for open tasks (starter, with one illustrative example per section) |
| [maintenance/decisions/](maintenance/decisions/) | One-decision-per-page log (starter, with one illustrative example) |

## How to read this

Start at this index, follow only the links a task actually needs, and fall back to a targeted search
(grep, symbol search) if you still need something specific. Never sweep an entire directory tree to answer
a question this index — or a file it links to — already answers.
