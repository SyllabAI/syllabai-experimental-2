# MANIFEST — images/ (Biology A (H020), complete set)

Downloaded: 2026-10-22T17:20:36Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=19` (AS) / `subjectID=544` (Biology A (H020)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 242 unique image URLs referenced by 95 harvested questions (`questions.jsonl`) → **242 downloaded** (26.15 MB).
- 148 question images, 94 answer images.
- Years covered (parsed from paper refs): 2017, 2018, 2019.
- Topics (18): Analysis, Biodiversity, Biological Membranes, Biological Molecules, Cell Diversity And Cellular Organisation, Cell Division, Cell Structure, Classification And Evolution, Communicable Diseases, Disease Prevention And The Immune System, Enzymes, Evaluation, Exchange Surfaces, Implementing, Nucleotides And Nucleic Acids, Planning, Transport In Animals, Transport In Plants.
- Harvested at: 2026-10-22T04:12:57+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 242/242 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
