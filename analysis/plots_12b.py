"""Slide figures for the model-size comparison (E4B vs 12B), all 207 problems.

  python analysis/plots_12b.py      -> results/figures/model_size.png, results/figures/12b_by_difficulty_heldout.png
"""
import json, sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis"), str(ROOT / "calib")]
from analyze import per_sample  # noqa: E402
from compare import interrupted  # noqa: E402
from scaling import maj_at_k  # noqa: E402
from plots import SURFACE, INK, INK2, GRID, S1, S2, MUTED, titles  # noqa: E402,F401

IDS = open(ROOT / "data/nongeo207.txt").read().split()
FIG = ROOT / "results/figures"


def agent(src):
    d = ROOT / src
    by = {}
    for l in open(d / "results.jsonl"):
        r = json.loads(l)
        if not r.get("error") and not interrupted(d, r):
            by.setdefault(r["id"], []).append(r)
    return {pid: (np.mean([bool(r["correct"]) for r in g]), np.mean([r["completion_tokens"] for r in g])) for pid, g in by.items()}


def single(src):
    by = per_sample(ROOT / src)
    return {pid: (np.mean([x["ok"] for x in ss]), maj_at_k(ss, len(ss)), np.mean([x["toks"] for x in ss]), len(ss), ss)
            for pid, ss in by.items() if pid in IDS}


def rows_for(model, calib, solo, swarm):
    s, so, sw = single(calib), agent(solo), agent(swarm)
    ids = [p for p in IDS if p in s and p in sw]
    return [
        ("One answer", np.mean([s[p][0] for p in ids]), np.mean([s[p][2] for p in ids]), MUTED, ""),
        ("Majority of 8", np.mean([s[p][1] for p in ids]), np.mean([s[p][2] * s[p][3] for p in ids]), MUTED, ""),
        ("Solo agent + Python", np.mean([so[p][0] for p in so if p in ids]), np.mean([so[p][1] for p in so if p in ids]), MUTED,
         "" if len(so) >= len(ids) else f"{len(so)} of {len(ids)} problems"),
        ("Swarm, 4 workers", np.mean([sw[p][0] for p in ids]), np.mean([sw[p][1] for p in ids]), S1, ""),
    ]


def model_size():
    panels = [("Gemma-4 E4B", rows_for("E4B", "runs/calib/gemma-4-E4B-it_think", "runs/swarm/ng207_e4b_solo", "runs/swarm/ng207_e4b_swarm")),
              ("Gemma-4 12B", rows_for("12B", "runs/calib/gemma-4-12B-it_think", "runs/swarm/ng207_12b_solo", "runs/swarm/ng207_12b_swarm"))]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), sharex=True)
    for ax, (name, rows) in zip(axes, panels):
        y = list(range(len(rows)))[::-1]
        for yi, (lab, v, tok, col, note) in zip(y, rows):
            ax.barh(yi, v, height=0.62, color=col, zorder=2)
            ax.text(v + 0.012, yi, f"{v:.0%}", va="center", ha="left", color=INK, fontsize=13,
                    fontweight="bold" if col == S1 else "normal")
            ax.text(1.0, yi, f"{tok / 1000:.0f}k tokens", va="center", ha="right", color=INK2, fontsize=10,
                    transform=ax.get_yaxis_transform())
            if note:
                ax.text(0.01, yi - 0.42, note, va="center", ha="left", color=INK2, fontsize=8.5, transform=ax.get_yaxis_transform())
        ax.set_yticks(y, [r[0] for r in rows], color=INK)
        ax.set_title(name, loc="left", color=INK, fontsize=13)
        ax.set_xlim(0, 1.2)
        ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
        ax.set_xticks([0, 0.25, 0.5, 0.75])
        ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)
        ax.tick_params(axis="y", length=0)
        ax.set_xlabel("problems solved (pass@1)")
    sw = [p[1][3][1] - p[1][0][1] for p in panels]
    titles(fig, f"The swarm adds about 12 points at both model sizes (+{sw[0] * 100:.1f} for E4B, +{sw[1] * 100:.1f} for 12B)",
           "207 IMO-AnswerBench problems (algebra, combinatorics, number theory). Tokens: completion tokens per problem.", top=0.86)
    fig.savefig(FIG / "model_size.png", dpi=200); plt.close(fig)
    for name, rows in panels:
        print(name, " | ".join(f"{r[0]} {r[1]:.3f} ({r[2] / 1000:.0f}k)" for r in rows))


def heldout_difficulty():
    """bucket from 12B samples 0-3, single pass@1 measured on samples 4-7 only (avoids regression to the mean)"""
    s, sw = single("runs/calib/gemma-4-12B-it_think"), agent("runs/swarm/ng207_12b_swarm")
    groups = {"0 of 4": [], "1 of 4": [], "2–3 of 4": [], "4 of 4": []}
    for pid, (_, _, _, _, ss) in s.items():
        d = {x["sample"]: x["ok"] for x in ss}
        if not all(i in d for i in range(8)) or pid not in sw:
            continue
        c = sum(d[i] for i in range(4))
        k = "0 of 4" if c == 0 else "1 of 4" if c == 1 else "2–3 of 4" if c < 4 else "4 of 4"
        groups[k].append((np.mean([d[i] for i in range(4, 8)]), sw[pid][0]))
    fig, ax = plt.subplots(figsize=(9, 4.8))
    names = list(groups)
    w = 0.36
    for i, (lab, col, idx) in enumerate([("One 12B answer (held-out samples)", MUTED, 0), ("12B swarm, 4 workers", S1, 1)]):
        xs = [j + (i - 0.5) * (w + 0.02) for j in range(len(names))]
        vals = [np.mean([g[idx] for g in groups[k]]) for k in names]
        ax.bar(xs, vals, width=w, color=col, label=lab, zorder=2)
        for x, v in zip(xs, vals):
            ax.text(x, v + 0.012, f"{v:.0%}", ha="center", va="bottom", color=INK, fontsize=10,
                    fontweight="bold" if idx else "normal")
    ax.set_xticks(range(len(names)), [f"{k}\n(n={len(groups[k])})" for k in names], color=INK)
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_ylabel("problems solved"); ax.set_xlabel("how many of the first 4 single 12B answers were right")
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, labelcolor=INK, handlelength=1.2)
    ax.set_ylim(0, 1.08)
    titles(fig, "The 12B swarm's gain is on the hard problems",
           f"Buckets from single 12B answers 1–4; grey bars use answers 5–8 only ({sum(len(g) for g in groups.values())} problems with 8 answers).",
           top=0.83)
    fig.savefig(FIG / "12b_by_difficulty_heldout.png", dpi=200); plt.close(fig)
    for k in names:
        print(k, len(groups[k]), f"single {np.mean([g[0] for g in groups[k]]):.3f} swarm {np.mean([g[1] for g in groups[k]]):.3f}")


if __name__ == "__main__":
    FIG.mkdir(parents=True, exist_ok=True)
    model_size()
    heldout_difficulty()
