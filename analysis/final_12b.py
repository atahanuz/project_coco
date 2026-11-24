"""12B swarm vs single 12B (pass@1, maj@k, pass@k) on all 207 problems, paired bootstrap CIs. python analysis/final_12b.py"""
import json, sys
from pathlib import Path
import numpy as np
ROOT=Path("/Users/atahanuz/Desktop/Claude/project_coco")
sys.path[:0]=[str(ROOT),str(ROOT/"analysis"),str(ROOT/"calib")]
from analyze import per_sample
from scaling import maj_at_k
from compare import interrupted, TAGS
IDS=open(ROOT/"data/nongeo207.txt").read().split()
by=per_sample(ROOT/"runs/calib/gemma-4-12B-it_think")
d=ROOT/"runs/swarm/ng207_12b_swarm"
rs=[json.loads(l) for l in open(d/"results.jsonl")]
rs={r["id"]:r for r in rs if not r.get("error") and not interrupted(d,r)}
e4=per_sample(ROOT/"runs/calib/gemma-4-E4B-it_think")
de=ROOT/"runs/swarm/ng207_e4b_swarm"
re4={}
for l in open(de/"results.jsonl"):
    r=json.loads(l)
    if not r.get("error") and not interrupted(de,r): re4.setdefault(r["id"],[]).append(bool(r["correct"]))
rows=[]
for pid in IDS:
    ss=by.get(pid,[])
    if not ss or pid not in rs: continue
    r=rs[pid]
    rows.append(dict(id=pid,k=len(ss),p1=np.mean([bool(x["ok"]) for x in ss]),maj=maj_at_k(ss,len(ss)),
        any=float(any(x["ok"] for x in ss)),sw=float(bool(r["correct"])),toks=r["completion_tokens"],
        stoks=np.mean([x["toks"] for x in ss])*len(ss), res=r.get("resumed",0) or 0, fin=r.get("final"),
        sec=r.get("seconds_total") or r.get("seconds"), cat=pid.split("-")[2], e4p=np.mean([bool(x["ok"]) for x in e4.get(pid,[])]) if e4.get(pid) else np.nan,
        e4sw=np.mean(re4[pid]) if pid in re4 else np.nan))
n=len(rows); A=lambda k: np.array([r[k] for r in rows])
p1,maj,sw,anyk=A("p1"),A("maj"),A("sw"),A("any")
rng=np.random.default_rng(0)
def ci(x):
    b=[x[rng.integers(0,len(x),len(x))].mean() for _ in range(10000)]
    return np.percentile(b,[2.5,97.5])
print("n",n,"mean k",A("k").mean(), "k==8:", (A("k")==8).sum())
print(f"single pass@1 {p1.mean():.3f}  maj@k {maj.mean():.3f}  pass@k {anyk.mean():.3f}  swarm {sw.mean():.3f}")
print("swarm-single", (sw-p1).mean(), ci(sw-p1)); print("swarm-maj",(sw-maj).mean(),ci(sw-maj))
print("tokens: swarm mean %.0f median %.0f ; single per sample %.0f ; maj@k total %.0f"%(A("toks").mean(),np.median(A("toks")),(A("stoks")/A("k")).mean(),A("stoks").mean()))
print("no answer:", sum(1 for r in rows if not r["fin"]))
print("resumed>0:", (A("res")>0).sum(), "acc", sw[A("res")>0].mean(), "| not resumed acc", sw[A("res")==0].mean())
for c in ["algebra","combinatorics","number_theory"]:
    m=np.array([r["cat"]==c for r in rows]); print(c,m.sum(),f"single {p1[m].mean():.3f} maj {maj[m].mean():.3f} swarm {sw[m].mean():.3f}")
for lo,hi,lab in [(0,0,"0/k"),(1e-9,0.375,"<=3/8"),(0.375+1e-9,0.75,"(3/8,6/8]"),(0.75+1e-9,1,">6/8")]:
    m=(p1>=lo)&(p1<=hi); print(lab,m.sum(),f"single {p1[m].mean():.3f} maj {maj[m].mean():.3f} swarm {sw[m].mean():.3f}")
# 12B swarm vs E4B swarm, E4B single
e4p,e4sw=A("e4p"),A("e4sw"); m=~np.isnan(e4sw)
print("on",m.sum(),"E4B single",np.nanmean(e4p[m]),"E4B swarm",e4sw[m].mean(),"12B single",p1[m].mean(),"12B swarm",sw[m].mean())
print("12B swarm solves, 12B single 0/k:", sum(1 for r in rows if r["sw"] and r["p1"]==0), "of", sum(1 for r in rows if r["p1"]==0))
print("12B swarm fails, 12B single >=6/8:", [ (r["id"],round(r["p1"],2)) for r in rows if not r["sw"] and r["p1"]>=0.75])
secs=A("sec"); print("wall min: median %.0f, max %.0f"%(np.nanmedian(secs)/60,np.nanmax(secs)/60))
