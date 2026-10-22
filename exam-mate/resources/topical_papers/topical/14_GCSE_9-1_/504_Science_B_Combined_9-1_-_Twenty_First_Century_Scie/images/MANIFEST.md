# MANIFEST — images/ (Science B, Combined (9-1) - Twenty First Century Science Suite J260, complete set)

Downloaded: 2026-10-22T16:43:37Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=14` (GCSE (9-1)) / `subjectID=504` (Science B, Combined (9-1) - Twenty First Century Science Suite J260) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 523 unique image URLs referenced by 140 harvested questions (`questions.jsonl`) → **523 downloaded** (41.78 MB).
- 328 question images, 195 answer images.
- Years covered (parsed from paper refs): ?.
- Topics (19): B1: You And Your Genes, B2: Keeping Healthy, B3: Living Together – Food And Ecosystems, B4: Using Food And Controlling Growth, B5: The Human Body – Staying Alive, B6: Life On Earth – Past, C1: Air And Water, C2: Chemical Patterns, C3: Chemicals Of The Natural Environment, C4: Material Choices, C5: Chemical Analysis, C6: Making Useful Chemicals, P1: Radiation And Waves, P2: Sustainable Energy, P3: Electric Circuits, P4: Explaining Motion, P5: Radioactive Materials, P6: Matter – Models And Explanations, Present And Future.
- Harvested at: 2026-10-22T03:59:42+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 523/523 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
