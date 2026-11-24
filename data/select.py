"""Select the COCO benchmark from the pool, using baseline statistics + cooperation tags.

  python data/select.py runs/calib/<RUN>/per_problem.csv [--target 50]

Selection rules (see DATA_SELECTION.md):
  1. auto-gradable answer, not geometry
  2. headroom w.r.t. the single small model (k samples, thinking on):
       sweet spot : 1 <= correct <= SWEET_MAX     -> keep (cooperation can lift an unreliable solver)
       hard       : correct == 0                   -> keep only if mode in {E, C} (code can crack it)
       easy       : correct >  SWEET_MAX           -> drop (no room to improve)
  3. tag each kept problem with its cooperation mode (E / N / C / R) and bucket
Writes data/coco_bench_v0.jsonl and data/coco_bench_v0.csv.
"""
import argparse, json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
MODE_NAMES = {"E": "explore", "N": "numeric", "C": "compute", "R": "reasoning"}


def load_tags():
    tags = {}
    for line in open(ROOT / "coop_tags.txt"):
        if line.startswith("#") or not line.strip():
            continue
        k, m = line.split()[:2]
        tags["imo-bench-" + k] = m
    return tags


def main(a):
    pool = {p["id"]: p for p in map(json.loads, open(ROOT / "pool.jsonl"))}
    tags = load_tags()
    st = pd.read_csv(a.stats)
    k = int(st.n.max())
    st = st[st.n == k]                                   # only fully sampled problems
    st = st[st.id.map(lambda i: pool[i]["autograde"] and pool[i]["category"] != "Geometry")]
    st["mode"] = st.id.map(tags)

    def bucket(r):
        if 1 <= r.correct <= a.sweet_max:
            return "sweet"
        if r.correct == 0:
            return "hard"
        return "easy"

    st["bucket"] = st.apply(bucket, axis=1)
    st["hidden"] = st.pass_k & ~st.maj_ok                # someone found it, majority vote misses it
    keep = st[(st.bucket == "sweet") | ((st.bucket == "hard") & st["mode"].isin(["E", "C"]))].copy()

    # rank: hidden-knowledge first, then sweet spot, then by how explorable the problem is
    pri = {"E": 0, "N": 1, "C": 2, "R": 3}
    keep["rank"] = (~keep.hidden).astype(int) * 10 + (keep.bucket != "sweet").astype(int) * 5 + keep["mode"].map(pri)
    keep = keep.sort_values(["rank", "p"], ascending=[True, False])
    if a.target and len(keep) > a.target:
        keep = keep.head(a.target)

    print(f"pool after filters: {len(st)} | kept {len(keep)} (k={k})")
    print(pd.crosstab(st.bucket, st["mode"], margins=True))
    print("\nselected:")
    print(pd.crosstab(keep.category, keep["mode"], margins=True))
    print(f"selected baseline pass@1 {keep.p.mean():.3f}, maj@{k} {keep.maj_ok.mean():.3f}, pass@{k} {keep.pass_k.mean():.3f}")

    out = []
    for _, r in keep.sort_values("id").iterrows():
        p = dict(pool[r.id])
        p.update(coop_mode=MODE_NAMES[r["mode"]], bucket=r.bucket, hidden_knowledge=bool(r.hidden),
                 baseline=dict(model=a.model, k=k, correct=int(r.correct), maj_ok=bool(r.maj_ok)))
        out.append(p)
    with open(ROOT / f"{a.name}.jsonl", "w") as f:
        for p in out:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    keep.drop(columns=["rank"]).to_csv(ROOT / f"{a.name}.csv", index=False)
    print(f"wrote data/{a.name}.jsonl ({len(out)} problems)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("stats")
    ap.add_argument("--target", type=int, default=0)
    ap.add_argument("--sweet-max", type=int, default=5)
    ap.add_argument("--model", default="gemma-4-12B-it")
    ap.add_argument("--name", default="coco_bench_v0")
    main(ap.parse_args())
