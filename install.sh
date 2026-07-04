#!/usr/bin/env bash
set -euo pipefail

TARGET="codex"
FORCE=0
DEST=""

usage() {
  cat <<'USAGE'
ecoMode installer

Usage:
  bash install.sh [--target codex|claude|vscode|all] [--dest PATH] [--force]

Targets:
  codex   -> ~/.codex/skills/ecomode
  claude  -> ~/.claude/skills/ecomode
  vscode  -> ./.github/skills/ecomode
  all     -> codex + claude + vscode

Examples:
  bash install.sh
  bash install.sh --target claude
  bash install.sh --target all --force
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --dest)
      DEST="${2:-}"
      shift 2
      ;;
    --force)
      FORCE=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

copy_skill() {
  local dest="$1"
  if [ -e "$dest" ] && [ "$FORCE" -ne 1 ]; then
    echo "exists: $dest"
    echo "Use --force to overwrite."
    return 1
  fi

  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  mkdir -p "$dest"

  tar \
    --exclude='.git' \
    --exclude='*.zip' \
    -C "$ROOT" \
    -cf - . | tar -C "$dest" -xf -

  echo "installed: $dest"
}

install_codex() {
  local base="${CODEX_HOME:-$HOME/.codex}"
  copy_skill "${DEST:-$base/skills/ecomode}"
}

install_claude() {
  local base="${CLAUDE_HOME:-$HOME/.claude}"
  copy_skill "${DEST:-$base/skills/ecomode}"
}

install_vscode() {
  copy_skill "${DEST:-$PWD/.github/skills/ecomode}"
}

case "$TARGET" in
  codex) install_codex ;;
  claude) install_claude ;;
  vscode) install_vscode ;;
  all)
    install_codex
    install_claude
    install_vscode
    ;;
  *)
    echo "Invalid target: $TARGET" >&2
    usage >&2
    exit 1
    ;;
esac

echo "Restart your agent so it reloads skills."
