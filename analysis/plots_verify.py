"""Slide figure for rounds 13-14: a blind checker picks among the pooled 12B answers; how much depends on the checker.

  python analysis/plots_verify.py      -> results/figures/12b_checker_ladder.png
Left: pass@1 on all 207 problems (pre-registered selection rule, §9.10); last bar = round 15 (§9.12): the pool plus
the 31B's own 4 answers, checked twice by the 31B, verdicts combined by the pre-registered pick_multi. Right: the checker's verdicts on the same
candidates: share of right answers it REFUTED and of wrong answers it CONFIRMED.
"""
import json, sys
from collections import Counter
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis"), str(ROOT / "calib")]
from plots import INK, INK2, GRID, S1, S2, MUTED, SURFACE, titles  # noqa: E402
from adaptive import problem_rows  # noqa: E402
from verify_pool import pool_of, pick, pick_multi, rows_of  # noqa: E402
from scaling import maj_at_k  # noqa: E402
from analyze import per_sample  # noqa: E402

CHECKERS = [("12B", "verify_12b"), ("26B-A4B", "verify_12b_c26"), ("31B", "verify_12b_c31")]


def run_scores(rows, name):
    res = {}
    for l in open(ROOT / "runs/swarm" / name / "results.jsonl"):
        x = json.loads(l)
        if not x.get("error"):
            res[x["id"]] = x
    acc, tab, n_chk = [], Counter(), 0
    for r in rows:
        c = pool_of(r)
        if len(c) <= 1:
            acc.append(float(any(e["ok"] for e in c.values())) if c else 0.0); continue
        if r["id"] not in res:        # not checked (yet): fall back to the same vote without a checker
            acc.append(pick(c, {}, 2)); continue
        n_chk += 1
        verd = {v["key"]: v["result"] for v in res[r["id"]]["verdicts"]}
        acc.append(pick(c, verd, 2))
        for v in res[r["id"]]["verdicts"]:
            tab[(c[v["key"]]["ok"], v["result"])] += 1
    right = sum(tab[(True, k)] for k in ("CONFIRMED", "REFUTED", "UNCLEAR"))
    wrong = sum(tab[(False, k)] for k in ("CONFIRMED", "REFUTED", "UNCLEAR"))
    return np.mean(acc), tab[(True, "REFUTED")] / right, tab[(False, "CONFIRMED")] / wrong, n_chk


def mix_score():
    rows = rows_of("MIX")
    res = {}
    for l in open(ROOT / "runs/swarm/verify_mix_c31/results.jsonl"):
        x = json.loads(l)
        if not x.get("error"):
            res.setdefault(x["id"], []).append({v["key"]: v["result"] for v in x["verdicts"]})
    acc = []
    for r in rows:
        c = pool_of(r)
        if len(c) <= 1:
            acc.append(float(any(e["ok"] for e in c.values())) if c else 0.0); continue
        acc.append(pick_multi(c, res.get(r["id"], []), 2))
    return np.mean(acc), np.mean([float(any(e["ok"] for e in pool_of(r).values())) for r in rows])


