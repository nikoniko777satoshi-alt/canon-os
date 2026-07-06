# Agent entry point (canon-os)

Read [INDEX.md](INDEX.md) first. The kernel ([kernel/](kernel/)) is authoritative — constitution, delegation
policy, security floor, vault policy. Read the index, then only the notes a task needs; don't sweep the whole
tree.

When you delegate to a sub-task, prepend [behavior/subagent-preamble.md](behavior/subagent-preamble.md) to the
worker's prompt (an output style does not reach sub-agents).

When a document contradicts another, don't silently resolve it — flag it and ask for a ruling (constitution
Article 8).

This file is the entry point for AGENTS.md-style tools (Codex and similar). For Claude Code, the same role is
played by a pointer in `~/.claude/CLAUDE.md` — see [INSTALL.md](INSTALL.md).
