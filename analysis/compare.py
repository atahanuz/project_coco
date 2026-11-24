"""Single model (no tools) vs solo agent (+python) vs swarm, per problem and aggregated.

  python analysis/compare.py --calib runs/calib/gemma-4-E4B-it_think \
      --solo runs/swarm/ng207_e4b_solo --swarm runs/swarm/ng207_e4b_swarm --out results/e4b_ng207

Only problems that have results for all three methods are compared. Breakdowns: category, cooperation tag
(data/coop_tags.txt), and difficulty bucket = how many of the k baseline samples were correct.
Writes <out>_per_problem.csv and <out>_summary.md (also printed).
"""
import argparse, json, sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "calib"))
from analyze import analyze, load_rescue, lines  # noqa: E402
from coco.grading import is_correct, last_boxed  # noqa: E402

TAGS = {"imo-bench-" + l.split()[0]: l.split()[1] for l in open(ROOT / "data/coop_tags.txt")
        if l.strip() and not l.startswith("#")}
TAG_NAME = {"E": "E explore", "N": "N numeric", "C": "C compute", "R": "R reasoning"}


def interrupted(d, r):
    """attempt cut off by a dead server (old code recorded these as finished attempts with no answer)"""
    if r.get("reason") != "limit" and r.get("calls", 1) != 0:
        return False
    t = Path(d) / f"{r['id']}__t{r['trial']}" / "trace.json"
    return r.get("calls", 1) == 0 or (t.exists() and "APIConnectionError" in t.read_text())


def agent_runs(d):
    rs = [json.loads(l) for l in open(Path(d) / "results.jsonl")]
    rs = [r for r in rs if not r.get("error") and not interrupted(d, r)]
    df = pd.DataFrame(rs)
    g = df.groupby("id")
    return pd.DataFrame(dict(n=g.size(), correct=g.correct.sum(), p=g.correct.mean(), toks=g.completion_tokens.mean(),
                             anycand=g.any_candidate_correct.mean()))


def heldout(calib):
    """per problem: correct count on samples 0-3 (used only for bucketing) and pass@1 on samples 4-7 (measurement)"""
    run, pool = Path(calib), {p["id"]: p for p in map(json.loads, open(ROOT / "data/pool.jsonl"))}
    rescue, rows = load_rescue(run), {}
    for line in lines(run, "samples"):
        r = json.loads(line)
        if r.get("error") is None:
            rows[(r["id"], r["sample"])] = r
    ok = {}
    for (pid, smp), r in rows.items():
        pred = last_boxed(r.get("content")) or rescue.get((pid, smp))
        ok.setdefault(pid, {})[smp] = bool(is_correct(pred, pool[pid]["answer"]))
    out = {}
    for pid, d in ok.items():
        a, b = [d[i] for i in range(4) if i in d], [d[i] for i in range(4, 8) if i in d]
        if len(a) == 4 and len(b) == 4:
            out[pid] = (sum(a), sum(b) / 4)
    return out


def bucket(c, n):
    f = c / n
    return "0/8 (unsolved)" if c == 0 else "1-2/8 (hard)" if f <= 0.25 else "3-5/8 (medium)" if f <= 0.625 else "6-8/8 (easy)"


def table(df, by, title):
    rows = []
    for key, g in ([("all", df)] if by is None else df.groupby(by)):
        rows.append(dict(group=key, problems=len(g), single_pass1=g.base_p.mean(), single_maj8=g.maj_ok.mean(),
                         solo_pass1=g.solo_p.mean(), swarm_pass1=g.swarm_p.mean(),
                         swarm_minus_single=g.swarm_p.mean() - g.base_p.mean()))
    t = pd.DataFrame(rows)
    s = f"\n### {title}\n\n| {by or ''} | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |\n|---|---|---|---|---|---|---|\n"
    for r in t.itertuples():
        s += (f"| {r.group} | {r.problems} | {r.single_pass1:.3f} | {r.single_maj8:.3f} | {r.solo_pass1:.3f} | "
              f"**{r.swarm_pass1:.3f}** | {r.swarm_minus_single:+.3f} |\n")
    return s


def main(a):
    base = analyze(Path(a.calib)).set_index("id")
    solo, swarm = agent_runs(a.solo), agent_runs(a.swarm)
    ids = sorted(set(base.index) & set(solo.index) & set(swarm.index))
    df = pd.DataFrame(index=ids)
    df["category"] = base.loc[ids, "category"]
    df["tag"] = [TAG_NAME.get(TAGS.get(i, "?"), "?") for i in ids]
    df["base_n"], df["base_correct"], df["base_p"] = base.loc[ids, "n"], base.loc[ids, "correct"], base.loc[ids, "p"]
    df["maj_ok"], df["base_toks"] = base.loc[ids, "maj_ok"].astype(float), base.loc[ids, "mean_toks"]
    for name, src in (("solo", solo), ("swarm", swarm)):
        for c in ("n", "correct", "p", "toks"):
            df[f"{name}_{c}"] = src.loc[ids, c]
    df["swarm_anycand"] = swarm.loc[ids, "anycand"]
    df["difficulty"] = [bucket(c, n) for c, n in zip(df.base_correct, df.base_n)]

    out = f"## {Path(a.swarm).name} vs {Path(a.solo).name} vs {Path(a.calib).name}\n\n"
    out += (f"{len(ids)} problems with all three results (baseline {len(base)}, solo {len(solo)}, swarm {len(swarm)}).\n\n"
            f"Mean completion tokens per attempt: single {df.base_toks.mean():,.0f} (maj@8: {8 * df.base_toks.mean():,.0f}), "
            f"solo {df.solo_toks.mean():,.0f}, swarm {df.swarm_toks.mean():,.0f}.\n"
            f"Swarm: the right answer appeared among the worker candidates in {df.swarm_anycand.mean():.3f} of attempts.\n")
    out += table(df, None, "Overall")
    out += table(df, "difficulty", "By single-model difficulty (correct out of 8 baseline samples)")
    out += table(df, "category", "By category")
    out += table(df, "tag", "By cooperation tag")
    ho = heldout(a.calib)
    if ho:
        h = df.loc[[i for i in df.index if i in ho]].copy()
        h["ho_bucket"] = [("0/4" if ho[i][0] == 0 else "1/4" if ho[i][0] == 1 else "2-3/4" if ho[i][0] <= 3 else "4/4")
                          + " of samples 0-3" for i in h.index]
        h["base_p"] = [ho[i][1] for i in h.index]          # single-model pass@1 measured on samples 4-7 only
        df.loc[h.index, "ho_bucket"], df.loc[h.index, "ho_base_p"] = h["ho_bucket"], h["base_p"]
        out += table(h, "ho_bucket", "Held-out difficulty: buckets from baseline samples 0-3, single pass@1 from samples 4-7 "
                                     "(maj@8 column still uses all 8, so ignore it here)")
    head = df[df.base_correct <= 0.625 * df.base_n]
    out += table(head, None, f"Headroom subset: problems the single model solves in at most 5 of 8 samples ({len(head)})")
    print(out)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(a.out + "_per_problem.csv")
        Path(a.out + "_summary.md").write_text(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--calib", required=True)
    ap.add_argument("--solo", required=True)
    ap.add_argument("--swarm", required=True)
    ap.add_argument("--out", default="")
    main(ap.parse_args())
