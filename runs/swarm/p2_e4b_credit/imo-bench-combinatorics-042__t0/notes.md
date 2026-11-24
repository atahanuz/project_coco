### [W4, round 1]
The number of weak quartets, $W$, in a graph $G=(V, E)$ is calculated by summing over every edge $(u, v) \in E$ the number of pairs of non-adjacent vertices $\{w, z\}$ that are not connected to $u$ or $v$.

1. **Define the auxiliary set $R_{u,v}$**: For a given edge $(u, v)$, $R_{u,v}$ is the set of vertices that are not $u$, not $v$, and are not neighbors of $u$ or $v$.
$$R_{u,v} = V \setminus (\{u, v\} \cup N(u) \cup N(v))$$

2. **Size of $R_{u,v}$**: Let $d(x)$ be the degree of vertex $x$, and $C(u, v) = |N(u) \cap N(v)|$ be the number of common neighbors of $u$ and $v$. The size of $R_{u,v}$ is:
$$|R_{u,v}| = N - 2 - d(u) - d(v) + C(u, v)$$

3. **Counting Weak Quartets containing $(u, v)$**: A pair $\{w, z\} \subset R_{u,v}$ forms a weak quartet with $(u, v)$ if and only if $(w, z)$ is *not* an edge.
Let $E(G[R_{u,v}])$ be the number of edges induced by $R_{u,v}$. The number of such non-edges is:
$$W_{(u, v)} = \binom{|R_{u,v}|}{2} - E(G[R_{u,v}])$$

4. **Total Count**: The total number of weak quartets $W$ is the sum over all edges:
$$W = \sum_{(u, v) \in E} \left( \binom{N - 2 - d(u) - d(v) + C(u, v)}{2} - E(G[R_{u,v}]) \right)$$

This expression relates $W$ to vertex degrees ($d(u), d(v)$), common neighbors ($C(u, v)$), and the internal density of the remainder set $R_{u,v}$ ($E(G[R_{u,v}])$).

### [W3, round 1]
Exploratory search for maximum weak quartets (exactly one edge in a set of 4 vertices, N=120).

1. Star Graph K_{1, 119}: Found 0 weak quartets, as any quartet containing the center has 2 or 3 edges, and quartets of leaves have 0 edges.
2. Complete Bipartite Graphs K_{a, b}: Found 0 weak quartets, as induced subgraphs on 4 vertices consistently yield 0, 3, or 4 edges.

3. Perfect Matching M: Let G be a perfect matching (60 edges). Any quartet Q must either contain 0 edges or 1 edge (since G is a matching). If Q contains exactly one edge {u, v}, since all other vertices V' = V \ {u, v} are isolated from {u, v} and from each other, Q is a weak quartet.
Number of weak quartets W = (Number of edges) * C(N-2, 2).
W = 60 * C(118, 2) = 60 * (118 * 117 / 2) = 30 * 13806 = 414180.
This serves as a strong candidate for the maximum.

### [W2, round 1]
Derivation of Upper Bound for Weak Quartets (N vertices):

1. Definition: A weak quartet is a set of 4 vertices $\{v_1, v_2, v_3, v_4\}$ inducing exactly 1 edge.
2. Counting via Edges: We count the total number of weak quartets $W(G)$ by summing over all edges $e=\{u, v\} \in E$ that might be the unique edge in the quartet.
3. Construction: If $\{u, v\}$ is the unique edge, the remaining two vertices, $x$ and $y$, must satisfy:
    a) $x, y \notin \{u, v\}$.
    b) $x$ and $y$ are not adjacent to $u$ or $v$.
    c) $x$ and $y$ are not adjacent to each other.
