"""Round 13, pooled verification: build the candidate lists, and pick answers from the checker's verdicts.

  python analysis/verify_pool.py build [E4B]    -> data/verify_12b.jsonl (problems whose candidates disagree)
                                                   (E4B: data/verify_e4b.jsonl; 8 single E4B answers + both E4B swarm trials)
  python analysis/verify_pool.py eval [run]     -> results/<run name>.md   (run default: runs/swarm/verify_12b;
                                                   round 14: runs/swarm/verify_12b_c31, runs/swarm/verify_12b_c26)

Candidates of a problem = the distinct answers among its ≈8 single 12B answers (runs/calib/gemma-4-12B-it_think) and the
12B swarm's final answer (runs/swarm/ng207_12b_swarm). Problems where all of them agree need no check: that answer is
submitted. Otherwise the blind 12B checker (swarm/verify.py) judges every candidate (at most 6, the most-voted).

Selection rule, fixed before the results (votes = single answers for it + 2 if the swarm gave it):
  the most-voted CONFIRMED candidate; if none is confirmed, the most-voted UNCLEAR one; if all are refuted, the most-voted.
  Ties are split (expected value). Variants with other swarm weights and without the swarm are reported as secondary.

Round 15 (MIX, data/verify_mix.jsonl): the 12B pool + the 31B's own single answers (3-4 per problem, frozen at build time
in data/verify_mix_31b.json); a 31B answer counts W_BIG = 2 votes. Several checker trials are combined per candidate by
verdict score = #CONFIRMED - #REFUTED (highest score wins, ties by votes, then split); for one trial this is the rule above.
"""
import json, sys
from collections import Counter
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis"), str(ROOT / "calib")]
from adaptive import problem_rows, boot  # noqa: E402
from scaling import maj_at_k  # noqa: E402

CANDS = {"12B": ROOT / "data/verify_12b.jsonl", "E4B": ROOT / "data/verify_e4b.jsonl", "MIX": ROOT / "data/verify_mix.jsonl"}
model_of = lambda run: "E4B" if "e4b" in Path(run).name else "MIX" if "mix" in Path(run).name else "12B"
MAX_ITEMS = 6
W_BIG = 2                                   # votes of one 31B single answer in the MIX pool
FREEZE31 = ROOT / "data/verify_mix_31b.json"  # {id: [31B sample indices in the MIX pool]}


def rows_of(model):
    """problem rows; for MIX the 12B rows + x31 = the frozen 31B single answers"""
    if model != "MIX":
        return problem_rows(model)
    from analyze import per_sample
    b31 = per_sample(ROOT / "runs/calib/gemma-4-31B-it_think")
    rows = problem_rows("12B")
    if FREEZE31.exists():
        fz = json.loads(FREEZE31.read_text())
        for r in rows:
            r["x31"] = [x for x in b31.get(r["id"], []) if x["sample"] in set(fz.get(r["id"], []))]
    else:
        for r in rows:
            r["x31"] = list(b31.get(r["id"], []))
    return rows


def pool_of(r):
    """{key: dict(answer, single votes, swarm votes, ok)} for one problem row of adaptive.problem_rows"""
    c = {}
    new = lambda ans: dict(answer=str(ans).strip(), single=0, swarm=0, big=0, ok=False)
    for x in r["ss"]:
        if x["key"] is None:
            continue
        e = c.setdefault(x["key"], new(x["pred"]))
        e["single"] += 1; e["ok"] |= x["ok"]
    for k, ok, raw in zip(r["swk"], r["swok"], r["swraw"]):
        if k is None:
            continue
        e = c.setdefault(k, new(raw))
        e["swarm"] += 1; e["ok"] |= ok
    for x in r.get("x31", []):   # MIX pool only
        if x["key"] is None:
            continue
        e = c.setdefault(x["key"], new(x["pred"]))
        e["big"] += 1; e["ok"] |= x["ok"]
    return c


