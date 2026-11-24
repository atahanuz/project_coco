r"""Robustness check for answer-only grading: evaluate closed-form LaTeX answers (3^{25}+1, \binom{10}{3}, 5!) exactly."""
import re, sys
from fractions import Fraction
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
sys.path.insert(0, "/Users/atahanuz/Desktop/Claude/project_coco")
from coco.grading import _clean, parse_answer, is_correct
TR = standard_transformations + (implicit_multiplication_application, convert_xor)

def _brace(s, i):
    """s[i]=='{' -> index of matching '}'"""
    d = 0
    for j in range(i, len(s)):
        d += s[j] == "{"; d -= s[j] == "}"
        if d == 0: return j
    return -1

def _cmd2(s, cmd, fmt):
    while True:
        k = s.find(cmd + "{")
        if k < 0: return s
        a0 = k + len(cmd); a1 = _brace(s, a0)
        if a1 < 0 or a1 + 1 >= len(s) or s[a1 + 1] != "{": return None
        b1 = _brace(s, a1 + 1)
        if b1 < 0: return None
        s = s[:k] + fmt.format(s[a0 + 1:a1], s[a1 + 2:b1]) + s[b1 + 1:]

def to_py(s):
    s = _clean(s)
    s = s.replace("\\cdot", "*").replace("\\times", "*").replace("\\,", "").replace(" ", "")
    s = re.sub(r"\\(?:binom|dbinom|tbinom)", r"\\binom", s)
    s = _cmd2(s, "\\frac", "(({})/({}))")
    if s is None: return None
    s = _cmd2(s, "\\binom", "binomial({},{})")
    if s is None: return None
    s = re.sub(r"\\sqrt\{", "sqrt{", s)
    s = re.sub(r"(\d+|\))!", r"factorial(\1)", s)
    s = s.replace("{", "(").replace("}", ")")
    if "\\" in s or re.search(r"[A-Za-z]", re.sub(r"binomial|factorial|sqrt", "", s)): return None
    return s

def _safe(e):
    for p in sp.preorder_traversal(e):
        if isinstance(p, sp.Pow) and p.exp.is_number and p.base.is_number:
            try:
                b, x = abs(float(p.base)), float(p.exp)
                if b > 1 and x * sp.log(b, 2) > 2e5: return False
            except Exception: return False
        if isinstance(p, sp.factorial) and p.args[0].is_number and float(p.args[0]) > 5000: return False
    return True

def evaluate(s):
    py = to_py(s)
    if not py: return None
    try:
        e = parse_expr(py, transformations=TR, evaluate=False)
        if e.free_symbols or not _safe(e): return None
        v = sp.nsimplify(sp.simplify(e)) if not e.is_Rational else e
        v = sp.Rational(v)
        return Fraction(int(v.p), int(v.q))
    except Exception:
        return None

def evaluate_any(s):
    """number or frozenset of numbers (top-level commas)"""
    v = evaluate(s)
    if v is not None: return ("num", v)
    c = _clean(s); parts, d, cur = [], 0, ""
    for ch in c:
        d += ch in "({["; d -= ch in ")}]"
        if ch == "," and d == 0: parts.append(cur); cur = ""
        else: cur += ch
    parts.append(cur)
    if len(parts) > 1:
        vs = [evaluate(p) for p in parts]
        if all(x is not None for x in vs): return ("set", frozenset(vs))
    return None

def is_correct2(pred, gold):
    r = is_correct(pred, gold)
    if r is not False or pred is None: return r
    p = parse_answer(pred)
    if p is None or p[0] != "raw": return r
    g = parse_answer(gold); v = evaluate_any(pred)
    if v is None: return False
    if g[0] == "num":
        return v[0] == "num" and v[1] == g[1] or (v[0] == "set" and v[1] == frozenset([g[1]]))
    if g[0] == "set":
        return (v[1] if v[0] == "set" else frozenset([v[1]])) == g[1]
    return False

if __name__ == "__main__":
    for a, g in [("3^{25}+1", "847288609444"), ("2^{10}-1", "1023"), ("\\binom{10}{3}", "120"), ("\\frac{2^{5}}{4}", "8"),
                 ("5!", "120"), ("2\\cdot 3^2", "18"), ("2^{2^{40}}", "1"), ("n+1", "5"), ("\\frac{1}{2}, 2^{2}", "1/2, 4"),
                 ("\\sqrt{2}", "1"), ("16!/4", "5230697472000")]:
        print(a, g, is_correct2(a, g))
