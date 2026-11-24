"""Summarise swarm / solo runs side by side.

  python swarm/analyze_swarm.py runs/swarm/dev12_e4b_swarm runs/swarm/dev12_e4b_solo ...

Per run: solved / done, any-candidate-correct (did the right answer appear anywhere), mean completion
tokens, LLM calls, python calls, notes, errors. Then a per-problem grid (1 = correct, . = wrong, - = missing).
"""
import json, sys
from pathlib import Path


def load(d):
    p = Path(d) / "results.jsonl"
    return [json.loads(l) for l in open(p)] if p.exists() else []


runs = {Path(d).name: load(d) for d in sys.argv[1:]}
print(f"{'run':28s} {'done':>4s} {'solved':>6s} {'anyCand':>7s} {'err':>3s} {'compTok':>8s} {'calls':>5s} {'py':>4s} {'notes':>5s} {'min':>5s}")
for name, rs in runs.items():
    ok = [r for r in rs if not r.get("error")]
    n = len(ok) or 1
    print(f"{name:28s} {len(rs):4d} {sum(r['correct'] for r in ok):6d} {sum(r['any_candidate_correct'] for r in ok):7d} "
          f"{len(rs) - len(ok):3d} {sum(r['completion_tokens'] for r in ok) / n:8.0f} {sum(r['calls'] for r in ok) / n:5.1f} "
          f"{sum(r['n_python'] for r in ok) / n:4.1f} {sum(r['n_notes'] for r in ok) / n:5.1f} {sum(r['seconds'] for r in ok) / n / 60:5.1f}")

ids = sorted({r["id"] for rs in runs.values() for r in rs})
if ids:
    print("\nper problem (trial 0):")
    print(f"{'id':34s} " + " ".join(f"{k[:14]:>14s}" for k in runs))
    for pid in ids:
        cells = []
        for rs in runs.values():
            r = next((x for x in rs if x["id"] == pid and x["trial"] == 0), None)
            cells.append("-" if r is None else ("ERR" if r.get("error") else ("1" if r["correct"] else ".")))
        gold = next((r["gold"] for rs in runs.values() for r in rs if r["id"] == pid and "gold" in r), "?")
        print(f"{pid:34s} " + " ".join(f"{c:>14s}" for c in cells) + f"   gold={gold}")
