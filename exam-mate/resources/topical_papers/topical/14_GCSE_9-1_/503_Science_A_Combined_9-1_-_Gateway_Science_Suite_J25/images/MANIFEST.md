# MANIFEST — images/ (Science A, Combined (9-1) - Gateway Science Suite J250, complete set)

Downloaded: 2026-10-22T16:27:39Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=14` (GCSE (9-1)) / `subjectID=503` (Science A, Combined (9-1) - Gateway Science Suite J250) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 790 unique image URLs referenced by 394 harvested questions (`questions.jsonl`) → **790 downloaded** (58.08 MB).
- 541 question images, 249 answer images.
- Years covered (parsed from paper refs): ?.
- Topics (19): B1: Cell Level Systems, B2: Scaling Up, B3: Organism Level Systems, B4: Community Level Systems, B5: Interaction Between Systems, B6: Global Challenges, C1: Particles, C2: Elements, C3: Chemical Reactions, C4: Predicting And Identifying Reactions And Products, C5: Monitoring And Controlling Chemical Reactions, C6: Global Challenges, Compounds And Mixtures, P1: Matter, P2: Forces, P3: Electricity And Magnetism, P4: Waves And Radioactivity, P5: Energy, P6: Global Challenges.
- Harvested at: 2026-10-22T03:59:16+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 790/790 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
