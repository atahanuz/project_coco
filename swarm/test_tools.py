"""Smoke test: does native tool calling work for Gemma-4 via vLLM (gemma4 tool parser)?"""
import json, sys, subprocess
from openai import OpenAI

port = sys.argv[1]
c = OpenAI(base_url=f"http://localhost:{port}/v1", api_key="x", timeout=1800)
tools = [{"type": "function", "function": {
    "name": "run_python", "description": "Run a Python 3 script and return its stdout. Use print() to see results.",
    "parameters": {"type": "object", "properties": {"code": {"type": "string", "description": "Python source code"}},
                   "required": ["code"]}}},
    {"type": "function", "function": {
    "name": "write_note", "description": "Append a note to the shared notes.md file that all team members can read.",
    "parameters": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}}}]
for think in (True, False):
    msgs = [{"role": "system", "content": "You are a careful math assistant with a Python tool."},
            {"role": "user", "content": "Find all positive integers k <= 200 such that the number of divisors of 2k^3 equals 2k. "
                                        "Use the run_python tool to search, then write your finding with write_note, then answer."}]
    print(f"\n######## think={think}", flush=True)
    for turn in range(6):
        r = c.chat.completions.create(model="m", messages=msgs, tools=tools, temperature=1.0, top_p=0.95, max_tokens=8000,
                                      extra_body={"top_k": 64, "chat_template_kwargs": {"enable_thinking": think}})
        m = r.choices[0].message
        reasoning = getattr(m, "reasoning", None) or getattr(m, "reasoning_content", None)
        print(f"--- turn {turn}: finish={r.choices[0].finish_reason} toks={r.usage.completion_tokens} "
              f"reasoning={len(reasoning or '')}ch content={(m.content or '')[:300]!r}", flush=True)
        if not m.tool_calls:
            break
        am = {"role": "assistant", "content": m.content or "", "tool_calls": [tc.model_dump() for tc in m.tool_calls]}
        if reasoning:
            am["reasoning"] = reasoning
        msgs.append(am)
        for tc in m.tool_calls:
            args = json.loads(tc.function.arguments)
            print(f"    TOOL {tc.function.name}: {json.dumps(args)[:400]}", flush=True)
            if tc.function.name == "run_python":
                p = subprocess.run([sys.executable, "-c", args["code"]], capture_output=True, text=True, timeout=60)
                out = (p.stdout + p.stderr)[-2000:]
            else:
                out = "note saved"
            print(f"    -> {out[:300]!r}", flush=True)
            msgs.append({"role": "tool", "tool_call_id": tc.id, "content": out})
