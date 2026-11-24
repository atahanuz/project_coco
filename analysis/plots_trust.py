"""Slide figure: reputation graded WITHOUT the answer key (peer agreement, v3) vs with it (v2), planted saboteur.

  python analysis/plots_trust.py      -> results/figures/p2_e4b_trust_v3.png
Left: pass@1 pooled over the seed-0 and seed-1 problem orders. Right: cumulative count of problems where the team submitted
the saboteur's wrong answer, seed-0 order, in completion order (the order the reputation saw them), expulsion marked.
"""
import json, sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis")]
from compare import agent_runs, interrupted  # noqa: E402
from plots import INK, INK2, GRID, S1, S2, MUTED, titles  # noqa: E402

CONDS = [("no defense", ["p2_e4b_sab", "p2_e4b_sab_s1"], S2),
         ("expel, graded by answer key", ["p2_e4b_sab_remove2", "p2_e4b_sab_remove2_s1"], MUTED),
         ("expel, graded by peer agreement\n(no answer key)", ["p2_e4b_sab_peer", "p2_e4b_sab_peer_s1"], S1)]


def records(run):
    d = ROOT / "runs/swarm" / run
    rs = [json.loads(l) for l in open(d / "results.jsonl")]
    return [r for r in rs if not r.get("error") and not interrupted(d, r)]


def expelled_at(rs):
    for r in rs:
        rem = (r.get("rep_before") or {}).get("removed")
        if rem:
            return int(next(iter(rem.values())))
    return None


def main():
    ref = agent_runs(ROOT / "runs/swarm/ng207_e4b_swarm").p.mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw=dict(width_ratios=[1, 1.15]))
    rows = [("no saboteur", ref, None)]
    for lab, runs, col in CONDS:
        rows.append((lab, np.mean([np.mean([bool(r["correct"]) for r in records(x)]) for x in runs]), col))
    y = list(range(len(rows)))[::-1]
    for yi, (lab, v, col) in zip(y, rows):
        ax1.barh(yi, v, height=0.62, color=col or GRID, edgecolor=INK2 if col is None else None,
                 linewidth=1 if col is None else 0, zorder=2)
        ax1.text(v + 0.008, yi, f"{v:.1%}", va="center", color=INK, fontsize=12, fontweight="bold" if col == S1 else "normal")
    ax1.set_yticks(y, [r[0] for r in rows], color=INK); ax1.tick_params(axis="y", length=0)
    ax1.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax1.set_xlim(0, 0.55); ax1.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax1.grid(axis="x", color=GRID, lw=0.8); ax1.set_axisbelow(True)
    ax1.set_title("problems solved (2 problem orders pooled)", color=INK2, fontsize=11, loc="left")

    short = {"no defense": "no defense", "expel, graded by answer key": "answer key",
             "expel, graded by peer agreement\n(no answer key)": "peer agreement"}
    top = 0
    for lab, runs, col in CONDS:
        rs = records(runs[0])
        c = np.cumsum([bool(r.get("final_is_saboteur")) and not r["correct"] for r in rs])
        top = max(top, c[-1])
        ax2.plot(np.arange(1, len(c) + 1), c, color=col, lw=2.4 if col != MUTED else 2.0, zorder=3)
        ax2.annotate(f"{short[lab]}: {int(c[-1])}", (len(c), c[-1]), xytext=(6, 0), textcoords="offset points",
                     va="center", color=INK, fontsize=11)
        k = expelled_at(rs)
        if k:
            ax2.scatter([k], [c[k - 1]], s=70, marker="v", color=col, edgecolor="white", linewidth=1.2, zorder=4)
            if col == S1:
                ax2.annotate(f"W4 expelled after {k}", (k, c[k - 1]), xytext=(8, -26), textcoords="offset points",
                             ha="left", va="top", color=INK2, fontsize=9.5,
                             arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8, shrinkA=0, shrinkB=4))
            else:
                ax2.annotate(f"W4 expelled after {k}", (k, c[k - 1]), xytext=(-8, 22), textcoords="offset points",
                             ha="right", va="bottom", color=INK2, fontsize=9.5,
                             arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8, shrinkA=0, shrinkB=4))
    ax2.set_xlim(0, 270); ax2.set_ylim(-2, top * 1.15)
    ax2.set_xlabel("problems finished (seed-0 order)")
    ax2.grid(color=GRID, lw=0.8); ax2.set_axisbelow(True)
    ax2.set_title("team submitted the saboteur's wrong answer (cumulative)", color=INK2, fontsize=11, loc="left")
    titles(fig, "No answer key needed: peer-agreement reputation stops the saboteur as well as the answer checker",
           "gemma-4-E4B, 207 problems  ·  W4 secretly steers the team toward wrong answers  ·  bars: both problem orders pooled",
           top=0.84)
    out = ROOT / "results/figures/p2_e4b_trust_v3.png"
    fig.savefig(out, dpi=200); plt.close(fig)
    print("wrote", out)


if __name__ == "__main__":
    main()
