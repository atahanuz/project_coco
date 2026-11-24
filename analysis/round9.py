"""Round 9: 12B swarm with doubled per-call limits (32k call / 64k agent / 16k master / 96k context) vs the 16k swarm
on the 64 hard problems (data/hard64_12b.txt).  Paired on the problems the 32k run has finished.

  python analysis/round9.py          (prints a table; writes results/round9_32k.md and results/round9_32k_per_problem.csv)
"""
import csv, json, sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis"), str(ROOT / "calib")]
from analyze import per_sample  # noqa: E402
from compare import interrupted  # noqa: E402
from scaling import maj_at_k  # noqa: E402
from grade_check import is_correct2  # noqa: E402  (closed forms such as 3^{25}+1 evaluated exactly)

HARD = open(ROOT / "data/hard64_12b.txt").read().split()
NEW, OLD = ROOT / "runs/swarm/hard64_12b_swarm_32k", ROOT / "runs/swarm/ng207_12b_swarm"


def finished(d):
    out = {}
    for l in open(d / "results.jsonl"):
        r = json.loads(l)
        if not r.get("error") and not interrupted(d, r):
            out[r["id"]] = r
    return out


def caps(d, pid):
    """worker / master calls by finish reason from the trace log"""
    t = d / f"{pid}__t0" / "trace.json"
    if not t.exists():
        return Counter(), Counter()
    w, m = Counter(), Counter()
    for e in json.load(open(t))["log"]:
        if "finish" in e:
            (m if e["agent"] == "master" else w)[e["finish"]] += 1
    return w, m


def boot(x, n=10000, seed=0):
    rng = np.random.default_rng(seed)
    b = [x[rng.integers(0, len(x), len(x))].mean() for _ in range(n)]
    return np.percentile(b, [2.5, 97.5])


def main():
    new, old, single = finished(NEW), finished(OLD), per_sample(ROOT / "runs/calib/gemma-4-12B-it_think")
    ids = [p for p in HARD if p in new and p in old]
    rows = []
    for pid in ids:
        a, b, ss = new[pid], old[pid], single.get(pid, [])
        wn, mn = caps(NEW, pid)
        wo, mo = caps(OLD, pid)
        rows.append(dict(id=pid, single=np.mean([bool(x["ok"]) for x in ss]) if ss else np.nan,
                         maj=maj_at_k(ss, len(ss)) if ss else np.nan,
                         old=float(bool(b["correct"])), new=float(bool(a["correct"])),
                         old2=float(bool(b["correct"]) or bool(b.get("final") and is_correct2(b["final"], b["gold"]))),
                         new2=float(bool(a["correct"]) or bool(a.get("final") and is_correct2(a["final"], a["gold"]))),
                         old_final=b.get("final") or "", new_final=a.get("final") or "", gold=a.get("gold"),
                         old_tok=b["completion_tokens"], new_tok=a["completion_tokens"],
                         new_min=(a.get("seconds_total") or a.get("seconds") or 0) / 60,
                         new_res=a.get("resumed", 0) or 0,
                         w_len_new=wn["length"], w_new=sum(wn.values()), w_len_old=wo["length"], w_old=sum(wo.values()),
                         m_len_new=mn["length"], m_new=sum(mn.values())))
    n = len(rows)
    A = lambda k: np.array([r[k] for r in rows], dtype=float)
    old_all = [old[p] for p in HARD if p in old]
    lines = [f"# Round 9: 12B swarm, 32k vs 16k per-call limit ({n} of {len(HARD)} hard problems finished)", ""]
    lines.append("Paired on the problems the 32k run has finished. The 16k numbers are the main 12B swarm "
                 "(ng207_12b_swarm) on the same problems.")
    lines.append("")
    lines.append(f"16k swarm on all {len(old_all)} hard problems: {np.mean([bool(r['correct']) for r in old_all]):.3f}, "
                 f"{sum(not r.get('final') for r in old_all)} with no answer.")
    lines.append("")
    lines.append("| | single 12B pass@1 | 12B maj@8 | swarm 16k | swarm 32k |")
    lines.append("|---|---|---|---|---|")
    lines.append(f"| solved | {np.nanmean(A('single')):.3f} | {np.nanmean(A('maj')):.3f} | {A('old').mean():.3f} | {A('new').mean():.3f} |")
    lines.append(f"| solved, closed forms evaluated | | | {A('old2').mean():.3f} | {A('new2').mean():.3f} |")
    lines.append(f"| no answer | | | {sum(not r['old_final'] for r in rows)} | {sum(not r['new_final'] for r in rows)} |")
    lines.append(f"| worker calls cut at the limit | | | {A('w_len_old').sum() / max(1, A('w_old').sum()):.1%} "
                 f"({int(A('w_len_old').sum())}/{int(A('w_old').sum())}) | {A('w_len_new').sum() / max(1, A('w_new').sum()):.1%} "
                 f"({int(A('w_len_new').sum())}/{int(A('w_new').sum())}) |")
    lines.append(f"| completion tokens per problem | | | {A('old_tok').mean() / 1e3:.0f}k | {A('new_tok').mean() / 1e3:.0f}k |")
    d = A("new") - A("old")
    lo, hi = boot(d)
    lines.append("")
    lines.append(f"32k − 16k: {d.mean() * 100:+.1f} points [{lo * 100:+.1f}, {hi * 100:+.1f}] (paired bootstrap, n={n}). "
                 f"Wins {int((d > 0).sum())}, losses {int((d < 0).sum())}, ties {int((d == 0).sum())}.")
    d2 = A("new2") - A("old2"); lo2, hi2 = boot(d2)
    lines.append(f"With closed forms evaluated: {d2.mean() * 100:+.1f} points [{lo2 * 100:+.1f}, {hi2 * 100:+.1f}].")
    lines.append(f"Minutes per problem (32k): median {np.median(A('new_min')):.0f}, max {A('new_min').max():.0f}; "
                 f"{int((A('new_res') > 0).sum())} resumed from a checkpoint.")
    lines.append("")
    lines.append("| problem | gold | 16k answer | 32k answer |")
    lines.append("|---|---|---|---|")
    for r in rows:
        if r["old"] != r["new"] or r["old2"] != r["new2"]:
            f = lambda s, ok: (s[:40] or "no answer") + (" ✓" if ok else " ✗")
            lines.append(f"| {r['id'].replace('imo-bench-', '')} | {str(r['gold'])[:30]} | {f(r['old_final'], r['old'])} | {f(r['new_final'], r['new'])} |")
    txt = "\n".join(lines) + "\n"
    print(txt)
    (ROOT / "results/round9_32k.md").write_text(txt)
    with open(ROOT / "results/round9_32k_per_problem.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    main()
