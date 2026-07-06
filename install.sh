#!/bin/sh
# canon-os installer — one command to set up the environment.
# POSIX sh, no dependencies. Non-destructive by default (prints changes; --write applies them).
#
# Usage:
#   ./install.sh [--target claude|agents|both] [--dest DIR] [--write]
#
#   --target  claude = Claude Code (output style + settings pointer)
#             agents = AGENTS.md-style tools (Codex, etc.): drop an AGENTS.md entry point
#             both   = do both (default)
#   --dest    where to place the canon-os knowledge tree (default: $HOME/.canon-os)
#   --write   install the style file and append the CLAUDE.md pointer (backed up first). The one line for
#             settings.json is printed, not auto-edited (JSON isn't safely editable in POSIX sh). Without
#             --write, all changes are printed only.

set -eu

SRC="$(cd "$(dirname "$0")" && pwd)"
TARGET="both"
DEST="${HOME}/.canon-os"
WRITE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --dest)   DEST="$2"; shift 2 ;;
    --write)  WRITE=1; shift ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

say() { printf '%s\n' "$*"; }
hr()  { printf '%s\n' "----------------------------------------------------------------"; }

# 1. Place the knowledge tree (idempotent copy).
say "canon-os: placing knowledge tree at ${DEST}"
mkdir -p "${DEST}"
for d in kernel behavior playbooks checklists templates maintenance; do
  [ -d "${SRC}/${d}" ] && cp -R "${SRC}/${d}" "${DEST}/"
done
for f in INDEX.md MODELS.md README.md; do
  [ -f "${SRC}/${f}" ] && cp "${SRC}/${f}" "${DEST}/"
done
say "  done."

install_claude() {
  hr; say "Claude Code adapter"
  STYLE_DIR="${HOME}/.claude/output-styles"
  STYLE_SRC="${SRC}/behavior/operating-style.md"
  SETTINGS="${HOME}/.claude/settings.json"
  POINTER="## canon-os

Norms, playbooks and knowledge for this environment start at \`${DEST}/INDEX.md\`.
The kernel (\`${DEST}/kernel/\`) is authoritative. Read the index, then only the notes a task needs."

  if [ "${WRITE}" = "1" ]; then
    mkdir -p "${STYLE_DIR}"
    cp "${STYLE_SRC}" "${STYLE_DIR}/operating-style.md"
    say "  installed output style -> ${STYLE_DIR}/operating-style.md"
    CLAUDE_MD="${HOME}/.claude/CLAUDE.md"
    [ -f "${CLAUDE_MD}" ] && cp "${CLAUDE_MD}" "${CLAUDE_MD}.bak.$(date +%Y%m%d%H%M%S)"
    printf '\n%s\n' "${POINTER}" >> "${CLAUDE_MD}"
    say "  appended canon-os pointer -> ${CLAUDE_MD} (backup kept if it existed)"
    say "  ACTION NEEDED: set \"outputStyle\": \"operating-style\" in ${SETTINGS}"
    say "                 (JSON is not auto-edited, to avoid clobbering your settings)"
  else
    say "  would install output style -> ${STYLE_DIR}/operating-style.md"
    say "  then set in ${SETTINGS}:"
    say "      \"outputStyle\": \"operating-style\""
    say "  and append to ${HOME}/.claude/CLAUDE.md:"
  fi
  say ""
  printf '%s\n' "${POINTER}"
  say ""
  say "  (Changes take effect in a NEW Claude Code session.)"
}

install_agents() {
  hr; say "AGENTS.md adapter"
  AGENTS_FILE="${PWD}/AGENTS.md"
  POINTER="# Agent entry point (canon-os)

Read \`${DEST}/INDEX.md\` first. The kernel (\`${DEST}/kernel/\`) is authoritative.
Read the index, then only the notes a task needs — don't sweep the whole tree.
When delegating to a sub-task, prepend \`${DEST}/behavior/subagent-preamble.md\`."

  if [ "${WRITE}" = "1" ]; then
    if [ -f "${AGENTS_FILE}" ]; then
      cp "${AGENTS_FILE}" "${AGENTS_FILE}.bak.$(date +%Y%m%d%H%M%S)"
      say "  existing AGENTS.md backed up."
    fi
    printf '%s\n' "${POINTER}" >> "${AGENTS_FILE}"
    say "  wrote ${AGENTS_FILE}"
  else
    say "  would write ${AGENTS_FILE}:"
    say ""
    printf '%s\n' "${POINTER}"
  fi
}

case "${TARGET}" in
  claude) install_claude ;;
  agents) install_agents ;;
  both)   install_claude; install_agents ;;
  *) echo "unknown target: ${TARGET}" >&2; exit 2 ;;
esac

hr
say "canon-os installed. Next: open a new session and confirm the operating style is active"
say "(ask the agent to summarize the constitution back at ${DEST}/kernel/constitution.md)."
[ "${WRITE}" = "1" ] || say "Re-run with --write to apply host-config changes automatically."
