### [W2, round 1]
Analysis of Removed Set R:
1. Additive Closure (Rule ii): If $R$ is non-empty, let $g = \text{gcd}(R)$. Every element $r \in R$ must be a multiple of $g$. Thus, $R \subseteq \{g, 2g, 3g, \ldots, kg\}$ where $kg \le 191$.
2. Interaction with Additive Closure: Sets closed under addition tend to be dense within the set of multiples of their GCD.
3. Doubling Property (Rule i): If $x \in R$, then $2x \in R$. This is consistent with the structure being multiples of $g$. If $x=kg$, then $2x=2kg$.
4. Conclusion: To minimize the sum of removed numbers (and maximize the remaining sum), we should seek the smallest possible $g$ that allows $|R| \ge 95$. If $g=1$, $R$ could potentially be all 191 numbers, but since we must minimize the sum, we look for the largest possible $g$ that still allows $|R| \ge 95$. The largest possible size for $R$ occurs when $g=1$. The smallest possible size for $R$ occurs when $g$ is large. Since $|R| \ge 95$, we need $\lfloor 191/g \rfloor \ge 95$.
$\lfloor 191/g \rfloor \ge 95 \implies 191/g \ge 95 \implies g \le 191/95 \approx 2.01$.
Therefore, $g$ can only be 1 or 2.
Findings: The GCD of the removed set, $g$, must be 1 or 2. The set $R$ must consist entirely of multiples of $g$.

### [W3, round 1]
Analysis of removal rules:
1. Rule (i) states that if $x$ is removed, all its multiples of 2 up to 191 must be removed ($x, 2x, 4x, \ldots$).
2. Combining Rule (i) and Rule (ii) (closure under addition), if any number $x$ is removed, all its integer multiples $kx$ (up to 191) must also be removed.
3. This implies that the set of removed numbers $R$ must be the set of all positive multiples of some integer $G$, up to 191. $R = R_G = \{G, 2G, \ldots, \lfloor 191/G \rfloor G\}$.

Constraint check: $|R| = \lfloor 191/G \rfloor \ge 95$. This limits possible values for $G$ to $G=1$ or $G=2$.

Optimization: To maximize the sum of remaining numbers ($\sum S \setminus R$), we must minimize the sum of removed numbers ($\sum R$).
- For $G=1$, $R=\{1, \ldots, 191\}$. $\sum R = 18336$. $\sum S' = 0$.
- For $G=2$, $R=\{2, 4, \ldots, 190\}$. $\sum R = 9120$. $\sum S' = 9216$.

The maximum value for the sum of remaining numbers is 9216.

### [W1, round 1]
Exploration of initial seeds (k=1, 2, 3) in set S = {1, ..., 191}.
Rules: (i) x removed => 2x removed. (ii) x, y removed => x+y removed.

1. Seed R_seed = {1}:
   The generated set R is {1, 2, ..., 191}.
   |R| = 191.
   Sum(R) = 18336.

2. Seed R_seed = {2}:
   The generated set R is {2, 4, 6, ..., 190} (multiples of 2).
   |R| = 95.
   Sum(R) = 9120.

3. Seed R_seed = {3}:
   The generated set R is {3, 6, 9, ..., 189} (multiples of 3).
   |R| = 63.
   Sum(R) = 6048.

Note: The condition that at least 95 numbers are removed is satisfied by k=1 and k=2, but not by k=3.

### [W4, round 1]
## Strategy Development: Minimizing Sum of Removed Numbers (A)

Based on W2's findings, the set of removed numbers $A$ must consist entirely of multiples of $g = \text{gcd}(A)$, and $g$ must be 1 or 2 to satisfy $|A| \ge 95$.

We aim to maximize the remaining sum, which means minimizing the sum of $A$ ($\sum A$). The structure of $A$ must be $A = \{g, 2g, 3g, \ldots, m_g g\}$, where $m_g = \lfloor 191/g \rfloor$, because closure under addition forces $A$ to contain all multiples of $g$ up to 191 if the smallest element $g$ is present.

We examine the two possibilities for $g$:

1.  **Case $g=1$:** $A = \{1, 2, \ldots, 191\}$. $|A|=191$. $\sum A = 191 \times 192 / 2 = 18336$. (This minimizes the remaining sum to 0).
2.  **Case $g=2$:** $A = \{2, 4, \ldots, 190\}$. $|A|=95$. $\sum A = 2 \times (1 + 2 + \ldots + 95) = 2 \times \frac{95 \times 96}{2} = 9120$. (This satisfies the minimum size constraint $|A|=95$).

Comparing the sums, the minimum sum of removed numbers is 9120, achieved by choosing $g=2$.

The maximum value of the remaining sum is Total Sum - Minimum Removed Sum.
Total Sum of $\{1, \ldots, 191\}$ is 18336.
Maximum Remaining Sum = $18336 - 9120 = 9216$.
