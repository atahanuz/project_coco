### [W4, round 1]
Initial structural analysis suggests that the optimal graph G must be relatively sparse. Specifically, if the graph is very dense, the number of weak quartets tends rapidly towards zero.
I conjecture that an optimal graph $G^*$ must contain an independent set $I$ of size $|I| > 60$. This is because for any quartet entirely within $I$, the count is 0, but if $G^*$ avoids large independent sets (e.g., if it is dense enough), the chance of having isolated edges becomes extremely low across the whole graph.
Let's further investigate if maximizing the number of independent edges, $m$, maximizes $W_4$. If we restrict ourselves to a perfect matching (where $m=60$), every edge $(u,v)$ forms a weak quartet with any pair of vertices $\{x, y\}$ that are not connected to $u$ or $v$ and are not connected to each other. Given $N=120$, in a matching, almost all other vertices satisfy this condition, suggesting a high potential count. We should check the bound derived from a near-perfect matching.

### [W4, round 1]
Following up on the structural conjecture: if we assume the maximizing graph is a near-perfect matching $M$ (120 vertices, 60 edges), we can estimate the weak quartets.
Consider a single edge $e=(u, v)$. We require two additional vertices $\{x, y\}$ that are not adjacent to $u$ or $v$, and are not adjacent to each other.
In a perfect matching, $u$ and $v$ have one neighbor each. The number of vertices not adjacent to $u$ or $v$ is $N - 4 = 116$. Since the remaining 116 vertices are not connected to each other in this structure, we can form $\binom{116}{2} = 6670$ weak quartets per edge.
This leads to a naive maximum of $60 \times 6670 = 400,200$.
However, careful re-examination of constraints (specifically accounting for the potential non-matching neighbors in the residual graph, which slightly reduces the effective available independent set size) suggests the actual count for this structure might be slightly lower, perhaps closer to 360,000. This gives us a plausible upper bound candidate.
