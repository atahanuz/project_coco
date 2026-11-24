"""Pooled verification (round 13): the blind CHECKER of swarm.py judges a fixed list of candidate answers per problem.

The candidates come from existing runs (e.g. the 8 single 12B answers + the 12B swarm's answer, data/verify_12b.jsonl,
built by analysis/verify_pool.py). The checker sees only the problem and the distinct candidate values under random
labels: no vote counts, no sources, no reasoning (the same prompt, tools and verdict handling as swarm.py --checker 1).
Answer selection from the verdicts happens offline (analysis/verify_pool.py), so the rule can be changed without rerunning.

  python swarm/verify.py --cands data/verify_12b.jsonl --pool data/pool.jsonl --out runs/verify/v12b --ports 8001,8002,8003

Resumable: finished (id, trial) pairs in results.jsonl are skipped; errored ones are rerun.
"""
from __future__ import annotations

import argparse, asyncio, json, random, sys, tempfile, time, traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import swarm as S  # noqa: E402


async def check(llm, prob, item, trial, a, outdir):
    cands = item["cands"][: a.max_items]
    order = list(range(len(cands)))
    random.Random(f"{prob['id']}|verify|{trial}").shuffle(order)
    labs = "ABCDEFGH"[: len(cands)]
    shown = [(lab, cands[i]["answer"]) for lab, i in zip(labs, order)]
    verdicts = {lab: None for lab in labs}
    budget, log = S.Budget(), []
    ws = tempfile.mkdtemp(prefix="ws_", dir=outdir)
    res = await S.run_agent(llm, budget, S.CHECKER_SYSTEM, S.checker_user(prob["problem"], shown), S.TOOLS_CHECKER, None,
                            "CHECKER", 1, ws, a, log, verdicts=verdicts)
    out = []
    for lab, i in zip(labs, order):
        v = verdicts[lab] or dict(result="UNCLEAR", evidence="(no verdict given)", via="none")
        out.append(dict(label=lab, key=cands[i]["key"], answer=cands[i]["answer"], **v))
    return out, res, budget, log


async def main(a):
    pool = {p["id"]: p for p in map(json.loads, open(a.pool))}
    items = [json.loads(l) for l in open(a.cands)]
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res_path = out / "results.jsonl"
    done = set()
    if res_path.exists():
        for l in open(res_path):
            r = json.loads(l)
            if not r.get("error"):
                done.add((r["id"], r["trial"]))
    jobs = [(it, t) for t in range(a.trials) for it in items if (it["id"], t) not in done]
    print(f"{len(items)} problems x {a.trials} trials; {len(jobs)} to run; ports {a.ports}; max {a.max_items} candidates",
          flush=True)
    llm = S.LLM(a.ports.split(","), bool(a.think), a.max_ctx)
    sem, lock, t0, n = asyncio.Semaphore(a.parallel), asyncio.Lock(), time.time(), 0

    async def one(it, trial):
        nonlocal n
        async with sem:
            if a.stop_new_after and time.time() > a.stop_new_after:
                return
            t = time.time(); d = out / f"{it['id']}__t{trial}"; d.mkdir(exist_ok=True)
            try:
                verd, res, budget, log = await check(llm, pool[it["id"]], it, trial, a, d)
                err = None
            except Exception:
                verd, err = None, traceback.format_exc()[-2000:]
        rec = dict(id=it["id"], trial=trial, error=err, seconds=round(time.time() - t, 1), n_cands=len(it["cands"]))
        if verd is not None:
            rec.update(verdicts=verd, status=res["status"], steps=res["steps"], calls=budget.calls,
                       prompt_tokens=budget.prompt, completion_tokens=budget.completion,
                       n_python=sum(1 for e in log for tc in e.get("tool_calls", []) if tc["name"] == "run_python"))
            (d / "trace.json").write_text(json.dumps(dict(record=rec, log=log), ensure_ascii=False, indent=1))
        async with lock:
            with open(res_path, "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
            vs = " ".join(f"{v['label']}={v['result'][:4]}" for v in verd) if verd else "-"
            print(f"[{n}/{len(jobs)} {(time.time() - t0) / 60:.1f} min] {it['id']} t{trial}: {vs} "
                  f"tokens={rec.get('completion_tokens')} err={bool(err)}", flush=True)

    await asyncio.gather(*(one(it, t) for it, t in jobs))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cands", required=True)
    ap.add_argument("--pool", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ports", default="8000")
    ap.add_argument("--trials", type=int, default=1)
    ap.add_argument("--parallel", type=int, default=16)
    ap.add_argument("--max-items", type=int, default=6)
    ap.add_argument("--think", type=int, default=1)
    ap.add_argument("--max-steps", type=int, default=12)
    ap.add_argument("--call-tokens", type=int, default=32768)
    ap.add_argument("--agent-tokens", type=int, default=65536)
    ap.add_argument("--max-ctx", type=int, default=65536)
    ap.add_argument("--py-timeout", type=int, default=60)
    ap.add_argument("--stop-new-after", type=float, default=0)
    asyncio.run(main(ap.parse_args()))
