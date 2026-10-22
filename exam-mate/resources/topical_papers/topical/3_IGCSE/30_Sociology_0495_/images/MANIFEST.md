# MANIFEST — images/ (Sociology(0495), complete set)

Downloaded: 2026-10-22T14:37:08Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=3` (IGCSE) / `subjectID=30` (Sociology(0495)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 2765 unique image URLs referenced by 480 harvested questions (`questions.jsonl`) → **2765 downloaded** (590.41 MB).
- 939 question images, 1826 answer images.
- Years covered (parsed from paper refs): 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019.
- Topics (10): Crime, Culture, Deviance And Social Control - P2, Education - P2, Family - P2, Identity And Socialization -p1, Media - P2, Methodology - Research Methods - Theory And Methods - P1, Power And Authority - P1, Social Stratification And Inequality - P1.
- Harvested at: 2026-10-22T03:17:32+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 2765/2765 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
