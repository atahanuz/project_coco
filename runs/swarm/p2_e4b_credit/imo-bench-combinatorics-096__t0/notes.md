### [W2, round 1]
Theoretical research on minimum edges E(N, D=3):
1. General Connectivity: Since the graph must be connected, $E \ge N-1$.
2. Diameter Constraint (D=3): Achieving a small diameter like D=3 requires significant connectivity relative to a tree structure. While a precise minimum bound E_min(N, 3) is complex, it must be significantly higher than N-1 for large N.
3. Degree Constraint ($\Delta \le 100$): This constraint limits the total possible number of vertices N for a given D. The Moore bound for D=3 and Delta=100 gives $N_{max} = 1 + \Delta + \Delta(\Delta-1) = 10001$. Since N=1875 is much less than 10001, the $\Delta \le 100$ constraint is *not* the limiting factor preventing the graph from existing, but it *is* a binding constraint that dictates the maximum possible edges ($E_{max} = N\Delta/2$).
4. Lower Bound Approach: To minimize E while maintaining D=3, we typically look for constructions that minimize the average degree while ensuring that every pair of nodes is within 3 steps. This suggests that the lower bound on E will be related to finding an optimal sparse structure, often approaching bounds related to diameter-preserving graphs, which typically require $E = \Omega(N \cdot f(D))$, where $f(D)$ grows with $D$.

Next Step: Attempting to find a more refined lower bound on E(N, 3) given N=1875.

### [W1, round 1]
Investigation of Small Graph Examples (N=10, 20, 50):
The star graph $K_{1, N-1}$ satisfies all given constraints ($D=2 \le 3$, $\delta=1$, and $\Delta = N-1$). Since $E=N-1$ is the minimum number of edges required for any connected graph (which this must be to have a finite diameter), the star graph provides the minimum E for these small cases, provided $\Delta \le 100$.

Results recorded:
N=10: E=9, Delta=9. Valid.
N=20: E=19, Delta=19. Valid.
N=50: E=49, Delta=49. Valid.

Scaling Trend:
For $N \le 101$, the minimum number of edges achieved is $E = N-1$, scaling linearly with $N$.

Note for N=1875: The optimal structure would be $E=N-1$ (Star Graph), but since $N-1 = 1874 > 100$, this structure fails the $\Delta \le 100$ constraint. A larger, more complex structure will be required for $N=1875$ to keep the diameter low while limiting the maximum degree.

### [W3, round 1]
The problem requires minimizing edges (E) for N=1875 with Delta <= 100 and Diameter <= 3. We used a hub-and-spoke construction requiring the hubs to form a clique ($K_k$) to ensure D<=2. We found the minimum number of hubs required was k=25. This configuration has 300 Hub-Hub edges (K_25) and 1850 Hub-Leaf edges, resulting in a total minimum of E = 2150. This construction satisfies all constraints, including having 1850 vertices of degree 1.

### [W4, round 1]
Lower bound derivation for minimum edges E:
1. The diameter constraint D <= 3 requires the graph to be highly dense relative to its size N=1875.
2. To maintain a small diameter D, the graph must possess a minimum required average degree, $\bar{d}$. This requirement is related to the generalized Moore bound.
3. We checked the smallest integer degree $d$ such that the maximum number of vertices $N_{max}$ achievable with diameter 3 is at least 1875.
$N_{max}(d, 3) = 1 + d + d(d-1) + d(d-1)^2$.
For $d=12$, $N_{max} = 1597 < 1875$.
For $d=13$, $N_{max} = 2042 \ge 1875$.
4. Therefore, the average degree $\bar{d}$ must be at least 13.
5. Using $2E = \sum \deg(v) \ge N \cdot \bar{d}$, we derive the lower bound: $2E \ge 1875 \times 13 = 24375$.
$E \ge 12187.5$. Since E must be an integer, $E_{min} \ge 12188$.
6. The constraints $\Delta \le 100$ and $\exists v, \deg(v)=1$ are compatible with this minimum density, as $13 \le 100$.
