# Delegation Policy (model / agent routing)

Last reviewed: 2026-07-17 / Index: [INDEX.md](../INDEX.md)

Principle: route each task to the cheapest capable tier and run it as a sub-agent. Keep the always-loaded
context thin; pull knowledge through the index. Model names are deliberately abstract here — map the tiers to
concrete models in [MODELS.md](../MODELS.md).

## Routing table

| Work | Tier |
|---|---|
| Unknown-unknown discovery, architecture, ruling on canon, pricing/business judgment, design handoff | **top** (+ operating-style, highest reasoning effort) |
| Bounded implementation, bug fixes, feature additions | **mid** (+ operating-style) |
| Build/lint fixes, routine tests, large file recon, enumeration, summarization | **cheap** / read-only explorer |
| Code review | specialist reviewers, in parallel |

The behavioral driving discipline ([operating-style.md](../behavior/operating-style.md)) is injected via the
host tool (see [INSTALL.md](../INSTALL.md)). A model's raw capability (first-shot correctness, long-horizon
autonomy) is not transferred by style — so back the most important judgments with the top tier plus verification.

## Asymmetric orchestration (optional, for heavy tasks)

For high-value work you can split roles across tiers: a `top` tier orchestrates and reviews, while a `mid` tier
generates and fixes. Effort annotations use `tier@effort` (see [MODELS.md](../MODELS.md)).

| Role | Tier@effort | Responsibility |
|---|---|---|
| Orchestrator (main) | `top@high` | decompose, delegate, integrate, final check |
| Worker (generation) | `mid@max` | bounded implementation, tests, recon |
| Reviewer (separate) | `top@high` | verify against explicit pass/fail criteria; prevent rubber-stamping |
| Fixer (review-driven) | `mid@xhigh` | address review findings |

Conditions (each is load-bearing):
1. The reviewer is a **separate instance and context** from the worker — ideally a different tier. Same-model
   self-review is lenient (self-preference bias). Worker=`mid`, reviewer=`top` satisfies this.
2. Give the reviewer **explicit pass/fail criteria** (e.g. the full test suite must run). Criteria-free review
   degrades into rubber-stamping.
3. Cap the review→fix loop (default `max_attempts=3`) with a fallback: escalate to the orchestrator or return
   the best attempt (operating rule 6).
4. `worker=max / fixer=xhigh` is a reasonable default, **not an empirically proven optimum** — measure and adjust.

Cost note: multi-agent runs typically consume several times the tokens of a single agent, so reserve this for
high-value tasks. Tightly-coupled work where all stages share heavy context (design + implementation + testing as
one) is often better done in a single top-tier session than fanned out.

## Operating rules

1. Two stages (design → implementation) are the default. The same (top) model may continue into implementation
   only when (a) the remaining work is bounded with settled acceptance criteria, and (b) no new design judgment
   has arisen. If a design judgment recurs mid-implementation, stop and return to the design layer.
2. Instruct sub-agents to "return a structured result." Don't have them carry back raw logs or full text.
   Prepend [subagent-preamble.md](../behavior/subagent-preamble.md) to every worker prompt (styles don't reach sub-agents).
3. Don't re-read a directory to answer a question a source map or summary already answers.
4. Design recurring / routine operations (report generation, audit fan-out) on a cheaper tier from the start.
5. One writer per file at a time. After delegating, wait — judge worker liveness by transcript activity, not
   by output files appearing. Don't touch a delegated target yourself; after an owner edit lands, re-read
   before editing. See [session-operations.md](../playbooks/session-operations.md).
6. Cap review→fix loops at `max_attempts` (default 3); if it doesn't converge, escalate to the orchestrator or
   return the best attempt. Judge pass/fail against explicit criteria and stop after two rounds with no progress.
7. When a delegation harness lets you pick the sub-agent's model, set it **explicitly** per stage — don't rely on
   inheriting the session default, or a routine fan-out may silently run every sub-agent on your most expensive tier.
8. Deleting temporary artifacts must never stall deliverable production. Scratch files and screenshots aren't
   required steps — don't delete them mid-workflow where a confirmation prompt could stall an unattended run;
   propose cleanup once, after the deliverable is reported, and leaving them in place is acceptable.

Related: [constitution.md](constitution.md) Article 7.
