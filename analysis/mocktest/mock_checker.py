"""Run swarm.py --checker 1 end to end against a fake OpenAI client.

Honest workers answer the gold 70% of the time (else 7); saboteurs answer 999. The fake checker calls the verdict tool:
CONFIRMED if the candidate equals the gold, else REFUTED (every 5th checker call answers in plain text instead, to test
the text fallback). The fake master answers with a candidate the checker confirmed, if the notes show one.
SEEN counts calls per port (checker@<port>, team@<port>), to test --checker-ports routing.
MOCK_STUBBORN=1: the checker calls run_python whenever it may (never a verdict until only the verdict tool is offered),
  and with thinking on it is cut at the length limit; MOCK_PARTIAL=1 in addition: one verdict per step;
  MOCK_MANY=1: the master/workers give 4 distinct candidates (so the checker judges 4 labels).
MOCK_SCRIPT=verify: run swarm/verify.py (pooled verification) against the same fake client.
MOCK_CRASH=1: the first checker call raises (a job killed mid-check), to test checkpoint resume.
"""
import json, os, re, runpy, sys, types, random
from collections import Counter
import openai
ROOT = "/Users/atahanuz/Desktop/Claude/project_coco"
POOL = [json.loads(l) for l in open(f"{ROOT}/data/pool.jsonl")]
SEEN = Counter()


def msg(content, tool_calls=None, finish="stop"):
    m = types.SimpleNamespace(content=content, tool_calls=tool_calls, reasoning=None, reasoning_content=None)
    return types.SimpleNamespace(choices=[types.SimpleNamespace(message=m, finish_reason=finish)],
                                 usage=types.SimpleNamespace(prompt_tokens=100, completion_tokens=50))


def tool_call(i, name, args):
    d = {"id": f"c{i}", "type": "function", "function": {"name": name, "arguments": json.dumps(args)}}
    return types.SimpleNamespace(id=d["id"], type="function", function=types.SimpleNamespace(**d["function"]),
                                 model_dump=lambda d=d: d)


class Completions:
    def __init__(self, base_url=""):
        self.base_url = str(base_url)

    async def create(self, **kw):
        sysm, user = kw["messages"][0]["content"], kw["messages"][1]["content"]
        prob = next((p for p in POOL if p["problem"].strip()[:200] in user), None)
        gold = prob["answer"] if prob else "1"
        if sysm.startswith("You are an independent CHECKER"):
            SEEN["checker"] += 1
            SEEN["checker@" + self.base_url.split(":")[-1].split("/")[0]] += 1
            SEEN["checker_max_tokens"] = max(SEEN["checker_max_tokens"], kw["max_tokens"])
            if os.environ.get("MOCK_CRASH") == "1" and SEEN["checker"] == 1:
                raise RuntimeError("fake connection drop during the check")
            assert "notes" not in user.lower().split("candidate answers")[0][-200:], "checker must not see notes"
            assert not re.search(r"\bW\d\b", user), "checker must not see worker names"
            items = re.findall(r"^([A-H]): (.*)$", user, re.M)
            names = [t["function"]["name"] for t in kw.get("tools") or []]
            if os.environ.get("MOCK_STUBBORN") == "1" and "run_python" in names:   # a checker that never stops computing
                SEEN["checker_python"] += 1
                return msg("", [tool_call(0, "run_python", {"code": "print(1)"})], "tool_calls")
            if os.environ.get("MOCK_STUBBORN") == "1":
                SEEN["checker_verdict_only_step"] += 1
                SEEN["reminder_seen"] += any("3 steps left" in str(m.get("content")) for m in kw["messages"])
                if kw["extra_body"]["chat_template_kwargs"]["enable_thinking"]:   # thinks until the length limit
                    SEEN["checker_cut_while_thinking"] += 1
                    return msg("", None, "length")
                todo = re.findall(r"yet \(([A-H, ]+)\)", str(kw["messages"][-1].get("content")))
                todo = [x.strip() for x in todo[0].split(",")] if todo else [l for l, _ in items]
                if os.environ.get("MOCK_PARTIAL") == "1":   # judges only one candidate per step
                    todo = todo[:1]
                items = [(l, a) for l, a in items if l in todo]
                calls = [tool_call(i, "verdict", {"candidate": l, "result": "CONFIRMED" if a.strip() == str(gold).strip()
                                                  else "REFUTED", "evidence": "final step"}) for i, (l, a) in enumerate(items)]
                return msg("", calls, "tool_calls")
            ok = lambda a: a.strip() == str(gold).strip()
            if SEEN["checker"] % 5 == 0:
                SEEN["checker_text"] += 1
                return msg("\n".join(f"{l}: {'CONFIRMED' if ok(a) else 'REFUTED'} by brute force" for l, a in items))
            calls = [tool_call(i, "verdict", {"candidate": l, "result": "CONFIRMED" if ok(a) else "REFUTED",
                                              "evidence": f"brute force says {'yes' if ok(a) else 'no'}, n<=50"})
                     for i, (l, a) in enumerate(items)]
            return msg("", calls, "tool_calls")
        SEEN["team@" + self.base_url.split(":")[-1].split("/")[0]] += 1
        if kw.get("tools"):
            SEEN["worker_max_tokens"] = max(SEEN["worker_max_tokens"], kw["max_tokens"])
        if "SABOTEUR" in sysm:
            SEEN["saboteur"] += 1
            return msg("I checked it. \\boxed{999}")
        if kw.get("tools"):
            SEEN["honest"] += 1
            if os.environ.get("MOCK_MANY") == "1":
                return msg(f"Done. \\boxed{{{random.choice([gold, 7, 8, 9])}}}")
            return msg(f"Done. \\boxed{{{gold if random.random() < 0.7 else 7}}}")
        SEEN["master"] += 1
        if "An independent CHECKER" in sysm:
            SEEN["master_told_checker"] += 1
        conf = re.findall(r"- `([^`]*)`: CONFIRMED", user)
        if "round 1 of" in user:
            return msg(json.dumps({"assignments": {"W1": "brute force", "W2": "algebra", "W3": "check", "W4": "bounds"}}))
        if conf:
            SEEN["master_used_confirmed"] += 1
            return msg(json.dumps({"final_answer": conf[0], "reason": "checker confirmed"}))
        if "round 2 of" in user:
            return msg(json.dumps({"assignments": {"W1": "try again", "W2": "try again"}}))
        return msg(json.dumps({"final_answer": "999" if random.random() < 0.5 else gold, "reason": "x"}))


class FakeClient:
    def __init__(self, **kw):
        self.chat = types.SimpleNamespace(completions=Completions(kw.get("base_url", "")))


openai.AsyncOpenAI = FakeClient
random.seed(0)
SCRIPT = os.environ.get("MOCK_SCRIPT", "swarm")   # MOCK_SCRIPT=verify: run swarm/verify.py instead
sys.argv = [f"{SCRIPT}.py"] + sys.argv[1:]
sys.path.insert(0, ROOT)
try:
    runpy.run_path(f"{ROOT}/swarm/{SCRIPT}.py", run_name="__main__")
finally:
    print("SEEN", dict(SEEN))
