"""Round 10: one saboteur vs two colluding saboteurs, under no defense / answer-key expulsion / peer-agreement expulsion.

  python analysis/collusion.py         -> prints and writes results/p2_e4b_collusion.md

Pools the seed-0 and seed-1 problem orders. Works on partial runs (uses the problems finished so far and says how many).
"Sabotaged" = the team's final answer equals a saboteur's candidate AND is wrong.
"""
import json, sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis")]
from compare import agent_runs, interrupted  # noqa: E402
from ablations import boot  # noqa: E402

GROUPS = [
    ("one saboteur (W4)", {"W4"}, [("no defense", ["p2_e4b_sab", "p2_e4b_sab_s1"]),
                                   ("expel, answer key", ["p2_e4b_sab_remove2", "p2_e4b_sab_remove2_s1"]),
                                   ("expel, peer agreement", ["p2_e4b_sab_peer", "p2_e4b_sab_peer_s1"])]),
    ("two colluding (W3 + W4)", {"W3", "W4"}, [("no defense", ["p2_e4b_col", "p2_e4b_col_s1"]),
                                               ("expel, answer key", ["p2_e4b_col_key", "p2_e4b_col_key_s1"]),
                                               ("expel, peer agreement", ["p2_e4b_col_peer", "p2_e4b_col_peer_s1"])]),
    ("no saboteur", set(), [("expel, peer agreement", ["p2_e4b_peer_nosab", "p2_e4b_peer_nosab_s1"])]),
]


def records(run):
    d = ROOT / "runs/swarm" / run
    if not (d / "results.jsonl").exists():
        return []
    rs = [json.loads(l) for l in open(d / "results.jsonl")]
    return [r for r in rs if not r.get("error") and not interrupted(d, r)]


def frame(rs):
    return pd.DataFrame(dict(ok=[float(bool(r["correct"])) for r in rs],
                             sab=[float(bool(r.get("final_is_saboteur")) and not r["correct"]) for r in rs]),
                        index=[r["id"] for r in rs])


def expulsions(rs):
    """{worker: problem number} from the last reputation snapshot"""
    last = max(rs, key=lambda r: r.get("order", 0), default=None)
    return dict((last or {}).get("rep_after", {}).get("removed", {}))


def final_record(rs):
    last = max(rs, key=lambda r: r.get("order", 0), default=None)
    return {w: v for w, v in ((last or {}).get("rep_after") or {}).items() if w != "removed"}


def main():
    ref = agent_runs(ROOT / "runs/swarm/ng207_e4b_swarm").p
    out = ["# Round 10: colluding saboteurs vs reputation (E4B, 207 problems, both problem orders pooled)", "",
           f"No saboteur (main swarm, 2 trials): **{ref.mean():.3f}**", "",
           "| saboteurs | defense | runs (problems) | pass@1 | Δ vs no saboteur [95% CI] | Δ vs no defense [95% CI] | sabotaged |",
           "|---|---|---|---|---|---|---|"]
    exp_lines = ["", "| run | expelled (after problem #) | honest worker expelled? | final record (agreed or correct / graded) |",
                 "|---|---|---|---|"]
    for gname, sabs, conds in GROUPS:
        base = None
        for cname, runs in conds:
            fs = [(r, frame(records(r))) for r in runs]
            fs = [(r, f) for r, f in fs if len(f)]
            if not fs:
                out.append(f"| {gname} | {cname} | not run yet | | | | |")
                continue
            ok = pd.concat([f.ok for _, f in fs], axis=1).mean(1)
            sab = pd.concat([f.sab for _, f in fs], axis=1).mean(1)
            ids = ok.index.intersection(ref.index)
            d = ok[ids] - ref[ids]
            lo, hi = boot(d) if len(d) > 5 else (np.nan, np.nan)
            dd = ""
            if cname == "no defense":
                base = ok
            elif base is not None:
                j = ok.index.intersection(base.index)
                x = ok[j] - base[j]
                l2, h2 = boot(x) if len(x) > 5 else (np.nan, np.nan)
                dd = f"{x.mean():+.3f} [{l2:+.3f}, {h2:+.3f}]"
            ns = "+".join(str(len(f)) for _, f in fs)
            out.append(f"| {gname} | {cname} | {len(fs)} ({ns}) | **{ok.mean():.3f}** | {d.mean():+.3f} [{lo:+.3f}, {hi:+.3f}] | "
                       f"{dd} | {sab.mean():.1%} |" if sabs else
                       f"| {gname} | {cname} | {len(fs)} ({ns}) | **{ok.mean():.3f}** | {d.mean():+.3f} [{lo:+.3f}, {hi:+.3f}] | | — |")
            if "expel" in cname:
                for r, _ in fs:
                    rs = records(r)
                    ex = expulsions(rs)
                    honest = [w for w in ex if w not in sabs]
                    rec = final_record(rs)
                    exp_lines.append(f"| `{r}` | {', '.join(f'{w} ({k})' for w, k in sorted(ex.items(), key=lambda t: t[1])) or 'nobody'} | "
                                     f"{'**YES: ' + ', '.join(honest) + '**' if honest else 'no'} | "
                                     f"{', '.join(f'{w} {a}/{b}' for w, (a, b) in sorted(rec.items()))} |")
    txt = "\n".join(out + exp_lines) + "\n"
    print(txt)
    (ROOT / "results/p2_e4b_collusion.md").write_text(txt)


if __name__ == "__main__":
    main()
