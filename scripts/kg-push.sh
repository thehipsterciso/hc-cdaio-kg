#!/usr/bin/env bash
# kg-push.sh — stage, commit, and push all KG changes without interruption
# Usage: ./scripts/kg-push.sh "commit message"

set -e

MSG="${1:-"chore(kg): auto-push KG changes"}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"

cd "$REPO"

# Rebuild split files from graph.json
python3 scripts/lib/kg-split.py

# Stage all tracked + untracked KG files
git add entities/ relationships/ .claude/plans/ docs/ DATA_ASSET_ENRICHMENT_REPORT.md 2>/dev/null || true

# Bail if nothing to commit
if git diff --cached --quiet; then
  echo "Nothing to commit."
  exit 0
fi

# Commit
git commit -m "$MSG

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

# Pull + rebase then push — handles diverged remote without prompting
git pull --rebase origin main
git push origin main

echo "Done. $(git log --oneline -1)"
