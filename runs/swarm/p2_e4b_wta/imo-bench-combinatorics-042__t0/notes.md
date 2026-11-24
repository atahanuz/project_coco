### [W4, round 1]
Analysis of edge contribution to weak quartets:
A weak quartet $\{u, v, x, y\}$ must have exactly one edge. If we fix the edge $e=(u, v)$, then all other pairs in the set must be non-edges. The pairs are: $(u, x), (u, y), (v, x), (v, y), (x, y)$.

Necessary conditions for $\{u, v, x, y\}$ to be a weak quartet containing $e=(u, v)$:
1. $(u, x)$ is not an edge $\implies x \notin N(u)$.
2. $(u, y)$ is not an edge $\implies y \notin N(u)$.
3. $(v, x)$ is not an edge $\implies x \notin N(v)$.
4. $(v, y)$ is not an edge $\implies y \notin N(v)$.
5. $(x, y)$ is not an edge $\implies x$ and $y$ are not friends.

Let $S$ be the set of candidate vertices $x$ and $y$. $S$ must exclude $u$, $v$, and all common neighbors of $u$ and $v$.
$S = V \setminus (\{u, v\} \cup N(u) \cup N(v))$.
Thus, $x, y \in S$.

The contribution of $e=(u, v)$ to the weak quartet count is the number of pairs $\{x, y\}$ chosen from $S$ such that $(x, y)$ is not an edge.
Let $s = |S|$, and $E_S$ be the number of edges in the subgraph induced by $S$.
The contribution is $\binom{s}{2} - E_S$.

### [W3, round 1]
Calculations for N=120:
1. Completely Sparse Graph (E=0): Number of weak quartets = 0.
2. Star Graph K_{1, 119}: Number of weak quartets = 0.
Conclusion: Both candidate structures yield 0 weak quartets. A maximal structure likely requires a graph density that allows for isolated edges within groups of four, suggesting a structure other than the extreme cases analyzed.

### [W2, round 1]
W is the number of weak quartets in a graph G=(V, E) with N vertices and m edges. A weak quartet is a set of 4 vertices $\{v_1, v_2, v_3, v_4\}$ containing exactly one edge.

We count W by iterating over the single edge $(u, v) \in E$. For a fixed edge $(u, v)$, we need to choose two other vertices $\{x, y\}$ from $V \setminus \{u, v\}$ such that:
1. Neither $x$ nor $y$ is adjacent to $u$ or $v$.
2. $x$ and $y$ are not adjacent to each other.

Let $R(u, v)$ be the set of vertices not adjacent to $u$ or $v$, excluding $u$ and $v$ themselves:
$R(u, v) = V \setminus (\{u, v\} \cup N(u) \cup N(v))$.
Let $k = |R(u, v)|$ and $m_R$ be the number of edges in the subgraph induced by $R(u, v)$.

The exact combinatorial expression for W is:
W = \sum_{(u, v) \in E} \left( \binom{|R(u, v)|}{2} - m_{R(u, v)} \right)

An upper bound $W_{UB}$ can be found by ignoring the edges within $R(u, v)$ (i.e., assuming $m_R=0$). Since $|R(u, v)| \le N - d_u - d_v$, where $d_u$ and $d_v$ are the degrees of $u$ and $v$:
W \le \sum_{(u, v) \in E} \binom{N - d_u - d_v}{2}

### [W1, round 1]
Analysis of weak quartets:
A weak quartet is a set of 4 users where exactly one pair is friends (i.e., the induced subgraph has exactly 1 edge).

Case N=5:
The maximum number of weak quartets is 4. This is achieved by a graph consisting of two disjoint edges and one isolated vertex ($M_2 \cup K_1$).
Example structure: Vertices {1, 2, 3, 4, 5}. Edges E = {(1, 2), (3, 4)}.
The 4 weak quartets are: {1, 2, 3, 5}, {1, 2, 4, 5}, {3, 4, 1, 5}, {3, 4, 2, 5}.

Case N=6:
The maximum number of weak quartets is 12. This is achieved by a perfect matching ($M_3$).
Example structure: Vertices {1, 2, 3, 4, 5, 6}. Edges E = {(1, 2), (3, 4), (5, 6)}.
For any given edge (e.g., (1, 2)), there are 4 ways to choose 2 other vertices from the remaining 4 ({3, 4, 5, 6}) such that no other edge is present among the chosen 2. Since there are 3 disjoint edges, the total is 3 * 4 = 12.
