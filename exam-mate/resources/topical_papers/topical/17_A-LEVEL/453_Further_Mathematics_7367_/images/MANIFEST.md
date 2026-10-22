# MANIFEST — images/ (Further Mathematics (7367), complete set)

Downloaded: 2026-10-22T17:30:34Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=17` (A-LEVEL) / `subjectID=453` (Further Mathematics (7367)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 151 unique image URLs referenced by 54 harvested questions (`questions.jsonl`) → **151 downloaded** (7.14 MB).
- 88 question images, 63 answer images.
- Years covered (parsed from paper refs): 2019.
- Topics (28): Binary Operations, Centres Of Mass And Moments, Chi Squared Tests, Circular Motion, Complex Numbers, Confidence Intervals, Continuous Random Variables, Critical Path Analysis, Differential Equations, Discrete Random Variables, Energy &amp; Power, Further Algebra And Functions, Further Calculus, Further Vectors, Game Theory For Zero-sum Games, Graphs, Hyperbolic Functions, Linear Programming, Matrices, Momentum And Collisions, Network Flows, Networks, Numerical Methods, One Sample T-distribution, Poisson Distribution, Proof, Type I And Type Ii Errors, Work.
- Harvested at: 2026-10-22T04:11:22+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 151/151 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
