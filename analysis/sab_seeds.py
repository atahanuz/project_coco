"""Planted saboteur: pool the seed-0 and seed-1 problem orders (2 runs per problem per condition), paired bootstrap CIs.

  python analysis/sab_seeds.py
"""
import json, sys
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis")]
from compare import agent_runs, interrupted  # noqa: E402
from ablations import boot  # noqa: E402

COND = [("saboteur, no defense", ["p2_e4b_sab", "p2_e4b_sab_s1"]),
        ("track record shown (v2)", ["p2_e4b_sab_rep2", "p2_e4b_sab_rep2_s1"]),
        ("track record + expulsion (v2, answer key)", ["p2_e4b_sab_remove2", "p2_e4b_sab_remove2_s1"]),
        ("track record + expulsion (v3, peer agreement)", ["p2_e4b_sab_peer", "p2_e4b_sab_peer_s1"])]


def load(run):
    d = ROOT / "runs/swarm" / run
    if not (d / "results.jsonl").exists():
        return None
    rs = [json.loads(l) for l in open(d / "results.jsonl")]
    rs = [r for r in rs if not r.get("error") and not interrupted(d, r)]
    return pd.DataFrame(dict(ok=[float(bool(r["correct"])) for r in rs], sab=[float(bool(r.get("final_is_saboteur")) and not r["correct"]) for r in rs]),
                        index=[r["id"] for r in rs])


ref = agent_runs(ROOT / "runs/swarm/ng207_e4b_swarm").p
rows, per = [], {}
for name, runs in COND:
    ds = [x for x in map(load, runs) if x is not None and len(x) >= 207]
    if not ds:
        continue
    ok = pd.concat([x.ok for x in ds], axis=1).mean(1)
    sab = pd.concat([x.sab for x in ds], axis=1).mean(1)
    per[name] = ok
    ids = ok.index.intersection(ref.index)
    d = ok[ids] - ref[ids]
    rows.append(dict(condition=name, seeds=len(ds), pass1=ok.mean(), d_ref=d.mean(), ci_ref=boot(d), sab_rate=sab.mean()))
base = per.get("saboteur, no defense")
print("| condition | orders | pass@1 | Δ vs no saboteur [95% CI] | Δ vs no defense [95% CI] | final = saboteur's wrong answer |")
print("|---|---|---|---|---|---|")
print(f"| no saboteur (main swarm, 2 trials) | | **{ref.mean():.3f}** | — | | — |")
for r in rows:
    dd = ""
    if base is not None and r["condition"] != "saboteur, no defense":
        x = per[r["condition"]] - base
        lo, hi = boot(x)
        dd = f"{x.mean():+.3f} [{lo:+.3f}, {hi:+.3f}]"
    print(f"| {r['condition']} | {r['seeds']} | **{r['pass1']:.3f}** | {r['d_ref']:+.3f} [{r['ci_ref'][0]:+.3f}, {r['ci_ref'][1]:+.3f}] | {dd} | {r['sab_rate']:.1%} |")
