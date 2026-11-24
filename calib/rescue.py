"""Budget forcing for truncated samples (as in s1, Muennighoff et al. 2025), and answer extraction for
samples that finished without \\boxed{}.

A thinking model that hits max_tokens never writes its final answer. For every
sample with finish_reason == "length", we feed the model its own (truncated)
reasoning as a partial assistant turn, append a short "commit now" suffix that ends
in "\\boxed{", and let it write only the answer (greedy, <= 64 tokens).

  python rescue.py --samples samples.jsonl --out rescue.jsonl --ports 8000,8001
"""
import argparse, asyncio, json
from pathlib import Path
from openai import AsyncOpenAI

from run_baseline import PROMPT

import sys
from pathlib import Path as _P
sys.path.insert(0, str(_P(__file__).resolve().parents[1]))
from coco.grading import last_boxed  # noqa: E402

SUFFIX = ("\n\nI have run out of time, so I must stop here and commit to the most likely final "
          "answer based on the work above.\n\nFinal answer: $\\boxed{")


async def main(a):
    pool = {p["id"]: p for p in map(json.loads, open(a.pool))}
    recs = {}
    for line in open(a.samples):
        r = json.loads(line)
        if r.get("error") is None:
            recs[(r["id"], r["sample"])] = r
    out = Path(a.out)
    done = set()
    if out.exists():
        for line in open(out):
            r = json.loads(line)
            if r.get("error") is None:
                done.add((r["id"], r["sample"]))
    # truncated samples, and finished samples that state an answer without \boxed{} (E4B does this ~17% of the time)
    todo = [r for k, r in recs.items() if k not in done and
            (r.get("finish_reason") == "length" or last_boxed(r.get("content")) is None)]
    print(f"{len(todo)} samples to rescue (truncated or no box; {len(done)} already done)", flush=True)

    clients = [AsyncOpenAI(base_url=f"http://localhost:{p}/v1", api_key="x", timeout=3 * 3600, max_retries=1)
               for p in a.ports.split(",")]
    sem = [asyncio.Semaphore(a.concurrency) for _ in clients]
    fout = out.open("a")
    lock = asyncio.Lock()

    async def one(i, r):
        ci = i % len(clients)
        partial = (r.get("reasoning") or "") + ("\n\n" + r["content"] if r.get("content") else "")
        partial = partial[-a.max_chars:]          # keep the end if it is extremely long
        msgs = [{"role": "user", "content": PROMPT.format(problem=pool[r["id"]]["problem"])},
                {"role": "assistant", "content": partial + SUFFIX}]
        rec = dict(id=r["id"], sample=r["sample"])
        async with sem[ci]:
            try:
                resp = await clients[ci].chat.completions.create(
                    model="m", messages=msgs, temperature=0.0, max_tokens=64,
                    extra_body={"continue_final_message": True, "add_generation_prompt": False,
                                "chat_template_kwargs": {"enable_thinking": False}})
                m = resp.choices[0].message
                cont = (m.content or "") or (getattr(m, "reasoning", None) or getattr(m, "reasoning_content", None) or "")
                rec.update(continuation=cont, forced="\\boxed{" + cont, error=None)
            except Exception as e:
                rec.update(error=repr(e)[:500])
        async with lock:
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()

    await asyncio.gather(*(one(i, r) for i, r in enumerate(todo)))
    fout.close()
    print("rescue finished", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", required=True)
    ap.add_argument("--samples", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ports", default="8000")
    ap.add_argument("--concurrency", type=int, default=32)
    ap.add_argument("--max-chars", type=int, default=60000)
    asyncio.run(main(ap.parse_args()))
