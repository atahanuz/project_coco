### [W1, round 1]
Task: Calculate N for the diagonal enumeration bijection f(x, y) = 1/2 * (x+y)(x+y+1) + x for 0 <= x, y < 100.
Method: Iteratively checked the parity of f(x, y) for all 10000 pairs (x, y).
Calculation results in N = 5000.

### [W3, round 1]
Analysis of $g(n) = n^2 - n + 1$ modulo 2:
We examine the parity of $g(n)$.
$g(n) = n(n-1) + 1$.
Since $n$ and $n-1$ are consecutive integers, their product $n(n-1)$ is always even (i.e., $n(n-1) \equiv 0 \pmod 2$).
Therefore, $g(n) = n(n-1) + 1 \equiv 0 + 1 \equiv 1 \pmod 2$.
Conclusion: $g(n)$ is always odd for all $n \in \mathbb{Z}_{\geqslant 0}$.

Implications for $f$:
The function $f$ is a bijection from $\mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0}$ to $\mathbb{Z}_{\geqslant 0}$. Since $\mathbb{Z}_{\geqslant 0}$ contains all non-negative integers (both even and odd), $f$ must take both even and odd values.
If $f$ were related to $g$ in such a way that $f(x, y) = g(h(x, y))$ for some function $h$, then $f(x, y)$ would always be odd, as $g$ always outputs odd values. This would contradict the requirement that $f$ is a bijection onto $\mathbb{Z}_{\geqslant 0}$. Therefore, $f$ cannot be directly or purely determined by $g$ in a way that restricts its range to only odd numbers. The parity of $f(x, y)$ must be determined by the specific mapping structure defined by the monotonicity conditions, and must cover all parities.

### [W2, round 1]
Initial analysis of the monotonicity constraints on f:
1. f is a bijection from Z_>=0 x Z_>=0 to Z_>=0.
2. The conditions state that relative ordering is preserved upon applying (x, y) -> (x+1, y) and (x, y) -> (x, y+1).
3. This strongly suggests that f must be a strictly increasing function in both x and y (i.e., f(x+1, y) > f(x, y) and f(x, y+1) > f(x, y)). If this is not true, the ordering could collapse or reverse, violating the strong preservation properties.

Focus on Parity P(x, y) = f(x, y) mod 2:
The conditions imply that if f(x1, y1) > f(x2, y2), then f(x1+1, y1) > f(x2+1, y2). This means the set of pairs {(x, y) | f(x, y) is odd} must transform consistently under shifts.
Since f is a bijection, the sequence of parities P(x, y) must eventually contain both 0 and 1 infinitely often.

We need to investigate how the parity sequence changes when moving one unit in x or y, assuming the function is constructed based on a standard enumeration scheme (like diagonal filling or lexicographical order). The possibility of different constructions of f (while satisfying the bijection and monotonicity) is what allows for different minimum (a) and maximum (b) values of N.

Next step: Investigate specific structural forms of f (e.g., related to pairing functions) and determine the resulting parity patterns, focusing on how the parity pattern relates to changes in x and y.

### [W4, round 1]
Investigation of function f:
The constraints on f, particularly the preservation of ordering upon shifting coordinates, are extremely strong. They imply that f must behave like a highly monotonic mapping, resembling linear bijections of the form f(x, y) = kx + cy, where k and c are positive, coprime integers (for f to be a bijection to Z_{>=0}).

Parity analysis based on linear solutions:
1. If f(x, y) = kx + cy, where k and c are both odd: f is odd iff x+y is odd. For the 100x100 grid (M=100), this yields N = 5000.
2. If k is even and c is odd (or vice versa): f is odd iff the coordinate corresponding to the odd coefficient is odd. This also yields N = 5000.
3. If k and c are both even: f is always even, violating the bijection requirement to Z_{>=0}.

The simplest solutions suggest that the parity distribution is rigidly balanced (50/50) when the domain side length (M=100) is even. We conjecture that the strong ordering constraint limits the structural freedom significantly, implying that the number of odd values N is constant, $N=5000$.
This suggests a=b=5000.
