"""Slide figure for round 12: a 12B checker on the E4B team, with and without two colluding saboteurs (seed-0 order).

  python analysis/plots_checker12.py      -> results/figures/p2_e4b_checker12.png
Left: pass@1 on 207 problems per defense; grey = the same team without saboteurs, coloured = with W3 + W4 colluding.
Right: cumulative count of problems where the team submitted a saboteur's wrong answer (completion order), expulsions marked.
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis")]
from compare import agent_runs  # noqa: E402
from plots import INK, INK2, GRID, S1, S2, MUTED, SURFACE, titles  # noqa: E402
from collusion import records  # noqa: E402
from plots_collusion import expel_events  # noqa: E402

LIGHT = "#b9d1f1"   # lighter step of the S1 ramp: 12B checker without expulsion
# (bar label, line label, run with colluders, control run without saboteurs, colour)
DEF = [("no defense", "no defense", "p2_e4b_col", None, S2),
       ("E4B checker\n+ expel on its\nverdicts", "E4B checker + expel", "p2_e4b_col_ckrep", "p2_e4b_ckrep_nosab", INK2),
       ("12B checker\nonly", "12B checker only", "p2_e4b_col_ck12", "ck12_e4b", LIGHT),
       ("12B checker\n+ expel on its\nverdicts", "12B checker + expel", "p2_e4b_col_ck12rep", "p2_e4b_ck12rep_nosab", S1)]
SABS = {"W3", "W4"}


def seed0(run):
    """trial-0 records of one run (round 12 dropped trial 1 of ck12_e4b)"""
    return [r for r in records(run) if r.get("trial", 0) == 0]


def p1(run):
    return np.mean([bool(r["correct"]) for r in seed0(run)])


def main():
    ref = agent_runs(ROOT / "runs/swarm/ng207_e4b_swarm").p.mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 5.3), gridspec_kw=dict(width_ratios=[1.15, 1]))
    xs = np.arange(len(DEF)); w = 0.36
    vals = []
    for x, (lab, _, col_run, ctl_run, col) in zip(xs, DEF):
        ctl = ref if ctl_run is None else p1(ctl_run)
        sab = p1(col_run)
        vals.append((ctl, sab))
        ax1.bar(x - w / 2 - 0.01, ctl, width=w, color=MUTED, zorder=2)
        ax1.bar(x + w / 2 + 0.01, sab, width=w, color=col, zorder=2)
        for dx, v, bold in ((-w / 2 - 0.01, ctl, False), (w / 2 + 0.01, sab, x == len(DEF) - 1)):
            ax1.text(x + dx, v + 0.01, f"{v:.0%}", ha="center", va="bottom", color=INK, fontsize=11,
                     fontweight="bold" if bold else "normal", zorder=4)
    from matplotlib.patches import Patch
    ax1.legend(handles=[Patch(color=MUTED, label="grey: the same team, no saboteur"),
                        Patch(facecolor="none", edgecolor=INK2, label="coloured: two colluding saboteurs")],
               frameon=False, loc="upper left", labelcolor=INK, fontsize=9.5)
    ax1.set_xticks(xs, [d[0] for d in DEF], color=INK, fontsize=9.5)
    ax1.tick_params(axis="x", length=0)
    ax1.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax1.set_ylim(0, 0.84); ax1.set_xlim(-0.6, len(DEF) - 0.4)
    ax1.grid(axis="y", color=GRID, lw=0.8); ax1.set_axisbelow(True)
    ax1.set_ylabel("problems solved (207)")
    ax1.set_title("E4B team of four; the checker sees only the problem and anonymised candidates", color=INK2,
                  fontsize=10.5, loc="left")

    ends = []
    for _, short, run, _, col in DEF:
        rs = sorted(seed0(run), key=lambda r: r.get("order", 0))
        c = np.cumsum([bool(r.get("final_is_saboteur")) and not r["correct"] for r in rs])
        ax2.plot(np.arange(1, len(c) + 1), c, color=col, lw=2.6 if col == S1 else 2.0, zorder=4 if col == S1 else 3)
        ends.append([c[-1], len(c), short, col])
        ev = expel_events(rs)
        assert not any(wk not in SABS for _, wk in ev), ev
        for k, _ in ev:
            ax2.scatter([k], [c[k - 1]], s=80, marker="v", color=col, edgecolor=SURFACE, linewidth=1.0, zorder=5)
    ends.sort(key=lambda e: e[0])
    for i in range(1, len(ends)):  # keep end labels apart
        ends[i][0] = max(ends[i][0], ends[i - 1][0] + 5)
    for y, n, short, col in ends:
        ax2.annotate(short, (n, y), xytext=(6, 0), textcoords="offset points", va="center", color=INK, fontsize=10)
    ax2.scatter([], [], marker="v", color=INK2, label="saboteur expelled (no honest worker ever was)")
    ax2.legend(frameon=False, loc="upper left", labelcolor=INK, fontsize=9.5)
    ax2.set_xlim(0, 300); ax2.set_xticks([0, 50, 100, 150, 200]); ax2.set_ylim(-2, max(e[0] for e in ends) * 1.2)
    ax2.set_xlabel("problems finished (seed-0 order)")
    ax2.grid(color=GRID, lw=0.8); ax2.set_axisbelow(True)
    ax2.set_title("team submitted a saboteur's wrong answer (cumulative)", color=INK2, fontsize=11, loc="left")
    ctl, sab = vals[-1]
    titles(fig, f"A 12B checker makes the E4B team better and robust: with two colluding saboteurs it still solves {sab:.0%}",
           f"gemma-4-E4B workers, 207 problems, seed-0 order  ·  W3 and W4 back the same wrong answer  ·  "
           f"the plain E4B swarm without saboteurs: {ref:.0%}", top=0.84)
    out = ROOT / "results/figures/p2_e4b_checker12.png"
    fig.savefig(out, dpi=200); plt.close(fig)
    print("wrote", out, [(d[1], round(a, 3), round(b, 3)) for d, (a, b) in zip(DEF, vals)])


if __name__ == "__main__":
    main()
