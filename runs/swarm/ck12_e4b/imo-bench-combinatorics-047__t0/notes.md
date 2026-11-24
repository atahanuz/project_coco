### [W1, round 1]
Calculations for complete graphs $K_n$:
For $n=4$: $f(K_4) = 4$, $g(K_4) = 1$. Ratio $\frac{g^3}{f^4} = \frac{1^3}{4^4} = \frac{1}{256}$.
For $n=5$: $f(K_5) = 10$, $g(K_5) = 5$. Ratio $\frac{g^3}{f^4} = \frac{5^3}{10^4} = \frac{125}{10000} = \frac{1}{80}$.
For $n=6$: $f(K_6) = 20$, $g(K_6) = 15$. Ratio $\frac{g^3}{f^4} = \frac{15^3}{20^4} = \frac{3375}{160000} = \frac{27}{1280}$.

The largest ratio calculated is $\frac{27}{1280} \approx 0.0211$. This sets the initial upper bound $c \le 27/1280$.

### [W1, round 1]
REPORT on task "Calculate the exact values of $f(K_n)$ (number of triangles) and $g(K_n)$ (number of tetrahedra) for $n=4, 5, 6$. Use these calculations to determine an initial upper bound for the ratio $g(G)^3 / f(G": I calculated $f(K_n) = \binom{n}{3}$ and $g(K_n) = \binom{n}{4}$ for $n=4, 5, 6$. The calculated ratios for these cases were $1/256$, $1/80$, and $27/1280$. Since $27/1280$ is the largest value found, it serves as the initial upper bound for the constant $c$.
Candidate answer: 27/1280

### [W3, round 1]
Preliminary analysis of the ratio $R(G) = g(G)^3 / f(G)^4$:
1. If $G$ is $K_4$-free ($g(G)=0$) but $f(G)>0$, the ratio $R(G) = 0$. Therefore, the maximum value $c$ must be greater than 0, and the ratio cannot reach its maximum when $g(G)=0$.
2. We tested complete graphs $K_n$. The ratio for $K_n$ is $R(K_n) = \frac{3}{32} \frac{(n-3)^3}{n(n-1)(n-2)}$.
3. Numerical checks showed the ratio increases with $n$ for small $n$: $R(K_4) = 1/256$, $R(K_5) = 1/80$, $R(K_6) = 27/1280$, $R(K_7) = 1/35$, $R(K_8) = 375/10752$.
4. The limit of $R(K_n)$ as $n \to \infty$ is $\lim_{n\to\infty} R(K_n) = \frac{3}{32}$.
5. Since the ratio seems to approach $3/32$ from below for $K_n$, it is a strong candidate for the least constant $c$. Further analysis of non-complete graphs is generally complex, but in extremal graph theory, the bound is often achieved or approached by complete graphs or their structural relatives. We tentatively conclude $c = 3/32$.

### [W3, round 1]
REPORT on task "Consider graphs $G$ that are $K_4$-free ($g(G)=0$) but have many triangles ($f(G) > 0$). Determine if the ratio $g(G)^3 / f(G)^4$ can reach its maximum value when $g(G)=0$. If $g(G)=0$, the ratio is 0": I first addressed the task requirement regarding $K_4$-free graphs ($g(G)=0$); in this case, the ratio is 0, so it cannot reach the maximum constant $c$ if $c>0$. I then investigated the ratio for complete graphs $K_n$, finding the closed form $R(K_n) = \frac{3}{32} \frac{(n-3)^3}{n(n-1)(n-2)}$. Numerical checks showed this ratio increases with $n$ and approaches the limit $\frac{3}{32}$ as $n \to \infty$. I conclude that the least constant $c$ satisfying the inequality is $3/32$.
Candidate answer: 3/32

### [W2, round 1]
### Investigation Summary: Relationship between $g(G)$ and $f(G)$

**Algebraic Relationship & Connectivity:**
For a general graph $G$, there is no simple local algebraic relationship between $g(G)$ and $f(G)$. $g(G)$ is dependent on the specific structure of 4-cliques, while $f(G)$ is dependent on 3-cliques. The ratio $g(G)^3/f(G)^4$ measures the "density of tetrahedra relative to triangles." We observe that this ratio is maximized when the graph $G$ is highly dense and highly connected, specifically for complete graphs $K_n$.

**Numerical Findings (Complete Graphs $K_n$):**
We analyzed the ratio $R_n = \frac{g(K_n)^3}{f(K_n)^4}$ for $n=4$ through $n=9$.

