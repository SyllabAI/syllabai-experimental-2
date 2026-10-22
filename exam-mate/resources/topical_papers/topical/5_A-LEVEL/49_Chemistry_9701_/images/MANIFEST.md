# MANIFEST — images/ (Chemistry(9701), complete set)

Downloaded: 2026-10-22T12:16:49Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=5` (A-LEVEL) / `subjectID=49` (Chemistry(9701)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 7552 unique image URLs referenced by 3693 harvested questions (`questions.jsonl`) → **7552 downloaded** (337.18 MB).
- 5511 question images, 2041 answer images.
- Years covered (parsed from paper refs): 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019.
- Topics (24): An Introduction To Organic Chemistry, An Introduction To The Chemistry Of Transition Elements, Analytical Techniques, Atomic Structure, Atoms, Carbonyl Compounds, Carboxylic Acids And Derivatives, Chemical Bonding, Chemical Energetics, Electrochemistry, Equilibria, Group 17, Group 2, Halogen Derivatives, Hydrocarbons, Hydroxy Compounds, Nitrogen &amp; Sulfur, Nitrogen Compounds, Organic Synthesis, Polymerisattion, Reaction Kinetics, States Of Matter, The Periodic Table : Chemical Periodicity, molecules &amp; Stoichiometry.
- Harvested at: 2026-10-22T03:30:04+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 7552/7552 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
