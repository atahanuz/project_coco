### [W2, round 1]
Initial investigation into the relationship between $g(G)$ (number of $K_4$s, $N_4$) and $f(G)$ (number of $K_3$s, $N_3$) was performed by examining the complete graph $K_n$, as this represents the densest configuration.

In $K_n$:
$N_3 = \binom{n}{3}$
$N_4 = \binom{n}{4}$

We analyzed the limit of the ratio $\frac{N_4^3}{N_3^4}$ as $n \to \infty$. Using the asymptotic behavior $\binom{n}{k} \sim n^k / k!$, the limit was calculated to be:
$$\lim_{n \to \infty} \frac{\binom{n}{4}^3}{\binom{n}{3}^4} = \frac{6^4}{24^3} = \frac{1296}{13824} = \frac{3}{32}$$

This suggests that the constant $c$ must be at least $3/32$, and $3/32$ is a strong candidate for the least upper bound. Further investigation is needed to confirm this bound holds for all graphs, particularly sparse ones.

### [W3, round 1]
Calculations for complete graphs $K_n$ ($n \ge 4$):

1.  **Number of Triangles, $f(K_n)$:**
    $f(K_n) = \binom{n}{3} = \frac{n(n-1)(n-2)}{6}$.

2.  **Number of Tetrahedra, $g(K_n)$:**
    $g(K_n) = \binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{24}$.

3.  **Ratio $R(K_n) = g(K_n)^3 / f(K_n)^4$:**
    We simplify the ratio:
    $$R(K_n) = \frac{\left(\binom{n}{4}\right)^3}{\left(\binom{n}{3}\right)^4} = \left(\frac{\binom{n}{4}}{\binom{n}{3}}\right)^3 \cdot \frac{1}{\binom{n}{3}}$$
    Since $\frac{\binom{n}{4}}{\binom{n}{3}} = \frac{n-3}{4}$, we have:
    $$R(K_n) = \left(\frac{n-3}{4}\right)^3 \cdot \frac{6}{n(n-1)(n-2)}$$
    $$R(K_n) = \frac{3}{32} \cdot \frac{(n-3)^3}{n(n-1)(n-2)}$$

4.  **Asymptotic Trend ($n \to \infty$):**
    The ratio of the polynomials in $n$ is:
    $$\lim_{n\to\infty} \frac{(n-3)^3}{n(n-1)(n-2)} = \lim_{n\to\infty} \frac{n^3 + O(n^2)}{n^3 + O(n^2)} = 1$$
    Therefore, the limit of the ratio for complete graphs is:
    $$\lim_{n\to\infty} R(K_n) = \frac{3}{32} \cdot 1 = \frac{3}{32}$$
The ratio $R(K_n)$ approaches $3/32$ as $n$ increases.

### [W4, round 1]
Initial Analysis of R(G) = g(G)^3 / f(G)^4:
The ratio favors graphs with a high density of tetrahedra (K4) relative to triangles (K3). Since every K4 contains exactly 4 K3s, the ratio g/f is inherently bounded downwards by 1/4, but we are interested in g^3 / f^4.

Baseline Test (Complete Graphs K_n):
For G = K_n, we have f(K_n) = binom(n, 3) and g(K_n) = binom(n, 4).
The ratio R(K_n) approaches a constant C = (3!)^4 / (4!)^3 = 1296 / 13824 = 1/10.666... as n -> infinity. This suggests the maximum constant 'c' might not be achieved by a single large complete graph.

Candidate Structural Families for Maximizing R(G):
1. Locally Dense, Globally Sparse (Block Graphs/Cliques connected sparsely):
   We should investigate graphs constructed from several large, dense cliques (e.g., K_m) that share very few vertices or edges (e.g., connected only by single bridges or paths of length 1). If we stack K_m's, the count of g(G) increases proportionally to the number of cliques, but f(G) increases much slower (only slightly more than the sum of the individual f(K_m)). This could potentially drive the ratio higher than in a single K_n, provided the overlap is minimized.

2. Quasi-Cliques / Structured Overlap:
   Look for graphs where many K3s share edges, but these K3s do not combine into many K4s. Conversely, look for graphs where the K4s overlap maximally, meaning a single K3 participates in many K4s. The latter scenario (highly overlapping K4s) is generally seen in very dense structures like Turan graphs, but given the $g^3/f^4$ weighting, we need a structure that is efficient at generating $K_4$'s without a proportional boost in $K_3$'s. A key target is finding configurations where $g(G) / f(G)$ is maximized locally across different regions of the graph.

Conclusion for next steps: Focus testing on graphs built by joining several dense components (K_m) with minimal connectivity.

### [W1, round 1]
---
**Task: Compute R(G) = g(G)^3 / f(G)^4 for specific graphs.**
$f(G)$ = number of triangles ($C_3$).
$g(G)$ = number of tetrahedra ($C_4$).

