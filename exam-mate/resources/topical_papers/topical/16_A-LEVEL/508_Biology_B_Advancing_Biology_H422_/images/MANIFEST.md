# MANIFEST — images/ (Biology B (Advancing Biology) (H422), complete set)

Downloaded: 2026-10-22T16:58:45Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=16` (A-LEVEL) / `subjectID=508` (Biology B (Advancing Biology) (H422)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 403 unique image URLs referenced by 144 harvested questions (`questions.jsonl`) → **403 downloaded** (67.54 MB).
- 267 question images, 136 answer images.
- Years covered (parsed from paper refs): 2017, 2018, 2019.
- Topics (34): Cells And Microscopy, Cellular Respiration, Controlling Communicable Diseases, Fertility And Assisted Reproduction, Food Production And Management Of The Environment, Gas Exchange In Mammals And Plants, Growth And Development, Kidney Functions And Malfunctions, Metabolism And Exercise, Monitoring Visual Function, Nucleic Acids, Pathogenic Microorganisms, Patterns Of Inheritance, Photosynthesis, Plant Reproduction, Population Genetics And Epigenetics, Practical Skills, Proteins And Enzymes, Respiratory Diseases And Treatment, The Cellular Basis Of Cancer And Treatment, The Developing Cell: Cell Division And Cell Differentiation, The Developing Individual: Meiosis, The Development Of Species: Evolution And Classification, The Effect Of Ageing On The Nervous System, The Effects Of Ageing On The Reproductive System, The Heart And Monitoring Heart Function, The Hormonal Control Of Blood Glucose And The Management Of Diabetes, The Immune System, The Impact Of Population Increase, The Nervous System And The Identification And Consequences Of Damage, The Principles And Importance Of Homeostasis, Transport Systems In Mammals, Transport Systems In Plants, Water And Its Importance In Plants And Animals.
- Harvested at: 2026-10-22T04:09:27+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 403/403 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
