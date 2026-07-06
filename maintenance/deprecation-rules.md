# Deprecation Rules (update / deprecate / delete / anti-bloat)

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

Applies to: canon-os itself, and the governance/knowledge documents of every project that uses it. Run
these at the cadence set in [maintenance-review.md](../playbooks/maintenance-review.md).

## Update, deprecate, delete

- **Update**: reality is authoritative; the document follows. Frozen documents (a design handoff) don't
  get their body rewritten — record changes in the numbered addendum instead.
- **Deprecate**: a document with a successor gets a header `> DEPRECATED (date): superseded by <path>` and
  stays through the next quarterly review.
- **Delete**: byte-identical duplicates and content-free boilerplate are delete candidates. Actual deletion
  always needs owner approval.
- **Rotate**: once `implementation-notes.md` exceeds 500 lines, put a current-state summary at the top and
  move old entries to `notes-archive/` (the record is never erased).

## Anti-bloat

- Keep each kernel file under 100 lines. Adding one rule means removing one, or recording the reason for
  net growth in [review-log.md](review-log.md).
- Knowledge files require a header (source / last-reviewed date). Files without one go on the next
  review's quarantine list.
- The "last reviewed" header applies to living documents that get re-read over time — kernel, playbooks,
  checklists, maintenance ledgers (review-log, backlog), and any per-project knowledge notes or charters.
  It does **not** apply to: frozen documents (addendum-only, e.g. a design handoff), `templates/`
  (fill-in forms, not documents in force), or `decisions/` and other dated logs (where "date:" is the
  authoritative timestamp, not "last reviewed"). If a review turns up false positives against this rule,
  narrow the applicability note here rather than chasing individual files.
- A project's agent file (CLAUDE.md/AGENTS.md) targets roughly 100 lines; anything beyond that moves to
  `docs/` with a "read first" link.
- A memory or notes index holds pointers only — don't write full content into the index itself.

Related: [constitution.md](../kernel/constitution.md) Article 9 (freshness duty).
