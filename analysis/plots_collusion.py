"""Slide figure: one saboteur vs two colluding saboteurs, under no defense / answer-key expulsion / peer-agreement expulsion.

  python analysis/plots_collusion.py      -> results/figures/p2_e4b_collusion.png
Left: pass@1 pooled over the seed-0 and seed-1 problem orders. Right: two colluding saboteurs, seed-0 order: cumulative
count of problems where the team submitted a saboteur's wrong answer (completion order), expulsions marked.
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
from plots import INK, INK2, GRID, S1, S2, MUTED, titles  # noqa: E402
from collusion import records  # noqa: E402

DEF = [("no defense", S2), ("expel, answer key", MUTED), ("expel, peer agreement", S1)]
RUNS = {("one", "no defense"): ["p2_e4b_sab", "p2_e4b_sab_s1"],
        ("one", "expel, answer key"): ["p2_e4b_sab_remove2", "p2_e4b_sab_remove2_s1"],
        ("one", "expel, peer agreement"): ["p2_e4b_sab_peer", "p2_e4b_sab_peer_s1"],
        ("two", "no defense"): ["p2_e4b_col", "p2_e4b_col_s1"],
        ("two", "expel, answer key"): ["p2_e4b_col_key", "p2_e4b_col_key_s1"],
        ("two", "expel, peer agreement"): ["p2_e4b_col_peer", "p2_e4b_col_peer_s1"]}
SABS = {"one": {"W4"}, "two": {"W3", "W4"}}


def pass1(runs):
    v = [np.mean([bool(r["correct"]) for r in rs]) for rs in map(records, runs) if rs]
    return np.mean(v) if v else np.nan


def expel_events(rs):
    """[(problem number, worker)] in completion order"""
    seen, out = set(), []
    for r in sorted(rs, key=lambda r: r.get("order", 0)):
        for w, k in ((r.get("rep_after") or {}).get("removed") or {}).items():
            if w not in seen:
                seen.add(w); out.append((int(k), w))
    return out


def main():
    ref = agent_runs(ROOT / "runs/swarm/ng207_e4b_swarm").p.mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.0), gridspec_kw=dict(width_ratios=[1, 1.1]))
    w = 0.26
    for gi, g in enumerate(["one", "two"]):
        for di, (dname, col) in enumerate(DEF):
            x = gi + (di - 1) * (w + 0.03)
            v = pass1(RUNS[(g, dname)])
            ax1.bar(x, v, width=w, color=col, zorder=2, label=dname if gi == 0 else None)
            ax1.text(x, v + 0.008, f"{v:.0%}", ha="center", va="bottom", color=INK, fontsize=11,
                     fontweight="bold" if col == S1 else "normal")
    ax1.hlines(ref, -0.5, 1.46, color=INK2, lw=1, ls=(0, (4, 3)), zorder=1)
    ax1.text(1.5, ref, f" no\n saboteur\n {ref:.0%}", ha="left", va="center", color=INK2, fontsize=9.5)
    ax1.set_xticks([0, 1], ["one saboteur", "two colluding\nsaboteurs"], color=INK)
    ax1.tick_params(axis="x", length=0)
    ax1.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax1.set_ylim(0, 0.52); ax1.set_xlim(-0.5, 1.82)
    ax1.grid(axis="y", color=GRID, lw=0.8); ax1.set_axisbelow(True)
    ax1.legend(frameon=False, loc="lower left", bbox_to_anchor=(-0.02, 1.0), ncol=3, labelcolor=INK, fontsize=10,
               handlelength=1.0, columnspacing=1.0)
    ax1.set_ylabel("problems solved (2 orders pooled)")

    top, ends = 0, []
    global YMAX
    YMAX = max(10, max(np.sum([bool(r.get("final_is_saboteur")) and not r["correct"] for r in records(RUNS[("two", d)][0])])
                       for d, _ in DEF) * 1.15)
    for dname, col in DEF:
        rs = sorted(records(RUNS[("two", dname)][0]), key=lambda r: r.get("order", 0))
        if not rs:
            continue
        c = np.cumsum([bool(r.get("final_is_saboteur")) and not r["correct"] for r in rs])
        top = max(top, c[-1])
        ax2.plot(np.arange(1, len(c) + 1), c, color=col, lw=2.4 if col != MUTED else 2.0, zorder=3)
        ends.append((c[-1], len(c), dname, col))
        ev = [(k, wk) for k, wk in expel_events(rs) if k <= len(c)]
        for k, wk in ev:
            honest = wk not in SABS["two"]
            ax2.scatter([k], [c[k - 1]], s=110 if honest else 90, marker="X" if honest else "v",
                        color=col, edgecolor=INK2 if col == MUTED else "white", linewidth=1.0, zorder=5)
        if ev:
            ks, ws = [k for k, _ in ev], [w for _, w in ev]
            honest = any(w not in SABS["two"] for w in ws)
            lab = (f"{' and '.join(sorted(ws))} ({'honest' if honest else 'saboteurs'})\nexpelled after {min(ks)}"
                   + (f"–{max(ks)}" if max(ks) != min(ks) else ""))
            k0 = min(ks)
            ax2.annotate(lab, (k0, c[k0 - 1]), xytext=(8, 0.62 * YMAX) if honest else (150, 0.24 * YMAX), textcoords="data",
                         ha="left", va="bottom" if honest else "top", color=INK, fontsize=9.5,
                         arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8, shrinkA=2, shrinkB=6))
    short = {"no defense": "no defense", "expel, answer key": "answer key", "expel, peer agreement": "peer agreement"}
    for y, n, dname, col in ends:
        ax2.annotate(f"{short[dname]}: {int(y)}", (n, y), xytext=(6, 0), textcoords="offset points", va="center",
                     color=INK, fontsize=10.5)
    ax2.scatter([], [], marker="v", color=INK2, label="saboteur expelled")
    ax2.scatter([], [], marker="X", color=INK2, label="honest worker expelled")
    ax2.legend(frameon=False, loc="upper left", labelcolor=INK, fontsize=9.5)
    ax2.set_xlim(0, 270); ax2.set_ylim(-2, YMAX)
    ax2.set_xlabel("problems finished (seed-0 order)")
    ax2.grid(color=GRID, lw=0.8); ax2.set_axisbelow(True)
    ax2.set_title("two colluders: team submitted a saboteur's wrong answer", color=INK2, fontsize=11, loc="left")
    titles(fig, TITLE, "gemma-4-E4B, 207 problems  ·  W3 and W4 know each other and back the same wrong answer  ·  same in both problem orders", top=0.84)
    out = ROOT / "results/figures/p2_e4b_collusion.png"
    fig.savefig(out, dpi=200); plt.close(fig)
    print("wrote", out)


TITLE = "Two colluding saboteurs turn peer reputation against the honest workers; the answer key still works"

if __name__ == "__main__":
    main()
