"""Compute-scaling and ablation figures for the swarm.

  python analysis/scaling.py --calib runs/calib/gemma-4-E4B-it_think --out results/figures/e4b_ng207 \
      --swarm 2=runs/swarm/ng207_e4b_swarm_w2 4=runs/swarm/ng207_e4b_swarm 8=runs/swarm/ng207_e4b_swarm_w8 \
      --ablate "one round=runs/swarm/ng207_e4b_swarm_r1" "no shared notes=runs/swarm/ng207_e4b_swarm_noshare" \
      --solo runs/swarm/ng207_e4b_solo --title "gemma-4-E4B, 207 problems"

1) <out>_scaling.png: accuracy vs completion tokens per problem. Single model with majority vote over k samples
   (exact expectation over all k-subsets of the 8 samples, ties split evenly) vs swarm with 2/4/8 workers.
2) <out>_ablations.png: pass@1 difference vs the 4-worker swarm, paired bootstrap 95% CI over problems.
All numbers use only problems that every run completed.
"""
import argparse, sys
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "analysis"))
sys.path.insert(0, str(ROOT / "calib"))
from compare import agent_runs  # noqa: E402
from analyze import per_sample  # noqa: E402
from ablations import boot  # noqa: E402
import plots  # noqa: E402  (rcParams, palette, titles)
from plots import plt, S1, S2, MUTED, INK, INK2, GRID, SURFACE, titles  # noqa: E402
import matplotlib  # noqa: E402


def maj_at_k(ss, k):
    """expected majority-vote correctness over all k-subsets; ties split evenly; no-answer samples never win"""
    vals = []
    for sub in combinations(ss, k):
        v = Counter(x["key"] for x in sub if x["key"] is not None)
        if not v:
            vals.append(0.0); continue
        top = max(v.values())
        winners = [kk for kk, c in v.items() if c == top]
        ok = {x["key"] for x in sub if x["ok"]}
        vals.append(sum(w in ok for w in winners) / len(winners))
    return float(np.mean(vals))


