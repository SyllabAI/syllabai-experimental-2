# MANIFEST — images/ (Mathematics A, Further (H245), complete set)

Downloaded: 2026-10-22T17:30:55Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=16` (A-LEVEL) / `subjectID=530` (Mathematics A, Further (H245)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 128 unique image URLs referenced by 52 harvested questions (`questions.jsonl`) → **128 downloaded** (6.04 MB).
- 52 question images, 76 answer images.
- Years covered (parsed from paper refs): 2019, ?.
- Topics (32): Centre Of Mass (mechanics), Complex Numbers (pure Math), Continuous Random Variables (statistics), Correlation (statistics), Decision Making In Project Management (discrete Mathematics), Differential Equations (pure Math), Dimensional Analysis (mechanics), Discrete Random Variables (statistics), Energy And Power (mechanics), Further Algebra (pure Math), Further Calculus (additional Pure Math), Further Calculus (pure Math), Further Dynamics And Kinematics (mechanics), Further Vectors (additional Pure Math), Further Vectors (pure Math), Game Theory (discrete Mathematics), Graphical Linear Programming (discrete Mathematics), Graphs And Networks (discrete Mathematics), Groups (additional Pure Math), Hyperbolic Functions (pure Math), Hypothesis Tests And Confidence Intervals (statistics), Mathematical Preliminaries (discrete Mathematics), Matrices (pure Math), Motion In A Circle (mechanics), Network Algorithms (discrete Mathematics), Number Theory (additional Pure Math), Polar Coordinates (pure Math), Probability (statistics), Sequences And Series (additional Pure Math), Series (pure Math), Surfaces And Partial Differentiation (additional Pure Math), Work.
- Harvested at: 2026-10-22T04:18:47+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 128/128 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
