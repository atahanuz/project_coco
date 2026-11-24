### [W2, round 1]
Structural Analysis: Interaction of Rules (i) and (ii) with small numbers $k \in R$.
The rules define closure properties for the removed set $D$: (i) $x \in D \implies 2x \in D$, and (ii) $x, y \in D \implies x+y \in D$.
If $k$ is small and $k \in R$, then $k \notin D$. This prevents $k$ from being a base element (a generator) of $D$.

1. Case $k=1$: If $1 \in R$, then $1 \notin D$. This means $D$ cannot be the set of all positive integers (or any set containing 1, since closure under addition would quickly generate all subsequent integers if 1 was present). Any element $d \in D$ must be greater than 1. The structure of $D$ must be based on generators $d_i > 1$.

2. Case $k=2$: If $2 \in R$, then $2 \notin D$.
    a. If $1$ were in $D$, rule (i) would immediately force $2 \in D$, leading to a contradiction. Therefore, if $2 \in R$, then $1$ must also be in $R$ (i.e., $1 \notin D$).
    b. If $D$ is based on a generator $d \in D$ such that $d$ is odd, then $2d$ is in $D$ by rule (i). If $d=3$, $6 \in D$. If $D$ is built upon $d=3$, and $2 \in R$, this is consistent.

3. Interaction Summary: The presence of small numbers in $R$ severely restricts the allowed generators for $D$. For example, $2 \in R$ implies $1 \in R$. This forces $D$ to be constructed from generators $d \ge 3$.

Next step should involve trying to find the minimal size $D$ based on the constraint $k \in R$, potentially focusing on $D$ being composed of numbers derived from $d=3, 5, 7, \ldots$ or $d=4, 8, 16, \ldots$.

### [W4, round 1]
Necessary Condition for R: Let R be a non-empty set satisfying the rules: (i) closure under doubling, (ii) closure under addition. If R is contained in {1, 2, ..., 191}, then R must be the set of all positive multiples of its greatest common divisor, g = gcd(R), up to 191. That is, R = {g, 2g, 3g, ..., floor(191/g) * g}.

Constraint check: We require |R| >= 95.
|R| = floor(191/g) >= 95.
191/g >= 95
g <= 191/95 approx 2.01.
Since g must be an integer, g can only be 1 or 2.

Optimization: Maximize Sum(S) = Sum(U) - Sum(R). This means minimizing Sum(R).

Case g=1: R = {1, 2, ..., 191}. |R|=191. Sum(R) = 18336. Sum(S) = 0.
Case g=2: R = {2, 4, ..., 190}. |R|=95. Sum(R) = 9120. Sum(S) = 18336 - 9120 = 9216.

Maximum sum of remaining numbers is 9216.

### [W3, round 1]
Goal: Minimize $\sum R$ subject to $|R| \ge 95$ and closure rules in $\{1, \ldots, 191\}$.
Hypothesis: To minimize the sum while maintaining size, the elements of R must be concentrated at the highest possible values, exploiting the boundary of 191.
Test Case: R = {k, k+1, ..., 191}. Size = 192 - k.
Constraint: 192 - k >= 95 => k <= 97.
To minimize the sum, we maximize k. We choose k=97.
Candidate Set R = {97, 98, ..., 191}. |R| = 95.

Verification:
1. Doubling: For any x in R, x >= 97. 2x >= 194. Since 194 > 191, 2x is outside the set {1, ..., 191}. The rule (i) is satisfied vacuously.
2. Addition: For any x, y in R, x+y >= 97+97 = 194. Since 194 > 191, x+y is outside the set {1, ..., 191}. The rule (ii) is satisfied vacuously.

This set satisfies all constraints and has the minimum sum achievable for a set of size 95 concentrated at the high end of the domain.
Sum of R = (95/2) * (97 + 191) = 95 * 144 = 13680.
