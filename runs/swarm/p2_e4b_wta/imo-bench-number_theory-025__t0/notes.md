### [W3, round 1]
ANALYSIS OF THE TASK:
The problem requires finding the smallest $n$ such that $\frac{\sum_{i=1}^n P_i(x)^2}{x^2 + 7} = Q(x)^2$.
Assuming $Q(x)=1$, we require $\sum_{i=1}^n P_i(x)^2 = x^2 + 7$.

1. Condition at $\alpha = i\sqrt{7}$:
The roots of the denominator are $\pm i\sqrt{7}$. Substituting $x = i\sqrt{7}$ into the required identity yields:
$\sum_{i=1}^n P_i(i\sqrt{7})^2 = (i\sqrt{7})^2 + 7 = -7 + 7 = 0$.

2. General equations (assuming $P_i(x) = a_i x + b_i$):
Matching coefficients of $\sum P_i(x)^2 = x^2 + 7$ gives:
(i) $\sum a_i^2 = 1$ (Coefficient of $x^2$)
(ii) $2 \sum a_i b_i = 0$ (Coefficient of $x$)
(iii) $\sum b_i^2 = 7$ (Constant term)

The task focuses on the required equation $\sum b_i^2 = 7$. This equation must be satisfied by integers $b_i$.

3. Minimum $n$ for $\sum b_i^2 = 7$:
We determine the smallest $n$ such that 7 is a sum of $n$ integer squares.
- $n=1$: $7 = b_1^2$. Impossible.
- $n=2$: $7 = b_1^2 + b_2^2$. Impossible (e.g., $4+3$, $1+6$).
- $n=3$: $7 = b_1^2 + b_2^2 + b_3^2$. By Legendre's three-square theorem, 7 cannot be written as the sum of three squares because it is of the form $8m+7$ (with $m=0$).
- $n=4$: $7 = b_1^2 + b_2^2 + b_3^2 + b_4^2$. Achieved by $4 + 1 + 1 + 1$.

The minimum required $n$ to satisfy $\sum b_i^2 = 7$ is 4. This value is likely the minimum $n$ for the original problem under the $Q(x)=1$ assumption.

### [W1, round 1]
Task analysis: Find minimum $n$ such that $\sum b_i^2 = 7$ under constraints derived from matching polynomial coefficients when $P_i(x) = a_i x + b_i$ and the quotient is a square of a constant $R(x)=c$.
The matching conditions yield:
1. $\sum a_i^2 = c^2$
2. $\sum a_i b_i = 0$
3. $\sum b_i^2 = 7 c^2$

Given the constraint $a_1=1$ and $b_1=0$.
From (1), $\sum_{i=2}^n a_i^2 = c^2 - 1$.
From (3), $\sum_{i=2}^n b_i^2 = 7c^2$.
The prompt implicitly guides us towards the case where $\sum a_i^2 = 1$, which forces $c^2=1$ and $c=\pm 1$.
If $c^2=1$:
1. $\sum_{i=2}^n a_i^2 = 0 \implies a_i = 0$ for $i \ge 2$.
2. $\sum_{i=2}^n b_i^2 = 7$.
3. $\sum_{i=2}^n 0 \cdot b_i = 0$ (Satisfied).

We need the minimum number of integers $k = n-1$ such that the sum of $k$ squares equals 7.
$7 = 4 + 1 + 1 + 1 = 2^2 + 1^2 + 1^2 + 1^2$.
This requires 4 terms.
Therefore, $n-1 = 4$, so $n=5$.

### [W2, round 1]
The task checks the solvability of sum(P_i(x)^2) = C^2(x^2+7) for N=5 (assuming N is the minimum). This requires 7C^2 to be a sum of 4 integer squares, which is always true by Lagrange's four-square theorem. A solution exists for all non-zero integer constants C.

### [W4, round 1]
Initial exploration suggests the intended problem structure requires $\sum P_i(x)^2 = Q(x)^2 (x^2+7)$. Due to degree constraints, $Q(x)$ must have even degree or be constant. The simplest case is $Q(x)=1$, requiring $\sum P_i(x)^2 = x^2+7$. Minimizing $n$ requires finding the minimum number of integer squares that sum to 7 (for the constant term after accounting for $x^2$). Since $7 = 2^2 + 1^2 + 1^2 + 1^2$, the minimum number of additional squares is 4. Including the square for $x^2$, the minimum $n$ is 5. This result holds for other simple even-degree $Q(x)$ as well.
