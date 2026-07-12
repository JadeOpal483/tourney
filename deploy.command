#!/bin/zsh
set -e
cd "/Users/ahmad/Documents/New project"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repository."
  exit 1
fi

BRANCH=$(git branch --show-current)
if [ "$BRANCH" != "main" ]; then
  echo "Current branch is '$BRANCH'. Switching to main..."
  git checkout main
fi

if [ -z "$(git status --porcelain)" ]; then
  echo "No changes to deploy."
  exit 0
fi

MSG="Deploy update $(date '+%Y-%m-%d %H:%M:%S')"

git add .
git commit -m "$MSG"
git push origin main

echo "Deploy pushed. Render will auto-deploy from main."
