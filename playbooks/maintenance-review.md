# Maintenance Review (monthly / quarterly)

Last reviewed: 2026-07-07 / Index: [INDEX.md](../INDEX.md)

A periodic review that keeps the OS and its governance files aligned with reality. The **rules** for
update / deprecate / delete / anti-bloat are authoritative in
[deprecation-rules.md](../maintenance/deprecation-rules.md). Review records go in
[review-log.md](../maintenance/review-log.md).

## Cadence

### Monthly, light (~30 min)

1. Reconcile [INDEX.md](../INDEX.md) against reality (new / gone / moved files).
2. Check active projects' PROGRESS.md for freshness.
3. Build a cleanup list of expired dates and passed deadlines inside governance files.
4. Check your notes/memory location for duplication or staleness.
5. Present every change as a proposal; execute only after user approval.
6. If you run an automated knowledge-vault lint job on your scheduler/runtime (cron, launchd, CI, or an
   agent runtime), reconcile its latest report against the compiled layer's git log — a missing report is
   itself worth logging as a scheduling gap.
7. A job being alive ≠ its report existing ≠ its artifacts being produced — check all three separately.
8. Audit your raw-layer capture area's modification times for unintended rewrites.
9. If a cloud-sync service touches your local canon files, confirm it isn't silently altering or
   duplicating them.

### Quarterly, deep (in addition to monthly)

10. Fan [project-audit.md](project-audit.md) out across every active repository via a cheap-tier sub-agent
    ([delegation-policy.md](../kernel/delegation-policy.md)).
11. Re-check knowledge-layer files whose "last reviewed" is over 90 days old; reconfirm or deprecate.
12. Execute the deletion of DEPRECATED documents (after approval).
13. Propose a review of the constitution and delegation policy themselves — do they still match reality?

## Kickoff prompt (copy-paste)

```
canon-os periodic maintenance review (<<monthly | quarterly>>).
First read <path-to-canon-os>/playbooks/maintenance-review.md and follow its procedure.

Monthly: (1) reconcile INDEX.md against reality (2) check active projects' PROGRESS.md freshness
(3) build a cleanup list of expired dates in governance files (4) check your notes/memory location for
duplication or staleness (5) if you run an automated vault-lint job on your scheduler/runtime, reconcile
its latest report against the compiled layer's git log (6) audit your raw-layer capture area's
modification times (7) confirm no cloud-sync service is silently altering your canon files
Quarterly: add (8) fan project-audit.md out across every active repository via a cheap-tier sub-agent
(9) execute approved deletions of DEPRECATED documents (10) propose whether the constitution and
delegation policy still match reality

Output: a list of proposed changes (all pending my approval) + an append to
<path-to-canon-os>/maintenance/review-log.md. Do not change any file without approval. State the next
review date when done.
```

Related: [constitution.md](../kernel/constitution.md) Article 9 (freshness duty).