4. Identifying the Candidate Pool: Let $A_{u, v}$ be the set of vertices that are non-neighbors of both $u$ and $v$, excluding $u$ and $v$: $A_{u, v} = V \setminus (N(u) \cup N(v) \cup \{u, v\})$.
5. Counting Contribution of $e$: The number of weak quartets containing $e$ is the number of non-edges in the induced subgraph $G[A_{u, v}]$, which is at most $\binom{|A_{u, v}|}{2}$.
6. Upper Bound on $|A_{u, v}|$: To find a general upper bound, we maximize $|A_{u, v}|$. This occurs when $d_u$ and $d_v$ are minimized (assuming $N \geq 4$). The minimum degree is at least 0. If $d_u=1$ and $d_v=1$ (and their neighbors are distinct), $|N(u) \cup N(v)| = 2$. Thus, $|A_{u, v}| \leq N - 2 - 2 = N - 4$.
7. General Bound: Summing the maximum possible contribution over all $E$ edges yields the general upper bound:
$$W(G) \leq E \cdot \binom{N-4}{2}$$

Applying to N=120:
$$W(G) \leq E \cdot \binom{116}{2} = E \cdot \frac{116 \times 115}{2} = 6670 E$$

### [W1, round 1]
Investigating weak quartets (subgraphs on 4 vertices with exactly 1 edge).

N=4: Max weak quartets = 1. Achieved by a graph with 1 edge (e.g., K2 + 2 isolated vertices).
N=5: Max weak quartets = 3. Achieved by a graph with 1 edge (e.g., K2 + 3 isolated vertices).
N=6: Max weak quartets = 6. Achieved by a graph with 1 edge (e.g., K2 + 4 isolated vertices).
N=8: Max weak quartets = 28. Achieved by a graph with 2 disjoint edges (e.g., 2K2 + 4 isolated vertices).

### [W1, round 2]
### W1 Investigation Summary: Density vs. Sparsity

The task requires investigating if slightly higher density than a perfect matching ($M$) can maximize the number of weak quartets ($W$).

1. **Baseline (Perfect Matching M):** For $N=120$, $E=60$. For any edge $(u, v)$, the residual set $|R_{u,v}| = N - 4 = 116$, and $E(G[R_{u,v}])=0$.
$$W_M = 60 \cdot \binom{116}{2} = 60 \cdot 6670 = 400,200$$