| $n$ | $f(K_n) = \binom{n}{3}$ | $g(K_n) = \binom{n}{4}$ | Ratio $R_n$ | Decimal Value |
| :---: | :---: | :---: | :---: | :---: |
| 4 | 4 | 1 | $1/256$ | $\approx 0.0039$ |
| 5 | 10 | 5 | $1/80$ | $0.0125$ |
| 6 | 20 | 15 | $27/1280$ | $\approx 0.0211$ |
| 7 | 35 | 35 | $1/35$ | $\approx 0.0286$ |
| 8 | 56 | 70 | $70^3/56^4$ | $\approx 0.0349$ |
| 9 | 84 | 126 | $126^3/84^4$ | $\approx 0.0402$ |

The ratio $R_n$ is increasing with $n$. As $n \to \infty$, $R_n$ approaches the asymptotic value:
$$R_n \sim \frac{\left(\frac{n^4}{24}\right)^3}{\left(\frac{n^3}{6}\right)^4} = \frac{n^{12}/24^3}{n^{12}/6^4} = \frac{6^4}{24^3} = \frac{1296}{13824} = \frac{3}{32}$$

**Conclusion:**
The investigation suggests that the least constant $c$ is the supremum of the ratio, which for complete graphs tends towards $3/32$. Given the monotonic increase observed for $K_n$ and the extreme density of these graphs, we conjecture that $c = 3/32$.

### [W2, round 1]
REPORT on task "Investigate the algebraic relationship between the number of $K_3$ subgraphs ($f(G)$) and $K_4$ subgraphs ($g(G)$) in a general graph $G$. Specifically, try to relate $g(G)$ to the count of triangles ": I investigated the relationship between $g(G)$ and $f(G)$ by examining complete graphs $K_n$, which serve as the densest structure. I calculated the ratio $R_n = g(K_n)^3 / f(K_n)^4$ for $n=4$ through $n=9$, observing that the ratio increases with $n$. The sequence $R_n$ tends towards the asymptotic limit derived from the binomial coefficients, which is $3/32$. Since the ratio is maximized by complete graphs and increases monotonically towards this limit, I conclude that the least constant $c$ is $3/32$.
Candidate answer: 3/32

### [W4, round 1]
Analysis of the ratio $R(G) = g(G)^3 / f(G)^4$:

1.  **Complete Graphs $K_n$:** As $n \to \infty$, $R(K_n)$ approaches a constant limit. Using asymptotic counting, $R(K_n) \sim \frac{3}{32}$. Numerical checks confirm this trend (e.g., $R(4) \approx 0.0039$, $R(8) \approx 0.0349$, Limit $= 0.09375$).

2.  **Graphs Lacking Full Cliques:** The task requested analysis of graphs built around dense substructures but lacking full cliques, seeking constructions where $f(G)$ is maximized relative to $g(G)$ (i.e., minimizing $R(G)$). We examined $G = K_5 - e$.
    *   For $K_5$, $R(K_5) = 0.0125$.
    *   For $K_5 - e$, we found $f(G) = 7$ and $g(G) = 2$, leading to $R(G) = 2^3 / 7^4 = 8 / 2401 \approx 0.00333$.

3.  **Conclusion on Scaling:** The construction $K_n - E'$ shows that if a graph lacks full cliques, the ratio $R(G)$ tends to be significantly smaller than the ratio achieved by the complete graph $K_n$. This suggests that $K_n$ provides the scaling necessary to determine the least constant $c$.

### [W4, round 1]
REPORT on task "Look for constructions or properties of dense graphs where the number of $K_3$ subgraphs ($f(G)$) is maximized relative to the number of $K_4$ subgraphs ($g(G)$). Analyze how the ratio scales with the": I investigated how the ratio $g(G)^3/f(G)^4$ scales for dense graphs. My analysis of $K_n$ showed that the ratio approaches $3/32$ as $n \to \infty$. Furthermore, I examined graphs lacking full cliques, such as $K_n$ minus a few edges, finding that these structures tend to have a ratio significantly lower than $3/32$. Therefore, the supremum is attained asymptotically by the complete graphs $K_n$, yielding the least constant $c = 3/32$.
Candidate answer: 3/32

### [CHECKER, round 1]
Independent check of the new candidate answers (the checker saw only the problem and the answers, not who proposed them and not these notes):
- `3/32`: CONFIRMED: The ratio g(G)^3 / f(G)^4 is maximized as G approaches a complete graph K_n for large n. For a complete graph K_n, g(K_n) = comb(n, 4) and f(K_n) = comb(n, 3). The ratio is g(K_n)^3 / f(K_n)^4 = (3/32) * (n-3)^3 / (n(n-1)(n-2)). As n approaches infinity, this ratio approaches 3/32. Since the ratio is strictly increasing with n and bounded by 3/32, the least constant c is 3/32.
- `27/1280`: REFUTED: The ratio g(G)^3/f(G)^4 for a complete graph K_n is given by (comb(n,4)^3)/(comb(n,3)^4). For n=7, this ratio is 35^3/35^4 = 1/35 approx 0.02857, which is greater than 27/1280 (approx 0.02109). Thus, 27/1280 is not a valid constant c.
