# STORAGE SPLIT — exam-mate images move to syllabai-experimental-2

**Decision date:** 2026-10-22 · **Decided by:** operator (user instruction:
*"Create a new repo. syllabai-experimental-2. There create a folder with
same name and store rest of the images there. Make sure both repos/folders
know about each other, and other agent will also know about it easily"*)

## Situation at decision time

- Question harvest was 100% complete in `syllabai-experimental`:
  132 subjects with data, 88,323 questions, 48 subjects site-empty.
- Image download was ~30% complete (~60k images, ~4.4 GB committed) when it
  paused at the sandbox disk ceiling (9.9 GB root fs; images cost ~2× once
  git objects are counted — effective ceiling ~4.5 GB of images).
- ~100k image URLs were still outstanding (biggest: Sociology 0495 ~570 MB,
  IB Physics ~430 MB — both mid-flight when pruned, plus every subject not
  yet imaged).
- The workspace was wiped the same day (sandbox recycle); both repos were
  restored by re-clone from GitHub. The 4.8 GB image checkout of the sister
  repo was replaced by a **sparse checkout** (images on GitHub only, ~42 MB
  materialized), freeing 5.4 GB for the continuation.

## Decision

1. **New repo `SyllabAI/syllabai-experimental-2`** holds **all exam-mate
   image downloads from 2026-10-22 onward**, under
   `exam-mate/resources/topical_papers/topical/...` — a folder with the
   **same name and layout** as the sister repo's workspace folder, so
   tooling and manifests stay homogeneous.
2. The sister repo **keeps everything it already had, unchanged and
   immutable** (raw-capture immutability): its 18 image subject dirs, all
   questions, research, docs, tools.
3. Image-phase tooling is **copied into the new repo and patched for the
   split**: bulk downloader gains `--questions-from` (questions read from
   the sister repo, images written here); driver knows both roots and
   skips subjects already completely imaged in the sister repo
   (`source_completed.json`).

## What lives where (authoritative)

| Data | Where |
|---|---|
| `questions.jsonl`, `meta.json` (all 132 subjects), `catalog.json`, `subject_taxonomy.json`, `progress.json` | **syllabai-experimental** (source-of-record) |
| Image sets completed 2026-10-22 (16 verified subjects: 0606, 0580, 0610, 0620, 0625, 0510, 0417, 0607, 4CH0, 4MA0, 4MB0, 4PH0, 9700, 9702, 4CH1, IB Chemistry; + 2 ledger-only: 4BI0, 9701) | **syllabai-experimental** (immutable; the 2 ledger-only ones are ALSO re-imaged fresh here) |
| Every image downloaded after 2026-10-22 (incl. re-imaging of 4BI0 + 9701, Sociology 0495, IB Physics, and all remaining subjects) | **syllabai-experimental-2** (this repo) |
| Image-phase tools (bulk + driver, split-storage aware) | **syllabai-experimental-2** `exam-mate/scripts/` (canonical); originals frozen in the sister repo |
| Question-phase tools (crawler, taxonomy, harvest_all, login) | **syllabai-experimental** `exam-mate/scripts/` (canonical; not duplicated) |

## Cross-referencing (so any agent discovers the split)

- `sister_repo.json` — identical machine-readable pointer committed at the
  root of **both** repos (clone either → discover the other).
- Root + `exam-mate/` READMEs in both repos state the split.
- GitHub repo descriptions of both repos state the split.
- Work log `/home/z/my-project/worklog.md` records it.
- `source_completed.json` (this repo) pins exactly which subjects are
  complete in the sister repo — the driver's skip-list. Regenerate only if
  the sister repo's image tree changes (criterion: tracked
  `images/MANIFEST.md` + `images/INDEX.jsonl`).

## Resume commands

```bash
timeout -k 5 520 python3 \
  /home/z/my-project/syllabai-experimental-2/exam-mate/scripts/exam_mate_images_all.py \
  --batch 6 --delay 0.7
# status:
python3 .../exam_mate_images_all.py --status
# after each finished subject: git add exam-mate/ && git commit && git push
```

Disk discipline: check `df -h /` between subjects; stop above ~1 GB free;
pushed subjects stay safe on GitHub (re-clone or sparse-add to re-materialize).
