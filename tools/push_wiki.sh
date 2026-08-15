#!/usr/bin/env bash
# Mirror docs/ into the GitHub wiki.
#
# The wiki is a separate git repository (std_time.wiki.git) on branch master.
# docs/ in this repo is the source of truth; this script makes the wiki match
# it, so the two histories cannot fork and the wiki cannot quietly become the
# place edits happen.
#
# Usage:  GH_TOKEN=<token> tools/push_wiki.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WIKI_URL="https://x-access-token:${GH_TOKEN}@github.com/hikari112/std_time.wiki.git"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

git clone --quiet --depth 1 "$WIKI_URL" "$WORK/wiki"

# Replace every page rather than merging, so a page deleted from docs/ also
# disappears from the wiki. .git is the only thing kept.
find "$WORK/wiki" -maxdepth 1 -name '*.md' -delete
cp "$REPO_ROOT"/docs/*.md "$WORK/wiki/"

cd "$WORK/wiki"
if git diff --quiet && git diff --cached --quiet && [ -z "$(git status --porcelain)" ]; then
    echo "wiki already matches docs/, nothing to push"
    exit 0
fi

git add -A
git -c user.name="Jesse Sanford" -c user.email="tabu112.com@gmail.com" \
    commit --quiet -m "Sync from docs/ at $(git -C "$REPO_ROOT" rev-parse --short HEAD)"
git push --quiet origin master

echo "pushed $(ls "$REPO_ROOT"/docs/*.md | wc -l) pages to the wiki"
