#!/usr/bin/env python3
"""Image-phase driver for the SPLIT-STORAGE layout (2026-10-22+).

Sister-repo split:
    READ root  — syllabai-experimental  (questions.jsonl, progress.json,
                source-of-record for questions; local checkout is sparse —
                its images/ dirs are NOT materialized, they live on GitHub)
    OUT root   — THIS repo (syllabai-experimental-2): all image downloads
                from 2026-10-22 onward land here, under
                exam-mate/resources/topical_papers/topical/... mirroring
                the sister repo's subject-dir layout.

Subjects whose image sets are already complete in the sister repo are
recorded in resources/topical_papers/source_completed.json and skipped.
Within-subject resume is automatic (images/INDEX.jsonl + file-size checks);
subjects killed mid-download resume cleanly on the next run.

Chunk-safe: killed at any moment, resumes at subject granularity.

Usage: python3 exam_mate_images_all.py            # loop until killed
       python3 exam_mate_images_all.py --status
       python3 exam_mate_images_all.py --cats 3,4,21
"""
import json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SISTER = "/home/z/my-project/syllabai-experimental"
BULK = os.path.join(HERE, "exam_mate_image_bulk.py")
OUT_TP = os.path.join(REPO, "exam-mate", "resources", "topical_papers")
SOURCE_TP = os.path.join(SISTER, "exam-mate", "resources", "topical_papers")
DEFAULT_STATE = os.path.join(OUT_TP, "images_progress.json")
SOURCE_COMPLETED = os.path.join(OUT_TP, "source_completed.json")
TIER_A = ["4", "21", "3"]
TIER_B = ["5", "6", "14", "15", "16", "17", "18", "19", "7", "13", "53", "54", "55"]


def load_state(state_file):
    if os.path.exists(state_file):
        return json.load(open(state_file))
    return {"done": {}, "current": None}


def load_source_completed():
    if os.path.exists(SOURCE_COMPLETED):
        return set(json.load(open(SOURCE_COMPLETED)).get("done_keys", []))
    return set()


def out_dir_of(src_dir):
    """OUT-root subject dir corresponding to a READ-root (sister) dir."""
    rel = os.path.relpath(src_dir, SOURCE_TP)
    return os.path.join(OUT_TP, rel)


def work_list(cats):
    """(image_url_count, 'cat:subj', source_subject_dir) biggest-first."""
    p = json.load(open(os.path.join(SOURCE_TP, "progress.json")))
    import glob
    items = []
    for key, info in p["done"].items():
        cid = key.split(":")[0]
        if cid not in cats:
            continue
        cands = glob.glob(
            f"{SOURCE_TP}/topical/{cid}_*/{key.split(':')[1]}_*/questions.jsonl")
        if not cands:
            continue
        n = 0
        for l in open(cands[0]):
            r = json.loads(l).get("payload", {})
            n += len(r.get("question_images", [])) + len(r.get("answer_images", []))
        if n == 0:
            continue
        items.append((n, key, os.path.dirname(cands[0])))
    items.sort(reverse=True)
    return items


def unique_urls(src_dir):
    """Unique downloadable URLs — STANDARD scheme only.

    Deliberately excludes /media/questions/ refs: already-completed
    subjects have their PNGs shed from the working tree (skip-worktree;
    files live on GitHub), and the bulk resume re-downloads anything
    INDEX-200-but-missing-on-disk. Counting media refs here would flip
    every completed subject to incomplete and trigger full re-downloads.
    Media refs ARE harvested for subjects whose standard count is 0
    (e.g. Turkish YKS-TYT), where the bulk task builder handles them.
    """
    from urllib.parse import urlparse
    import re
    pat = re.compile(r"^/questions/(\d+)/(\d+)/([^/]+\.png)$")
    urls = set()
    for l in open(os.path.join(src_dir, "questions.jsonl")):
        p = json.loads(l).get("payload", {})
        for u in p.get("question_images", []) + p.get("answer_images", []):
            if pat.match(urlparse(u).path):
                urls.add(u)
    return len(urls)


def subject_complete(key, src_dir):
    if key in load_source_completed():
        return True
    out = out_dir_of(src_dir)
    s = os.path.join(out, "images", "_summary.json")
    idxp = os.path.join(out, "images", "INDEX.jsonl")
    if not os.path.exists(s) or not os.path.exists(idxp):
        return False
    try:
        summ = json.load(open(s))
        # every successful file present on disk
        if not (summ.get("index_entries", 0) > 0
                and summ.get("files_on_disk") == summ.get("index_entries")):
            return False
        # every unique URL attempted (ok or genuine origin fail) — counted
        # from the RAW ledger, last entry per URL wins (summary.failed is
        # always 0 because the compacted index only keeps status-200 rows)
        best = {}
        for l in open(idxp):
            try:
                e = json.loads(l)
            except Exception:
                continue
            u = e.get("url")
            if u:
                best[u] = e
        ok = sum(1 for e in best.values() if e.get("status") == 200)
        fail = len(best) - ok
        return ok + fail >= unique_urls(src_dir) - 2  # -2 ledger-dupe tolerance
    except Exception:
        return False


def main(cats, state_file, batch, delay):
    st = load_state(state_file)
    items = work_list(cats)
    todo = [(n, k, d) for n, k, d in items if not subject_complete(k, d)]
    print(f"[images-all] subjects with images todo: {len(todo)} "
          f"(done already: {len(st['done'])} here + "
          f"{len(load_source_completed())} in sister repo)", flush=True)
    for n, key, src in todo:
        if subject_complete(key, src):
            continue
        print(f"[images-all] == {key} ({n} urls) {os.path.basename(src)}",
              flush=True)
        r = subprocess.run(
            [sys.executable, BULK, "--phase", "all",
             "--subject-dir", os.path.relpath(src, SOURCE_TP),
             "--questions-from", os.path.join(src, "questions.jsonl"),
             "--batch", str(batch), "--delay", str(delay)],
            cwd=HERE, capture_output=True, text=True)
        if subject_complete(key, src):
            summ = json.load(open(os.path.join(
                out_dir_of(src), "images", "_summary.json")))
            st["done"][key] = {"entries": summ["index_entries"],
                               "mb": round(summ["total_bytes"] / 1e6, 1)}
            print(f"[images-all] DONE {key}: {summ['index_entries']} images "
                  f"({summ['total_bytes']/1e6:.1f} MB)", flush=True)
        else:
            tail = "\n".join((r.stdout or "").splitlines()[-3:])
            print(f"[images-all] PARTIAL {key} (resumable) rc={r.returncode}\n{tail}",
                  flush=True)
        json.dump(st, open(state_file, "w"), indent=1, ensure_ascii=False)
    print("[images-all] all subjects processed", flush=True)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--cats", default=",".join(TIER_A + TIER_B))
    ap.add_argument("--state-file", default=DEFAULT_STATE)
    ap.add_argument("--batch", type=int, default=6)
    ap.add_argument("--delay", type=float, default=0.7)
    a = ap.parse_args()
    if a.status:
        st = load_state(a.state_file)
        n = sum(v["entries"] for v in st["done"].values())
        mb = sum(v["mb"] for v in st["done"].values())
        print(f"subjects imaged here: {len(st['done'])} | images: {n} | "
              f"{mb:.0f} MB | +{len(load_source_completed())} subjects in "
              f"sister repo")
        sys.exit(0)
    main(a.cats.split(","), a.state_file, a.batch, a.delay)
