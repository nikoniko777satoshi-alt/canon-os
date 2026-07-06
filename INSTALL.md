# Install

Three ways in. The first two are one-shot; the third is manual.

## A. One command

```sh
git clone <this-repo> canon-os && cd canon-os && ./install.sh
```

`install.sh` places the knowledge tree at `~/.canon-os/` and **prints** the host-config changes (safe to run
anywhere — it doesn't modify your settings by default). Re-run with `--write` to install the style file and
append the `CLAUDE.md` pointer automatically (backed up first). The one line for `settings.json` is printed for
you to add — JSON isn't auto-edited, to avoid clobbering your settings.

```sh
./install.sh --target both --write     # apply to Claude Code + AGENTS.md tools
./install.sh --target claude           # print Claude Code changes only
./install.sh --dest ~/my-vault         # place the tree elsewhere
```

## B. One prompt (via an agent)

Paste [INSTALL_PROMPT.md](INSTALL_PROMPT.md) into a coding agent with this repo in the working directory. It
wires itself in. Good when you'd rather have the agent do it than run a shell script.

## C. Manual

### Claude Code

1. Copy `behavior/operating-style.md` → `~/.claude/output-styles/operating-style.md`.
2. In `~/.claude/settings.json`, set `"outputStyle": "operating-style"`.
3. Append a pointer to `~/.claude/CLAUDE.md`:
   ```markdown
   ## canon-os
   Norms and playbooks start at `~/.canon-os/INDEX.md`. The kernel (`~/.canon-os/kernel/`) is authoritative.
   Read the index, then only the notes a task needs.
   ```
4. Start a **new** session (output styles load at session start).

### AGENTS.md-style tools (Codex, etc.)

1. Place the knowledge tree somewhere stable (e.g. `~/.canon-os/`).
2. Add an `AGENTS.md` in your project (or `~`) whose content points to `INDEX.md` as the entry point and names
   `kernel/` as authoritative. See `AGENTS.md` in this repo for the exact shape.
3. When delegating to a sub-task, prepend `behavior/subagent-preamble.md` (styles don't reach sub-agents).

## Map the model tiers

Edit [MODELS.md](MODELS.md) to map `top` / `mid` / `cheap` to the models you actually use.

## Verify

Open a new session and ask the agent to summarize `kernel/constitution.md` back. If it leads with the
conclusion, states uncertainty explicitly, and stays in scope, the operating style is active.
