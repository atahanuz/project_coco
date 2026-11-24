"""Compare swarm variants on the problems they all completed.

  python analysis/ablations.py --ref runs/swarm/ng207_e4b_swarm \
      runs/swarm/ng207_e4b_swarm_noshare runs/swarm/ng207_e4b_swarm_r1 runs/swarm/ng207_e4b_swarm_w2 \
      [--calib runs/calib/gemma-4-E4B-it_think] [--out results/e4b_ablations]

pass@1 per problem = mean over that run's error-free trials. Differences vs --ref use a paired bootstrap over problems.
"""
import argparse, sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "analysis"))
sys.path.insert(0, str(ROOT / "calib"))
from compare import agent_runs, TAGS, TAG_NAME  # noqa: E402


def boot(d, B=10000, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(d), (B, len(d)))
    m = d.values[idx].mean(1)
    return np.percentile(m, 2.5), np.percentile(m, 97.5)


def main(a):
    runs = {Path(r).name: agent_runs(r) for r in [a.ref] + a.runs}
    if a.calib:
        from analyze import analyze
        b = analyze(Path(a.calib)).set_index("id")
        runs["single model (no tools)"] = pd.DataFrame(dict(p=b.p, toks=b.mean_toks, n=b.n))
        runs["single model maj@8"] = pd.DataFrame(dict(p=b.maj_ok.astype(float), toks=8 * b.mean_toks, n=b.n))
    ids = sorted(set.intersection(*(set(r.index) for r in runs.values())))
    ref = Path(a.ref).name
    out = f"## Swarm ablations on {len(ids)} problems completed by every run (reference: `{ref}`)\n\n"
    out += "| run | pass@1 | Δ vs reference [95% CI] | tokens / attempt | trials per problem |\n|---|---|---|---|---|\n"
    for name, r in runs.items():
        r = r.loc[ids]
        d = r.p - runs[ref].loc[ids].p
        ci = "—" if name == ref else f"{d.mean():+.3f} [{boot(d)[0]:+.3f}, {boot(d)[1]:+.3f}]"
        out += f"| {name} | **{r.p.mean():.3f}** | {ci} | {r.toks.mean():,.0f} | {r.n.mean():.1f} |\n"
    tags = pd.Series({i: TAG_NAME.get(TAGS.get(i, "?"), "?") for i in ids})
    out += "\n### pass@1 by cooperation tag\n\n| run | " + " | ".join(f"{t} (n={(tags == t).sum()})" for t in sorted(tags.unique())) + " |\n"
    out += "|---|" + "---|" * tags.nunique() + "\n"
    for name, r in runs.items():
        r = r.loc[ids]
        out += f"| {name} | " + " | ".join(f"{r.p[tags == t].mean():.3f}" for t in sorted(tags.unique())) + " |\n"
    print(out)
    if a.out:
        Path(a.out + ".md").write_text(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True)
    ap.add_argument("runs", nargs="+")
    ap.add_argument("--calib", default="")
    ap.add_argument("--out", default="")
    main(ap.parse_args())
