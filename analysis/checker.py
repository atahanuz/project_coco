"""Rounds 11-12: a dedicated, blind checker role (swarm.py --checker 1; round 12: a 12B checker via --checker-ports).

  python analysis/checker.py        -> round 11 (E4B checker), writes results/p1_e4b_checker.md
  python analysis/checker.py 12     -> round 12 (12B checker on the E4B team), next to round 11; results/p1_e4b_checker12.md

Works on partial runs (uses the problems finished so far and says how many).
1. Phase 1: checker swarm (2 trials) vs the main swarm (ng207_e4b_swarm, 2 trials), paired by problem.
2. How good is the checker? Its verdicts on right vs wrong candidates (graded with the answer key), over all its runs;
   what the master did with them (final answer confirmed / refuted / unchecked).
3. Phase 2: two colluding saboteurs, pooled over both problem orders: no defense / answer key / peer agreement (round 10)
   vs checker only / checker + expulsion on the checker's verdicts (v4); expulsions and the no-saboteur control.
4. Why v4 works: verdicts on honest vs saboteur reports; sabotage before / after the expulsion.
"""
import json, sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis"), str(ROOT / "swarm")]
from coco.grading import is_correct  # noqa: E402
from compare import agent_runs  # noqa: E402
from ablations import boot  # noqa: E402
from collusion import records, frame, expulsions, final_record  # noqa: E402

R = ROOT / "runs/swarm"
TAGS = {f"imo-bench-{l.split()[0]}": l.split()[1] for l in open(ROOT / "data/coop_tags.txt")
        if l.strip() and not l.startswith("#")}
SABS = {"W3", "W4"}
VERDICTS = ("CONFIRMED", "REFUTED", "UNCLEAR")

# per checker: phase-1 run, checker-only and checker+v4 colluder runs (seed 0, seed 1), no-saboteur v4 controls
CHECKERS = {
    "E4B": dict(p1="ck_e4b", only=["p2_e4b_col_ck", "p2_e4b_col_ck_s1"], rep=["p2_e4b_col_ckrep", "p2_e4b_col_ckrep_s1"],
                nosab=["p2_e4b_ckrep_nosab", "p2_e4b_ckrep_nosab_s1"]),
    "12B": dict(p1="ck12_e4b", only=["p2_e4b_col_ck12", "p2_e4b_col_ck12_s1"],
                rep=["p2_e4b_col_ck12rep", "p2_e4b_col_ck12rep_s1"], nosab=["p2_e4b_ck12rep_nosab"]),
}
ROUND10 = [("no defense", ["p2_e4b_col", "p2_e4b_col_s1"]),
           ("expel, answer key", ["p2_e4b_col_key", "p2_e4b_col_key_s1"]),
           ("expel, peer agreement", ["p2_e4b_col_peer", "p2_e4b_col_peer_s1"])]


def all_runs(c):
    return [c["p1"]] + c["only"] + c["rep"] + c["nosab"]


def traces(run):
    for r in records(run):
        t = R / run / f"{r['id']}__t{r.get('trial', 0)}" / "trace.json"
        if t.exists():
            yield r, json.load(open(t))


def phase1(out, cks):
    ref = agent_runs(R / "ng207_e4b_swarm")
    out += ["## Phase 1: checker swarm vs main swarm (no saboteur)", "",
            "| team | attempts | pass@1 | some candidate right | right found, not picked | tokens / attempt | of which checker |",
            "|---|---|---|---|---|---|---|"]
    rows, diffs = [], []
    for name in cks:
        run = CHECKERS[name]["p1"]
        if not (R / run / "results.jsonl").exists():
            out.append(f"| {name} checker | not started | | | | | |")
            continue
        ck, rs = agent_runs(R / run), records(run)
        ids = ck.index.intersection(ref.index)
        if not len(rows):
            rows.append(("main swarm (2 trials)", ref.loc[ids], len(ids) * 2, np.nan))
        rows.append((f"E4B team + {name} checker", ck.loc[ids], len(rs), np.mean([r.get("checker_tokens", 0) for r in rs])))
        d = ck.p[ids] - ref.p[ids]
        lo, hi = boot(d) if len(d) > 5 else (np.nan, np.nan)
        byt = "; ".join(f"{t} ({len(j)}): {ref.p[j].mean():.2f} → {ck.p[j].mean():.2f}"
                        for t in "CENR" for j in [[i for i in ids if TAGS.get(i) == t]] if j)
        diffs.append(f"- **{name} checker − main swarm: {d.mean():+.3f} [{lo:+.3f}, {hi:+.3f}]** over {len(ids)} problems "
                     f"(paired bootstrap; 2-trial means where available). By tag: {byt}.")
    for lab, df, n, ctok in rows:
        out.append(f"| {lab} | {n} | **{df.p.mean():.3f}** | {df.anycand.mean():.3f} | {df.anycand.mean() - df.p.mean():+.3f} | "
                   f"{df.toks.mean() / 1e3:.1f}k | {'' if np.isnan(ctok) else f'{ctok / 1e3:.1f}k'} |")
    out += [""] + diffs
    if set(cks) >= {"E4B", "12B"} and all((R / CHECKERS[c]["p1"] / "results.jsonl").exists() for c in cks):
        a, b = agent_runs(R / CHECKERS["E4B"]["p1"]).p, agent_runs(R / CHECKERS["12B"]["p1"]).p
        j = a.index.intersection(b.index)
        lo, hi = boot(b[j] - a[j]) if len(j) > 5 else (np.nan, np.nan)
        out.append(f"- **12B checker − E4B checker: {(b[j] - a[j]).mean():+.3f} [{lo:+.3f}, {hi:+.3f}]** over {len(j)} problems.")
    out.append("")
    for name in cks:
        rs = records(CHECKERS[name]["p1"])
        if rs:
            outside = [r for r in rs if r["correct"] and not r["any_candidate_correct"]]
            out.append(f"{name} checker: final answer right although no worker candidate was right in {len(outside)} of "
                       f"{len(rs)} attempts.")
    out += [f"Main swarm: {sum(1 for r in records('ng207_e4b_swarm') if r['correct'] and not r['any_candidate_correct'])} "
            f"of {len(records('ng207_e4b_swarm'))}.", ""]