def main():
    rows = problem_rows("12B")
    single = np.mean([np.mean([x["ok"] for x in r["ss"]]) for r in rows])
    maj = np.mean([maj_at_k(r["ss"], len(r["ss"])) for r in rows])
    swarm = np.mean([r["sw"] for r in rows])
    vote = np.mean([pick(pool_of(r), {}, 2) if pool_of(r) else 0.0 for r in rows])
    upper = np.mean([float(any(e["ok"] for e in pool_of(r).values())) for r in rows])
    sc = {lab: run_scores(rows, name) for lab, name in CHECKERS}
    b31 = per_sample(ROOT / "runs/calib/gemma-4-31B-it_think")
    ids = [r["id"] for r in rows if r["id"] in b31]
    s31 = np.mean([np.mean([x["ok"] for x in b31[i]]) for i in ids])
    partial31 = len(ids) < len(rows)
    m31 = np.mean([maj_at_k(b31[i], 4) for i in ids])
    mix, upper_mix = mix_score()

    bars = [("one 12B\nanswer", single, MUTED), ("12B\nmajority\nof 8", maj, MUTED), ("12B\nswarm", swarm, MUTED),
            ("pooled vote\n(8 answers\n+ swarm)", vote, INK2)] + \
           [(f"pool +\n{lab}\nchecker", sc[lab][0], {"12B": "#b9d1f1", "26B-A4B": "#76a9ea", "31B": S1}[lab]) for lab, _ in CHECKERS] + \
           [("pool + 31B\nanswers,\n31B checks\ntwice", mix, "#174f96")]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 5.3), gridspec_kw=dict(width_ratios=[1.75, 1]))
    xs = np.arange(len(bars))
    for x, (lab, v, col) in zip(xs, bars):
        ax1.bar(x, v, width=0.64, color=col, zorder=2)
        ax1.text(x, v + 0.01, f"{v:.0%}", ha="center", va="bottom", color=INK, fontsize=11.5, zorder=4,
                 fontweight="bold" if x == len(bars) - 1 else "normal", bbox=dict(boxstyle="square,pad=0.12", fc=SURFACE, ec="none"))
    ax1.hlines(upper, -0.5, len(bars) - 1.5, color=INK2, lw=1, ls=(0, (4, 3)), zorder=3)
    ax1.hlines(upper_mix, len(bars) - 1.5, len(bars) - 0.5, color=INK2, lw=1, ls=(0, (4, 3)), zorder=3)
    ax1.text(-0.45, upper + 0.01, f"some candidate in the pool is right: {upper:.0%}  (with the 31B's answers: {upper_mix:.0%})",
             ha="left", va="bottom", color=INK2, fontsize=9.5)
    for yv, lab in ((s31, f"one 31B\nanswer: {s31:.0%}"), (m31, f"31B majority\nof 4: {m31:.0%}")):
        ax1.hlines(yv, 3.5, len(bars) - 0.5, color=S1, lw=1.2, ls=(0, (2, 2)), zorder=3)
        ax1.text(len(bars) - 0.42, yv, lab + ("\n(partial)" if partial31 else ""), ha="left", va="center", color=INK2, fontsize=9.5)
    ax1.set_xticks(xs, [b[0] for b in bars], color=INK, fontsize=9.5)
    ax1.tick_params(axis="x", length=0)
    ax1.axvline(3.5, color=GRID, lw=1.2, zorder=1)
    ax1.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax1.set_ylim(0.5, 0.94); ax1.set_xlim(-0.55, len(bars) + 0.35)
    ax1.grid(axis="y", color=GRID, lw=0.8); ax1.set_axisbelow(True)
    ax1.set_ylabel("problems solved (207)")
    ax1.set_title("12B answers, chosen by a blind checker", color=INK2, fontsize=11, loc="left")

    labs = [lab for lab, _ in CHECKERS]
    y = np.arange(len(labs))[::-1]
    h = 0.34
    ax2.barh(y + h / 2, [sc[l][1] for l in labs], height=h, color=S2, zorder=2, label="right answers it REFUTED")
    ax2.barh(y - h / 2, [sc[l][2] for l in labs], height=h, color=MUTED, zorder=2, label="wrong answers it CONFIRMED")
    for yi, l in zip(y, labs):
        for dy, v in ((h / 2, sc[l][1]), (-h / 2, sc[l][2])):
            ax2.text(v + 0.006, yi + dy, f"{v:.0%}", va="center", ha="left", color=INK, fontsize=10.5)
    ax2.set_yticks(y, [f"{l} checker" for l in labs], color=INK, fontsize=10.5)
    ax2.tick_params(axis="y", length=0)
    ax2.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax2.set_xlim(0, 0.5)
    ax2.grid(axis="x", color=GRID, lw=0.8); ax2.set_axisbelow(True)
    ax2.legend(frameon=False, loc="center right", labelcolor=INK, fontsize=9.5)
    ax2.set_title("its mistakes on the same candidates", color=INK2, fontsize=11, loc="left")
    n12 = sc["12B"][3]
    titles(fig, f"A stronger checker turns the 12B's answers into {mix:.0%} solved (12B swarm {swarm:.0%}, "
                f"31B majority of 4 {m31:.0%})",
           "gemma-4, 207 problems  ·  pool = 8 single 12B answers + the swarm's  ·  blind check of the distinct values  ·  "
           "pre-registered rules" + ("" if n12 == 129 else f"  ·  12B checker: {n12}/129 checked"),
           top=0.86)
    out = ROOT / "results/figures/12b_checker_ladder.png"
    fig.savefig(out, dpi=200); plt.close(fig)
    print("wrote", out, "mix", round(mix, 3), "31B maj@4", round(m31, 3), {k: tuple(round(float(x), 3) for x in v) for k, v in sc.items()}, "31B single", round(s31, 3), len(ids))


if __name__ == "__main__":
    main()
