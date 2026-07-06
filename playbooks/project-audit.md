# Project Audit Playbook

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

Purpose: a point-in-time audit of a single repository's governance, records, doc-vs-code drift, security,
and value. [maintenance-review.md](maintenance-review.md)'s quarterly cycle fans this out across every
active repository via a cheap-tier sub-agent. **Read-only — fixes happen only after approval.**

## Audit items

1. **Governance**: freshness of the project's agent file (CLAUDE.md/AGENTS.md) — last-reviewed date,
   expired deadlines, drift from reality — unnecessary restating of global norms, presence of a canon
   hierarchy ("read first = authoritative"), contradictions between CLAUDE.md and AGENTS.md if both exist.
2. **Records**: implementation-notes.md's rule compliance (decision / assumption / trade-off / deviation /
   skipped scope / tests / risk / follow-up), a rotation proposal if it exceeds 500 lines
   ([deprecation-rules.md](../maintenance/deprecation-rules.md)), duplication with PROGRESS.md.
3. **Doc-vs-code drift**: a table of mismatches between the spec/README's description and the actual
   implementation.
4. **Security**: the location of secrets, internal amounts, and PII (cite location only, never the value),
   client-facing vocabulary-discipline violations, leak paths into public surfaces
   ([security-floor.md](../kernel/security-floor.md) criteria).
5. **Value**: which customer transformation does this repository serve? Is there an option to stop or
   consolidate it — watch especially for overlapping or duplicate projects covering the same ground.

## Output

Findings (severity order, with evidence) + a fix-proposal list (execute only after approval) + a draft
append to [review-log.md](../maintenance/review-log.md).

## Audit prompt (copy-paste)

```
Single-repository audit. Target: <<path>>. Read-only — do not make changes.
First read <path-to-canon-os>/kernel/constitution.md and <path-to-canon-os>/INDEX.md.

Audit items:
1. Governance: freshness of CLAUDE.md/AGENTS.md (last-reviewed date, expired deadlines, drift from
   reality), unnecessary restating of global norms, presence of a canon hierarchy ("read first =
   authoritative"), contradictions between CLAUDE.md and AGENTS.md
2. Records: implementation-notes.md rule compliance (decision/assumption/trade-off/deviation/skipped/
   tests/risk/follow-up), a rotation proposal if over 500 lines, duplication with PROGRESS.md
3. Doc-vs-code drift: a table of mismatches between the spec/README and the actual implementation
4. Security: location of secrets/internal amounts/PII (location only, never the value), client-facing
   vocabulary-discipline violations, leak paths into public surfaces
5. Value: which customer transformation does this repository serve? Is there an option to stop or
   consolidate it (watch especially for overlapping or duplicate projects covering the same ground)

Output: findings (severity order, with evidence) + a fix-proposal list (execute only after approval) + a
draft append to <path-to-canon-os>/maintenance/review-log.md
```
