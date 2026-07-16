# Self-maintenance loop

Last reviewed: 2026-07-17 / Index: [../INDEX.md](../INDEX.md)

Keep the knowledge tree honest over time with two light jobs. Neither needs any particular scheduler — a plain
prompt you run by hand is enough, so this never breaks canon-os's one-command install. Wire a scheduler only if
you want the jobs to fire on their own.

## The two jobs

1. **Weekly lint** — [../maintenance/vault-lint.py](../maintenance/vault-lint.py). Read-only, standard library +
   git only, no LLM. Reports broken relative Markdown links, files whose freshness marker is stale/missing, and
   (optionally) raw-vault-vs-tree drift. Run it against your tree:

   ```
   python3 maintenance/vault-lint.py --root . --out-dir maintenance
   ```

   Flags: `--root` (tree to scan), `--vault-dir` (optional raw store to compare), `--out-dir`, `--stale-days`
   (default 90), `--marker` (regex whose group 1 is an ISO date; default `Last reviewed:\s*(\d{4}-\d{2}-\d{2})`),
   `--exclude` (path prefixes exempt from the marker check; default `templates/ decisions/`).

2. **Monthly review** — an LLM read-only pass over the tree using the kickoff prompt in
   [maintenance-review.md](maintenance-review.md). It proposes changes (for your approval) and writes a dated
   report; it must not modify the tree itself.

## Wiring options (pick one — or none)

The jobs are just "run a script" and "run a prompt," so any runner works. Adapt paths to your setup.

- **Manual (always works, the baseline).** Run the lint command above when you think of it, and paste the
  monthly kickoff prompt from [maintenance-review.md](maintenance-review.md) into your agent. No scheduler, no
  daemon. This alone satisfies the loop.
- **cron (Linux/macOS).** `45 8 * * 1 cd /path/to/tree && python3 maintenance/vault-lint.py --root .`
- **launchd (macOS).** A `StartCalendarInterval` LaunchAgent whose `ProgramArguments` are
  `[/usr/bin/python3, /path/to/maintenance/vault-lint.py, --root, /path/to/tree]`. launchd catches up on a
  missed fire after sleep, which plain cron does not.
- **systemd timer (Linux).** A `.timer` (`OnCalendar=Mon *-*-* 08:45`) plus a `.service` running the same command.
- **GitHub Actions.** A `schedule:` workflow — only if the tree lives in the repo being checked out; the runner
  has no access to your local filesystem otherwise.
- **Agent-runtime cron.** If you already run an agent framework with a scheduler, register the monthly review as
  a job there.

For the monthly review under a headless runner, invoke your agent in one-shot mode with a **restricted, read-only
tool policy** (allow file reads + the report-output path; deny writes to the tree) so an unattended run can't edit
the tree or stall on a permission prompt. If it can't be made non-interactive, fall back to the manual kickoff.

- Interactive-auth MCP servers and other external connectors become unreachable under a headless runner, and the
  agent can stall indefinitely waiting on the connection (observed in practice: normal progress partway through,
  then a permanent wedge at 0% CPU). Disable them at headless startup (for example, in Claude Code:
  `--strict-mcp-config`).
- A watchdog's SIGTERM can be ignored, so escalate to SIGKILL after a grace period rather than relying on a
  single signal.
- If it still doesn't stabilize, fall back to notify-only: the scheduler only sends a notification, and the
  actual review runs in an interactive session.

## Notes

- Point the monthly review's step that reconciles "weekly report vs. tree commits" at wherever the lint writes.
- A job that fires but produces nothing still tells you it's alive — have the lint emit a one-line report even
  when it finds nothing, so a *missing* report is itself the alarm.
- Related: [maintenance-review.md](maintenance-review.md) (the review procedure) and
  [../kernel/delegation-policy.md](../kernel/delegation-policy.md) (route the monthly review to a cheap tier).