**1. Complete Graph $K_4$ ($n=4$):**
$f(K_4) = \binom{4}{3} = 4$.
$g(K_4) = \binom{4}{4} = 1$.
$R(K_4) = 1^3 / 4^4 = 1 / 256$.

**2. Complete Graph $K_5$ ($n=5$):**
$f(K_5) = \binom{5}{3} = 10$.
$g(K_5) = \binom{5}{4} = 5$.
$R(K_5) = 5^3 / 10^4 = 125 / 10000 = 1 / 80$.

**3. Complete Graph $K_6$ ($n=6$):**
$f(K_6) = \binom{6}{3} = 20$.
$g(K_6) = \binom{6}{4} = 15$.
$R(K_6) = 15^3 / 20^4 = 3375 / 160000$.
Simplifying the fraction: $3375/160000 = 135/6400 = 27/1280$.

**4. Cycle Graph $C_5$ ($n=5$):**
$C_5$ is triangle-free, so $f(C_5) = 0$.
$C_5$ contains no cycles of length 4, so $g(C_5) = 0$.
$R(C_5) = 0^3 / 0^4$, which is indeterminate (0/0).

Note on the problem context: If we considered a graph like $C_4$, $f(C_4)=0$ but $g(C_4)=1$, leading to $R(C_4) = \infty$. This suggests that a finite constant $c$ might not exist for *every* graph $G$. However, the computation for the required graphs is complete.
---

### [W1, round 2]
### [W1, round 2] Verification Steps Completed

**Verification 1: Checking $R(K_n)$ against $c=3/32$**
We verified the ratio $R(G) = g(G)^3 / f(G)^4$ for $K_4, K_5, K_6$ against the proposed limit $c=3/32$.
1. $R(K_4) = 1/256$. Since $1/256 \approx 0.0039$ and $3/32 = 0.09375$, $R(K_4) \le 3/32$. (Confirmed)
2. $R(K_5) = 1/80$. Since $1/80 = 0.0125$ and $3/32 = 0.09375$, $R(K_5) \le 3/32$. (Confirmed)
3. $R(K_6) = 27/1280$. Since $27/1280 \approx 0.0211$ and $3/32 = 0.09375$, $R(K_6) \le 3/32$. (Confirmed)

**Verification 2: Handling $f(G)=0$**
Since a tetrahedron ($K_4$) must contain 4 triangles ($K_3$'s), if $f(G)=0$, then $g(G)$ must also be 0. In this case, the ratio is $0^3/0^4$. To satisfy the bounding condition $R(G) \le c$, we only need to consider graphs where $f(G)>0$. This step is confirmed.

### [W4, round 2]
### [W4, round 2] - Test Case: Two Cliques Joined at a Vertex ($G'$)

**Construction:** $G'$ consists of two cliques $K_m^{(1)}$ and $K_m^{(2)}$ sharing exactly one vertex $v$.

**Formulae:**
$f(G') = 2 \binom{m}{3}$
$g(G') = 2 \binom{m}{4}$
$R(G') = \frac{g(G')^3}{f(G')^4}$

**Case m=5:**
$f(G') = 2 \binom{5}{3} = 20$.
$g(G') = 2 \binom{5}{4} = 10$.
$R(G') = \frac{10^3}{20^4} = \frac{1000}{160000} = \frac{1}{160} = 0.00625$.
Comparison to $3/32 \approx 0.09375$: $R(G')$ is significantly smaller.

**Case m=6:**
$f(G') = 2 \binom{6}{3} = 40$.
$g(G') = 2 \binom{6}{4} = 30$.
$R(G') = \frac{30^3}{40^4} = \frac{27000}{2560000} = \frac{27}{2560} \approx 0.01055$.
Comparison to $3/32 \approx 0.09375$: $R(G')$ is significantly smaller.

**Conclusion:** This block structure does not appear to maximize the ratio $R(G)$. The results confirm the strong candidate nature of the asymptotic limit derived from a single large complete graph $K_n$.

### [W2, round 2]
Theoretical Argument for Supremum C:
The conjecture R(G) <= R(K_n) is proven for any graph G containing at least one triangle (f(G) > 0). Since counting subgraphs is monotonic, for a graph G on n vertices, we have g(G) <= g(K_n) and f(G) <= f(K_n).
Therefore, R(G) = g(G)^3 / f(G)^4 <= g(K_n)^3 / f(G)^4. Since f(G) <= f(K_n), we have 1/f(G)^4 <= 1/f(K_n)^4.
Combining these bounds yields R(G) <= R(K_n).
Since the limit of R(K_n) as n -> infinity is 3/32, and R(K_n) approaches this value asymptotically (and remains bounded by it), the least constant c must be 3/32. This confirms that the complete graph family provides the maximum ratio, and the theoretical supremum is 3/32.
(Note: Graphs where f(G)=0 result in R(G)=0/0, which is indeterminate, but if we take limits or require a non-zero f(G), the result holds.)