def build(model="12B"):
    CANDS_ = CANDS[model]
    rows = rows_of(model)
    if model == "MIX":
        FREEZE31.write_text(json.dumps({r["id"]: [x["sample"] for x in r["x31"]] for r in rows}))
    n_un = 0
    with open(CANDS_, "w") as f:
        for r in rows:
            c = pool_of(r)
            if len(c) <= 1:
                n_un += 1; continue
            ks = sorted(c, key=lambda k: -(c[k]["single"] + 2 * c[k]["swarm"] + W_BIG * c[k]["big"]))
            f.write(json.dumps(dict(id=r["id"], cands=[dict(key=k, answer=c[k]["answer"], single=c[k]["single"],
                                                            swarm=c[k]["swarm"], big=c[k]["big"]) for k in ks]),
                               ensure_ascii=False) + "\n")
    m = sum(1 for _ in open(CANDS_))
    print(f"wrote {CANDS_}: {m} problems to check, {n_un} unanimous (incl. no answer at all)")


def pick(c, verd, w, use_swarm=True):
    """expected correctness of the selection rule; verd: {key: CONFIRMED/REFUTED/UNCLEAR}"""
    v = {k: e["single"] + W_BIG * e.get("big", 0) + (w * e["swarm"] if use_swarm else 0) for k, e in c.items()}
    v = {k: x for k, x in v.items() if x > 0}
    if not v:
        return 0.0
    for tier in ("CONFIRMED", "UNCLEAR", None):
        pool = [k for k in v if tier is None or verd.get(k, "UNCLEAR") == tier]
        if pool:
            t = max(v[k] for k in pool); win = [k for k in pool if v[k] == t]
            return sum(c[k]["ok"] for k in win) / len(win)


def soft(c, verd, w=4, conf=2.0, ref=0.5, unc=1.0):
    """frozen soft rule (chosen on the first 35 checked problems of round 13): score = votes x multiplier by verdict"""
    mult = {"CONFIRMED": conf, "UNCLEAR": unc, "REFUTED": ref}
    sc = {k: (e["single"] + W_BIG * e.get("big", 0) + w * e["swarm"]) * mult[verd.get(k, "UNCLEAR")] for k, e in c.items()}
    t = max(sc.values()); win = [k for k in sc if abs(sc[k] - t) < 1e-9]
    return sum(c[k]["ok"] for k in win) / len(win)


def pick_multi(c, verds, w=2):
    """several checker trials: verdict score = #CONFIRMED - #REFUTED per candidate; highest score, then votes; ties split"""
    v = {k: e["single"] + W_BIG * e.get("big", 0) + w * e["swarm"] for k, e in c.items()}
    v = {k: x for k, x in v.items() if x > 0}
    if not v:
        return 0.0
    s = {k: sum((d.get(k) == "CONFIRMED") - (d.get(k) == "REFUTED") for d in verds) for k in v}
    best = max((s[k], v[k]) for k in v); win = [k for k in v if (s[k], v[k]) == best]
    return sum(c[k]["ok"] for k in win) / len(win)


DEV_N = 35   # the first 35 problems round 13 finished: the soft rule was chosen on them


