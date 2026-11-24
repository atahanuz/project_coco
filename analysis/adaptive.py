"""Adaptive swarm (offline, existing runs): draw m single answers first; if at least t of them agree, submit that
answer and stop; otherwise call the swarm and submit its answer. Everything the rule looks at is available at test time
(the single answers' agreement), never the gold answer.

  python analysis/adaptive.py            -> results/adaptive.md

Expected values: every m-subset of a problem's single samples is one equally likely draw (as in maj_at_k), and the swarm
term averages over its trials. Cost = m single answers + the swarm's tokens when it is called.
Also reported: "swarm as a vote" = the 8 single answers plus the swarm's answer counted w times.
"""
import json, sys
from collections import Counter
from itertools import combinations
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "analysis"), str(ROOT / "calib")]
from analyze import per_sample, key  # noqa: E402
from scaling import maj_at_k  # noqa: E402
from compare import interrupted  # noqa: E402

IDS = open(ROOT / "data/nongeo207.txt").read().split()
MODELS = {"12B": ("gemma-4-12B-it_think", "ng207_12b_swarm"), "E4B": ("gemma-4-E4B-it_think", "ng207_e4b_swarm")}


def swarm_runs(name):
    d = ROOT / "runs/swarm" / name
    out = {}
    for l in open(d / "results.jsonl"):
        r = json.loads(l)
        if r.get("error") or interrupted(d, r):
            continue
        out.setdefault(r["id"], {})[r["trial"]] = r  # last write wins per trial
    return {pid: list(v.values()) for pid, v in out.items()}


def top(sub):
    v = Counter(x["key"] for x in sub if x["key"] is not None)
    if not v:
        return 0, [], set()
    t = max(v.values())
    return t, [k for k, c in v.items() if c == t], {x["key"] for x in sub if x["ok"]}


def problem_rows(model):
    calib, sw = MODELS[model]
    by, rs = per_sample(ROOT / "runs/calib" / calib), swarm_runs(sw)
    rows = []
    for pid in IDS:
        ss, tr = by.get(pid, []), rs.get(pid, [])
        if not ss or not tr:
            continue
        rows.append(dict(id=pid, ss=ss, sw=np.mean([bool(r["correct"]) for r in tr]),
                         swk=[key(r.get("final")) for r in tr], swok=[bool(r["correct"]) for r in tr],
                         swraw=[r.get("final") for r in tr],
                         swtok=np.mean([r["completion_tokens"] for r in tr]), stok=np.mean([x["toks"] for x in ss])))
    return rows


def gated(row, m, t):
    """(expected accuracy, P(swarm called)) for one problem"""
    acc, esc, n = 0.0, 0.0, 0
    for sub in combinations(row["ss"], m):
        c, winners, ok = top(sub)
        n += 1
        if c >= t:
            acc += sum(w in ok for w in winners) / len(winners)
        else:
            acc += row["sw"]; esc += 1
    return acc / n, esc / n


def swarm_vote(row, w):
    """8 single answers + the swarm's answer with weight w; ties split; averaged over swarm trials"""
    vals = []
    for sk, sok in zip(row["swk"], row["swok"]):
        v = Counter(x["key"] for x in row["ss"] if x["key"] is not None)
        if sk is not None:
            v[sk] += w
        if not v:
            vals.append(0.0); continue
        t = max(v.values()); winners = [k for k, c in v.items() if c == t]
        ok = {x["key"] for x in row["ss"] if x["ok"]} | ({sk} if sok else set())
        vals.append(sum(k in ok for k in winners) / len(winners))
    return float(np.mean(vals))


def boot(x, rng, B=10000):
    x = np.asarray(x)
    b = x[rng.integers(0, len(x), (B, len(x)))].mean(1)
    return np.percentile(b, [2.5, 97.5])


