### [W1, round 1]
Calculations for graphs on n=11 vertices, where edge label is $|\deg(u) - \deg(v)|$:

1. Complete Graph $K_{11}$:
   - All degrees are 10.
   - All edge labels are $|10 - 10| = 0$.
   - Sum of edge labels = 0.

2. Path Graph $P_{11}$:
   - Two endpoints have degree 1. Nine internal vertices have degree 2.
   - The two edges connected to the degree-1 vertices contribute $|1-2|=1$ each.
   - Sum of edge labels = 2.

3. Cycle Graph $C_{11}$:
   - All degrees are 2.
   - All edge labels are $|2 - 2| = 0$.
   - Sum of edge labels = 0.

4. Star Graph $S_{11}$:
   - One center vertex has degree 10. Ten leaves have degree 1.
   - There are 10 edges, each connecting the center (10) to a leaf (1).
   - Each edge label is $|10 - 1| = 9$.
   - Sum of edge labels = 10 * 9 = 90.

Observed Pattern:
Graphs where all vertices have the same degree (regular graphs, like $K_{11}$ and $C_{11}$) result in a total sum of 0. Highly irregular graphs, like the star graph, result in the largest sums.

### [W4, round 1]
ANALYSIS OF SUM S:
The sum S is defined as S = sum_{ (u,v) in E } |deg(u) - deg(v)|.
We partition the vertex set V into V_k, where V_k contains all vertices with degree k.
An edge (u, v) between V_k and V_j contributes |k - j| to S.

To maximize S, we require:
1. Edges must preferentially connect sets V_k and V_j where |k - j| is large.
2. Edges connecting vertices within the same set (k=j) contribute 0 and should be minimized, especially in the construction of the graph.

If we let E_{k, j} be the number of edges between V_k and V_j (with k <= j), then:
S = sum_{k <= j} (j - k) * E_{k, j}

Necessary Condition for Maximization: The degree sequence must concentrate vertices at the extreme ends of the possible degree range (0 to 10 for N=11) to maximize the possible differences (j - k).

Next step: Investigate concrete, extremal degree sequences (e.g., sequences with many 0s and many 10s) that are graphic and calculate the resulting S.

### [W4, round 1]
ADVANCEMENT:
We tested the complete bipartite graph $K_{a, b}$ for $N=11$.
The maximum S found in this family is $S=126$, achieved by $K_{2, 9}$.
In $K_{2, 9}$, the degrees are partitioned into $V_2$ (size 9) and $V_9$ (size 2). All 18 edges contribute $|9-2|=7$ to the sum, resulting in $18 \times 7 = 126$.

This suggests the optimal graph likely maximizes the edges between two well-separated degree sets. The next task is to investigate whether a non-bipartite graph structure could achieve a higher S by utilizing more complex degree distributions or by having internal edges that somehow contribute positively (though edges within the same $V_k$ contribute 0, mixing degrees might help overall). We should check if a slight perturbation of the $K_{2, 9}$ structure can increase $S$.

### [W2, round 1]
# Analysis of Maximum Edge Label Sum (S)
**Goal:** Find the theoretical upper bound for $S = \sum_{e=\{u, v\} \in E} |d_u - d_v|$ for a simple graph $G$ with $n=11$ vertices.

**1. Dependence on Degrees and Edges:**
The sum $S$ is fundamentally determined by the degree sequence $\{d_1, \dots, d_n\}$ and the specific configuration of edges $E$. To maximize $S$, edges must preferentially connect vertices whose degrees are maximally separated.

**2. Seeking the Upper Bound (Maximization Strategy):**
We seek $\max_{G} S(G)$. To maximize the sum of differences, we must maximize the disparity between the degrees present in the graph. The maximal possible degree difference is $(n-1) - 0 = 10$.

A configuration that maximizes degree disparity while allowing for many edges is the Star Graph, $K_{1, n-1}$.

**3. Bound Derived from $K_{1, n-1}$:**
Let $G = K_{1, n-1}$. It has a central vertex $v_C$ with degree $d_C = n-1$, and $n-1$ leaf vertices $v_L$ with degree $d_L = 1$.
The number of edges is $|E| = n-1$.
Every edge connects $v_C$ and a $v_L$. The label for every edge is:
$L(e) = |d_C - d_L| = |(n-1) - 1| = n-2$.
The total sum $S$ is:
$S = |E| \times (n-2) = (n-1)(n-2)$.

**4. Result for n=11:**
Setting $n=11$:
$S \le (11-1)(11-2) = 10 \times 9 = 90$.

This derived value, 90, serves as a strong candidate for the theoretical upper bound, as the star graph provides the configuration with the highest degree contrast across the maximum possible number of edges connecting the extreme degrees. We conjecture that $S_{max} = (n-1)(n-2)$.

### [W3, round 1]
Maximum sum S is achieved by concentrating degrees at two levels: a small set of high-degree vertices (V_H) and a large set of low-degree vertices (V_L).

We tested $K_{k, 11-k}$ structures and found that $K_{2, 9}$ yields $S = 2 \cdot 9 \cdot |2-9| = 126$.
By adding an edge within the high-degree partition $V_H=\{v_1, v_2\}$ (assuming $k=2$), the degrees become $d_1=10, d_2=10$, while $d_{3..11}=2$.
The resulting graph structure $G = K_{2, 9} + (v_1, v_2)$ gives:
1. 9 edges between $v_1$ and $V_L$, label $|10-2|=8$. Sum = 72.
2. 9 edges between $v_2$ and $V_L$, label $|10-2|=8$. Sum = 72.
3. 1 edge $(v_1, v_2)$, label $|10-10|=0$. Sum = 0.
Total S = 72 + 72 + 0 = 144.

