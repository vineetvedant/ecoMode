#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-codex}"

remove_path() {
  local path="$1"
  if [ -d "$path" ]; then
    rm -rf "$path"
    echo "removed: $path"
  else
    echo "not found: $path"
  fi
}

case "$TARGET" in
  codex) remove_path "${CODEX_HOME:-$HOME/.codex}/skills/ecomode" ;;
  claude) remove_path "${CLAUDE_HOME:-$HOME/.claude}/skills/ecomode" ;;
  vscode) remove_path "$PWD/.github/skills/ecomode" ;;
  all)
    remove_path "${CODEX_HOME:-$HOME/.codex}/skills/ecomode"
    remove_path "${CLAUDE_HOME:-$HOME/.claude}/skills/ecomode"
    remove_path "$PWD/.github/skills/ecomode"
    ;;
  *)
    echo "Usage: bash uninstall.sh [codex|claude|vscode|all]" >&2
    exit 1
    ;;
esac
