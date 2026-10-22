# MANIFEST — images/ (Biyoloji, complete set)

Downloaded: 2026-10-22T17:47:14Z · Source: `https://www.exam-mate.com` TOPICAL PAST PAPERS, subject `categoryID=54` (AYT (YKS)) / `subjectID=783` (Biyoloji) · Method: fixed-fingerprint headless Chromium, in-page `fetch()` pipeline (WAF-immune; `scripts/exam_mate_image_bulk.py`) · Rate: batches of 4 concurrent fetches, 1 s between batches.

## Contents

| Path | What |
|---|---|
| `INDEX.jsonl` | **Per-image metadata ledger — the provenance record.** One JSON object per unique image URL. |
| `questions/{qfolder}/{src_qid}/{original_filename}.png` | PNGs, original site filenames preserved. Local path after `images/` == URL path, so `https://www.exam-mate.com/` + `<file>` reconstructs the source URL. |
| `by_paper.json` | Derived view: `paper_ref` → qid, topics, MCQ answer, parsed fields, image lists. Sorted newest-first. |
| `by_topic.json` | Derived view: individual topic → entries (site topic strings verbatim). |
| `_summary.json` | Machine summary of the download + integrity run. |

## Coverage vs. harvest

- 26 unique image URLs referenced by 26 harvested questions (`questions.jsonl`) → **26 downloaded** (0.83 MB).
- 26 question images, 0 answer images.
- Years covered (parsed from paper refs): ?.
- Topics (13): Bitki Biyolojisi (plant Biology), Canlılar Ve Çevre (organisms &amp; Environment / Ecology), Canlılarda Enerji Dönüşümleri (energy Transformations In Living Organisms), Canlıların Sınıflandırılması (sistematik)  (classification Of Living Organisms (systematics)), Destek Ve Hareket Sistemi (support &amp; Movement System), Dolaşım Ve Bağışıklık Sistemi (circulatory &amp; Immune System), Endokrin Sistem Ve Hormonlar (endocrine System &amp; Hormones), Genden Proteine (from Gene To Protein), Komünite Ve Popülasyon Ekolojisi (community &amp; Population Ecology), Sindirim Sistemi (digestive System), Sinir Sistemi (nervous System), Solunum Sistemi (respiratory System), Üriner Sistem / Boşaltım Sistemi (urinary/excretory System).
- Harvested at: 2026-10-22T04:38:18+0000.

## INDEX.jsonl fields

`file`, `url` (source), `kind` (question|answer), `sha256`, `bytes`, `content_type`, `status`, `width`/`height`/`format`, `qid` (site list id), `src_qid` (image-store id from the URL path — both id spaces preserved), `qfolder`, `event_key`, `page`, `paper_ref` (site's own reference string), `parsed` {syllabus, paper, season, year, question}, `topics` (verbatim), `mcq_answer`, `category_id`, `subject_id`, `downloaded_at`.

## Integrity

- Every file's SHA-256 recorded at download time in `INDEX.jsonl`.
- Coverage cross-check: 26/26 unique URLs on disk.

## Copyright note

These PNGs reproduce exam-board copyrighted questions via the third-party site exam-mate.com. Experimental research copy only — license review required before any of this content ships (same discipline as `syllabai-pastpapers`).
