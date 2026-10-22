# MANIFEST — images/ (Biology(4BI0), complete set)

Downloaded: 2026-10-22T14:01:36Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=4` (IGCSE) / `subjectID=32` (Biology(4BI0)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 1430 unique image URLs referenced by 415 harvested questions (`questions.jsonl`) → **1430 downloaded** (160.76 MB).
- 864 question images, 566 answer images.
- Years covered (parsed from paper refs): 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019.
- Topics (23): Blood And Circulation, Breathing And Gas Exchange, Cell Division, Chemical Coordination, Chemical Coordination In Plants, Chromosomes, Coordination, Ecosystems, Food And Digestion, Genes And Dna, Genes And Inheritance, Genetic Modification, Homeostasis And Excretion, Human Influences On The Environment, Life Processes, Natural Selection And Evolution, Plants And Food, Reproduction In Humans, Reproduction In Plants, Selective Breeding, The Variety Of Living Organisms, Transport In Plants, Using Microorganisms.
- Harvested at: 2026-10-22T01:50:35+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 1430/1430 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
