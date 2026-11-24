### [W1, round 1]
Total possible distinct pairs (games) among 40 teams: 780.
The maximum number of rounds possible ($R_{max}$) is 39, since 20 games are played per round (780 / 20 = 39).

### [W2, round 1]
### Analysis for finding smallest 'a'

1.  **Graph Theory Formulation:** Let $V$ be the set of 40 teams. The complete graph $K_{40}$ represents all possible games, with $|E(K_{40})| = 780$ edges. Each round corresponds to a 1-factor (a perfect matching) $F_i$ of $K_{40}$. A schedule of $a$ rounds $E'$ is a union of $a$ distinct 1-factors.
2.  **Condition for 'a':** The condition that round $a+1$ *must* necessarily involve a repeated game means that the set of unused edges $G' = K_{40} \setminus E'$ contains *no* perfect matching. If $G'$ had a perfect matching $F_{a+1}$, that matching would consist of games not played before, violating the condition.
3.  **Finding the Minimum Edge Removal:** We seek the minimum size $|E'| = 20a$ such that $K_{40} \setminus E'$ is matching-deficient. We use Tutte's Theorem. $K_{40} \setminus E'$ lacks a perfect matching if there exists a set $S \subset V$ such that the number of odd components $o(G' \setminus S)$ satisfies $o(G' \setminus S) > |S|$.
4.  **Minimizing $|E'|$:** To minimize $|E'|$, we construct $S$ and $V' = V \setminus S$ such that the required edge removal is minimized. Let $s=|S|$ and $|V'| = 40-s$. If we choose $s=19$, then $|V'|=21$. We require $o(G' \setminus S) > 19$. We achieve this by making all 21 vertices in $V'$ isolated (single-vertex odd components). This requires removing all edges within $V'$ (a $K_{21}$) and all edges connecting $V'$ to $S$.
    *   Edges within $V'$: $\binom{21}{2} = 210$.
    *   Edges between $S$ and $V'$: $19 \times 21 = 399$.
    *   Minimum required edges $|E'_{min}| = 210 + 399 = 609$.
5.  **Determining 'a':** Since $E'$ must be a union of 1-factors, $|E'|$ must be a multiple of 20. We require $20a \ge 609$.
    *   $a \ge 609 / 20 = 30.45$.
    *   The smallest positive integer $a$ is 31.

**Conclusion:** The smallest positive integer $a$ is 31. This is because $31 \times 20 = 620$ edges are sufficient to form a set $E'$ whose removal guarantees that the remaining graph lacks a perfect matching, thereby forcing the $(a+1)$-th round to reuse a game.

### [W1, round 2]
### [W1, review of W2's derivation]
I have critically reviewed W2's derivation regarding the minimum number of games required, $|E'_{min}|$.
The application of Tutte's Theorem with $s=19$ and $|V'|=21$ is correct, as this setup guarantees $o(G'\setminus S) = 21 > 19 = |S|$.
The calculation for the minimum edge removal $|E'_{min}|$ required to isolate all 21 vertices in $V'$ (by removing all internal edges $K_{21}$ and all edges between $S$ and $V'$) is verified:
$|E'_{min}| = \binom{21}{2} + (19 \times 21) = 210 + 399 = 609$.
Since $|E'| = 20a$, we require $20a \ge 609$, leading to $a \ge 30.45$. The smallest positive integer $a$ is correctly determined as 31. The derivation is sound.
