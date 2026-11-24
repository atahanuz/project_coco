"""How many answers the closed-form evaluator (grade_check.py) would regrade as correct, per approach. python analysis/grade_check_flips.py"""
import warnings; warnings.filterwarnings("ignore")
import json, sys
from pathlib import Path
import numpy as np
sys.path[:0]=["/Users/atahanuz/Desktop/Claude/project_coco/analysis","/Users/atahanuz/Desktop/Claude/project_coco/calib","/Users/atahanuz/Desktop/Claude/project_coco"]
from grade_check import is_correct2
from analyze import per_sample
from compare import interrupted
from build_explorer import APPROACHES, POOL, IDS
ROOT=Path("/Users/atahanuz/Desktop/Claude/project_coco")
for key, model, label, kind, src in APPROACHES:
    if kind=="majority": continue
    old=new=n=0; ex=[]
    if kind=="single":
        by=per_sample(ROOT/src); per_o=[]; per_n=[]
        for pid in IDS:
            ss=by.get(pid,[])
            if not ss: continue
            o=[bool(x["ok"]) for x in ss]; nn=[bool(x["ok"]) or bool(is_correct2(x["pred"],POOL[pid]["answer"])) for x in ss]
            per_o.append(np.mean(o)); per_n.append(np.mean(nn))
            for x,a,b in zip(ss,o,nn):
                if b and not a: ex.append((pid[10:],x["pred"]))
        print(f"{key:12s} pass@1 {np.mean(per_o):.3f} -> {np.mean(per_n):.3f}  flips {len(ex)}  e.g. {ex[:4]}")
    else:
        d=ROOT/src; rs=[json.loads(l) for l in open(d/"results.jsonl")]
        rs=[r for r in rs if not r.get("error") and not interrupted(d,r) and r["id"] in POOL]
        per={}
        for r in rs:
            a=bool(r.get("correct")); b=a or bool(is_correct2(r.get("final"),POOL[r["id"]]["answer"]))
            per.setdefault(r["id"],[]).append((a,b))
            if b and not a: ex.append((r["id"][10:],r.get("final")))
        po=np.mean([np.mean([a for a,b in v]) for v in per.values()]); pn=np.mean([np.mean([b for a,b in v]) for v in per.values()])
        print(f"{key:12s} pass@1 {po:.3f} -> {pn:.3f}  flips {len(ex)}  e.g. {ex[:4]}")
