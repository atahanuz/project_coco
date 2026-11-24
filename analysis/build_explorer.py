"""Build the data files behind the COCO Problem Explorer dashboard (results/explorer/*.json).

  python analysis/build_explorer.py

problems.json   one row per problem: statement, gold answer, category, cooperation tag, E4B / 12B single-model difficulty
outcomes.json   one row per (problem, approach): share of runs correct, runs, the answer(s) given, tokens per run
traces.json     one row per swarm step (E4B 4-worker swarm trial 0, 12B swarm): master plan / worker task + candidate / final
"""
import json, re, sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "analysis")); sys.path.insert(0, str(ROOT / "calib"))
from coco.grading import is_correct  # noqa: E402
from compare import TAGS, interrupted  # noqa: E402
from analyze import per_sample  # noqa: E402
from scaling import maj_at_k  # noqa: E402

OUT = ROOT / "results/explorer"
POOL = {p["id"]: p for p in map(json.loads, open(ROOT / "data/pool.jsonl"))}
IDS = open(ROOT / "data/nongeo207.txt").read().split()
CAT = {"algebra": "Algebra", "combinatorics": "Combinatorics", "number_theory": "Number theory"}
TAGN = {"E": "Explore small cases", "N": "Numeric search", "C": "Direct computation", "R": "Pure reasoning"}

# hand-picked examples: (short id, title, why it is interesting). The notes describe what the run logs show.
FEATURED = [
    ("alg-088", "The team corrects itself",
     "In round 1 no worker finds a value, but they narrow the innermost floor down to 23–29. In round 2 three of four "
     "workers check those cases and find a = 1/7. Single E4B answers say there is no solution in 6 of 8 samples, so a "
     "majority vote fails."),
    ("comb-024", "A small case points the way",
     "W1 brute-forces the sum for 4 numbers (−4/5) and W3 finds the general pattern, −2024/2025. Swarms of 2, 4 and 8 "
     "workers all solve it, but with only one round the swarm fails both times. No single E4B answer is right."),
    ("comb-072", "Shared notes carry the data",
     "Workers simulate small games and post the averages to the shared notes. In round 3 two workers turn them into "
     "1040. The same team without shared notes answers 551.75 and 3056. A single E4B answer is never right."),
    ("comb-088", "Only the 8-worker swarm",
     "The star graph gives 90, the most common single answer, and the 2- and 4-worker swarms stop there too. The "
     "8-worker swarm finds 168, as does one of the two one-round runs."),
    ("comb-079", "Only the 12B swarm",
     "Every E4B approach fails, and a single 12B answer is right in 1 of 8 samples. The 12B swarm finds 81,729,648,000."),
    ("comb-025", "The right answer spreads",
     "Every E4B approach fails, and single 12B answers scatter over 2, 4, 58, 505 and others. In round 1, W3 writes a "
     "minimax dynamic program and gets 290. In round 2 two more workers rebuild the program and get 290, in round 3 all "
     "four do, and the master answers 290. 12B solo + Python runs out of tokens without an answer."),
    ("alg-100", "Python finds the other six",
     "A single 12B answer says 2 in 7 of 8 samples: it finds (1, 1, 1) and (−1, −1, −1) and stops. In round 1, W1 "
     "searches the sphere numerically and finds 8 solutions. In round 2 three workers confirm all 8 with other solvers, "
     "and the master answers 8. 12B solo + Python also finds 8; no E4B approach does."),
    ("comb-033", "The team talks itself out of the right answer",
     "W4 has the right answer, 498, in round 1. In round 2 W2 'refines' W4's argument to 500, and the master goes with "
     "500. Every E4B swarm variant fails, while single E4B answers get 498 in 6 of 8 samples."),
    ("alg-018", "Everyone misses the second answer",
     "Every approach answers 2026. The full answer is 2026 and 2030, so nobody gets it right."),
    ("nt-004", "Everyone solves it",
     "An easy problem: every approach finds (1, 2, 3) every time. The swarm checks it with a brute-force search and a "
     "proof."),
]

