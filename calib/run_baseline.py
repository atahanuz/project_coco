"""Single-model baseline: k independent attempts per problem, no tools, no cooperation.

Talks to one or more OpenAI-compatible vLLM servers (one per GPU) and appends one
JSON line per finished sample, so the run is resumable and survives a time limit.

  python run_baseline.py --pool pool.jsonl --out samples.jsonl --ports 8000,8001 --k 8
"""
import argparse, asyncio, json, random, time
from pathlib import Path
from openai import AsyncOpenAI

PROMPT = ("Solve the following olympiad problem. Reason carefully, then give the final "
          "answer in \\boxed{{}}.\n\n{problem}")


def load_done(path: Path):
    done = set()
    if path.exists():
        for line in path.open():
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if r.get("error") is None:
                done.add((r["id"], r["sample"]))
    return done


async def main(a):
    pool = [json.loads(l) for l in open(a.pool)]
    if a.only_autograde:
        pool = [p for p in pool if p["autograde"]]
    if a.ids:
        keep = set(open(a.ids).read().split())
        pool = [p for p in pool if p["id"] in keep]
    out = Path(a.out)
    done = load_done(out)
    jobs = [(p, s) for p in pool for s in range(a.k) if (p["id"], s) not in done]
    random.Random(0).shuffle(jobs)  # mix easy/hard so servers stay evenly loaded
    print(f"{len(pool)} problems x {a.k} = {len(pool) * a.k}; {len(done)} done, {len(jobs)} to go", flush=True)

    clients = [AsyncOpenAI(base_url=f"http://localhost:{p}/v1", api_key="x", timeout=6 * 3600, max_retries=1)
               for p in a.ports.split(",")]
    sem = [asyncio.Semaphore(a.concurrency) for _ in clients]
    lock = asyncio.Lock()
    fout = out.open("a")
    t0, n_done = time.time(), 0

    async def one(i, p, s):
        nonlocal n_done
        ci = i % len(clients)
        async with sem[ci]:
            t = time.time()
            rec = dict(id=p["id"], sample=s, model=a.model_name, think=a.think)
            try:
                r = await clients[ci].chat.completions.create(
                    model="m",
                    messages=[{"role": "user", "content": PROMPT.format(problem=p["problem"])}],
                    temperature=a.temperature, top_p=0.95, max_tokens=a.max_tokens, seed=1000 * s + 17,
                    extra_body={"top_k": 64, "chat_template_kwargs": {"enable_thinking": a.think}},
                )
                m = r.choices[0].message
                rec.update(content=m.content,
                           reasoning=getattr(m, "reasoning", None) or getattr(m, "reasoning_content", None),
                           finish_reason=r.choices[0].finish_reason,
                           prompt_tokens=r.usage.prompt_tokens, completion_tokens=r.usage.completion_tokens,
                           seconds=round(time.time() - t, 1), error=None)
            except Exception as e:  # keep going; failed samples are retried on resume
                rec.update(error=repr(e)[:500], seconds=round(time.time() - t, 1))
        async with lock:
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()
            n_done += 1
            if n_done % 50 == 0:
                el = time.time() - t0
                print(f"{n_done}/{len(jobs)} done, {el / 60:.1f} min, eta {el / n_done * (len(jobs) - n_done) / 60:.1f} min", flush=True)

    await asyncio.gather(*(one(i, p, s) for i, (p, s) in enumerate(jobs)))
    fout.close()
    print("finished", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ports", default="8000")
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--max-tokens", type=int, default=16384)
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--concurrency", type=int, default=128, help="in-flight requests per server")
    ap.add_argument("--think", type=int, default=1)
    ap.add_argument("--model-name", default="")
    ap.add_argument("--ids", default="", help="optional file with problem ids to run")
    ap.add_argument("--only-autograde", type=int, default=0)
    asyncio.run(main(ap.parse_args()))
