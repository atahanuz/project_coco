### [W1, round 1]
Tested small cases (N=4, N=6). For N=6, a perfect matching (3 edges) yielded W=12, which was maximal compared to graphs with fewer or more edges (e.g., 1 edge -> W=6, 2 edges -> W=10). This suggests a perfect matching configuration maximizes the weak quartets count.

Calculated the result for N=120 assuming a perfect matching structure (60 edges).
Let $N=120$, $k=60$. For any edge $e$, there are $N-2=118$ potential vertices. Among these 118 vertices, the remaining $k-1=59$ edges from the matching are present.
The number of ways to choose 2 non-adjacent vertices from 118 is $\binom{118}{2} - 59 = 6903 - 59 = 6844$.
Total weak quartets = $k \times W_e = 60 \times 6844 = 410640$.

### [W3, round 1]
The maximum number of weak quartets in a graph with $N$ vertices is achieved when the graph consists of exactly one edge $e$, and the remaining $N-2$ vertices form an independent set entirely disconnected from $e$'s endpoints. In this case, $N=120$, so $N-2=118$. The number of weak quartets is $\binom{118}{2} = \frac{118 \times 117}{2} = 6903$. This structure ensures that every quartet containing the single edge has exactly one edge, while adding any other edge would increase the edge count in some quartets, destroying the weak quartet property.

### [W1, round 1]
REPORT on task "Use Python to compute small cases / brute-force search, record data and patterns in notes.md, and propose a candidate answer.": I analyzed the problem by studying small cases (N=4, 6) and found that a perfect matching configuration appears to maximize the number of weak quartets. I implemented this structure for N=120, where a perfect matching has 60 edges. For each edge, the number of weak quartets it contributes is $\binom{118}{2} - 59 = 6844$. The maximum possible number of weak quartets is therefore $60 \times 6844 = 410,640$.
Candidate answer: 410640

### [W3, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": I modeled the social network as a graph and interpreted a weak quartet as an induced subgraph $K_2 \cup 2K_1$. To maximize the count, I determined that the graph must be as sparse as possible while maintaining exactly one edge. The maximal configuration is a graph consisting of a single edge and 118 isolated vertices. This structure ensures that every choice of two users from the 118 isolated users, combined with the single edge, forms a weak quartet. The maximum count is $\binom{118}{2} = 6903$.
Candidate answer: 6903

### [W4, round 1]
The problem asks for the maximum number of weak quartets (subgraphs induced by 4 vertices having exactly 1 edge) in a graph $G$ with $N=120$ vertices.
A weak quartet containing a specific edge $e=(u, v)$ is formed by choosing two additional vertices $x, y$ such that $\{u, v, x, y\}$ has only the edge $(u, v)$. This requires $x$ and $y$ to be non-neighbors of $u$ and $v$, and also non-adjacent to each other.
We analyzed the strategy of using a perfect matching $M$ ($m=N/2=60$ edges).
For any edge $e$ in a perfect matching, the set $S_e$ of remaining vertices not adjacent to $u$ or $v$ has size $|S_e| = N-2 = 118$. The subgraph induced by $S_e$ consists of $m-1 = 59$ disjoint edges.
The number of weak quartets containing $e$ is $\binom{118}{2} - 59 = 6903 - 59 = 6844$.
Since there are 60 such edges, the total number is $60 \times 6844 = 410640$.
This construction maximizes the size of $S_e$ for every edge and provides a strong candidate for the maximum.

### [W4, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": The maximum number of weak quartets is achieved when the network forms a perfect matching on the 120 users. For any edge $e$ in this matching, there are 6844 ways to complete a weak quartet using the remaining 118 vertices. Since there are 60 such edges, the total maximum number is $60 \times 6844 = 410640$.
Candidate answer: 410640

### [W2, round 1]
Revisiting the comparison between graph structures:
1. Single Edge structure ($M=1$): $K_S = \binom{N-2}{2} = \binom{118}{2} = 6903$.
2. Perfect Matching structure ($M=N/2=60$): $K_M = M \left( \binom{N-2}{2} - (M-1) \right) = 60 \times (\binom{118}{2} - 59) = 60 \times 6844 = 410,640$.

The perfect matching structure yields a significantly higher number of weak quartets. The analysis for the perfect matching configuration (disjoint edges) is robust and verified for $N=6$. Therefore, 410,640 is the candidate maximum.

### [W2, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": I analyzed the problem by modeling the social network as a graph and seeking to maximize the number of induced subgraphs on 4 vertices containing exactly one edge. I compared two extremal constructions: a single edge combined with an independent set, and a perfect matching. The perfect matching configuration, where $N=120$ vertices are divided into 60 disjoint edges, yields the maximum count. For each of the 60 edges, there are 6844 ways to choose two non-adjacent remaining vertices, resulting in a total maximum of 410,640 weak quartets.
Candidate answer: 410640
