# MANIFEST — images/ (Physics(WPH01), complete set)

Downloaded: 2026-10-22T13:55:22Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=6` (A-LEVEL) / `subjectID=70` (Physics(WPH01)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 2314 unique image URLs referenced by 1146 harvested questions (`questions.jsonl`) → **2314 downloaded** (285.77 MB).
- 1654 question images, 660 answer images.
- Years covered (parsed from paper refs): 2009, 2010, 2011, 2012, 2013, 2014, 2015, ?.
- Topics (24): Basic Waves, Behaviour Of Waves, Capacitors, Circular Motion, Electric Fields, Electrical Circuits, Electrical Quantities, Electromagnetic Effects, Energy, Fluids, Further Momentum, Gravitational Fields, Heat &amp; Temperature, Motion, Optics, Oscillations, Particle Accelerators And Detectors, Particle Interactions, Probing Matter, Quantum Physics, Radioactivity, Solid Materials, Space &amp; Astronomy, Units And Estimation.
- Harvested at: 2026-10-22T03:57:34+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 2314/2314 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
