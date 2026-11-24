"""Grade baseline samples and compute per-problem statistics.

  python calib/analyze.py runs/calib/<RUN> [more run dirs ...]

Reads every samples*.jsonl (and rescue*.jsonl) in the run dir. Writes <run_dir>/per_problem.csv with, for every problem:
  n, correct, p (pass@1 estimate), pass@k, maj (majority-vote answer), maj_ok,
  n_distinct (distinct boxed answers), no_box (samples without a final answer),
  truncated (finish_reason == length), mean completion tokens.
"""
import json, sys
from collections import Counter
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from coco.grading import last_boxed, is_correct, parse_answer

ROOT = Path(__file__).resolve().parents[1]
POOL = {p["id"]: p for p in map(json.loads, open(ROOT / "data/pool.jsonl"))}


def key(ans):
    """Canonical form of an answer, for majority voting."""
    p = parse_answer(ans)
    return None if p is None else repr(p)


def lines(run: Path, prefix: str):
    for f in sorted(run.glob(prefix + "*.jsonl")):
        yield from open(f)


def load_rescue(run: Path):
    """forced answers for truncated samples (calib/rescue.py), keyed by (id, sample)"""
    out = {}
    if True:
        for line in lines(run, "rescue"):
            r = json.loads(line)
            if r.get("error") is None:
                out[(r["id"], r["sample"])] = last_boxed(r["forced"])
    return out


def per_sample(run: Path, forced: bool = True) -> dict:
    """{problem id: [dict(pred, key, ok, trunc, toks, sample), ...]} for auto-gradable problems"""
    return _per_sample(run, forced)


def analyze(run: Path, forced: bool = True) -> pd.DataFrame:
    by = _per_sample(run, forced)
    return _aggregate(by)


def _per_sample(run: Path, forced: bool) -> dict:
    rescue = load_rescue(run) if forced else {}
    rows = {}
    for line in lines(run, "samples"):
        r = json.loads(line)
        if r.get("error") is not None:
            continue
        rows[(r["id"], r["sample"])] = r          # last write wins
    by = {}
    for (pid, s), r in rows.items():
        if not POOL[pid]["autograde"]:
            continue
        gold = POOL[pid]["answer"]
        pred = last_boxed(r.get("content"))
        if pred is None:                       # truncated, or answered without \boxed{}: use the forced answer
            pred = rescue.get((pid, s))
        by.setdefault(pid, []).append(dict(pred=pred, key=key(pred), ok=bool(is_correct(pred, gold)),
                                           trunc=r.get("finish_reason") == "length",
                                           toks=r.get("completion_tokens", 0), sample=s))
    return by


def _aggregate(by: dict) -> pd.DataFrame:
    out = []
    for pid, ss in by.items():
        votes = Counter(x["key"] for x in ss if x["key"] is not None)
        maj_key = votes.most_common(1)[0][0] if votes else None
        maj_ok = any(x["ok"] for x in ss if x["key"] == maj_key) if maj_key else False
        p = POOL[pid]
        out.append(dict(id=pid, category=p["category"], subcategory=p["subcategory"], source=p["source"],
                        answer=p["answer"], n=len(ss), correct=sum(x["ok"] for x in ss),
                        p=sum(x["ok"] for x in ss) / len(ss), pass_k=any(x["ok"] for x in ss),
                        maj=next((x["pred"] for x in ss if x["key"] == maj_key), None), maj_ok=maj_ok,
                        n_distinct=len(votes), no_box=sum(x["pred"] is None for x in ss),
                        truncated=sum(x["trunc"] for x in ss), mean_toks=round(sum(x["toks"] for x in ss) / len(ss))))
    return pd.DataFrame(out).sort_values("id")


def summary(df: pd.DataFrame, name: str):
    print(f"\n=== {name}: {len(df)} problems, {int(df.n.sum())} samples")
    print(f"pass@1 {df.p.mean():.3f} | maj@k {df.maj_ok.mean():.3f} | pass@k {df.pass_k.mean():.3f} | "
          f"truncated {df.truncated.sum() / df.n.sum():.3f} | no box {df.no_box.sum() / df.n.sum():.3f} | "
          f"mean tokens {df.mean_toks.mean():.0f}")
    g = df.groupby("category").agg(n=("id", "size"), pass1=("p", "mean"), maj=("maj_ok", "mean"), passk=("pass_k", "mean"))
    print(g.round(3).to_string())
    k = int(df.n.max())
    print("solve-count histogram (correct out of k):", df.correct.value_counts().sort_index().to_dict())
    hidden = df[(df.pass_k) & (~df.maj_ok)]
    print(f"'hidden knowledge' (pass@{k} but majority wrong): {len(hidden)}")


if __name__ == "__main__":
    for run in map(Path, sys.argv[1:]):
        summary(analyze(run, forced=False), run.name + " [strict: truncated = wrong]")
        if any(run.glob("rescue*.jsonl")):
            df = analyze(run, forced=True)
            summary(df, run.name + " [budget-forced answers for truncated samples]")
        else:
            df = analyze(run, forced=False)
        df.to_csv(run / "per_problem.csv", index=False)
