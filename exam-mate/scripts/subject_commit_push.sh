#!/bin/bash
# Commit+push+shed one completed subject in repo 2 (sparse/partial-clone safe).
# Usage: subject_commit_push.sh <subject-rel-dir> "<commit message>"
# - adds the subject dir + images_progress.json via PLUMBING (git add
#   porcelain refuses paths outside sparse-checkout patterns; plumbing
#   does not check them)
# - commits, pushes (dedicated window), then `git sparse-checkout
#   reapply` sheds the subject's PNGs from the working tree (they stay
#   in the commit + on GitHub; ledgers remain materialized)
set -eu
REPO=/home/z/my-project/syllabai-experimental-2
SUBJ="$1"; MSG="$2"
cd "$REPO"
LIST=$(mktemp)
find "exam-mate/resources/topical_papers/$SUBJ/images" -type f > "$LIST" || { echo "[scp] FATAL: find failed for $SUBJ"; rm -f "$LIST"; exit 1; }
[ -s "$LIST" ] || { echo "[scp] FATAL: no files found for $SUBJ (bad path?)"; rm -f "$LIST"; exit 1; }
echo "[scp] adding $(wc -l < "$LIST") files"
git update-index --add --stdin < "$LIST"
rm -f "$LIST"
git update-index --add exam-mate/resources/topical_papers/images_progress.json
git commit -q -m "$MSG"
echo "[scp] committed $(git rev-parse --short HEAD)"
timeout 540 git push -q origin main || { echo "[scp] PUSH INCOMPLETE — will retry next run"; exit 2; }
timeout 180 git sparse-checkout reapply || echo "[scp] reapply issue (non-fatal, check tree)"
echo "[scp] pushed + shed. tree status:"; git status --porcelain | wc -l
df -h / | tail -1
