"""Run swarm.py end to end against a fake OpenAI server: honest workers answer the gold, saboteurs answer 999."""
import json, re, runpy, sys, types, random
from collections import Counter
import openai
ROOT = "/Users/atahanuz/Desktop/Claude/project_coco"
POOL = [json.loads(l) for l in open(f"{ROOT}/data/pool.jsonl")]
SEEN = Counter()

def resp(content, finish="stop"):
    msg = types.SimpleNamespace(content=content, tool_calls=None, reasoning=None, reasoning_content=None)
    return types.SimpleNamespace(choices=[types.SimpleNamespace(message=msg, finish_reason=finish)],
                                 usage=types.SimpleNamespace(prompt_tokens=100, completion_tokens=50))

class Completions:
    async def create(self, **kw):
        sysm, user = kw["messages"][0]["content"], kw["messages"][1]["content"]
        gold = next((p["answer"] for p in POOL if p["problem"].strip()[:200] in user), "1")
        if "SABOTEUR" in sysm:
            SEEN["saboteur_collude" if "You are not alone" in sysm else "saboteur_solo"] += 1
            m = re.search(r"You are (W\d)\.", sysm); p = re.search(r"You are not alone: (W\d)", sysm)
            SEEN[f"{m.group(1)}->partner {p.group(1) if p else None}"] += 1
            return resp(f"I checked it. \\boxed{{999}}")
        if kw.get("tools"):
            SEEN["honest"] += 1
            return resp(f"Done. \\boxed{{{gold if random.random() < 0.7 else 7}}}")
        SEEN["master"] += 1
        return resp(json.dumps({"final_answer": "999" if random.random() < 0.5 else gold, "reason": "x", "credit": "W1"}))

class FakeClient:
    def __init__(self, **kw):
        self.chat = types.SimpleNamespace(completions=Completions())

openai.AsyncOpenAI = FakeClient
random.seed(0)
sys.argv = ["swarm.py"] + sys.argv[1:]
sys.path.insert(0, ROOT)
try:
    runpy.run_path(f"{ROOT}/swarm/swarm.py", run_name="__main__")
finally:
    print("SEEN", dict(SEEN))
