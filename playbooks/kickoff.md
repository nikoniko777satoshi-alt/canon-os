# Kickoff Playbook

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

Prerequisite: canon-os is installed (see [INSTALL.md](../INSTALL.md)).

**The reproduction principle**: a mid-tier model reproduces top-tier *behavior* not through raw
intelligence, but through structure — parallel multi-perspective panels, adversarial synthesis,
canonization, and delegation.

## Steps

1. Create the project directory and start your coding agent on the **top** tier (see
   [MODELS.md](../MODELS.md) for the tier mapping), at the highest reasoning effort available. Confirm the
   [operating style](../behavior/operating-style.md) is active (see [INSTALL.md](../INSTALL.md)'s verify
   step) — it only takes effect from a new session.
2. Paste the kickoff prompt below, swapping in one paragraph describing the project.
3. The agent reads INDEX.md → kernel → playbooks, in that order, and runs Phases 0-3. It runs the UUDP
   multi-perspective panel as parallel sub-agents, and does the adversarial synthesis itself.
4. Once you approve the charter and governance files, the top tier continues into the Phase 4 design
   handoff.
5. Implementation goes to a lower tier per [delegation-policy.md](../kernel/delegation-policy.md); the top
   tier shifts to ruling and review-integration.
6. At close: update the project's own implementation-notes.md and PROGRESS.md. (canon-os itself keeps no
   registry of the projects that use it — that bookkeeping is yours to keep, wherever you track your own
   work.)

Starting from a different tool or agent runtime works the same way: whatever agent you begin with, open
with "read INDEX.md and kernel/ first," and it connects to the same canon.

## Kickoff prompt (copy-paste)

```
Launching a new project. You are the top-tier agent (see MODELS.md for the tier mapping). Follow canon-os.

Read first (in this order — nothing else before these):
1. <path-to-canon-os>/INDEX.md
2. <path-to-canon-os>/kernel/constitution.md and delegation-policy.md
3. <path-to-canon-os>/playbooks/project-launch.md and unknown-unknown-protocol.md
4. <path-to-canon-os>/checklists/value-gate.md

Project brief: <<one paragraph: what, for whom, by when, client work or own venture, budget/pricing sense>>

How to proceed:
- Start from Playbook Phase 0 (the value gate). Ask me anything you can't answer yourself.
- Phase 1 (UUDP): run the multi-perspective panel (customer-value / regulatory-legal / operations /
  revenue-pricing / tech-dependency / exit) as parallel sub-agents, then synthesize adversarially
  yourself into a K-ledger.
- Phase 2-3: produce a one-page charter and the governance files (use templates/) and get my approval.
- Don't write implementation code yet. Implementation starts only after the design handoff is approved,
  and goes to a lower tier per delegation-policy.md.
- Read knowledge and context through an index; never sweep a whole directory.
```

Related: [project-launch.md](project-launch.md) for phase detail.
