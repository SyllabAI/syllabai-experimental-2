#!/bin/bash
# Edexcel-focus image harvester for repo 2 (split-storage mode).
# Usage: edexcel_batch.sh <subject-rel-dir> [<subject-rel-dir> ...]
# Each subject: bulk download+organize with a 500s ceiling (resumable).
set -u
BULK=/home/z/my-project/syllabai-experimental-2/exam-mate/scripts/exam_mate_image_bulk.py
SRC=/home/z/my-project/syllabai-experimental/exam-mate/resources/topical_papers
cd /home/z/my-project/syllabai-experimental-2/exam-mate/scripts || exit 1
for rel in "$@"; do
  echo "=== $rel ==="
  timeout -k 5 500 python3 "$BULK" --phase all \
    --subject-dir "$rel" \
    --questions-from "$SRC/$rel/questions.jsonl" \
    --batch 6 --delay 0.7 2>&1 | tail -11
  echo "--- exit: $? ---"
done