def evaluate(run):
    model = model_of(run)
    rows = {r["id"]: r for r in rows_of(model)}
    res = {}
    for l in open(run / "results.jsonl"):
        x = json.loads(l)
        if not x.get("error"):
            res.setdefault(x["id"], []).append(x)
    rng = np.random.default_rng(0)
    ids = list(rows)
    sw = np.array([rows[i]["sw"] for i in ids]); maj = np.array([maj_at_k(rows[i]["ss"], len(rows[i]["ss"])) for i in ids])
    todo = [json.loads(l)["id"] for l in open(CANDS[model])]
    have = [i for i in todo if i in res]
    out = [f"# Pooled verification of the {model} answers, checker run `{run.name}` ({len(have)} of {len(todo)} contested problems checked)", ""]

    def score(i, w, use_swarm=True, rule=pick, nocheck=False):
        c = pool_of(rows[i])
        if len(c) <= 1:   # unanimous: submit it (no check)
            return float(any(e["ok"] for e in c.values())) if c else 0.0
        if nocheck:
            return pick(c, {}, w, use_swarm)
        if rule is pick_multi:
            return pick_multi(c, [{v["key"]: v["result"] for v in x["verdicts"]} for x in res[i]], w)
        if rule is soft:
            return float(np.mean([soft(c, {v["key"]: v["result"] for v in x["verdicts"]}) for x in res[i]]))
        vals = [pick(c, {v["key"]: v["result"] for v in x["verdicts"]}, w, use_swarm) for x in res[i]]
        return float(np.mean(vals))

    done_ids = [i for i in ids if i in have or i not in todo]   # every unanimous problem + the checked ones
    m = np.array([i in done_ids for i in ids])
    ntr = Counter(len(res[i]) for i in have)
    out += [f"On the {m.sum()} problems available so far (all unanimous + checked ones); checker trials per problem: "
            f"{dict(sorted(ntr.items()))}", "",
            "| method | pass@1 | vs swarm [95% CI] |", "|---|---|---|",
            f"| maj@8 | {maj[m].mean():.3f} | |", f"| swarm | {sw[m].mean():.3f} | |"]
    variants = [("vote, no checker: maj@8 + swarm ×2", dict(w=2, nocheck=True)),
                ("vote, no checker: maj@8 + swarm ×4", dict(w=4, nocheck=True)),
                ("**checker, pre-registered rule (w = 2)**", dict(w=2)),
                ("checker, same rule, w = 1", dict(w=1)), ("checker, same rule, w = 4", dict(w=4)),
                ("**checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5)", dict(w=4, rule=soft)),
                ("checker over the 8 single answers only (no swarm)", dict(w=0, use_swarm=False)),
                ("checker, trials combined (score = #CONFIRMED - #REFUTED, then votes, w = 2)", dict(w=2, rule=pick_multi))]
    for lab, kw in variants:
        s = np.array([score(i, **kw) for i in done_ids]); d = s - sw[m]; lo, hi = boot(d, rng)
        out.append(f"| {lab} | {s.mean():.3f} | {d.mean()*100:+.1f} [{lo*100:+.1f}, {hi*100:+.1f}] |")
    # the checker's contribution beyond the vote, on contested problems; for round 13 only on the held-out ones
    fin = [json.loads(l)["id"] for l in open(run / "results.jsonl") if not json.loads(l).get("error")]
    test = [i for i in have if not (run.name == "verify_12b" and i in set(fin[:DEV_N]))]
    for lab, kw in [("pre-registered rule", dict(w=2)), ("soft rule", dict(w=4, rule=soft))]:
        a = np.array([score(i, **kw) for i in test]); b = np.array([score(i, w=kw["w"], nocheck=True) for i in test])
        d = a - b; lo, hi = boot(d, rng)
        out.append(f"\nChecker's contribution beyond the same vote, {lab}, on {len(test)} contested problems"
                   f"{' (held out: not used to choose the soft rule)' if run.name == 'verify_12b' else ''}: "
                   f"{a.mean():.3f} vs {b.mean():.3f}, **{d.mean()*100:+.1f} [{lo*100:+.1f}, {hi*100:+.1f}]**")
    # checker quality on these pools
    tab = Counter()
    for i in have:
        c = pool_of(rows[i])
        for x in res[i]:
            for v in x["verdicts"]:
                tab[(c[v["key"]]["ok"] if v["key"] in c else None, v["result"])] += 1
    for ok in (True, False):
        tot = sum(tab[(ok, r)] for r in ("CONFIRMED", "REFUTED", "UNCLEAR"))
        if tot:
            out.append(f"\n{'right' if ok else 'wrong'} candidates ({tot}): " + ", ".join(
                f"{r} {tab[(ok, r)] / tot:.0%}" for r in ("CONFIRMED", "REFUTED", "UNCLEAR")))
    conf = tab[(True, "CONFIRMED")] + tab[(False, "CONFIRMED")]
    if conf:
        out.append(f"precision of CONFIRMED: {tab[(True, 'CONFIRMED')] / conf:.0%}")
    toks = [x["completion_tokens"] for i in have for x in res[i]]
    if toks:
        out.append(f"\nchecker tokens per checked problem: mean {np.mean(toks)/1e3:.0f}k, median {np.median(toks)/1e3:.0f}k")
    p = ROOT / f"results/{run.name}.md"; p.write_text("\n".join(out) + "\n"); print("\n".join(out))


if __name__ == "__main__":
    if sys.argv[1] == "build":
        build(sys.argv[2] if len(sys.argv) > 2 else "12B")
    else:
        evaluate(Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "runs/swarm/verify_12b")
