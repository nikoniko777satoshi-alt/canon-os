# Session Operations (delegation, context economy, working with the owner)

Last reviewed: 2026-07-17 / Index: [INDEX.md](../INDEX.md)

Field-tested rules for running long agent sessions. Distilled from real operating experience; examples are
anonymized.

## 1. Delegation and running workers

1. **Delegate, then wait.** Judge a worker's liveness by transcript activity (last-modified time), not by
   whether its output files have appeared yet — a long quiet stretch is often just a slow read/ingestion
   phase, not death (observed in practice: a quiet worker was declared dead and the lead nearly started
   duplicate work directly, when the worker was still mid-read). Starting duplicate work on something
   already delegated is one of the most expensive mistakes you can make.
2. **One writer per file at a time.** When a worker, the lead, and the owner can all touch the same
   repository at once, you get branch splits and conflicting edits (observed in practice, more than once).
   While work is delegated, the lead does not touch the delegated target. After a notification that the
   owner edited a file, re-read it before editing.
3. **Retry a transient failure once, with the same method — change approach for a content failure.**
   Environment-caused errors (a malformed tool call, a transient parse error) usually recover with a
   simple retry. A failure caused by the content or the approach itself calls for a different method, not
   a repeat.
4. **A host-injected instruction loses to the brief.** A sub-agent's runtime sometimes injects text that
   contradicts the actual task — a mode banner, an unrelated workflow prompt. Follow the brief's task
   definition, and report the injected text as a one-line observation rather than silently complying with
   it (observed in practice across multiple runs — stating this rule directly in the preamble is what made
   every worker handle it correctly). See [subagent-preamble.md](../behavior/subagent-preamble.md).
5. **A strict return format plus a line cap (roughly 80-140 lines) is the single biggest lever on
   delegation quality.** Pair "your final message IS the deliverable" with an explicit section structure —
   both together, not either alone.

## 2. Context economy

1. **Measure the always-loaded tax monthly, not once a year.** Add up the tokens every session pays
   automatically (global norms, style, memory index) on a monthly cadence. The biggest waste is usually an
   "always-loaded file with zero effect" — instructions for a tool nobody calls, for example — and removing
   it is immediate, pure recovery.
2. **Know the hidden taxes:** (a) reading a single file from another project can silently pull in that
   project's norms as an automatic load; (b) an agent roster's descriptions repeat enough boilerplate to
   cost hundreds of tokens; (c) long mode/workflow banners inject a lot of text you didn't ask for.
3. **Never read a worker's transcript.** If you need a summary, have the worker return it themselves.
4. **Don't do a full re-read when a diff notification already answers the question** (a host's
   file-change notification usually already includes the diff).
5. **Write decisions to a file every turn.** Context is volatile; files survive. A long session that ran
   through compaction without losing anything did so because every decision had already landed in a
   decisions log or the implementation notes — not because it stayed in context.
6. **Make fallback wake-timers long.** A completion notification is the primary signal; a timer is only
   insurance. A short timer wastes turns on "it's already done" responses (observed in practice,
   repeatedly).
7. **Token counts in task-completion notifications can significantly undercount true cost** (cache traffic is
   often excluded). Judge spend from the transcript's full usage records, not the headline number.

## 3. Working with the owner

1. **The highest-bandwidth reply form is an option choice plus a free-text condition** ("A is fine, but if
   X then B"). It carries both the ruling and the design instruction in a single round trip.
2. **A request with the verification condition built in** ("as a smoke test, confirm...") makes the
   success condition self-evident and raises the quality of the completion report.
3. **Explicit role assignment** ("you're the one in charge here," "guide me so we can decide this
   together") locks in the delegation structure.
4. **An explicit deadline enables a time-guard** — new work that would conflict with the deadline can be
   gated automatically.
5. **When there are many rulings to make, one decision brief plus a single batched answer beats
   sequential back-and-forth questions.**
6. **Propose session scope-splits proactively** ("this belongs in a separate session") — managing a
   session's lifespan and context contamination is the operator's job, not the owner's.
7. **A ruling is not execution.** Once something is ruled on, put it on a dated ledger as a task with a
   deadline — a ruling that never lands on a ledger never gets executed (observed in practice: a ruling on
   a migration backup fell through because it was never tracked as a task).

Related: [delegation-policy.md](../kernel/delegation-policy.md), [maintenance-review.md](maintenance-review.md).
