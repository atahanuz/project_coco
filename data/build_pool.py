"""Build the candidate pool from IMO-AnswerBench (v2) -> data/pool.jsonl."""
import json, sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from coco.grading import answer_type

ROOT = Path(__file__).resolve().parent
a = pd.read_csv(ROOT / "raw/imobench/answerbench_v2.csv")
rows = []
for _, r in a.iterrows():
    cat = {"Functional Equation": "Algebra"}.get(r["Category"], r["Category"])
    gold = str(r["Short Answer"]).strip()
    at = answer_type(gold)
    rows.append(dict(id=r["Problem ID"], problem=str(r["Problem"]).strip(), answer=gold,
                     category=cat, subcategory=r["Subcategory"], source=str(r["Source"]).strip(),
                     answer_type=at, autograde=at != "other"))
with open(ROOT / "pool.jsonl", "w") as f:
    for x in rows:
        f.write(json.dumps(x, ensure_ascii=False) + "\n")
d = pd.DataFrame(rows)
print(len(d), "problems"); print(pd.crosstab(d.category, d.answer_type, margins=True))
