# Unknown-Unknown Discovery Protocol (UUDP)

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

Run this: before submitting a quote, before signing a contract, before starting implementation, before a
major pivot. Takes 1-2 sessions. **Don't implement anything while this protocol is running.**

## Steps

0. **Input assembly**: gather the raw request, existing assets (similar repos, knowledge notes, memory),
   and known constraints in one place.
1. **Asset inventory**: search across repos and your knowledge layer (via [INDEX.md](../INDEX.md)) for
   "don't we already have something like this," and list reuse candidates. (e.g., a "new" CMS turned out
   to be a fork of two prior internal projects stitched together.)
2. **Assumption inventory**: write out every implicit assumption and classify each as
   [verified / unverified / unverifiable].
3. **Parallel panel** (parallel sub-agents, one seat per perspective. The shared question for every seat:
   "what has no document, no owner, and no number behind it?"):
   - **customer-value**: whose before→after is this? Can you state the reason to buy in the customer's
     own words?
   - **regulatory-legal**: licenses, zoning, contracts, copyright, advertising law. (e.g., in a
     physical-venue launch, a permit/zoning requirement turned out to be the single biggest unknown.)
   - **operations**: after launch, who does what, monthly? Where does manual human work remain?
     (e.g., a client's "automated" monthly cycle turned out to be executed almost entirely by hand.)
   - **revenue-pricing**: run the [value gate](../checklists/value-gate.md). Is the price backed by
     delivered value rather than cost alone? Did you backcast from the margin needed to sustain the work?
   - **tech-dependency**: external APIs, shared infrastructure, data-migration traps. Audit doc-vs-code
     drift (see [project-audit.md](project-audit.md)).
   - **exit**: what event triggers a stop? Where's the sunk-cost line? Can you slice the work into real
     options?
4. **Adversarial synthesis**: integrate the panel's findings, rule on any contradictions between seats,
   then write the three most likely failure scenarios for this plan.
5. **K-ledger**: K1..Kn (content / confidence / impact / cheapest verification / deadline). Kill the top
   three before starting, with a spike or a direct question to a stakeholder — a simple numbered question
   list works well for this.

## Output

The project's own `docs/charter/unknowns-register.md` (format: the K-ledger section of
[charter.template.md](../templates/charter.template.md)).

Related: run this as Phase 1 of [project-launch.md](project-launch.md). Delegate panel seats per
[delegation-policy.md](../kernel/delegation-policy.md).
