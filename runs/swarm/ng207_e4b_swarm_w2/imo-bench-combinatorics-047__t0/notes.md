### [W1, round 1]
Calculations for $\frac{g(K_n)^3}{f(K_n)^4}$ for $n=3, 4, 5, 6$:
$n=3$: $\frac{0^3}{1^4} = 0$.
$n=4$: $\frac{1^3}{4^4} = \frac{1}{256} \approx 0.00390625$.
$n=5$: $\frac{5^3}{10^4} = \frac{125}{10000} = \frac{1}{80} = 0.0125$.
$n=6$: $\frac{15^3}{20^4} = \frac{3375}{160000} = \frac{27}{1280} \approx 0.02109375$.

### [W1, round 1]
REPORT on task "Calculate the values of the expression $\frac{g(K_n)^3}{f(K_n)^4}$ for $n=3, 4, 5, 6$, where $f(K_n)$ is the number of triangles and $g(K_n)$ is the number of tetrahedra in $K_n$. Record these values ": I calculated the value of the expression $\frac{g(K_n)^3}{f(K_n)^4}$ for $n=3, 4, 5, 6$. Using the formulas $f(K_n) = \binom{n}{3}$ and $g(K_n) = \binom{n}{4}$, I found the values to be 0 for $n=3$, $1/256$ for $n=4$, $1/80$ for $n=5$, and $27/1280$ for $n=6$. These results have been recorded in notes.md for the team.
Candidate answer: N/A (Calculations completed as per instruction)

### [W2, round 1]
**Theoretical Analysis of $g(G)$ vs $f(G)$**

The maximum value of the ratio $\frac{g(G)^3}{f(G)^4}$ is expected to be achieved by complete graphs $K_n$, as they are the densest possible graphs.

For $G = K_n$, we have $f(K_n) = \binom{n}{3}$ and $g(K_n) = \binom{n}{4}$. We calculate the ratio $R(K_n) = \frac{g(K_n)^3}{f(K_n)^4}$.

We use the relationship $\binom{n}{4} = \frac{n-3}{4} \binom{n}{3}$, so $g(K_n) = \frac{n-3}{4} f(K_n)$.
$$R(K_n) = \frac{\left(\frac{n-3}{4} f(K_n)\right)^3}{f(K_n)^4} = \frac{\left(\frac{n-3}{4}\right)^3}{f(K_n)}$$

As $n \to \infty$:
$f(K_n) = \binom{n}{3} \sim \frac{n^3}{6}$
$\left(\frac{n-3}{4}\right)^3 \sim \left(\frac{n}{4}\right)^3 = \frac{n^3}{64}$

$$ \lim_{n \to \infty} R(K_n) = \lim_{n \to \infty} \frac{n^3/64}{n^3/6} = \frac{6}{64} = \frac{3}{32} $$

We note from the previous calculations (n=4, 5, 6) that $R(K_n)$ approaches $3/32$ from below. Given that $K_n$ is the densest graph structure, we conjecture that the least constant $c$ is $3/32$. This conjecture relies on the assumption that for any non-complete graph $G$, the ratio is bounded by the ratio achieved by the best $K_n$ of comparable size or density, or is simply bounded by the asymptotic limit of $K_n$.

### [W2, round 1]
REPORT on task "Theoretically analyze the relationship between the number of tetrahedra $g(G)$ and the number of triangles $f(G)$ for general graphs $G$. Explore upper bounds for $g(G)$ as a function of $f(G)$ by con": I analyzed the relationship between the number of tetrahedra $g(G)$ and triangles $f(G)$ by examining complete graphs $K_n$, which represent the densest possible graphs. By calculating the ratio $\frac{g(K_n)^3}{f(K_n)^4}$, I found that the ratio asymptotically approaches $3/32$ as $n \to \infty$. Based on this limiting behavior, I conjecture that the least constant $c$ is $3/32$.
Candidate answer: 3/32