def main():
    rng = np.random.default_rng(0)
    out = ["# Adaptive swarm: call the swarm only when single answers disagree (offline, existing runs)", "",
           "Rule (m, t): draw m single answers; if at least t agree, submit their answer, otherwise run the swarm. "
           "The rule uses only the single answers' agreement, never the gold answer. Expected values over every m-subset "
           "of the ≈8 stored single answers and over the swarm's trials. Paired 95% CIs by bootstrap over problems.", ""]
    for model in ["12B", "E4B"]:
        rows = problem_rows(model)
        n = len(rows)
        p1 = np.array([np.mean([x["ok"] for x in r["ss"]]) for r in rows])
        maj = np.array([maj_at_k(r["ss"], len(r["ss"])) for r in rows])
        sw = np.array([r["sw"] for r in rows])
        stok = np.array([r["stok"] for r in rows]); swtok = np.array([r["swtok"] for r in rows])
        k = np.array([len(r["ss"]) for r in rows])
        out += [f"## {model} ({n} problems)", "",
                "| method | pass@1 | vs swarm | swarm called | tokens / problem |", "|---|---|---|---|---|",
                f"| single answer | {p1.mean():.3f} | | | {stok.mean()/1e3:.0f}k |",
                f"| maj@8 | {maj.mean():.3f} | | | {(stok*k).mean()/1e3:.0f}k |",
                f"| swarm | {sw.mean():.3f} | | 100% | {swtok.mean()/1e3:.0f}k |"]
        best = None
        for m, t in [(2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (6, 5)]:
            keep = [i for i, r in enumerate(rows) if len(r["ss"]) >= m]
            g = [gated(rows[i], m, t) for i in keep]
            acc = np.array([a for a, _ in g]); esc = np.array([e for _, e in g])
            d = acc - sw[keep]; lo, hi = boot(d, rng)
            cost = (m * stok[keep] + esc * swtok[keep]).mean()
            note = "" if len(keep) == n else f" ({len(keep)} problems with ≥ {m} answers)"
            out.append(f"| adaptive m={m}, t={t}{note} | **{acc.mean():.3f}** | {d.mean()*100:+.1f} [{lo*100:+.1f}, {hi*100:+.1f}] "
                       f"| {esc.mean():.0%} | {cost/1e3:.0f}k |")
            if len(keep) == n and (best is None or acc.mean() > best[0]):
                best = (acc.mean(), m, t)
        for w in [1, 2, 3, 4]:
            v = np.array([swarm_vote(r, w) for r in rows]); d = v - sw; lo, hi = boot(d, rng)
            out.append(f"| maj@8 + swarm answer ×{w} | {v.mean():.3f} | {d.mean()*100:+.1f} [{lo*100:+.1f}, {hi*100:+.1f}] "
                       f"| 100% | {((stok*k)+swtok).mean()/1e3:.0f}k |")
        anyc = np.array([float(any(x["ok"] for x in r["ss"]) or any(r["swok"])) for r in rows])
        out += ["", f"Upper bound, any of the single answers or the swarm right: {anyc.mean():.3f}.", ""]
        # where the gated rule wins and loses, for the best full-coverage rule
        _, m, t = best
        g = np.array([gated(r, m, t)[0] for r in rows])
        bucket = lambda lo, hi: (p1 >= lo) & (p1 <= hi)
        out += [f"By single-answer difficulty, adaptive m={m}, t={t} (buckets from the same samples, so the hard buckets favour "
                "the swarm through regression to the mean):", "",
                "| bucket | problems | single | maj@8 | swarm | adaptive |", "|---|---|---|---|---|---|"]
        for lo, hi, lab in [(0, 0, "0 right"), (1e-9, .375, "≤ 3/8"), (.375 + 1e-9, .75, "3/8 – 6/8"), (.75 + 1e-9, 1, "> 6/8")]:
            b = bucket(lo, hi)
            out.append(f"| {lab} | {b.sum()} | {p1[b].mean():.3f} | {maj[b].mean():.3f} | {sw[b].mean():.3f} | {g[b].mean():.3f} |")
        out.append("")
    p = ROOT / "results/adaptive.md"
    p.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
