"""Slide figures from analysis/compare.py output.

  python analysis/plots.py results/e4b_ng207_per_problem.csv results/figures/e4b_ng207 "E4B, 207 problems"
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
S1, S2, S3 = "#2a78d6", "#eb6834", "#1baf7a"      # categorical slots 1-3 (validated all-pairs)
MUTED = "#b9b8b2"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
                     "savefig.facecolor": SURFACE, "axes.spines.top": False, "axes.spines.right": False})


def titles(fig, main, sub, top=0.87):
    fig.text(0.015, 0.975, main, ha="left", va="top", color=INK, fontsize=14)
    fig.text(0.015, 0.915, sub, ha="left", va="top", color=INK2, fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, top))


def headline(df, out, title):
    rows = [("Single model\n(1 sample)", df.base_p.mean(), df.base_toks.mean(), MUTED),
            ("Solo agent\n+ Python", df.solo_p.mean(), df.solo_toks.mean(), MUTED),
            ("Majority vote\nof 8 samples", df.maj_ok.mean(), 8 * df.base_toks.mean(), MUTED),
            ("Swarm\n(1 master + 4 workers)", df.swarm_p.mean(), df.swarm_toks.mean(), S1)]
    fig, ax = plt.subplots(figsize=(9, 4.6))
    y = range(len(rows))[::-1]
    for yi, (lab, v, tok, col) in zip(y, rows):
        ax.barh(yi, v, height=0.62, color=col)
        ax.text(v + 0.008, yi, f"{v:.0%}", va="center", ha="left", color=INK, fontsize=13,
                fontweight="bold" if col == S1 else "normal")
        ax.text(0.995, yi, f"{tok / 1000:.0f}k tokens", va="center", ha="right", color=INK2, fontsize=10,
                transform=ax.get_yaxis_transform())
    ax.set_yticks(list(y), [r[0] for r in rows], color=INK)
    ax.set_xlim(0, max(r[1] for r in rows) * 1.45)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("problems solved (pass@1)")
    titles(fig, "A swarm of small models solves more problems, with less compute than majority voting", title)
    fig.savefig(out + "_headline.png", dpi=200); plt.close(fig)


def cost(df, out, title):
    pts = [("Single model", df.base_toks.mean(), df.base_p.mean(), MUTED),
           ("Solo + Python", df.solo_toks.mean(), df.solo_p.mean(), MUTED),
           ("Majority of 8", 8 * df.base_toks.mean(), df.maj_ok.mean(), MUTED),
           ("Swarm", df.swarm_toks.mean(), df.swarm_p.mean(), S1)]
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    for lab, x, v, col in pts:
        ax.scatter(x / 1000, v, s=110, color=col, edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.annotate(lab, (x / 1000, v), xytext=(8, 6), textcoords="offset points", color=INK, fontsize=11)
    ax.set_xlabel("completion tokens per problem (thousands)")
    ax.set_ylabel("problems solved")
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xlim(0, 52); ax.set_ylim(0.2, 0.52)
    ax.grid(color=GRID, lw=0.8); ax.set_axisbelow(True)
    titles(fig, "Accuracy vs compute", title)
    fig.savefig(out + "_cost.png", dpi=200); plt.close(fig)


def grouped(df, by, order, out, title, sub, xlabel, series=None):
    series = series or [("Single model", "base_p", S2), ("Majority of 8", "maj_ok", S3), ("Swarm", "swarm_p", S1)]
    g = df.groupby(by)
    groups = [k for k in order if k in g.groups]
    fig, ax = plt.subplots(figsize=(9, 4.8))
    w = 0.78 / len(series)
    for i, (lab, col, c) in enumerate(series):
        xs = [j + (i - (len(series) - 1) / 2) * (w + 0.015) for j in range(len(groups))]
        vals = [g.get_group(k)[col].mean() for k in groups]
        ax.bar(xs, vals, width=w, color=c, label=lab, zorder=2)
        if lab == "Swarm":
            for x, v in zip(xs, vals):
                ax.text(x, v + 0.012, f"{v:.0%}", ha="center", va="bottom", color=INK, fontsize=10)
    ax.set_xticks(range(len(groups)), [f"{k}\n(n={len(g.get_group(k))})" for k in groups], color=INK)
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_ylabel("problems solved"); ax.set_xlabel(xlabel)
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=3, labelcolor=INK, handlelength=1.2)
    ax.set_ylim(0, 1.05)
    titles(fig, title, sub, top=0.84)
    fig.savefig(out, dpi=200); plt.close(fig)


if __name__ == "__main__":
    csv, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(csv, index_col=0)
    headline(df, out, title)
    cost(df, out, title)
    grouped(df, "tag", ["N numeric", "C compute", "E explore", "R reasoning"], out + "_by_tag.png",
            "Gains are largest where the work can be split", title, "cooperation mode (hand-labelled before the experiment)")
    if "ho_bucket" in df:   # held-out buckets (samples 0-3) and single pass@1 on samples 4-7: no selection bias
        df = df.dropna(subset=["ho_bucket"]).copy()
        df["ho_bucket"] = df.ho_bucket.str.replace(" of samples 0-3", "")
        grouped(df, "ho_bucket", ["0/4", "1/4", "2-3/4", "4/4"], out + "_by_difficulty.png",
                "The swarm gains at every difficulty level", title,
                "difficulty: correct out of 4 held-out single-model samples (bars use the other 4 samples)",
                series=[("Single model", "ho_base_p", S2), ("Swarm", "swarm_p", S1)])
    print("wrote", out + "_*.png")
