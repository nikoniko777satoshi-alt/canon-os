# Project Launch Playbook

Last reviewed: 2026-07-06 / Index: [INDEX.md](../INDEX.md)

Applies to: websites, systems, contracted engagements, and new-venture launches alike.

## Phases

- **Phase 0 — Value gate**: run the [value gate](../checklists/value-gate.md) → Go/No-Go. Record the
  rationale for a No-Go too — declining is itself a form of customer selection.
- **Phase 1 — Unknown-unknowns**: run [UUDP](unknown-unknown-protocol.md) → produces the
  unknowns-register.
- **Phase 2 — Charter (one page)**: purpose (before→after) / scope / non-goals (won't-build list) / canon
  hierarchy declaration / skeleton of the acceptance-criteria × verification matrix / for contracted work,
  the contract and pricing boundary. Format: [charter.template.md](../templates/charter.template.md).
- **Phase 3 — Governance files**: from `templates/`, generate the project's agent file (≤100 lines: "read
  first (= authoritative)" / "confirmed facts" / "absolute rules" / "next action") plus
  implementation-notes.md and PROGRESS.md →
  [project-agent-file.template.md](../templates/project-agent-file.template.md) /
  [implementation-notes.template.md](../templates/implementation-notes.template.md) /
  [PROGRESS.template.md](../templates/PROGRESS.template.md).
- **Phase 4 — Design run (top tier)**: produce the design handoff — D-numbered design decisions,
  H-numbered acceptance criteria (distinguish, line by line, what's unit-verifiable from what's only
  verifiable in a real environment), a won't-build list, and a copy-paste implementation prompt. Format:
  [handoff.template.md](../templates/handoff.template.md).
- **Phase 5 — Implementation run (lower tier)**: delegate in bounded task units
  ([delegation-policy.md](../kernel/delegation-policy.md)). Test-first. Record any deviation from the
  design as a numbered addendum to the handoff. Update implementation-notes.md as you go.
- **Phase 6 — Verify / publish gate**: report the matrix split into "verified / unverified." Don't hide
  unverified items. Run the pre-publish checklist
  ([security-floor.md](../kernel/security-floor.md) §5: secrets, internal-sensitive info, PII gate,
  vocabulary discipline) before anything goes public.
- **Phase 7 — Operating cycle**: a recurring measure → agree on improvements → make the minor fix →
  confirm next period's effect loop (monthly is typical). Design human tasks and automated tasks as
  distinct from the start — an "automated" cycle often turns out to be mostly manual; verify, don't
  assume.
- **Phase 8 — After-care / graduation**: offer whatever after-care fits (training, documentation hand-off,
  monitoring, on-call) and define the graduation condition explicitly. The goal is the client's
  self-sufficiency, not lock-in.

## Emphasis by kind of project

- **Client work** → Phase 2's contract boundary is mandatory.
- **New venture** → strengthen Phase 1's regulatory-legal panel seat.
- **Internal / own product** → weight Phase 0 and Phase 7 more heavily.

Related: the launch prompt for kicking this off is in [kickoff.md](kickoff.md).
