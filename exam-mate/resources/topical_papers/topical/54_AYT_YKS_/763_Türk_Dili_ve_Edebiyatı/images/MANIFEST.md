# MANIFEST — images/ (Türk Dili ve Edebiyatı, complete set)

Downloaded: 2026-10-22T17:46:52Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=54` (AYT (YKS)) / `subjectID=763` (Türk Dili ve Edebiyatı) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 47 unique image URLs referenced by 47 harvested questions (`questions.jsonl`) → **47 downloaded** (0.96 MB).
- 47 question images, 0 answer images.
- Years covered (parsed from paper refs): ?.
- Topics (9): Edebiyat Bilgileri (literary Concepts), Hikâye Ve Tiyatro (novel, Milli Edebiyat Ve Cumhuriyet Dönemi (national Literature And Republican Era), Roman, Story And Drama), Tanzimat Ve Servet-i Fünun Edebiyatı (tanzimat And Servet-i Fünun Literature), İslamiyet Etkisindeki Türk Edebiyatı (turkish Literature Under Islamic Influence), İslamiyet Öncesi Türk Edebiyatı (pre-islamic Turkish Literature), Şiir Bilgisi (poetry).
- Harvested at: 2026-10-22T04:40:02+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 47/47 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
