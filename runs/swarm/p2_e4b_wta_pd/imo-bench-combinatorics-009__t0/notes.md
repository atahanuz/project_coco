### [W4, round 1]
# Analysis of Maximizing $M$ (Non-edges with Common Neighbors)

**1. Matrix Formulation:**
Let $N=456$ be the number of participants. $A$ is the $N \times N$ adjacency matrix of the friendship graph, where $A_{uv} = 1$ if $u$ and $v$ are friends, and $0$ otherwise. $A$ is symmetric with zeros on the diagonal.
The number of common neighbors between participants $u$ and $v$ is given by the $(u, v)$-entry of $A^2$, i.e., $(A^2)_{uv} = \sum_{w=1}^N A_{uw} A_{wv}$.

The quantity $M$ to be maximized is the count of pairs $\{u, v\}$ that are not friends ($A_{uv}=0, u \neq v$) but share at least one common friend ($(A^2)_{uv} > 0$).

Mathematically, $M = \sum_{u < v} \mathbb{I}(A_{uv} = 0 \text{ and } (A^2)_{uv} \ge 1)$, where $\mathbb{I}(\cdot)$ is the indicator function.

**2. Theoretical Strategy Development:**
Maximizing $M$ requires maximizing the presence of triangles (paths of length 2 between non-adjacent nodes) while ensuring the graph $G$ is not complete ($K_N$) and not too sparse.

*   **Observation:** $M$ is maximized when the graph is "locally dense" relative to its global structure. If the graph is too sparse (e.g., few edges), $A^2$ will have few non-zero entries, resulting in low $M$. If the graph is too dense (e.g., close to $K_N$), the number of non-edges is small, restricting $M$.
*   **Candidate Structures (Focus on Graph Properties):**
    1. **Regularity:** Highly regular graphs (where every vertex has the same degree $k$) often maximize structural counts like this because they distribute local connectivity evenly across all pairs.
    2. **Strongly Regular Graphs (SRG):** If $N$ allowed for an SRG, this structure would be a strong candidate. An SRG is defined by parameters $(N, k, \lambda, \mu)$, where $\lambda$ is the number of common neighbors of two adjacent vertices, and $\mu$ is the number of common neighbors of two non-adjacent vertices. Maximizing $M$ is strongly related to maximizing $\mu$ across all non-edges.
    3. **Cliques and Independent Sets:** Strategically placing missing edges within large cliques or carefully separating large independent sets (anti-cliques) could concentrate the opportunities for common neighbors, but this must be balanced against the need for overall connectivity.

**3. Maximization Principle:**
The strategy must focus on constructing a graph $G$ such that the number of pairs $\{u, v\}$ where $A_{uv}=0$ is high, but the "connectivity deficit" of these pairs (i.e., $A^2_{uv}$) is maximal. This implies that the graph should resemble a complete graph locally, even if it is sparse globally.

*Hypothesis: The maximum value of $M$ will likely be achieved by a graph structure that closely approximates a balanced or highly symmetric regular graph, provided $N=456$ allows for such a structure.*

### [W3, round 1]
### Analysis of Graph Constructions for N=456

The problem asks for the maximum number $M$ of pairs $\{u, v\}$ such that $u$ and $v$ are not adjacent (not friends) but share a common neighbor (common friend).

**1. Path Graph $P_{456}$**
In $P_{456}$, two vertices $u$ and $v$ share a common neighbor if and only if the distance $d(u, v) = 2$.
The pairs at distance 2 are $\{i, i+2\}$ for $1 \le i \le 454$.
$M(P_{456}) = N - 2 = 456 - 2 = 454$.

**2. Cycle Graph $C_{456}$**
In $C_{456}$, two non-adjacent vertices share a common neighbor if and only if their distance $d(u, v) = 2$.
There are $N$ such pairs (e.g., $\{i, i+2 \pmod{456}\}$).
$M(C_{456}) = N = 456$.

**3. Complete Bipartite Graph $K_{a, b}$ where $a+b=456$**
Let $V = A \cup B$, with $|A|=a$ and $|B|=b$. Non-adjacent pairs must belong to the same partition set (either $A$ or $B$).
- Pairs in $A$: $\binom{a}{2}$. Since all nodes in $B$ are neighbors of all nodes in $A$, any pair in $A$ has $b$ common friends.
- Pairs in $B$: $\binom{b}{2}$. Similarly, any pair in $B$ has $a$ common friends.
Total $M(K_{a, b}) = \binom{a}{2} + \binom{b}{2}$.
To maximize this quantity subject to $a+b=456$, we must make $a$ and $b$ as unbalanced as possible.
Let $a=1$ and $b=455$.
$M(K_{1, 455}) = \binom{1}{2} + \binom{455}{2} = 0 + \frac{455 \times 454}{2} = 455 \times 227 = 103285$.