# approach key, model, label, kind, source
APPROACHES = [
    ("e4b_single", "E4B", "One answer", "single", "runs/calib/gemma-4-E4B-it_think"),
    ("e4b_maj", "E4B", "Majority of 8 answers", "majority", "runs/calib/gemma-4-E4B-it_think"),
    ("e4b_solo", "E4B", "Solo agent + Python", "agent", "runs/swarm/ng207_e4b_solo"),
    ("e4b_swarm2", "E4B", "Swarm, 2 workers", "agent", "runs/swarm/ng207_e4b_swarm_w2"),
    ("e4b_swarm4", "E4B", "Swarm, 4 workers", "agent", "runs/swarm/ng207_e4b_swarm"),
    ("e4b_swarm8", "E4B", "Swarm, 8 workers", "agent", "runs/swarm/ng207_e4b_swarm_w8"),
    ("e4b_r1", "E4B", "Swarm, one round only", "agent", "runs/swarm/ng207_e4b_swarm_r1"),
    ("e4b_noshare", "E4B", "Swarm, no shared notes", "agent", "runs/swarm/ng207_e4b_swarm_noshare"),
    ("12b_single", "12B", "One answer", "single", "runs/calib/gemma-4-12B-it_think"),
    ("12b_maj", "12B", "Majority of 8 answers", "majority", "runs/calib/gemma-4-12B-it_think"),
    ("12b_solo", "12B", "Solo agent + Python", "agent", "runs/swarm/ng207_12b_solo"),
    ("12b_swarm", "12B", "Swarm, 4 workers", "agent", "runs/swarm/ng207_12b_swarm"),
]


def clean(s, n=None):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if n is None or len(s) <= n else s[:n - 1].rstrip() + "…"


def answer_mix(ss):
    """'42 ×5 · 17 ×2 · no answer ×1' for a list of single-model samples"""
    c, rep, ok = Counter(), {}, {}
    for x in ss:
        k = x["key"] if x["key"] is not None else "∅"
        c[k] += 1
        rep.setdefault(k, x["pred"])
        ok[k] = ok.get(k, False) or bool(x["ok"])
    parts = []
    for k, n in c.most_common(4):
        lab = "no answer" if k == "∅" else clean(rep[k], 40)
        parts.append(f"{lab} ×{n}" + (" ✓" if ok[k] else ""))
    if len(c) > 4:
        parts.append(f"{sum(n for _, n in c.most_common()[4:])} other")
    return " · ".join(parts)


def single_rows(key, src):
    by = per_sample(ROOT / src)
    rows = []
    for pid in IDS:
        ss = by.get(pid, [])
        if not ss:
            continue
        n_ok = sum(bool(x["ok"]) for x in ss)
        if key.endswith("_maj"):
            share = maj_at_k(ss, len(ss))
            votes = Counter(x["key"] for x in ss if x["key"] is not None)
            top = votes.most_common(1)[0][0] if votes else None
            ans = next((clean(x["pred"], 60) for x in ss if x["key"] == top), "no answer") if top else "no answer"
            rows.append(dict(id=pid, runs=len(ss), correct=None, share=round(share, 3),   # ties split: share can be 0.5
                             answer=f"{ans} (most common of {len(ss)})", tokens=round(sum(x["toks"] for x in ss))))
        else:
            rows.append(dict(id=pid, runs=len(ss), correct=n_ok, share=round(n_ok / len(ss), 3), answer=answer_mix(ss),
                             tokens=round(np.mean([x["toks"] for x in ss]))))
    return rows


