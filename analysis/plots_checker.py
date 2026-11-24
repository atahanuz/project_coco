"""Slide figure for round 11: two colluding saboteurs vs the round-10 defenses and the blind checker (v4).

  python analysis/plots_checker.py      -> results/figures/p2_e4b_checker.png
Left: pass@1 pooled over the seed-0 and seed-1 problem orders. Right: seed-0 order, cumulative count of problems where
the team submitted a saboteur's wrong answer (completion order), expulsions marked.
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
from plots import INK, INK2, GRID, S1, S2, S3, MUTED, SURFACE, titles  # noqa: E402
from collusion import records  # noqa: E402
from plots_collusion import pass1, expel_events  # noqa: E402

# (label on the bar, label in the line panel, runs, colour, shown in the line panel)
DEF = [("no\ndefense", "no defense", ["p2_e4b_col", "p2_e4b_col_s1"], S2, True),
       ("expel on\npeer\nagreement", "peer agreement", ["p2_e4b_col_peer", "p2_e4b_col_peer_s1"], MUTED, False),
       ("expel on\nthe answer\nkey", "answer key", ["p2_e4b_col_key", "p2_e4b_col_key_s1"], INK2, True),
       ("checker\nonly", "checker only", ["p2_e4b_col_ck", "p2_e4b_col_ck_s1"], S3, True),
       ("checker +\nexpel on its\nverdicts", "checker + expel", ["p2_e4b_col_ckrep", "p2_e4b_col_ckrep_s1"], S1, True)]
SABS = {"W3", "W4"}
LABEL_AT = {"checker + expel": ((75, 8), "left"), "answer key": ((122, 86), "right")}  # empty areas of the line panel


def main():
    ref = agent_runs(ROOT / "runs/swarm/ng207_e4b_swarm").p.mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 5.2), gridspec_kw=dict(width_ratios=[1.05, 1]))
    xs = np.arange(len(DEF))
    for x, (lab, _, runs, col, _) in zip(xs, DEF):
        v = pass1(runs)
        ax1.bar(x, v, width=0.62, color=col, zorder=2)
        ax1.text(x, v + 0.008, f"{v:.0%}", ha="center", va="bottom", color=INK, fontsize=11.5, zorder=4,
                 fontweight="bold" if col == S1 else "normal",
                 bbox=dict(boxstyle="square,pad=0.15", fc=SURFACE, ec="none"))
    ax1.hlines(ref, -0.5, len(DEF) - 0.5, color=INK2, lw=1, ls=(0, (4, 3)), zorder=3)
    ax1.text(-0.45, ref + 0.008, f"no saboteur {ref:.0%}", ha="left", va="bottom", color=INK2, fontsize=9.5)
    ax1.set_xticks(xs, [d[0] for d in DEF], color=INK, fontsize=9.5)
    ax1.tick_params(axis="x", length=0)
    ax1.axvline(2.5, color=GRID, lw=1.2, zorder=1)
    ax1.text(1.0, 0.505, "round 10", ha="center", color=INK2, fontsize=9.5)
    ax1.text(3.5, 0.505, "round 11: blind checker", ha="center", color=INK2, fontsize=9.5)
    ax1.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax1.set_ylim(0, 0.54); ax1.set_xlim(-0.55, len(DEF) - 0.45)
    ax1.grid(axis="y", color=GRID, lw=0.8); ax1.set_axisbelow(True)
    ax1.set_ylabel("problems solved (2 orders pooled)")
    ax1.set_title("two colluding saboteurs in a team of four", color=INK2, fontsize=11, loc="left")

    ends = []
    for _, short, runs, col, show in DEF:
        if not show:
            continue
        rs = sorted(records(runs[0]), key=lambda r: r.get("order", 0))
        c = np.cumsum([bool(r.get("final_is_saboteur")) and not r["correct"] for r in rs])
        ax2.plot(np.arange(1, len(c) + 1), c, color=col, lw=2.6 if col == S1 else 2.0, zorder=4 if col == S1 else 3)
        ends.append([c[-1], len(c), short, col])
        ev = expel_events(rs)
        for k, wk in ev:
            ax2.scatter([k], [c[k - 1]], s=80, marker="v", color=col, edgecolor=SURFACE, linewidth=1.0, zorder=5)
        if ev:
            ks = [k for k, _ in ev]
            assert not any(w not in SABS for _, w in ev), ev
            xy, ha = LABEL_AT[short]
            ax2.annotate(f"W3 and W4 expelled\nafter {min(ks)}–{max(ks)}", (max(ks), c[max(ks) - 1]),
                         xytext=xy, textcoords="data", ha=ha, va="center", color=INK, fontsize=9.5,
                         arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8, shrinkA=2, shrinkB=5))
    ends.sort(key=lambda e: e[0])
    for i in range(1, len(ends)):  # keep end labels apart
        ends[i][0] = max(ends[i][0], ends[i - 1][0] + 6)
    for y, n, short, col in ends:
        ax2.annotate(f"{short}", (n, y), xytext=(6, 0), textcoords="offset points", va="center", color=INK, fontsize=10)
    ax2.scatter([], [], marker="v", color=INK2, label="saboteur expelled (no honest worker ever was)")
    ax2.legend(frameon=False, loc="upper left", labelcolor=INK, fontsize=9.5)
    ax2.set_xlim(0, 262); ax2.set_ylim(-2, max(e[0] for e in ends) * 1.18)
    ax2.set_xlabel("problems finished (seed-0 order)")
    ax2.grid(color=GRID, lw=0.8); ax2.set_axisbelow(True)
    ax2.set_title("team submitted a saboteur's wrong answer (cumulative)", color=INK2, fontsize=11, loc="left")
    titles(fig, "A blind checker replaces the answer key: expelling on its verdicts removes the colluders 3× faster",
           "gemma-4-E4B, 207 problems  ·  W3 and W4 back the same wrong answer  ·  the checker is the same model and sees only "
           "the problem and anonymised candidates", top=0.84)
    out = ROOT / "results/figures/p2_e4b_checker.png"
    fig.savefig(out, dpi=200); plt.close(fig)
    print("wrote", out)


if __name__ == "__main__":
    main()
