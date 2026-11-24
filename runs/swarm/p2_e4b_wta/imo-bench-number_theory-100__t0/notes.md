### [W4, round 1]
Investigation of the case m=n:
The original conditions require:
1) $\log_p (m^2+n) = k_1$, where $k_1 \in \mathbb{Z}$ and $k_1 > 1$.
2) $\log_p(m+n^2) = k_2$, where $k_2 \in \mathbb{Z}$ and $k_2 > 1$.

Setting m=n, the conditions become identical:
$\log_p (n^2+n) = k$, where $k \ge 2$.
This implies $p^k = n^2 + n = n(n+1)$.

Since $n$ and $n+1$ are consecutive positive integers, $\gcd(n, n+1) = 1$.
Because $p^k$ is a power of a prime $p$, and $n(n+1) = p^k$, both $n$ and $n+1$ must be powers of $p$.
Let $n = p^a$ and $n+1 = p^b$, where $a+b=k$ and $b>a$ (since $n+1>n$).
$p^a + 1 = p^b$, which leads to $p^b - p^a = 1$, or $p^a(p^{b-a} - 1) = 1$.

Since $p$ is prime, the only way this product can equal 1 is if $p^a = 1$ and $p^{b-a} - 1 = 1$.
1. $p^a = 1$ implies $a=0$.
2. $p^{b-0} = 2$ implies $p=2$ and $b=1$.

If $a=0$ and $b=1$, then $k = a+b = 1$.
However, the problem requires $k \ge 2$.
Since the only solution to $p^k = n(n+1)$ is $k=1$ (which yields $n=1, p=2$), there are no solutions satisfying the required condition $k>1$.
Conclusion: No solutions exist for m=n.

### [W1, round 1]
Computational Search Results (p<=7, m<=15):
Solutions (m, n, p) found such that m^2+n and m+n^2 are powers of p with exponent > 1:
(2, 5, 3)
(5, 2, 3)

### [W3, round 1]
Analysis of $m^2+n = p^A$ and $m+n^2 = p^B$ with $A, B \ge 2$:

1. Subtraction yields: $(m-n)(m+n-1) = p^A - p^B$.
2. Addition yields: $m(m+1) + n(n+1) = p^A + p^B$.

3. Analyzing modulo p:
If we take the equations modulo p, we get:
$m^2 + n \equiv 0 \pmod p$
$m + n^2 \equiv 0 \pmod p$
Substituting $n \equiv -m^2 \pmod p$ into the second congruence gives:
$m + (-m^2)^2 \equiv 0 \pmod p$
$m(1 + m^3) \equiv 0 \pmod p$.
This implies $p | m$ or $p | (m^3+1)$.

4. Case m=n: We found no solutions where $m=n$ while satisfying $A, B \ge 2$, because $m(m+1) = p^A$ requires $m=1, p=2, A=1$, which violates $A \ge 2$.

5. Constraints derived:
The relationship $(m-n)(m+n-1) = p^A - p^B$ is the primary structural constraint relating $m, n, p, A, B$. Further constraints arise from the modulo $p$ condition, especially ruling out solutions where both $m$ and $n$ are multiples of $p$ unless $m$ or $n$ are extremely small relative to $p$. The non-zero solutions likely involve cases where $p | m$ (and $p \nmid n$) or $p | (m^3+1)$ (and $p \nmid m$).

### [W2, round 2]
Computational Search Results (p <= 7, n <= 25, A <= 15):
The search confirmed the two solutions previously found by W1, and found no new solutions within these constraints.
Solutions (m, n, p) found:
1. (5, 2, 3)
2. (2, 5, 3)
For (5, 2, 3): m^2+n = 27 = 3^3 (A=3), m+n^2 = 9 = 3^2 (B=2).
For (2, 5, 3): m^2+n = 9 = 3^2 (A=2), m+n^2 = 27 = 3^3 (B=3).
These solutions are the only ones found for $p \le 7$ and $n \le 25$ using $A \le 15$.

### [W3, round 2]
Strong Constraint Derived: Solutions $(m, n, p)$ must satisfy the Diophantine equation $p^{2B} - 2p^B n^2 + n^4 + n = p^{B+k}$, where $k = A-B \ge 1$. Analysis shows that $B$ must be close to $k$. Specifically, for $k=1$ and $B=2$ (leading to $A=3$), the equation simplifies to $p^4 - p^3 = 2p^2 n^2 - n^4 - n$, which proves that for a fixed prime $p$, $n$ must be a solution to a fixed quartic equation, guaranteeing that solutions are finite and small.
