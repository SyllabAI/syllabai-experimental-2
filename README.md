# syllabai-experimental-2

**Companion image-storage repo for [`SyllabAI/syllabai-experimental`](https://github.com/SyllabAI/syllabai-experimental).**
Created 2026-10-22 because the primary repo's image download phase hit the
sandbox disk ceiling (9.9 GB disk; images cost ~2× in working tree + git
objects). **Every exam-mate image downloaded from 2026-10-22 onward lives
here.** Questions and everything harvested before that date stay in the
sister repo.

> Any agent landing in either repo: read `sister_repo.json` (machine-
> readable) and `exam-mate/docs/STORAGE-SPLIT.md` (decision record) —
> together they fully describe the split. The same pointer file exists in
> the sister repo, so cloning either repo is enough to discover the other.

## The two repos

| | [syllabai-experimental](https://github.com/SyllabAI/syllabai-experimental) | **this repo (syllabai-experimental-2)** |
|---|---|---|
| Role | primary experiment repo | image-storage continuation |
| Holds | exam-mate research, tools, **questions.jsonl + meta.json for all 132 harvested subjects**, question-phase taxonomy/catalog, image sets completed ≤ 2026-10-22 (18 subject dirs, ~4.4 GB, incl. 0606, 0580, 0610, 0620, 0625, 9700, 9701*, 9702, 4MA0, 4MB0, 4CH0, 4PH0, 4BI0*, 4CH1, IB Chemistry…), plus the senecalearning / undergroundmathematics / znotes experiments | **all exam-mate image downloads after 2026-10-22** — the ~100k image URLs still outstanding (Sociology 0495, IB Physics, plus every subject not yet imaged), re-imaging of the two ledger-only subjects (*) |
| exam-mate workspace folder | `exam-mate/` | `exam-mate/` — **same name, mirrored layout** |
| Image-phase tooling | original scripts (frozen) | patched copies in `exam-mate/scripts/` (split-storage aware — the canonical image-phase tooling from now on) |

## Layout (mirrors the sister repo's `exam-mate/` folder)

```
syllabai-experimental-2/
  sister_repo.json                 # machine-readable bidirectional pointer
  exam-mate/
    README.md                      # folder conventions
    docs/STORAGE-SPLIT.md          # the storage-split decision record
    scripts/                       # exam_mate_client.py (copy),
                                   # exam_mate_image_bulk.py (+--questions-from),
                                   # exam_mate_images_all.py (split-storage driver)
    resources/topical_papers/
      MANIFEST.md                  # dataset manifest + provenance chain
      source_completed.json        # subjects already imaged in the sister repo (skip-list)
      images_progress.json         # driver state (resumable)
      topical/<cat>/<subject>/images/   # downloads land here — same layout
                                        # as the sister repo's subject dirs
```

## Resuming the image phase

```bash
# chunked foreground runs (background processes do not survive tool-call
# boundaries); per-subject + per-image resume is automatic
timeout -k 5 520 python3 \
  /home/z/my-project/syllabai-experimental-2/exam-mate/scripts/exam_mate_images_all.py \
  --batch 6 --delay 0.7

# progress
python3 .../exam_mate_images_all.py --status
```

- Reads `questions.jsonl` from the sister repo (read-only); writes `images/`
  + `INDEX.jsonl` + `MANIFEST.md` here.
- **Mind the disk**: commit + push after each finished subject
  (`git add exam-mate/ && git commit && git push`); check `df -h /`.
- Image fetching is anonymous and unmetered (unlike question-list serving);
  no exam-mate login is required for this phase.

## Conventions (inherited from the sister repo — unchanged)

- **Provenance first**: every resource records source URL, capture date,
  method. Per-image ledger `INDEX.jsonl` carries sha256, bytes, dimensions,
  both site id spaces, paper_ref, topics, mcq_answer, timestamp.
- **Raw captures are immutable**: files under `resources/` are read-only
  once committed; corrections supersede, never overwrite.
- **Storage path mirrors source URL path**: local path after `images/` ==
  the URL path on www.exam-mate.com.
- Nothing in this repo is of record — experimental workspace, same charter
  as the sister repo's root README.