def agent_rows(src):
    d = ROOT / src
    rs = [json.loads(l) for l in open(d / "results.jsonl")]
    rs = [r for r in rs if not r.get("error") and not interrupted(d, r)]
    by = {}
    for r in rs:
        by.setdefault(r["id"], []).append(r)
    rows = []
    for pid in IDS:
        if pid not in by:
            continue
        g = sorted(by[pid], key=lambda r: r["trial"])
        ans = " / ".join(clean(r.get("final") or "no answer", 50) + (" ✓" if r.get("correct") else " ✗") for r in g)
        rows.append(dict(id=pid, runs=len(g), correct=sum(bool(r.get("correct")) for r in g),
                         share=round(np.mean([bool(r.get("correct")) for r in g]), 3), answer=ans,
                         tokens=round(np.mean([r.get("completion_tokens") or 0 for r in g]))))
    return rows


def traces(run_key, src):
    d, rows = ROOT / src, []
    for pid in IDS:
        tf = d / f"{pid}__t0" / "trace.json"
        if not tf.exists():
            continue
        t = json.load(open(tf))
        rec, gold = t["record"], POOL[pid]["answer"]
        if rec.get("error"):
            continue
        plans = {}
        for e in t["log"]:
            if e.get("agent") == "master" and e.get("assignments"):
                plans[int(e["round"])] = e["assignments"]
        step = 0
        for rnd in sorted(plans):
            for x in [x for x in t["reports"] if int(x["round"]) == rnd]:
                a = x.get("answer")
                rows.append(dict(id=pid, run=run_key, step=step, round=rnd, who=x["worker"], task=clean(x.get("task"), 170),
                                 answer=clean(a, 60) if a else "", ok=bool(a) and bool(is_correct(a, gold)),
                                 note=clean(x.get("report"), 200)))
                step += 1
        fin = rec.get("final")
        rows.append(dict(id=pid, run=run_key, step=step, round=max(plans) + 1 if plans else 1, who="Master",
                         task="Final decision", answer=clean(fin, 60) if fin else "no answer", ok=bool(rec.get("correct")),
                         note=clean(rec.get("reason"), 240)))
    return rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    outcomes = []
    for key, model, label, kind, src in APPROACHES:
        rows = single_rows(key, src) if kind in ("single", "majority") else agent_rows(src)
        for r in rows:
            outcomes.append(dict(r, approach=key, model=model, label=label))
        print(f"{key:12s} {len(rows):4d} problems  solved {np.mean([r['share'] for r in rows]):.3f}")
    occ = {}
    for o in outcomes:
        occ[(o["id"], o["approach"])] = o
    probs = []
    for pid in IDS:
        p = POOL[pid]
        cat = pid.replace("imo-bench-", "").rsplit("-", 1)[0]
        e4 = occ.get((pid, "e4b_single")); tw = occ.get((pid, "12b_single"))
        probs.append(dict(id=pid, short=pid.replace("imo-bench-", "").replace("number_theory", "nt").replace("combinatorics", "comb")
                          .replace("algebra", "alg"), category=CAT[cat], tag=TAGN.get(TAGS.get(pid, ""), ""),
                          statement=p["problem"].strip(), gold=str(p["answer"]).strip(),
                          e4b_k=e4["correct"] if e4 else None, e4b_n=e4["runs"] if e4 else None,
                          d12_share=tw["share"] if tw else None, featured=None, feature_title="", feature_note=""))
    short = {p["short"]: p for p in probs}
    for i, (sid, title, note) in enumerate(FEATURED):
        short[sid].update(featured=i + 1, feature_title=title, feature_note=note)
    tr = traces("e4b_swarm4", "runs/swarm/ng207_e4b_swarm") + traces("12b_swarm", "runs/swarm/ng207_12b_swarm")
    for name, rows in [("problems", probs), ("outcomes", outcomes), ("traces", tr)]:
        txt = "[\n" + ",\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n]\n"
        (OUT / f"{name}.json").write_text(txt)
        print(f"wrote {name}.json: {len(rows)} rows, {len(txt) / 1e3:.0f} kB")


if __name__ == "__main__":
    main()
