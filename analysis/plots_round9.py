"""Slide figure for round 9: 12B swarm with a 16k vs 32k per-call token limit on the 64 hard problems.

  python analysis/round9.py && python analysis/plots_round9.py      -> results/figures/12b_round9_limit.png
Reads results/round9_32k_per_problem.csv. Solved = graded with closed forms evaluated (grade_check.is_correct2).
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "analysis")]
from plots import INK, INK2, GRID, S1, S2, MUTED, SURFACE, titles  # noqa: E402


def main():
    d = pd.read_csv(ROOT / "results/round9_32k_per_problem.csv", keep_default_na=False)
    n = len(d)
    rows = []
    for lab, ok, fin, wl, wt, tok in [("swarm, 16k tokens\nper call", "old2", "old_final", "w_len_old", "w_old", "old_tok"),
                                      ("swarm, 32k tokens\nper call", "new2", "new_final", "w_len_new", "w_new", "new_tok")]:
        solved = d[ok].astype(float).sum()
        none = (d[fin].astype(str).str.strip() == "").sum()
        rows.append((lab, solved / n, (n - solved - none) / n, none / n,
                     d[wl].astype(float).sum() / d[wt].astype(float).sum(), d[tok].astype(float).mean()))
    single = pd.to_numeric(d.single, errors="coerce").mean()
    maj = pd.to_numeric(d.maj, errors="coerce").mean()

    fig, ax = plt.subplots(figsize=(10.5, 3.9))
    ys = [1, 0]
    for y, (lab, s, w, na, cut, tok) in zip(ys, rows):
        left = 0
        for v, col, txt, tc in [(s, S1, f"solved {s:.0%}", "white"), (w, MUTED, f"wrong answer {w:.0%}", INK),
                                (na, S2, f"no answer\n{na:.0%}", INK)]:
            if v <= 0:
                continue
            ax.barh(y, v, left=left, height=0.58, color=col, edgecolor=SURFACE, linewidth=2, zorder=2)
            if v >= 0.09:
                ax.text(left + v / 2, y, txt, ha="center", va="center", color=tc, fontsize=11,
                        fontweight="bold" if col == S1 else "normal")
            left += v
        ax.text(1.02, y, f"{cut:.0%} of worker calls cut off\n{tok / 1e3:.0f}k tokens per problem", ha="left",
                va="center", color=INK2, fontsize=10, transform=ax.get_yaxis_transform())
    ax.axvline(single, color=INK2, lw=1, ls=(0, (4, 3)), zorder=1)
    ax.text(single, 1.43, f"  single 12B answer {single:.0%}, majority of 8 {maj:.0%}", ha="left", va="bottom",
            color=INK2, fontsize=10)
    ax.set_yticks(ys, [r[0] for r in rows], color=INK)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, 1); ax.set_ylim(-0.5, 1.62)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.set_xlabel(f"share of the {n} hard problems")
    titles(fig, "Doubling the 12B swarm's token limit fills in the missing answers, mostly with wrong ones",
           f"gemma-4-12B, 1 master + 4 workers  ·  the {n} problems a single 12B answer solves at most 3 of 8 times", top=0.80)
    fig.subplots_adjust(right=0.78)
    out = ROOT / "results/figures/12b_round9_limit.png"
    fig.savefig(out, dpi=200); plt.close(fig)
    print("wrote", out, [(r[0].split(",")[1].split()[0], round(r[1], 3), round(r[3], 3)) for r in rows])


if __name__ == "__main__":
    main()