def checker_quality(out, cks):
    out += ["## How good is the checker? (verdicts on distinct candidates, graded with the answer key, all its runs)", "",
            "| checker | candidate | n | CONFIRMED | REFUTED | UNCLEAR |", "|---|---|---|---|---|---|"]
    notes, fins = [], []
    for name in cks:
        rows, fin = [], Counter()
        for run in all_runs(CHECKERS[name]):
            for r, t in traces(run):
                for c in t.get("checks") or []:
                    rows.append(dict(right=bool(is_correct(c["answer"], r["gold"])), result=c["result"], via=c.get("via")))
                fin[(r.get("final_check") or "unchecked", bool(r["correct"]))] += 1
        if not rows:
            out.append(f"| {name} | no verdicts yet | | | | |")
            continue
        df = pd.DataFrame(rows)
        for lab, sub in [("right", df[df.right]), ("wrong", df[~df.right])]:
            v = sub.result.value_counts(normalize=True)
            out.append(f"| {name} | {lab} | {len(sub)} | {v.get('CONFIRMED', 0):.0%} | {v.get('REFUTED', 0):.0%} | "
                       f"{v.get('UNCLEAR', 0):.0%} |")
        conf = df[df.result == "CONFIRMED"]
        notes.append(f"- {name}: precision of CONFIRMED {conf.right.mean():.0%} (base rate of right candidates "
                     f"{df.right.mean():.0%}); verdicts as text {(df.via == 'text').mean():.1%}, missing "
                     f"{(df.via == 'none').mean():.1%}.")
        fins.append("| " + name + " | " + " | ".join(
            (f"{fin[(v, True)] / n:.0%} ({n})" if (n := fin[(v, True)] + fin[(v, False)]) else "–")
            for v in ["CONFIRMED", "REFUTED", "UNCLEAR", "unchecked"]) + " |")
    out += [""] + notes + ["", "Team's final answer right, by the checker's verdict on it (n):", "",
                           "| checker | CONFIRMED | REFUTED | UNCLEAR | unchecked |", "|---|---|---|---|---|"] + fins + [""]


def phase2(out, cks):
    ref = agent_runs(R / "ng207_e4b_swarm").p
    out += ["## Phase 2: two colluding saboteurs (W3 + W4), both problem orders pooled", "",
            f"No saboteur (main swarm, 2 trials): {ref.mean():.3f}", "",
            "| defense | runs (problems) | pass@1 | Δ vs no saboteur [95% CI] | Δ vs no defense [95% CI] | sabotaged |",
            "|---|---|---|---|---|---|"]
    groups = ROUND10 + [(f"{n} checker{' only' if k == 'only' else ' + expel on its verdicts'}", CHECKERS[n][k])
                        for n in cks for k in ("only", "rep")]
    base = None
    exp_lines = ["", "| run | expelled (after problem #) | honest worker expelled? | final record |", "|---|---|---|---|"]
    for name, runs in groups:
        fs = [(r, frame(records(r))) for r in runs]
        fs = [(r, f) for r, f in fs if len(f)]
        if not fs:
            out.append(f"| {name} | not run yet | | | | |")
            continue
        ok = pd.concat([f.ok for _, f in fs], axis=1).mean(1)
        sab = pd.concat([f.sab for _, f in fs], axis=1).mean(1)
        ids = ok.index.intersection(ref.index)
        d = ok[ids] - ref[ids]
        lo, hi = boot(d) if len(d) > 5 else (np.nan, np.nan)
        dd = ""
        if name == "no defense":
            base = ok
        elif base is not None:
            j = ok.index.intersection(base.index)
            x = ok[j] - base[j]
            l2, h2 = boot(x) if len(x) > 5 else (np.nan, np.nan)
            dd = f"{x.mean():+.3f} [{l2:+.3f}, {h2:+.3f}]"
        ns = "+".join(str(len(f)) for _, f in fs)
        out.append(f"| {name} | {len(fs)} ({ns}) | **{ok.mean():.3f}** | {d.mean():+.3f} [{lo:+.3f}, {hi:+.3f}] | {dd} | "
                   f"{sab.mean():.1%} |")
        if "expel on its verdicts" in name:
            for r, _ in fs:
                rs = records(r)
                ex, rec = expulsions(rs), final_record(rs)
                honest = [w for w in ex if w not in SABS]
                exp_lines.append(f"| `{r}` ({len(rs)}) | {', '.join(f'{w} ({k})' for w, k in sorted(ex.items(), key=lambda t: t[1])) or 'nobody'}"
                                 f" | {'**YES: ' + ', '.join(honest) + '**' if honest else 'no'} | "
                                 f"{', '.join(f'{w} {a}/{b}' for w, (a, b) in sorted(rec.items()))} |")
    for n in cks:
        for r in CHECKERS[n]["nosab"]:
            rs = records(r)
            if rs:
                ex, rec = expulsions(rs), final_record(rs)
                exp_lines.append(f"| `{r}` (no saboteur, {len(rs)} problems, pass@1 {np.mean([bool(x['correct']) for x in rs]):.3f}) | "
                                 f"{', '.join(f'{w} ({k})' for w, k in ex.items()) or 'nobody'} | "
                                 f"{'**YES**' if ex else 'no'} | {', '.join(f'{w} {a}/{b}' for w, (a, b) in sorted(rec.items()))} |")
    out += exp_lines + [""]