**Conclusion so far:**
The maximum value found among these constructions is $M = 103285$, achieved by the star graph $K_{1, 455}$. We should further investigate highly regular graphs or other structures if a larger value is expected, but this construction provides a large baseline result.

### [W1, round 1]
Analysis of the maximum number of non-friend pairs with a common friend (M) for small N:
N=4: Max M = 4
N=5: Max M = 9
N=6: Max M = 18

The maximum M for N=6 is achieved by the complete bipartite graph $K_{3,3}$.
The vertex set V is partitioned into two independent sets, $V_1$ and $V_2$, each of size 3.
Let $V_1 = \{0, 1, 2\}$ and $V_2 = \{3, 4, 5\}$. Edges exist only between a vertex in $V_1$ and a vertex in $V_2$.
There are $\binom{3}{2} + \binom{3}{2} = 6$ pairs of non-friends (all pairs within $V_1$ or $V_2$).
For any such non-friend pair $\{u, v\}$, they share all 3 vertices of the opposite partition as common friends.
Total M = (3 pairs in $V_1$) * 3 + (3 pairs in $V_2$) * 3 = 9 + 9 = 18.

### [W2, round 1]
**Problem Analysis: Max Non-Edges with Common Neighbors (M)**

1.  **Graph Translation:** Let $G=(V, E)$ be the friendship graph, where $N=|V|=456$. $M$ is the number of non-edges $\{u, v\} \notin E$ such that there exists a vertex $w$ connected to both $u$ and $v$. In terms of the adjacency matrix $A$, $M = |\{(u, v) : u < v, A_{uv} = 0, (A^2)_{uv} \ge 1\}|$.

2.  **Relationship to Density:** To maximize $M$, we need two properties:
    a) A large number of non-edges (low overall density, $|E|$).
    b) The non-edges must be positioned such that they have many common neighbors (high local clustering around non-edges).

3.  **Extremal Structure Candidate:** Structures that maximize non-edges while maintaining high common neighbor counts often involve bipartite graphs. Consider a complete bipartite graph $G = K_{\lfloor N/2 \rfloor, \lceil N/2 \rceil}$. Let $N_1 = \lfloor N/2 \rfloor$ and $N_2 = \lceil N/2 \rceil$.

4.  **Analysis of $K_{N_1, N_2}$:**
    *   The non-edges occur exclusively within the two partitions $V_1$ and $V_2$.
    *   Consider any pair $\{u, v\} \subset V_1$. They are not friends ($A_{uv}=0$). Since $G$ is complete bipartite, $u$ and $v$ are both connected to *every* vertex in $V_2$.
    *   The number of common neighbors for $\{u, v\} \subset V_1$ is $N_2 = \lceil N/2 \rceil$. Since $N \ge 2$, this is $\ge 1$.
    *   Thus, every non-edge in $K_{N_1, N_2}$ contributes to $M$.

5.  **Calculating $M$ for $K_{N_1, N_2}$:**
    *   The number of non-edges $M$ is the sum of pairs within $V_1$ and pairs within $V_2$:
        $M = \binom{N_1}{2} + \binom{N_2}{2}$.

6.  **Deriving the Upper Bound:** For $N=2k$ (even), $N_1=N_2=k=N/2$.
    $M = 2 \binom{N/2}{2} = 2 \cdot \frac{(N/2)(N/2 - 1)}{2} = \frac{N}{2}\left(\frac{N}{2} - 1\right) = \frac{N^2}{4} - \frac{N}{2} = \frac{N(N-2)}{4}$.

    For $N=2k+1$ (odd), $N_1=k, N_2=k+1$.
    $M = \binom{k}{2} + \binom{k+1}{2} = \frac{k(k-1)}{2} + \frac{(k+1)k}{2} = \frac{k}{2} (k-1 + k+1) = k^2$.
    Since $k = (N-1)/2$, $M = \left(\frac{N-1}{2}\right)^2 = \frac{(N-1)^2}{4}$.

7.  **Conclusion for Upper Bound:** Both cases are approximated by $N^2/4$. The maximum value achieved is $M_{max} = \lfloor N^2/4 \rfloor - \lfloor N/2 \rfloor + 1$ (or simply $\binom{\lfloor N/2 \rfloor}{2} + \binom{\lceil N/2 \rceil}{2}$ which is the precise bound). This bound is related to the density of the graph being $1/2$ (the complete bipartite graph has density $1/2$), which provides the best trade-off between edge sparsity (maximizing non-edges) and structural common neighbors.
