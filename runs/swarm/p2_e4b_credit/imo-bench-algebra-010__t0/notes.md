### [W2, round 1]
Analysis of small blackboard set B = {0, 1}.
1. P1 (Differences): P1 = {f - g | f, g in {0, 1}} = {-1, 0, 1}.
2. P2 (Triple products): P2 = {3pq r | p, q in P1} = {3 * p * q * r}. Since P1 contains 0, 0 is in P2. The non-zero elements are $3(1)(1)r = 3r$ and $3(1)(-1)r = -3r$. Thus, P2 = {0, 3r, -3r}.
3. P3 (Quadratic sum/difference): P3 = {x^2 + y^2 - z^2 - w^2 | x, y, z, w in P1}. Since P1^2 = {0, 1}, P3 elements are formed by sums/differences of elements from {0, 1}. P3 = {-2, -1, 0, 1, 2}.
4. Constraint Check (P2 subset P3): For P2 to be a subset of P3, we must have $3r \in \{-2, -1, 0, 1, 2\}$ and $-3r \in \{-2, -1, 0, 1, 2\}$.
5. Counterexample Insight: If we choose $r=1$, then $3r=3$. Since $3 \notin P_3$, $r=1$ is not a solution. This confirms that $r$ must be constrained such that $|3r| \le 2$.

### [W4, round 1]
Analysis of P2 $\subseteq$ P3 reveals that P2 depends on the given real number $r$ as a scaling factor: $P_2 = \{ (3r) \cdot p \cdot q \mid p, q \in P_1 \}$. Since P3 is fixed solely by the initial blackboard set $S$, and $P_2$ scales with $r$, the condition P2 $\subseteq$ P3 is fundamentally dependent on $r$. The condition holds universally only if $r=0$, which makes $P_2 = \{0\}$. To make the condition independent of $r$, $r$ should not act as an external scaling factor. A reasonable modification is to define P2 as $\{3pq \mid p, q \in P_1\}$, thereby removing $r$ from the definition entirely.

### [W1, round 1]
Analysis of P1: P1 is the set of all pairwise differences of the 100 distinct blackboard numbers S. $P_1 = \{f-g \mid f, g \in S\}$. It is closed under negation ($d \in P_1 \implies -d \in P_1$) and contains $0$.

Analysis of P3: P3 elements are of the form $x^2+y^2-z^2-w^2$, where $x, y, z, w \in P_1$. Since $P_1$ is closed under negation, we can rewrite this structure. Let $A = x^2+y^2$ and $B = z^2+w^2$. $P_3 = \{A - B \mid A, B \text{ are sums of two squares from } P_1\}$.

Simplifying P3: An element $d \in P_3$ means $d = (x^2+y^2) - (z^2+w^2)$. Since $P_1$ is derived from the initial set $S$, the properties of $P_3$ depend heavily on the structure of $S$. For $P_2 \subseteq P_3$ to hold regardless of $S$, $P_3$ must be an extremely robust set (like $\mathbb{R}$ or $\mathbb{Z}$) or $P_2$ must be trivial.

General Property of P3: $P_3$ is a set of differences of sums of two squares of elements from $P_1$. Since $P_1$ is symmetric, $P_3$ is also symmetric (if $d \in P_3$, then $-d \in P_3$ by swapping the roles of $(x, y)$ and $(z, w)$).

### [W3, round 1]
Analysis of P2 \subseteq P3:
Let B be the set of 100 distinct real numbers on the blackboard.
P1 = {f-g | f, g in B}
P2 = {3pqr | p, q in P1} (Assuming r is the third variable based on problem context)
P3 = {x^2+y^2-z^2-w^2 | x, y, z, w in P1}

We require that for any choice of B, every element N = 3pqr in P2 is also in P3.
This means that for any p, q in P1, the equation:
3pqr = x^2+y^2-z^2-w^2
must hold for some x, y, z, w in P1.

Since p, q, x, y, z, w are differences of elements of B, they are linear functions of the elements of B.
If we choose B such that its elements are algebraically independent (a generic choice), then p, q, x, y, z, w are polynomials of degree 1 in the elements of B.
The Left Hand Side (LHS), 3pqr, is a homogeneous cubic polynomial in the elements of B.
The Right Hand Side (RHS), x^2+y^2-z^2-w^2, is a homogeneous quadratic polynomial in the elements of B.

For a cubic polynomial to equal a quadratic polynomial regardless of the values of the underlying variables (the elements of B), the cubic polynomial must be identically zero.
Since p and q can be chosen to be non-zero (e.g., by setting B={0, 1, ...}), p*q is generally non-zero.
Therefore, we must have 3r = 0.

This implies r = 0.

If r=0, then P2 = {0}. Since P1 always contains 0 (by choosing f=g), and 0^2+0^2-0^2-0^2 = 0, P3 always contains 0. Thus P2 \subseteq P3 holds when r=0.