2. **Perturbed Structure (E=61):** Consider taking $M$ and adding a single edge $(u, w)$ where $u$ and $w$ were matched to different partners ($u'$ and $w'$ respectively).
    *   New edge $(u, w)$: $d(u)=2, d(w)=2, C(u, w)=0$. $|R_{u,w}| = 120 - 6 = 114$. Contribution: $\binom{114}{2} = 6441$.
    *   Old edge $(u, u')$: $d(u)=2, d(u')=1, C(u, u')=0$. $|R_{u,u'}| = 115$. Contribution: $\binom{115}{2} = 6555$.
    *   The 59 other edges remain untouched, contributing $59 \cdot 6670 = 393,430$.
    $$W_{G'} = 393,430 + 6555 + 6441 = 406,426$$

**Finding:** A graph with slightly higher density ($E=61$) yielded a greater total number of weak quartets ($406,426 > 400,200$). This suggests that while sparsity is necessary to keep $|R_{u,v}|$ large, a controlled, low-degree increase in density can increase the total count by boosting $E$ faster than it reduces the individual term contributions.

**Next Step:** Investigate the optimal density $E$ and the structure required to maximize $\sum \binom{|R_{u,v}|}{2}$ while minimizing the reduction in $|R_{u,v}|$ across all edges.<|tool_call>call:read_notes{

### [W2, round 2]
### Verification of $|A_{u, v}|$ and Upper Bound

**1. Rigorous Verification of $|A_{u, v}|$**
For an edge $(u, v) \in E$, the set $A_{u, v}$ is defined as $A_{u, v} = V \setminus (N(u) \cup N(v) \cup \{u, v\})$. Since $u$ and $v$ are connected, $u \in N(v)$ and $v \in N(u)$, meaning $\{u, v\} \subset N(u) \cup N(v)$.
Therefore, $N(u) \cup N(v) \cup \{u, v\} = N(u) \cup N(v)$.
By Inclusion-Exclusion: $|N(u) \cup N(v)| = d(u) + d(v) - C(u, v)$.
Thus, the precise size of $A_{u, v}$ is:
$$|A_{u, v}| = N - (d(u) + d(v) - C(u, v))$$
The maximum size occurs when $d(u) + d(v) - C(u, v)$ is minimized, which happens when $d(u)=1, d(v)=1, C(u, v)=0$ (e.g., in a matching). In this case, $|A_{u, v}|_{max} = N - 2$.

**2. Precise Upper Bound for Fixed E**
The number of weak quartets $W$ is bounded by $W \leq \sum_{(u, v) \in E} \binom{|A_{u, v}|}{2}$.
The general upper bound is:
$$W_{UB}(E) = E \cdot \binom{N-2}{2}$$
For $N=120$: $W_{UB}(E) = E \cdot \binom{118}{2} = E \cdot 6903$.

**3. Comparison: Matching vs. Complete Graph**
*   **Perfect Matching ($E=60$):** For any edge, $|A_{u, v}| = 118$. Since all vertices in $A_{u, v}$ are isolated from each other in a matching, $E(G[A_{u,v}])=0$.
    $W_{PM} = 60 \cdot \binom{118}{2} = 60 \cdot 6903 = 414,180$. (This confirms the finding in W3).
*   **Complete Graph ($E=7140$):** For any edge, $d(u)=119, d(v)=119, C(u, v)=118$.
    $|A_{u, v}| = 120 - (119 + 119 - 118) = 0$.
    $W_{K_{120}} = 7140 \cdot \binom{0}{2} = 0$.

The maximum number of weak quartets is strongly achieved when the graph structure is sparse, specifically matching the structure analyzed in the Perfect Matching case.

### [W3, round 2]
### [W3, round 2] Verification of Perfect Matching (M) and Edge Modification Analysis

**1. Verification of Perfect Matching (M):**
For $N=120$ and $E=60$ (perfect matching), the calculation derived in [W3, round 1] is verified to be correct. For any edge $\{u, v\}$, $R_{u,v} = V \setminus \{u, v\}$, so $|R_{u,v}| = N-2 = 118$. Since there are no edges induced by $R_{u,v}$, the contribution of each edge is $\binom{118}{2} = 6903$.
Total $W = 60 \times 6903 = 414,180$.

**2. Analysis of Simple Modification (Adding one edge $e'$):**
We analyzed the effect of adding a single edge $e' = (x, y)$ to $M$, resulting in $G'$ with $E'=61$.
The structure $M$ loses its extremal property, as the contribution of $\{u, v\}$ decreases by 1 ($\binom{118}{2} \to \binom{118}{2} - 1$), while the new edge $e'=(x, y)$ introduces a contribution of $\binom{116}{2} = 6670$.
The total weak quartets in $G'$ is $W(G') = W(M) - 1 + 6670 = 414,180 - 1 + 6670 = 420,849$.
This demonstrates that a simple modification (adding one edge) *increases* the count of weak quartets, meaning the Perfect Matching is likely not the structure that maximizes $W$. The upper bound derived in [W2, round 1], $W(G) \leq E \cdot \binom{N-4}{2}$, suggests maximizing $E$ is beneficial, but the trade-off between high $E$ and low induced internal edges needs further investigation.

### [W4, round 3]
### [W4, round 3] Assistance for W3: Formalizing Summation Complexity (Degree Constraint $d_i \in \{1, 2, 3\}$)

To help W3 model the expected sum complexity for $W = \sum_{(u, v) \in E} \left( \binom{|R_{u,v}|}{2} - E(G[R_{u,v}]) \right)$, we formalize the dependencies based on the vertex degree constraints $d_i \in \{1, 2, 3\}$.

**1. Formalization of $|R_{u,v}|$:**
The size of the residual set is defined as:
$$|R_{u,v}| = N - 2 - d(u) - d(v) + C(u, v)$$
where $N=120$ and $C(u, v) = |N(u) \cap N(v)|$.

**2. Bounds on $|R_{u,v}|$ due to degree constraints:**
Since $d(u), d(v) \in \{1, 2, 3\}$, the sum $d(u) + d(v)$ is bounded in $[2, 6]$.
$C(u, v)$ is bounded in $[0, \min(d(u)-1, d(v)-1)]$.

*   **Minimum $|R_{u,v}|$ (Worst case for the $\binom{\cdot}{2}$ term):** Occurs when $d(u)$ and $d(v)$ are maximal (3, 3) and $C(u, v)$ is maximal (which is 2, as $u$ and $v$ are neighbors).
    $$|R_{u,v}|_{min} = 120 - 2 - 3 - 3 + 2 = 114.$$
*   **Maximum $|R_{u,v}|$ (Best case for the $\binom{\cdot}{2}$ term):** Occurs when $d(u)$ and $d(v)$ are minimal (1, 1) and $C(u, v)$ is minimal (0).
    $$|R_{u,v}|_{max} = 120 - 2 - 1 - 1 + 0 = 116.$$
Thus, the dominant term is bounded by $\binom{114}{2} \le \binom{|R_{u,v}|}{2} \le \binom{116}{2}$.

**3. Complexity Analysis of $E(G[R_{u,v}])$:**
The structure of $G[R_{u,v}]$ is highly dependent on how the remaining vertices connect. However, since $R_{u,v}$ contains no neighbors of $u$ or $v$, these internal edges cannot involve $u$ or $v$.
The maximum complexity of the sum relies on bounding $E(G[R_{u,v}])$. Since $|R_{u,v}| \le 116$, the maximum possible value for $E(G[R_{u,v}])$ is $\binom{116}{2} = 6670$.

**4. Modeling the Expected Sum Complexity:**
The total sum complexity $W$ is driven by two opposing factors:
*   **Positive Driver:** The term $\binom{|R_{u,v}|}{2}$ is large ($\approx 6000$ to $6670$ per edge), meaning the total count $W$ is expected to scale linearly with the number of edges, $E$.
*   **Negative Driver:** The term $E(G[R_{u,v}])$ acts as a reduction factor, subtracting the number of actual edges within the potential pool $R_{u,v}$.

To model the complexity, we assume the worst-case scenario for the total sum, which is when $E(G[R_{u,v}])$ is minimized (i.e., $R_{u,v}$ is an independent set, $E(G[R_{u,v}])=0$). This provides a strong upper bound based on degree constraints:

$$W_{UB}(d_i \le 3) \approx E \cdot \binom{116}{2}$$

If $E$ is constrained (e.g., $E \approx 60$ to maximize sparsity), the complexity is $O(E \cdot N^2)$. If $E$ grows larger while maintaining $d_i \le 3$, the complexity remains $O(E \cdot N^2)$, but the lower bound on $|R_{u,v}|$ (114) will start to restrict the growth faster due to the required density.
This formal structure allows W3 to test edge cases by selecting specific combinations of $(d(u), d(v), C(u, v))$.

### [W2, round 3]
### [W2, round 2] - Refining the Upper Bound under Constraint

The coordinator requested derivation of $W_{UB}$ assuming the constraint $d(u) + d(v) - C(u, v) = 2$ holds for all edges $(u, v) \in E$.

1. **Interpretation of the Constraint:**
The term $d(u) + d(v) - C(u, v)$ is precisely the size of the union of the neighbor sets: $|N(u) \cup N(v)|$.
If $|N(u) \cup N(v)| = 2$, and since $(u, v) \in E$ implies $v \in N(u)$ and $u \in N(v)$, the only way this union can have size 2 is if $N(u) = \{v\}$ and $N(v) = \{u\}$. This means every vertex incident to an edge must have a degree of exactly 1 (relative to that edge being the only neighbor).
If this property must hold for *every* edge in $G$, then $G$ must be a set of disjoint edges, i.e., a matching.

2. **Maximizing E:**
For $N=120$, the maximum number of edges $E$ subject to $G$ being a matching is $E_{max} = N/2 = 60$ (a perfect matching, $M$).

3. **Deriving $W_{UB}$ for the Matching Structure:**
For any edge $(u, v)$ in a perfect matching $M$:
*   $d(u) = 1, d(v) = 1, C(u, v) = 0$.
*   The size of the candidate pool $A_{u, v}$ is $|A_{u, v}| = N - (1 + 1 - 0) = N - 2 = 118$.
*   $A_{u, v} = V \setminus \{u, v\}$. Since $M$ is a perfect matching, $V \setminus \{u, v\}$ consists of 59 other disjoint edges. There are no edges induced by $A_{u, v}$. Thus, $E(G[A_{u,v}]) = 0$.
*   The contribution of each edge is $W_{(u, v)} = \binom{118}{2} - 0 = 6903$.

The tightest theoretical upper bound $W_{UB}$ under this constraint is achieved by the perfect matching:
$$W_{UB} = E_{max} \cdot \binom{N-2}{2} = 60 \cdot \binom{118}{2} = 60 \cdot 6903 = 414,180.$$

### [W3, round 3]
W3 Analysis of Trade-off (E=60 to E=61):
1. Baseline $W(E=60)$ (Perfect Matching): $414,180$.
2. Observed $W(E=61)$: $420,849$.
3. Marginal Gain: $\Delta W = 6669$.
4. The marginal gain is positive, indicating that the gain from increasing the count of edges $E$ outweighs the marginal loss due to the reduction in the residual set size $|R_{u,v}|$ at this density.
5. This suggests that the optimal density $E_{opt}$ is greater than 61. However, since the contribution $\binom{|R_{u,v}|}{2}$ is quadratic in $|R_{u,v}|$, and $|R_{u,v}|$ decreases linearly with the average degree $\bar{d} \propto E$, the positive marginal gain must eventually diminish and become negative.
6. Based on the initial strong positive trend, $E_{opt}$ is likely slightly higher than 61, but the structure required to maximize $W$ will involve careful management of degrees to minimize induced edges $E(G[R_{u,v}])$.

### [W1, round 3]
### [W1, round 3] Systematic Investigation of Sparse Structures (Adding disjoint edges to M)

We are investigating the trade-off between increasing the number of edges $E$ and maintaining a large residual set size $|R_{u,v}|$, starting from the Perfect Matching $M$ ($E=60, W=414,180$). We analyze structures $G_k = M \cup E'$, where $E'$ consists of $k$ disjoint edges, such that all edges in $E'$ introduce only degree-2 vertices (where $k$ is the number of added edges).

The general calculation for $G_k$ ($E=60+k$):
$W_{G_k} = (60-2k) \cdot \binom{N-2}{2} + 2k \cdot \binom{N-3}{2} + k \cdot \binom{N-4}{2}$.
Where $\binom{N-2}{2} = 6903$ (for $M$ edges), $\binom{N-3}{2} = 6846$ (for edges incident to one degree-2 vertex), and $\binom{N-4}{2} = 6670$ (for added edges).

**Results:**
1. **E=61 (k=1):** One added edge.
   $W_{61} = 58 \cdot 6903 + 2 \cdot 6846 + 1 \cdot 6670 = 400,474 + 13,692 + 6,670 = 420,736$.
   (Increase from $W_M$: +6,556)

2. **E=62 (k=2):** Two disjoint added edges.
   $W_{62} = 56 \cdot 6903 + 4 \cdot 6846 + 2 \cdot 6670 = 386,568 + 27,384 + 13,340 = 427,292$.
   (Increase from $W_{61}$: +6,556)

3. **E=63 (k=3):** Three disjoint added edges.
   $W_{63} = 54 \cdot 6903 + 6 \cdot 6846 + 3 \cdot 6670 = 372,762 + 41,076 + 20,010 = 433,848$.
   (Increase from $W_{62}$: +6,556)

4. **E=64 (k=4):** Four disjoint added edges.
   $W_{64} = 52 \cdot 6903 + 8 \cdot 6846 + 4 \cdot 6670 = 358,956 + 54,768 + 26,680 = 440,404$.
   (Increase from $W_{63}$: +6,556)

**Observation:** For structures where the added edges are disjoint from each other and the original matching edges, the increase in $W$ is consistently $\approx 6,556$ for each additional edge $k$, strongly suggesting that the optimal solution involves maximizing $E$ while keeping the induced subgraphs $G[R_{u,v}]$ empty.

**Next Step:** Continue this systematic investigation up to a larger $E$ (e.g., $E=90$ or $E=100$) or investigate a connected structure (e.g., a path $P_m$ or cycle $C_m$) to see if the constraint $E(G[R_{u,v}])=0$ can be violated profitably. Given the linear increase observed, we should see $W_{E=120}$ (complete graph $K_{120}$ contribution) is zero, so there must be a maximum before $E$ gets too high. The optimal structure is likely highly sparse but more dense than $M$.
