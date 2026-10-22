# MANIFEST — images/ (History(9389), complete set)

Downloaded: 2026-10-22T15:10:11Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=5` (A-LEVEL) / `subjectID=164` (History(9389)) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 2597 unique image URLs referenced by 1020 harvested questions (`questions.jsonl`) → **2597 downloaded** (245.04 MB).
- 1227 question images, 1370 answer images.
- Years covered (parsed from paper refs): 2015, 2016, 2017, 2018, 2019.
- Topics (25): 1789–1917, 1815–1871, 1840–1941, 1846–1861, 1871–1945, 1918–1941, 1919–1945, 1941–1950, 1945–1990, 1945–1990s, 1945–1991, African History, C.1850–1939, Europe Of The Dictators, International History, International Relations, Liberalism And Nationalism In Italy And Germany, Modern Europe, Southeast Asian History, The Causes And Impact Of British Imperialism, The History Of The Usa, The Holocaust, The Origins And Development Of The Cold War, The Origins Of The Civil War, The Search For International Peace And Security.
- Harvested at: 2026-10-22T03:40:29+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 2597/2597 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
