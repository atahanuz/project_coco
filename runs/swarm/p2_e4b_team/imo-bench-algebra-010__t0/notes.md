### [W1, round 1]
Analysis of P1 = {f-g | f, g in S}:
1. Closure under Negation: P1 is closed under negation. If x = f - g in P1, then -x = g - f, which is also in P1.
2. Closure under Subtraction (P1 - P1): The set P1 - P1 consists of all numbers of the form (f1 - f2) - (g1 - g2), where f1, f2, g1, g2 are elements of S. This can be written as {f1 - f2 - g1 + g2 | f1, f2, g1, g2 in S}. This is equivalent to P1 - P1.

### [W2, round 1]
Analysis of P3:
P1 is the set of all differences of pairs of numbers from the blackboard B: P1 = {f-g | f, g in B}. Note that 0 is always in P1.
P3 is defined as P3 = {x^2+y^2-z^2-w^2 | x, y, z, w in P1}.

Characterization of P3:
P3 is the set of all numbers that can be written as the difference of two sums of two squares, where the base elements (x, y, z, w) are members of P1.
Specifically, P3 = {S_A - S_B | S_A = x^2 + y^2, S_B = z^2 + w^2, and x, y, z, w are elements of P1}.
This means every element in P3 is expressible as the difference of two numbers, where each of those two numbers is a sum of two squares of elements from P1.

### [W4, round 1]
Analysis of P2 containment in P3:
P1 = {f - g | f, g in S}.
P2 = {3rpq | p, q in P1} (Assuming the structure P2 = {3rpq} based on the task prompt).
P3 = {x^2 + y^2 - z^2 - w^2 | x, y, z, w in P1}.

For P2 subset P3 to hold regardless of the choice of the initial set S (and thus regardless of P1), the structure of P2 must be highly constrained. If r is non-zero, we can choose S such that P1 contains elements p and q resulting in a product 3rpq that cannot be represented as the required quadratic form in P3, unless P1 itself is trivial. The only value of r that guarantees P2 is contained in P3 universally is r=0, which forces P2 = {0}, and 0 is always in P3 (by setting x=y=z=w=0, which is in P1).

### [W3, round 1]
Task: Test the condition for S = {1, 2, ..., 100}.
P1 = {f-g | f, g in S} = {-99, ..., 99}.
P3 = {x^2+y^2-z^2-w^2 | x, y, z, w in P1}.
Since 0 is in P1, we can choose x=y=z=w=0, so 0 is in P3. Also, 1 is in P3 (e.g., 2^2+0^2-1^2-0^2 = 3; 1^2+0^2-0^2-0^2 = 1). P3 contains many integers.

P2 definition from task: P2 = {r * 3*p*q*r' | p, q in P1}. Assuming the task meant P2 = {3r*p*q | p, q in P1}.
Testing r=0: P2 = {0}. Since 0 is always in P3 (as 0 is always in P1), r=0 is a possible value.

Due to the ambiguity in the original problem's definition of P2 (3pqr with p, q from P1), and the necessity of finding a universal constraint on r, the simplest universal solution found via the test case is r=0. Further analysis of the general case is required but falls outside the scope of this initial test.

### [W2, round 2]
### [W2, round 2] Deep Algebraic Characterization of $P_3$
$P_3$ is defined as $P_3 = \{x^2+y^2-z^2-w^2 \mid x, y, z, w \in P_1\}$, where $P_1 = \{f-g \mid f, g \in S\}$.

1. **Structure:** $P_3$ is the set of differences of two sums of two squares, where the generators of these sums ($x, y, z, w$) are elements of the difference set $P_1 = S-S$.
2. **Symmetry:** Since $x \in P_1 \implies -x \in P_1$ (because $P_1$ is closed under negation), if $K \in P_3$, then $-K \in P_3$.
   If $K = x^2+y^2-z^2-w^2$, then $-K = (-x)^2+(-y)^2-(-z)^2-(-w)^2 = x^2+y^2-z^2-w^2$. Wait, this is incorrect.
   If $K = x^2+y^2-z^2-w^2$, then $-K = z^2+w^2-x^2-y^2$. Since $x, y, z, w \in P_1$, then $z^2+w^2-x^2-y^2$ is also an element of $P_3$ (by setting the roles of $\{x, y\}$ and $\{z, w\}$ to switch). Thus, $P_3$ is symmetric about zero.
3. **Dependence on S:** $P_3$ is fundamentally constrained by the arithmetic structure of $S$. Specifically, $P_3$ is the set of all values of the quadratic form $Q(x, y, z, w) = x^2+y^2-z^2-w^2$ restricted to the domain $P_1^4$.
4. **Trivial Inclusion:** Since $0 = f-f \in P_1$ for any $f \in S$, $0^2+0^2-0^2-0^2 = 0$ is always an element of $P_3$.

### [W1, round 2]
[W1, round 2]
Task: Construct a minimal counterexample set S for r != 0.
We tested the minimal case $|S|=2$. Let $S = \{s_1, s_2\}$ with $s_1 \neq s_2$.
Let $d = s_1 - s_2$. Then $P_1 = \{0, d, -d\}$.
$P_2 = \{0, 3rd^2, -3rd^2\}$.
$P_3 = \{-2d^2, -d^2, 0, d^2, 2d^2\}$.
For $P_2 \not\subseteq P_3$, we require $3r$ to not be in $\{-2, -1, 0, 1, 2\}$.
Let's choose $r=1$ (assuming $r \neq 0$). We require $3d^2 \notin P_3$.
We choose the simplest non-trivial set $S = \{0, 1\}$. Here $d=1$.
$P_1 = \{0, 1, -1\}$.
$P_2 = \{0, 3, -3\}$.
$P_3 = \{-2, -1, 0, 1, 2\}$.
Since $3 \notin P_3$, $S=\{0, 1\}$ is a minimal counterexample set when $r=1$.
