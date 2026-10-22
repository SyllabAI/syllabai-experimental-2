# MANIFEST — images/ (Economics(0455), complete set)

Downloaded: 2026-10-22T15:50:29Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=3` (IGCSE) / `subjectID=17` (Economics(0455)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 1414 unique image URLs referenced by 1410 harvested questions (`questions.jsonl`) → **1414 downloaded** (84.78 MB).
- 1410 question images, 4 answer images.
- Years covered (parsed from paper refs): 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019.
- Topics (10): Basic Economic Problem: Choice And The Allocation Of Resources, Consumer And Borrower, Developed And Developing Economies: Trends In Production, Economic Indicators, International Aspects, Population And Living Standards, Role Of Government In Economy, The Allocation Of Resources: How The Market Works; Market Failure, The Individual As Producer, The Private Firm As Producer And Employer.
- Harvested at: 2026-10-22T02:05:53+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 1414/1414 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
