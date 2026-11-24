# Showcase: a problem the swarm solved and the single model never did

**Problem** (IMO-AnswerBench `number_theory-019`): Find all positive integer triples $(a,b,c)$ with $a \le b \le c$ and
$a^3(b^3+c^3) = 2012(abc+2)$. **Answer:** $(2, 251, 252)$.

**Single model** (gemma-4-E4B, 8 independent attempts, thinking, 64k-token budget): 0 of 8 correct. Seven attempts answered
"no solutions"; the eighth gave no answer.

**Swarm** (the same E4B model as 1 master + 4 workers, shared `notes.md`): correct, in 3 rounds and 48k tokens.
Run: `runs/swarm/ng207_e4b_swarm/imo-bench-number_theory-019__t0/`.

| round | what the master assigned | what came back (in notes.md) |
|---|---|---|
| 1 | **W1:** Python search for a = 1–4.<br>**W2:** derive an upper bound on a.<br>**W3:** case a = 1.<br>**W4:** case a = 2. | W1 finds **(2, 251, 252)**.<br>W2 proves **a ≤ 10**: since b, c ≥ a, the left side is at least 2a⁶ and grows faster than the right.<br>W4 reduces the a = 2 case to b³ + c³ = 503(bc + 1). |
| 2 | **W1:** independently **verify** (2, 251, 252).<br>**W2:** search a = 3, 4.<br>**W3:** continue a = 2 for b ≥ 5.<br>**W4:** look for a structural property. | Verified. No solutions for a = 3, 4. |
| 3 | Cover the rest of the range that W2's bound allows: a = 5, 6 (W2), a = 7–9 (W3), a = 10 (W1), and a growth argument for a ≥ 3 (W4). | No other solutions. |
| final | **Master:** "(2, 251, 252): found for a = 2, verified, and the remaining a ≤ 10 were searched." | ✔ correct |

**Why it worked.** This is the proposal's *sequential collaboration* pattern (Example 1). One agent's bound (a ≤ 10)
turned the problem into finitely many cases. The master spread those cases over the team and had the candidate checked
independently. A single E4B, thinking alone, guessed that no solution exists.

**Honest caveats** (both are fine for a demo, and both motivate the trust and verification part of the project):
- The searches use b, c ≤ 2000, so the "no other solutions" part is checked numerically rather than proved.
- The master's round-2 task states 2012 = 4·7·71. That is wrong: 2012 = 4·503. W3 had already written the correct
  factorisation in the notes, and nobody flagged the error.
