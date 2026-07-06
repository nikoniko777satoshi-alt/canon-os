# One-shot install prompt

Paste this into any capable coding agent (Claude Code, Codex, etc.) with this repository available in the
working directory. The agent wires canon-os into the current environment by itself.

```text
You are installing canon-os into this environment. The repository is in the current directory.

Do this, and only this:
1. Read ./INDEX.md and ./INSTALL.md to learn the structure and the per-tool adapter steps.
2. Detect which tool you are running in:
   - Claude Code: copy ./behavior/operating-style.md into ~/.claude/output-styles/, tell me the exact line to
     add to settings ("outputStyle": "operating-style"), and the pointer block to append to ~/.claude/CLAUDE.md.
   - An AGENTS.md-style tool: create or append an AGENTS.md in this directory that points to ./INDEX.md as the
     entry point and names ./kernel/ as authoritative.
3. Place (or, if you cannot write outside the repo, print) the files and config exactly as INSTALL.md specifies.
4. Verify: read ./kernel/constitution.md and ./kernel/delegation-policy.md and summarize, in three lines,
   (a) the value gate (Article 6), (b) which tier this environment routes design work to, and (c) whether the
   operating style is now active for you.

Constraints:
- Wire only what already exists in this repository. Do not invent norms, examples, or content.
- Do not modify anything outside the install targets above. Back up any file you overwrite.
- If a step needs a decision only I can make (e.g. editing settings.json), print the exact change and ask.
```

After this, open a **new** session so the operating style loads, and you're running canon-os.
