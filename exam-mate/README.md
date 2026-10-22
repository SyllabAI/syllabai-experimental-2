# exam-mate (in syllabai-experimental-2)

This folder has **the same name and layout as the `exam-mate/` workspace
folder in the sister repo [`syllabai-experimental`](https://github.com/SyllabAI/syllabai-experimental)** —
it is the continuation of that workspace for one specific purpose:
**image storage from 2026-10-22 onward**.

Read first (in this order):

1. `../../sister_repo.json` — machine-readable pointer, describes both repos
2. `docs/STORAGE-SPLIT.md` — the decision record for the split
3. `resources/topical_papers/MANIFEST.md` — what this dataset holds
4. Sister repo's `exam-mate/research/2026-10-22-exam-mate-topical-past-papers-reverse-engineering.md` — how the site was decoded (not duplicated here)

## Why this folder exists here

The sister repo's image download phase (~30% done, ~60k images, 4.4 GB)
hit the sandbox disk ceiling (9.9 GB; images cost ~2× in working tree +
git objects). Per the operator's decision, **all image downloads from
2026-10-22 onward land in this repo** — the sister repo keeps everything
it already had, frozen and immutable, and remains the source-of-record
for questions.

## Layout

```
exam-mate/
  docs/STORAGE-SPLIT.md          # decision record
  scripts/                       # image-phase tooling (canonical from now on)
    exam_mate_client.py          #   WAF-immune fetch client (copy of sister's)
    exam_mate_image_bulk.py      #   per-subject bulk downloader (+ --questions-from
                                 #    for split-storage: questions read from sister,
                                 #    images written here)
    exam_mate_images_all.py      #   driver: walks all subjects, skips
                                 #    source_completed.json, resumable
  resources/topical_papers/
    MANIFEST.md                  # dataset manifest + provenance chain
    source_completed.json        # skip-list: subjects already imaged in the sister repo
    images_progress.json         # driver state (resumable across chunks)
    topical/<cat>/<subject>/images/   # downloads land here — identical layout
                                      # to the sister repo's subject dirs
```

## Conventions — inherited verbatim from the sister repo's `exam-mate/`

- **Provenance first**: source URL + capture date + method recorded next to
  every resource (per-image `INDEX.jsonl` ledger with sha256).
- **Raw captures are immutable**: once committed, files under `resources/`
  are read-only; corrections supersede, never overwrite.
- **Storage path mirrors source URL path**: local path after `images/` ==
  the URL path on www.exam-mate.com, so any image reconstructs its source.
- **Research docs are dated** `YYYY-MM-DD-topic.md`; decisions live in `docs/`.
- This folder is **not of record** — experimental workspace, same charter.

## Operating notes for agents

- The question-phase tooling (crawler, taxonomy, harvest_all, login) stays
  in the sister repo — do not duplicate it here.
- Question data (`questions.jsonl`) is READ from the sister repo's local
  checkout at `/home/z/my-project/syllabai-experimental/` (that checkout is
  sparse: its images/ trees are not on disk, but questions/ledgers are).
- Image fetching is anonymous + unmetered; the metered part of exam-mate is
  question-LIST serving, which is not needed for the image phase.
- Commit + push after every finished subject; watch `df -h /` (9.9 GB disk,
  ~2× image cost).
