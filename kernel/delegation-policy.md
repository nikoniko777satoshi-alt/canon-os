# Delegation Policy (model / agent routing)

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

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

## Operating rules

1. Two stages (design → implementation) are the default. The same (top) model may continue into implementation
   only when (a) the remaining work is bounded with settled acceptance criteria, and (b) no new design judgment
   has arisen. If a design judgment recurs mid-implementation, stop and return to the design layer.
2. Instruct sub-agents to "return a structured result." Don't have them carry back raw logs or full text.
   Prepend [subagent-preamble.md](../behavior/subagent-preamble.md) to every worker prompt (styles don't reach sub-agents).
3. Don't re-read a directory to answer a question a source map or summary already answers.
4. Design recurring / routine operations (report generation, audit fan-out) on a cheaper tier from the start.

Related: [constitution.md](constitution.md) Article 7.
