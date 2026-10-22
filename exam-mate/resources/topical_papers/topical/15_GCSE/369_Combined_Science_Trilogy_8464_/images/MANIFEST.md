# MANIFEST — images/ (Combined Science: Trilogy (8464), complete set)

Downloaded: 2026-10-22T16:29:33Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=15` (GCSE) / `subjectID=369` (Combined Science: Trilogy (8464)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 779 unique image URLs referenced by 162 harvested questions (`questions.jsonl`) → **779 downloaded** (89.35 MB).
- 495 question images, 284 answer images.
- Years covered (parsed from paper refs): 2018, 2019.
- Topics (27): And The Properties Of Matter, B1.cell Biology, B2.organisation, B3.infection And Response, B4.bioenergetics, B5.homeostasis And Response, B6.inheritance, B7.ecology, C1.atomic Structure And The Periodic Table, C10.using Resources, C2.bonding, C3.quantitative Chemistry, C4.chemical Changes, C5.energy Changes, C6.the Rate And Extent Of Chemical Change, C7.organic Chemistry, C8.chemical Analysis, C9.chemistry Of The Atmosphere, P1.energy, P2.electricity, P3.particle Model Of Matter, P4.atomic Structure, P5.forces, P6.waves, P7.magnetism And Electromagnetism, Structure, Variation And Evolution.
- Harvested at: 2026-10-22T04:07:57+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 779/779 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
