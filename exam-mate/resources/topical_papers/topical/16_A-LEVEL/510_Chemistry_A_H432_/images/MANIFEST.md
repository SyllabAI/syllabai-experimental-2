# MANIFEST — images/ (Chemistry A (H432), complete set)

Downloaded: 2026-10-22T16:53:25Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=16` (A-LEVEL) / `subjectID=510` (Chemistry A (H432)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 434 unique image URLs referenced by 146 harvested questions (`questions.jsonl`) → **434 downloaded** (28.85 MB).
- 248 question images, 186 answer images.
- Years covered (parsed from paper refs): 2017, 2018, 2019.
- Topics (30): Acid–base And Redox Reactions, Alcohols And Haloalkanes, Amount Of Substance, Analytical Techniques (ir And Ms), Aromatic Compounds, Atoms, Basic Concept Of Organic Chemistry, Bonding And Structure, Carbonyl Compounds, Carboxylic Acids And Esters, Chromatography And Spectroscopy (nmr), Compounds, Electrons, Enthalpy, Enthalpy Changes, Entropy And Free Energy, Group 2 And The Halogens, Hydrocarbons, Molecules And Equations, Nitrogen Compounds, Organic Synthesis, Ph And Buffers, Polymers, Practical Skills, Qualitative Analysis, Reaction Rates And Equilibrium (qualitative), Reaction Rates And Equilibrium (quantitative), Redox And Electrode Potentials, The Periodic Table And Periodicity, Transition Elements.
- Harvested at: 2026-10-22T04:09:39+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 434/434 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
