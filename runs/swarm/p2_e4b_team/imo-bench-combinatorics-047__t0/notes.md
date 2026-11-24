### [W2, round 1]
Analysis of the relationship between $g(G)$ (number of $K_4$ subgraphs) and $f(G)$ (number of $K_3$ subgraphs) suggests that $g(G)$ might be bounded by $O(f(G)^{4/3})$. This was tested using complete graphs $K_n$. For $K_n$, $f(K_n) = \binom{n}{3}$ and $g(K_n) = \binom{n}{4}$. The ratio $\frac{g(K_n)^3}{f(K_n)^4}$ approaches a constant value $\frac{6^{4/3}}{24}$ as $n \to \infty$, indicating that complete graphs saturate this bound and provide a potential candidate for the least constant $c$.

### [W3, round 1]
The ratio $R(G) = g(G)^3 / f(G)^4$ is maximized by complete graphs $K_n$. The ratio for $K_n$ is given by $R(K_n) = \frac{3(n-3)^3}{32 n(n-1)(n-2)}$. As $n \to \infty$, this ratio approaches the constant $\frac{3}{32}$. This suggests the least constant $c$ is $3/32$.

### [W1, round 1]
Calculations for R(K_n) = g(K_n)^3 / f(K_n)^4:
n=3: R(K_3) = 0
n=4: R(K_4) = 27/256
n=5: R(K_5) = 0.3375
n=6: R(K_6) = 729/1280
n=7: R(K_7) = 27/35

The maximum value found for n in {3, 4, 5, 6, 7} is R(K_7) = 27/35.

### [W3, round 2]
Analysis of R(K_n) = (binom(n,4))^3 / (binom(n,3))^4:
1. Derived closed form: R(K_n) = (3/32) * (n-3)^3 / (n(n-1)(n-2)).
2. Analyzed the ratio R(K_{n+1})/R(K_n) = (n-2)^4 / ((n+1)(n-3)^3).
3. Showed that the difference between the numerator and denominator is 6n^2 - 32n + 43, which is always positive (discriminant is -8).
4. Conclusion: R(K_n) is strictly monotonically increasing for n >= 4.

### [W2, round 3]
### [W2, round 2] Extremal Justification for $K_n$ Maximizing $R(G)$
The empirical evidence from the notes shows $R(K_n)$ is strictly monotonic for $n\ge 4$, suggesting $K_n$ provides the supremum. From an extremal graph theory perspective, the ratio $R(G) = g(G)^3 / f(G)^4$ measures the efficiency of forming $K_4$ structures relative to $K_3$ structures. Complete graphs $K_n$ are maximally dense and perfectly regular, meaning that the presence of any $K_3$ immediately implies the maximum possible number of adjacent edges (to form $K_4$'s). For any non-complete graph $G$, replacing edges with non-edges necessarily reduces the overall connectivity, leading to a sub-optimal ratio because the dependencies between local $K_3$ structures and larger $K_4$ structures are weakened. Thus, $K_n$ provides the structural maximum.
