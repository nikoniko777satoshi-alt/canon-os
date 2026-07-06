<!-- canon-os template (design handoff). Usage: the top-tier agent creates this at project-launch.md
Phase 4. Once created, the body is frozen — record changes only in the numbered addendum at the end.
This is the design→implementation handoff pattern (see README.md's thesis on structure over raw
intelligence). -->
# <<Project name>> — Design Handoff v<<X.Y>>

- Created: <<YYYY-MM-DD>> / <<design tier — see MODELS.md>>
- Status: **proposed (awaiting user approval)** <<once approved, update to "approved (YYYY-MM-DD)">>
- Implementer: <<implementation tier/agent, per kernel/delegation-policy.md>>
- Update rule: the body is frozen. Changes go in the numbered addendum at the end.

## 0. Canon hierarchy

1. <<the top authority for this project, e.g. this handoff>>
2. <<next in line, e.g. the project's agent file>>

If you find a contradiction, don't silently fix it — report it and ask for a ruling.

## 1. Purpose (before→after)

<<Whose state changes, and how. One sentence plus detail>>

## 2. Design decisions (D-numbered)

| # | Decision | Rationale | Alternatives considered and why rejected |
|---|---|---|---|
| D1 | <<what was decided>> | <<why>> | <<alternative — why not>> |

## 3. Acceptance criteria × verification matrix (H-numbered)

| # | Criterion | Verification | Coverage |
|---|---|---|---|
| H1 | <<condition to satisfy>> | <<command / procedure>> | <<unit-verifiable / only verifiable in a real environment>> |

When reporting implementation complete, split every H into "verified (with real output)" or "unverified."
Never hide an unverified one.

## 4. Won't-build list (non-goals)

- <<what you won't build this round, and why (a seawall against scope creep)>>

## 5. Copy-paste implementation prompt

```
<<the prompt to hand the implementing agent. Include the path to this file as canon, the task list,
verification steps, and prohibitions.>>
```

## 6. Assumptions, unverified items, known limits

1. <<assumptions not yet confirmed at design time, or material you haven't read>>

## 7. Addendum (numbered, append-only)

<!-- format: A1: YYYY-MM-DD <what changed and why>. Never rewrite the body. -->
(none yet)