### [W1, round 2]
### [W1, round 3]
Calculations for $R(K_n) = g(K_n)^3 / f(K_n)^4$ for $n=8, 9, 10$:
$n=8$: $f(K_8)=56, g(K_8)=70$. $R(K_8) = 70^3 / 56^4 = 125/3584 \approx 0.03488$.
$n=9$: $f(K_9)=84, g(K_9)=126$. $R(K_9) = 126^3 / 84^4 = 9/224 \approx 0.04018$.
$n=10$: $f(K_{10})=120, g(K_{10})=210$. $R(K_{10}) = 210^3 / 120^4 = 343/7680 \approx 0.04466$.

These values confirm the monotonic increase towards the asymptotic limit of $3/32 \approx 0.09375$. The sequence $R(K_n)$ appears to be strictly increasing for $n \ge 4$.

### [W1, round 2]
REPORT on task "Calculate the values of the ratio $R(K_n) = g(K_n)^3 / f(K_n)^4$ for $n=8, 9, 10$ to confirm the monotonic increase towards $3/32$.": I calculated the required ratio $R(K_n) = g(K_n)^3 / f(K_n)^4$ for $n=8, 9, 10$. The results found were $R(K_8) \approx 0.03488$, $R(K_9) \approx 0.04018$, and $R(K_{10}) \approx 0.04466$. These calculations confirm the observed trend of monotonic increase for $K_n$, supporting the theoretical conjecture that the least constant $c$ is the asymptotic limit of $3/32$.
Candidate answer: 3/32

### [W2, round 2]
W2's Investigation: Supporting the Conjecture that $K_n$ Maximizes $\frac{g(G)^3}{f(G)^4}$

The conjecture relies on the principle that complete graphs ($K_n$) maximize local density, which maximizes the proportion of higher-order cliques ($K_4$) relative to lower-order cliques ($K_3$).

1.  **Density Maximization:** $K_n$ is the densest possible graph on $n$ vertices. Since $f(G)$ and $g(G)$ count cliques, the densest structure is expected to maximize the ratio $\frac{g(G)^3}{f(G)^4}$.
2.  **Impact of Sparsity:** If a graph $G$ is sparse compared to $K_n$, it means there exist non-edges $(u, v)$. The presence of a non-edge limits the formation of both triangles and tetrahedra.
3.  **Local Structure Argument:** The formation of a tetrahedron ($K_4$) requires a very high degree of local connectivity (a 4-clique), while a triangle ($K_3$) requires only 3-clique connectivity. In $K_n$, for any two vertices $u$ and $v$, their common neighbors form a complete subgraph of size $n-2$. This maximal local connectivity ensures that for any $K_3$ in $K_n$, the maximum number of ways it can be extended into a $K_4$ is realized.
4.  **Conclusion:** Any deviation from the complete graph structure forces a disproportionate reduction in the growth rate of $g(G)$ relative to $f(G)$ compared to $K_n$. Therefore, the supremum is strongly conjectured to be the limit derived from $K_n$, which is $3/32$.

### [W2, round 2]
REPORT on task "Investigate whether the maximum ratio $\frac{g(G)^3}{f(G)^4}$ is attained by complete graphs $K_n$, providing a proof or a strong theoretical argument demonstrating that for any graph $G$ on $n$ verti": I investigated the conjecture that the supremum of the ratio $\frac{g(G)^3}{f(G)^4}$ is attained by complete graphs $K_n$. I found that for $K_n$, the ratio asymptotically approaches $3/32$. My theoretical argument concludes that $K_n$ maximizes local density, which maximizes the formation of higher-order cliques ($K_4$) relative to lower-order cliques ($K_3$). Any deviation from the complete graph structure introduces non-edges that disproportionately reduce the count of tetrahedra ($g(G)$) relative to triangles ($f(G)$), thereby supporting the conjecture that the least constant $c$ is $3/32$.
Candidate answer: 3/32
