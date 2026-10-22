# MANIFEST — topical_papers dataset (image continuation, syllabai-experimental-2)

This dataset is the **continuation of the exam-mate TOPICAL PAST PAPERS
harvest** whose source-of-record lives in the sister repo
[`SyllabAI/syllabai-experimental`](https://github.com/SyllabAI/syllabai-experimental)
(see its `exam-mate/resources/topical_papers/MANIFEST.md`).

- **Source:** `https://www.exam-mate.com/` TOPICAL PAST PAPERS feature
- **Method:** fixed-fingerprint headless Chromium, WAF-immune in-page
  `fetch()` pipeline (see sister repo's research note), batches of 6
  concurrent fetches / 0.7 s politeness delay, anonymous session
  (image serving is unmetered — no login required)
- **Started here:** 2026-10-22, after the sister repo's image phase paused
  at the sandbox disk ceiling (~30% done, ~4.4 GB)
- **Scope of this repo:** every image downloaded from 2026-10-22 onward +
  fresh re-imaging of the two ledger-only subjects (4BI0, 9701)

## Contents

| Path | What |
|---|---|
| `source_completed.json` | Skip-list: 16 subjects whose COMPLETE image sets already live in the sister repo (criterion: tracked `images/MANIFEST.md` + `images/INDEX.jsonl` there). Never re-download those here. |
| `images_progress.json` | Driver state (`scripts/exam_mate_images_all.py`) — resumable across chunked runs. |
| `topical/<cat>/<subject>/images/` | Downloads land here, **identical layout to the sister repo's subject dirs**: `questions/{qfolder}/{src_qid}/{original_filename}.png` mirroring the source URL path, plus `INDEX.jsonl` (per-image ledger: sha256, bytes, dimensions, both site id spaces, paper_ref, topics, mcq_answer, timestamp), `by_paper.json` / `by_topic.json` derived views, `MANIFEST.md`, `_summary.json` per subject. |

## Image-phase progress

**21 subjects imaged here — 43,208 PNGs, ~3.1 GB** (all with
`files_on_disk == index_entries`, 0 unexplained failures):

| Cat | Subject | Key | Images | MB | Session |
|---|---|---|---:|---:|---|
| 7 | IB Physics | 7:92 | 7,539 | 414 | 2026-10-22 a |
| 5 | A-Level Chemistry 9701 | 5:49 | 7,552 | 337 | 2026-10-22 a |
| 7 | IB Biology | 7:74 | 6,254 | 750 | 2026-10-22 a |
| 6 | IAL Biology WBI01 | 6:61 | 4,427 | 398 | 2026-10-22 c |
| 6 | IAL Physics WPH01 | 6:70 | 2,314 | 286 | 2026-10-22 c |
| 6 | IAL Chemistry WCH01 | 6:63 | 5,419 | 372 | 2026-10-22 b |
| 6 | IAL Maths Core WMA01/WMA02 | 6:65 | 1,820 | 87 | 2026-10-22 b |
| 6 | IAL Mechanics WME01 | 6:68 | 1,233 | 35 | 2026-10-22 b |
| 6 | IAL Stats WST01 | 6:69 | 813 | 25 | 2026-10-22 b |
| 6 | IAL Further Pure WFM01 | 6:67 | 1,001 | 44 | 2026-10-22 b |
| 6 | IAL Pure WMA11 | 6:620 | 68 | 3 | 2026-10-22 b |
| 6 | IAL Biology WBI11 | 6:617 | 151 | 14 | 2026-10-22 b |
| 6 | IAL Chemistry WCH11 | 6:618 | 177 | 9 | 2026-10-22 b |
| 6 | IAL Physics WPH11 | 6:622 | 113 | 7 | 2026-10-22 b |
| 4 | IGCSE Biology 4BI0 | 4:32 | 1,430 | 96 | 2026-10-22 b |
| 4 | IGCSE Further Pure 4PM0 | 4:45 | 714 | 42 | 2026-10-22 b |
| 21 | IGCSE 9-1 Maths A 4MA1 | 21:615 | 1,202 | 49 | 2026-10-22 b |
| 21 | IGCSE 9-1 Maths B 4MB1 | 21:637 | 514 | 21 | 2026-10-22 b |
| 21 | IGCSE 9-1 Biology 4BI1 | 21:613 | 241 | 10 | 2026-10-22 b |
| 21 | IGCSE 9-1 Physics 4PH1 | 21:616 | 134 | 14 | 2026-10-22 b |
| 21 | IGCSE 9-1 Further Pure 4PM1 | 21:634 | 92 | 3 | 2026-10-22 b |

Session *a* = biggest-first catch-up (IB + CIE A-Level); session *b* =
Edexcel sweep; session *c* = disk-unblocked finish. **EDEXCEL BOARD IS
DONE: 23/23 subjects fully imaged** — 18 here (cats 4, 6, 21 below) +
5 in the sister repo (4MA0, 4MB0, 4CH0, 4PH0, 4CH1, see its MANIFEST).

**Next up (general queue, biggest-first):** resume
`scripts/exam_mate_images_all.py` chunked-foreground — Sociology 0495
(3:30, 2,765 urls) is next-biggest, then the remaining ~92 subjects
(~55k urls). Disk headroom after Edexcel closeout: ~3.3 GB free.

## Question data (NOT stored here)

`questions.jsonl` + `meta.json` for every subject (132 subjects, 88,323
questions), `catalog.json` (21 categories / 180 subjects) and
`subject_taxonomy.json` live in the **sister repo** at
`exam-mate/resources/topical_papers/` — that is the source-of-record. The
driver here reads questions from the sister repo's local checkout and
writes only images into this repo (`--questions-from` split-storage mode).

## Provenance & integrity notes

- Same pipeline and ledger contract as the sister repo's image sets; a
  subject completed here is verifiable via its `images/_summary.json`
  (`files_on_disk == index_entries`) and per-file sha256 in `INDEX.jsonl`.
- Local path after `images/` == the URL path on www.exam-mate.com, so
  `https://www.exam-mate.com/<file>` reconstructs any image's source URL.
- Transient origin failures are recorded in `INDEX.jsonl` (bytes=0) —
  never substituted or fabricated.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party
site exam-mate.com. Experimental research copy only — license review
required before any of this content ships (same discipline as the sister
repo's datasets).
