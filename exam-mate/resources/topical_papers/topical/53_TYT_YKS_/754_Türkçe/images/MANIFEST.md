# MANIFEST — images/ (Türkçe, complete set)

Downloaded: 2026-10-22T17:46:28Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=53` (TYT (YKS)) / `subjectID=754` (Türkçe) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 80 unique image URLs referenced by 80 harvested questions (`questions.jsonl`) → **80 downloaded** (2.12 MB).
- 80 question images, 0 answer images.
- Years covered (parsed from paper refs): ?.
- Topics (13): Bağlaç, Cümlede Anlam, Dil Bilgisi (fiil, Edat, Isim, Noktalama Işaretleri, Paragraf (anlam Ve Anlatım), Sözcükte Anlam, Sıfat, Yazım Kuralları, Zamir, Zarf, ünlem Vb.).
- Harvested at: 2026-10-22T04:38:08+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 80/80 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