def main(a):
    by = per_sample(Path(a.calib))
    swarm = {int(k): agent_runs(p) for k, p in (s.split("=", 1) for s in a.swarm)}
    ablate = {k: agent_runs(p) for k, p in (s.split("=", 1) for s in a.ablate)}
    solo = agent_runs(a.solo) if a.solo else None
    sets = [set(r.index) for r in list(swarm.values()) + list(ablate.values())] + [{i for i, ss in by.items() if len(ss) == 8}]
    if solo is not None:
        sets.append(set(solo.index))
    ids = sorted(set.intersection(*sets))
    toks1 = np.mean([np.mean([x["toks"] for x in by[i]]) for i in ids])
    ks = [1, 2, 4, 8]
    maj = {k: np.mean([maj_at_k(by[i], k) for i in ids]) for k in ks}
    p1 = np.mean([np.mean([x["ok"] for x in by[i]]) for i in ids])
    maj[1] = p1                                   # k=1 is plain pass@1 (also counts no-answer samples as wrong)
    sw = {w: (r.loc[ids].toks.mean(), r.loc[ids].p.mean()) for w, r in sorted(swarm.items())}
    ab = {n: (r.loc[ids].toks.mean(), r.loc[ids].p.mean()) for n, r in ablate.items()}

    print(f"{len(ids)} problems")
    for k in ks:
        print(f"  single maj@{k}: {maj[k]:.3f} at {k * toks1 / 1000:.1f}k tokens")
    for w, (t, p) in sw.items():
        print(f"  swarm {w} workers: {p:.3f} at {t / 1000:.1f}k tokens")
    for n, (t, p) in ab.items():
        print(f"  swarm, {n}: {p:.3f} at {t / 1000:.1f}k tokens")
    if solo is not None:
        print(f"  solo + python: {solo.loc[ids].p.mean():.3f} at {solo.loc[ids].toks.mean() / 1000:.1f}k tokens")

    # ---- 1) scaling
    fig, ax = plt.subplots(figsize=(8.6, 4.9))
    xs, ys = [k * toks1 / 1000 for k in ks], [maj[k] for k in ks]
    ax.plot(xs, ys, color=S2, lw=2, zorder=2, label="Single model, majority vote of k samples")
    ax.scatter(xs, ys, s=70, color=S2, edgecolor=SURFACE, linewidth=2, zorder=3)
    for k, x, y in zip(ks, xs, ys):
        ax.annotate(f"k={k}", (x, y), xytext=(0, -17), textcoords="offset points", ha="center", color=INK2, fontsize=10)
    xs, ys = [t / 1000 for t, _ in sw.values()], [p for _, p in sw.values()]
    ax.plot(xs, ys, color=S1, lw=2, zorder=2, label="Swarm, 1 master + W workers")
    ax.scatter(xs, ys, s=80, color=S1, edgecolor=SURFACE, linewidth=2, zorder=3)
    for w, x, y in zip(sw, xs, ys):
        ax.annotate(f"W={w}", (x, y), xytext=(0, 9), textcoords="offset points", ha="center", color=INK, fontsize=10,
                    fontweight="bold")
    for n, (t, p) in ab.items():
        ax.scatter(t / 1000, p, s=70, facecolor=SURFACE, edgecolor=S1, linewidth=2, zorder=3)
        ax.annotate(f"swarm, {n}", (t / 1000, p), xytext=(-9, 7), textcoords="offset points", ha="right", color=INK2,
                    fontsize=10)
    if solo is not None:
        t, p = solo.loc[ids].toks.mean() / 1000, solo.loc[ids].p.mean()
        ax.scatter(t, p, s=70, color=MUTED, edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.annotate("solo agent + Python", (t, p), xytext=(8, -12), textcoords="offset points", color=INK2, fontsize=10)
    ax.set_xlabel("completion tokens per problem (thousands)")
    ax.set_ylabel("problems solved (pass@1)")
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xlim(0, max(max(xs), 8 * toks1 / 1000) * 1.12)
    lo = min(list(maj.values()) + ([solo.loc[ids].p.mean()] if solo is not None else []))
    ax.set_ylim(lo - 0.06, max(ys) + 0.06)
    ax.grid(color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, labelcolor=INK, handlelength=1.6)
    titles(fig, "At equal compute, a swarm beats majority voting, and it keeps scaling with workers", a.title, top=0.84)
    fig.savefig(a.out + "_scaling.png", dpi=200); plt.close(fig)

    # ---- 2) ablations: difference vs the 4-worker swarm
    ref = swarm[4].loc[ids].p
    rows = [(f"{w} workers instead of 4", swarm[w].loc[ids].p) for w in sorted(swarm) if w != 4]
    rows += [(n[0].upper() + n[1:], r.loc[ids].p) for n, r in ablate.items()]
    rows = sorted(rows, key=lambda r: (r[1] - ref).mean())
    fig, ax = plt.subplots(figsize=(8.6, 0.7 * len(rows) + 1.9))
    his, los = [], []
    for yi, (lab, p) in enumerate(rows):
        d = p - ref
        lo_, hi_ = boot(d)
        sig = lo_ > 0 or hi_ < 0
        ax.plot([lo_, hi_], [yi, yi], color=S1 if sig else MUTED, lw=2.2, solid_capstyle="round", zorder=2)
        ax.scatter(d.mean(), yi, s=90, color=S1 if sig else MUTED, edgecolor=SURFACE, linewidth=2, zorder=3)
        his.append(hi_); los.append(lo_)
        ax.annotate(f"{d.mean() * 100:+.1f} pts", (hi_, yi), xytext=(8, 0),
                    textcoords="offset points", va="center", color=INK, fontsize=10)
    ax.axvline(0, color=INK2, lw=1)
    ax.set_yticks(range(len(rows)), [r[0] for r in rows], color=INK)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v * 100:+.0f}" if abs(v) > 1e-9 else "0"))
    ax.set_xlabel("change in problems solved vs the default swarm (percentage points, 95% CI)")
    ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.set_xlim(min(los + [0]) - 0.01, max(his + [0]) + 0.035)
    titles(fig, "Multiple rounds matter most; shared notes likely help",
           a.title + "  ·  default: 4 workers, 3 rounds, shared notes  ·  blue: CI excludes 0",
           top=0.80 if len(rows) < 5 else 0.84)
    fig.savefig(a.out + "_ablations.png", dpi=200); plt.close(fig)
    print("wrote", a.out + "_scaling.png", a.out + "_ablations.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--calib", required=True)
    ap.add_argument("--swarm", nargs="+", required=True, help="W=run_dir; must include 4")
    ap.add_argument("--ablate", nargs="*", default=[], help="label=run_dir")
    ap.add_argument("--solo", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default="")
    main(ap.parse_args())