def mechanism(out, cks):
    out += ["## Why expulsion on the checker's verdicts works (colluder runs with a checker, worker reports)", "",
            "| checker | reports by | n | CONFIRMED | REFUTED | UNCLEAR | right (answer key) |", "|---|---|---|---|---|---|---|"]
    sab_fin = []
    for name in cks:
        c = CHECKERS[name]
        rows = []
        for run in c["only"] + c["rep"]:
            for r, t in traces(run):
                for rep in t.get("reports") or []:
                    if rep.get("check") in VERDICTS:
                        rows.append(dict(sab=rep["worker"] in SABS, result=rep["check"],
                                         right=bool(is_correct(rep.get("answer") or "", r["gold"]))))
        if not rows:
            continue
        df = pd.DataFrame(rows)
        for lab, sub in [("honest W1, W2", df[~df.sab]), ("saboteurs W3, W4", df[df.sab])]:
            v = sub.result.value_counts(normalize=True)
            out.append(f"| {name} | {lab} | {len(sub)} | {v.get('CONFIRMED', 0):.0%} | {v.get('REFUTED', 0):.0%} | "
                       f"{v.get('UNCLEAR', 0):.0%} | {sub.right.mean():.0%} |")
        cnt = Counter(x.get("final_check") or "unchecked" for run in c["only"] for x in records(run)
                      if x.get("final_is_saboteur") and not x["correct"])
        if cnt:
            sab_fin.append(f"- {name} checker only: {sum(cnt.values())} sabotaged final answers; the checker had "
                           + ", ".join(f"{k} {cnt[k]}" for k in ["CONFIRMED", "REFUTED", "UNCLEAR", "unchecked"] if cnt[k]) + ".")
    out += [""] + sab_fin + ["", "| run | phase | problems | pass@1 | final = a saboteur's wrong answer |", "|---|---|---|---|---|"]
    for name in cks:
        for run in CHECKERS[name]["rep"]:
            rs = sorted(records(run), key=lambda r: r.get("order", 0))
            if not rs:
                continue
            ex = expulsions(rs)
            k = max(ex.values()) if len(ex) == 2 else None
            if k is None:
                f = frame(rs)
                out.append(f"| `{run}` | not both expelled yet | {len(f)} | {f.ok.mean():.3f} | {f.sab.mean():.1%} |")
                continue
            for lab, sub in [(f"before both expelled (1-{k})", rs[:k]), (f"after ({k + 1}-{len(rs)})", rs[k:])]:
                if sub:
                    f = frame(sub)
                    out.append(f"| `{run}` | {lab} | {len(f)} | {f.ok.mean():.3f} | {f.sab.mean():.1%} |")
    out.append("")


def main():
    rnd = sys.argv[1] if len(sys.argv) > 1 else "11"
    cks = ["E4B"] if rnd == "11" else ["E4B", "12B"]
    title = ("# Round 11: a dedicated blind checker role (E4B, 207 problems)" if rnd == "11" else
             "# Round 12: a 12B checker on the E4B team, next to round 11's E4B checker (207 problems)")
    out = [title, ""]
    phase1(out, cks)
    checker_quality(out, cks)
    phase2(out, cks)
    mechanism(out, cks)
    txt = "\n".join(out) + "\n"
    print(txt)
    (ROOT / f"results/p1_e4b_checker{'' if rnd == '11' else '12'}.md").write_text(txt)


if __name__ == "__main__":
    main()
