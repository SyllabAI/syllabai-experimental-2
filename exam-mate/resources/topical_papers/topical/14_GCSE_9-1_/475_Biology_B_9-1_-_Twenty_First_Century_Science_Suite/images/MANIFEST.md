# MANIFEST — images/ (Biology B (9-1) - Twenty First Century Science Suite J257, complete set)

Downloaded: 2026-10-22T17:16:47Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=14` (GCSE (9-1)) / `subjectID=475` (Biology B (9-1) - Twenty First Century Science Suite J257) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 282 unique image URLs referenced by 63 harvested questions (`questions.jsonl`) → **282 downloaded** (23.64 MB).
- 164 question images, 118 answer images.
- Years covered (parsed from paper refs): 2018, 2019.
- Topics (8): Ideas About Science, Keeping Healthy, Life On Earth – Past, Living Together – Food And Ecosystems, Present And Future, The Human Body – Staying Alive, Using Food And Controlling Growth, You And Your Genes.
- Harvested at: 2026-10-22T03:20:40+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 282/282 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