This structure (G = K_{2, 9} plus one internal edge) provides a strong candidate for the maximal sum S.

### [W1, round 2]
### [W1, Round 2] Formal Summary of Construction $G = K_{2, 9} + e$

W3 proposed a construction $G$ on $N=11$ vertices by starting with the complete bipartite graph $K_{2, 9}$ and adding a single edge $e$ between the two vertices in the smaller partition. This construction ensures the graph remains simple.

**Graph Structure and Degrees:**
Let $V$ be the vertex set. We partition $V$ into $V_H$ (size 2) and $V_L$ (size 9).
1. **Initial State ($K_{2, 9}$):**
   - Vertices in $V_H$ (say $v_1, v_2$) have degree $d(v_i) = 9$.
   - Vertices in $V_L$ have degree $d(u_j) = 2$.
2. **Final State ($G = K_{2, 9} + (v_1, v_2)$):**
   - The added edge $e=(v_1, v_2)$ increases the degrees of $v_1$ and $v_2$.
   - $d(v_1) = 9 + 1 = 10$.
   - $d(v_2) = 9 + 1 = 10$.
   - $d(u_j) = 2$ (degrees in $V_L$ are unchanged).

**Edge Accounting and Sum Calculation (S):**
The edges of $G$ are accounted for in three sets:

1. **Edges between $V_H$ and $V_L$ ($E_{H, L}$):** There are $2 \times 9 = 18$ such edges.
   - For edges incident to $v_1$: There are 9 edges. Label $L = |10 - 2| = 8$. Contribution: $9 \times 8 = 72$.
   - For edges incident to $v_2$: There are 9 edges. Label $L = |10 - 2| = 8$. Contribution: $9 \times 8 = 72$.
   - Total from $E_{H, L}$: $72 + 72 = 144$.

2. **Edge within $V_H$ ($E_{H, H}$):** There is 1 edge, $e=(v_1, v_2)$.
   - Label $L = |10 - 10| = 0$. Contribution: $1 \times 0 = 0$.

**Total Sum:**
The total sum of the edge labels is $S = 144 + 0 = 144$. This confirms W3's derivation.

### [W4, round 2]
### [W4, round 2]
ANALYSIS OF THREE-CLUSTER DISTRIBUTION:
The maximum sum $S=144$ was achieved by concentrating degrees into exactly two levels: $V_{10}$ (size 2) and $V_2$ (size 9). This structure maximized the overall degree disparity while maintaining a high number of edges between the extremal sets.

Hypothesis: To maximize $S$, the degree sequence must remain highly concentrated at the extreme values (high and low). Introducing a third degree level ($d_m$, where $2 < d_m < 10$) risks reducing the average magnitude of the differences $|d_i - d_j|$ across the existing high-contributing edges, or forcing the graph to have fewer edges connecting the true extremes.

To test this, consider partitioning $N=11$ vertices into $n_L, n_M, n_H$ clusters with degrees $d_L, d_M, d_H$. If we assume a configuration similar to the $S=144$ case (where most edges are inter-cluster), $S$ is proportional to the sum of products $n_i n_j |d_i - d_j|$.

A three-cluster structure is unlikely to beat the current optimum unless the structure can dramatically increase the number of edges while maintaining large differences. Given the successful perturbation of the bipartite graph to increase $S$, the current two-cluster structure is highly optimized for edge count vs. degree difference tradeoff.

Further investigation would require searching over all graphic partitions of 11 vertices into three clusters, which is computationally complex. We currently maintain the conjecture that the maximal configuration is likely limited to two degree clusters.

### [W3, round 2]
### [W3, round 2]
**Systematic Search using $G = K_{k, N-k} + K_k$ construction:**
To systematically test the required modifications, we considered graphs where $k$ vertices ($V_H$) form a clique ($K_k$) and are fully connected to $N-k$ vertices ($V_L$), which form an independent set. This structure ensures the high-degree vertices $d_H$ reach $N-1=10$, while low-degree vertices $d_L$ remain equal to $k$.

The total sum of labels $S$ for this structure is:
$S = |E_{H, L}| \times |d_H - d_L| = k(N-k) \times ((N-1) - k)$.
For $N=11$, $S(k) = k(11-k)(10-k)$.

Testing values of $k$:
*   $k=2$: $S(2) = 2(9)(8) = 144$. (Matches previous result).
*   $k=3$: $S(3) = 3(8)(7) = 168$.
*   $k=4$: $S(4) = 4(7)(6) = 168$.
*   $k=5$: $S(5) = 5(6)(5) = 150$.

The maximum value found is $S=168$, achieved when $k=3$ or $k=4$.
The corresponding degree sequence for $k=3$ is $\{10, 10, 10, 3^8\}$.
The corresponding degree sequence for $k=4$ is $\{10, 10, 10, 10, 4^7\}$.

This construction provides a clear candidate for the maximum sum. We conclude that 168 is the best result found under this powerful family of extremal graphs.

### [W2, round 2]
The maximum sum S is achieved by constructing a graph G where the vertex set V is partitioned into V_H (|V_H|=k) and V_L (|V_L|=n-k). We maximize S by ensuring V_H is a clique (K_k) and all edges between V_H and V_L exist (K_{k, n-k}).
For n=11, the maximum sum is found by analyzing S = k(n-k) * |(n-1) - k|.
Testing k=3 and k=4 yields the maximum value S = 168.
For k=3, we have 3 high-degree vertices (d=10) and 8 low-degree vertices (d=3). There are 24 edges contributing |10-3|=7 each, resulting in S = 24 * 7 = 168.
This construction establishes a strong upper bound candidate.
