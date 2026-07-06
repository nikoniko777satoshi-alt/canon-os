<!-- canon-os template (implementation-notes). Usage: copy into your project and adapt. Use the Type A
(coded task) or Type B (non-coded task) entry form; a project that needs both can mix them (tell them
apart by heading). -->
# <<Project name>> — implementation-notes

Last reviewed: <<YYYY-MM-DD>>

Operating rules (see [maintenance/deprecation-rules.md](../maintenance/deprecation-rules.md)):
- Append-only. Put new entries on top.
- Past 500 lines, add a "current-state summary" at the top and move old entries to `notes-archive/`
  (never delete the record).

## Current-state summary (latest)

<<Update this past 500 lines, or at a milestone. The skeleton of the current design and the constraints
still in force, 10 lines max>>

---

<!-- ============ Type A: coded-task entry ============ -->

## <<YYYY-MM-DD>> <<task name>>

- **Decision**: <<what you decided to build, and how>>
- **Assumptions**: <<dependencies you're relying on (environment, data, external APIs)>>
- **Trade-offs**: <<options you rejected, and why>>
- **Deviation from spec**: <<none / yes — what, why, and the handoff addendum number if one exists>>
- **Skipped scope**: <<what you didn't do or didn't check>>
- **Tests**: <<what you verified and how (command + result). State unverified work as unverified>>
- **Risks**: <<open concerns>>
- **Follow-up**: <<what to do next>>

<!-- ============ Type B: non-coded-task entry (docs, strategy, research) ============ -->

## <<YYYY-MM-DD>> <<task name>>

- **Decision and rationale**: <<what you decided, and why (data / the user's own words / a principle)>>
- **Alternatives not taken**: <<the option, and why it was rejected>>
- **Unverified assumptions**: <<assumptions you haven't confirmed>>
- **Reusable learning**: <<insight that transfers to other projects (a candidate for promotion to a
  shared knowledge note, if you keep one)>>
