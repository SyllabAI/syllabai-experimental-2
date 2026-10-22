# MANIFEST — topical_papers dataset (image continuation, syllabai-experimental-2)

This dataset is the **continuation of the exam-mate TOPICAL PAST PAPERS
harvest** whose source-of-record lives in the sister repo
[`SyllabAI/syllabai-experimental`](https://github.com/SyllabAI/syllabai-experimental)
(see its `exam-mate/resources/topical_papers/MANIFEST.md`).

- **Source:** `https://www.exam-mate.com/` TOPICAL PAST PAPERS feature
- **Method:** fixed-fingerprint headless Chromium, WAF-immune in-page
  `fetch()` pipeline (see sister repo's research note), batches of 6
  concurrent fetches / 0.7 s politeness delay, anonymous session
  (image serving is unmetered — no login required)
- **Started here:** 2026-10-22, after the sister repo's image phase paused
  at the sandbox disk ceiling (~30% done, ~4.4 GB)
- **Scope of this repo:** every image downloaded from 2026-10-22 onward +
  fresh re-imaging of the two ledger-only subjects (4BI0, 9701)

## Contents

| Path | What |
|---|---|
| `source_completed.json` | Skip-list: 16 subjects whose COMPLETE image sets already live in the sister repo (criterion: tracked `images/MANIFEST.md` + `images/INDEX.jsonl` there). Never re-download those here. |
| `images_progress.json` | Driver state (`scripts/exam_mate_images_all.py`) — resumable across chunked runs. |
| `topical/<cat>/<subject>/images/` | Downloads land here, **identical layout to the sister repo's subject dirs**: `questions/{qfolder}/{src_qid}/{original_filename}.png` mirroring the source URL path, plus `INDEX.jsonl` (per-image ledger: sha256, bytes, dimensions, both site id spaces, paper_ref, topics, mcq_answer, timestamp), `by_paper.json` / `by_topic.json` derived views, `MANIFEST.md`, `_summary.json` per subject. |

## Question data (NOT stored here)

`questions.jsonl` + `meta.json` for every subject (132 subjects, 88,323
questions), `catalog.json` (21 categories / 180 subjects) and
`subject_taxonomy.json` live in the **sister repo** at
`exam-mate/resources/topical_papers/` — that is the source-of-record. The
driver here reads questions from the sister repo's local checkout and
writes only images into this repo (`--questions-from` split-storage mode).

## Provenance & integrity notes

- Same pipeline and ledger contract as the sister repo's image sets; a
  subject completed here is verifiable via its `images/_summary.json`
  (`files_on_disk == index_entries`) and per-file sha256 in `INDEX.jsonl`.
- Local path after `images/` == the URL path on www.exam-mate.com, so
  `https://www.exam-mate.com/<file>` reconstructs any image's source URL.
- Transient origin failures are recorded in `INDEX.jsonl` (bytes=0) —
  never substituted or fabricated.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party
site exam-mate.com. Experimental research copy only — license review
required before any of this content ships (same discipline as the sister
repo's datasets).
