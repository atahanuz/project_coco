"""Answer extraction + automatic grading for short-answer olympiad problems.

Only answers we can grade *exactly* are auto-graded: a single integer, a set of
integers, or a rational number. Everything else (functions, conditions, intervals)
is marked `autograde=False` and needs an LLM judge.
"""
from __future__ import annotations
import re
from fractions import Fraction

# ---------------------------------------------------------------- extraction
def last_boxed(text: str | None) -> str | None:
    """Content of the last \\boxed{...} (or \\fbox{...}) in text, braces balanced."""
    if not text:
        return None
    idx = max(text.rfind("\\boxed"), text.rfind("\\fbox"))
    if idx < 0:
        return None
    i = text.find("{", idx)
    if i < 0:
        return None
    depth, j = 0, i
    while j < len(text):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1 : j]
        j += 1
    return None

# ---------------------------------------------------------------- normalisation
_STRIP = [r"\left", r"\right", r"\displaystyle", r"\,", r"\;", r"\!", r"\ ", "$", r"\quad", r"\qquad"]

def _clean(s: str) -> str:
    s = s.strip()
    for t in _STRIP:
        s = s.replace(t, "")
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\(?:mathrm|textbf|mathbf)\{([^}]*)\}", r"\1", s)
    s = s.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    s = s.replace("{,}", "")              # 1{,}000
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+", s.strip()):   # 1,000,000
        s = s.replace(",", "")
    s = s.strip().rstrip(".").strip()
    # drop a leading "x =", "n=", "N =", "answer:" etc.
    s = re.sub(r"^(?:[A-Za-z]\w*(?:_\{?\w+\}?)?\s*(?:=|\\in)\s*)", "", s)
    s = s.strip("{}[]() ") if re.fullmatch(r"[\{\[\(]?[-\d,\s]+[\}\]\)]?", s) else s
    s = s.replace(r"\{", "").replace(r"\}", "")
    return s.strip()

def _to_number(s: str) -> Fraction | None:
    s = s.replace(" ", "")
    m = re.fullmatch(r"(-?)\\frac\{(-?\d+)\}\{(-?\d+)\}", s)
    if m:
        v = Fraction(int(m.group(2)), int(m.group(3)))
        return -v if m.group(1) else v
    m = re.fullmatch(r"(-?\d+)/(\d+)", s)
    if m:
        return Fraction(int(m.group(1)), int(m.group(2)))
    if re.fullmatch(r"-?\d+", s):
        return Fraction(int(s))
    if re.fullmatch(r"-?\d+\.\d+", s):
        return Fraction(s)
    return None

def parse_answer(s: str | None):
    """-> ('num', Fraction) | ('set', frozenset) | ('tuple', tuple) | ('raw', str) | None"""
    if s is None:
        return None
    raw = s.strip().strip("$").strip().rstrip(".")
    raw = raw.replace(r"\left", "").replace(r"\right", "").strip()
    if re.fullmatch(r"\[\s*-?[\d.]+\s*,\s*-?[\d.]+\s*\]", raw):     # closed interval [a,b]
        return ("raw", re.sub(r"\s+", "", raw))
    m = re.fullmatch(r"\(\s*(-?\d+(?:\s*,\s*-?\d+)+)\s*\)", raw)    # ordered tuple (a,b,c)
    if m:
        return ("tuple", tuple(int(x) for x in m.group(1).split(",")))
    c = _clean(s)
    v = _to_number(c)
    if v is not None:
        return ("num", v)
    parts = [p for p in re.split(r",|\\text\{and\}|\band\b|;|\\cup", c) if p.strip()]
    if len(parts) > 1:
        vals = [_to_number(_clean(p)) for p in parts]
        if all(x is not None for x in vals):
            return ("set", frozenset(vals), tuple(vals))
    return ("raw", re.sub(r"\s+", "", c))

def answer_type(gold: str) -> str:
    p = parse_answer(gold)
    if p is None or p[0] == "raw":
        return "other"
    if p[0] == "num":
        return "int" if p[1].denominator == 1 else "rational"
    if p[0] == "tuple":
        return "int_tuple"
    return "int_set" if all(x.denominator == 1 for x in p[1]) else "num_set"

def is_correct(pred: str | None, gold: str) -> bool | None:
    """True/False for auto-gradable gold answers, None if gold needs a judge."""
    if answer_type(gold) == "other":
        return None
    g, p = parse_answer(gold), parse_answer(pred)
    if p is None or p[0] == "raw":
        return False
    if g[0] == "tuple":                       # order matters: (x, n, k)
        seq = p[1] if p[0] == "tuple" else (p[2] if p[0] == "set" else None)
        return seq is not None and tuple(Fraction(x) for x in seq) == tuple(Fraction(x) for x in g[1])
    if g[0] == "num":
        if p[0] == "set" and len(p[1]) == 1:
            p = ("num", next(iter(p[1])))
        return p[0] == "num" and p[1] == g[1]
    # gold is a set: order-free comparison
    pset = p[1] if p[0] == "set" else frozenset([p[1]]) if p[0] == "num" else frozenset(Fraction(x) for x in p[1])
    return pset == g[1]
