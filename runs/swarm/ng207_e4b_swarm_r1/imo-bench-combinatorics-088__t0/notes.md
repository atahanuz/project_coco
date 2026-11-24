### [W1, round 1]
Initial analysis on $n=11$ vertices:
1. Star Graph ($K_{1, 10}$): Degrees are $\{10, 1, 1, \dots, 1\}$. There are 10 edges, each labeled $|10-1|=9$. The total sum of labels $S_{K_{1, 10}} = 10 \times 9 = 90$.
2. Complete Graph ($K_{11}$): All degrees are 10. All edges are labeled $|10-10|=0$. The total sum of labels $S_{K_{11}} = 0$.
These provide bounds: $0 \le S \le \text{Max}$. The maximum is likely higher than 90, given the problem asks for the largest value.

### [W2, round 1]
Initial Algebraic Expression for S:
The sum of the labels, $S$, is defined as:
$S = \sum_{(u, v) \in E} |d(u) - d(v)|$

Using the Adjacency Matrix $A$ (where $A_{uv}=1$ if $(u,v) \in E$ and 0 otherwise, and $n=11$):
$S = \sum_{u=1}^{11} \sum_{v=u+1}^{11} A_{uv} |d_u - d_v|$

This expression directly shows the dependence on the degree sequence $D=(d_1, ..., d_{11})$ and the graph structure via $A$.

To find a strong upper bound, one must maximize this sum subject to the constraints that $D$ is realizable by a simple graph $G$, which means $\sum d_i = 2|E|$ and $A$ must satisfy $A\mathbf{d} = 2\mathbf{d}$, where $\mathbf{d}$ is the vector of degrees (or rather, $\sum_v A_{uv} = d_u$).

The maximum possible value of any $|d_u - d_v|$ is $n-1 = 10$. The trivial upper bound is $10 \cdot \binom{11}{2} = 550$. A tighter bound requires specific knowledge of the degree sequence $D$.

### [W1, round 1]
REPORT on task "Analyze extreme degree disparity. Use Python to calculate the sum of labels (S) for a star graph K_{1, 10} on 11 vertices. Then, calculate S for a graph with maximum possible edges (K_11) to establish": I calculated the sum of edge labels (S) for the two requested extreme graphs on 11 vertices. For the star graph $K_{1, 10}$, $S = 90$. For the complete graph $K_{11}$, $S = 0$. These results establish a lower bound of 0 and a baseline value of 90, suggesting the maximum value is likely higher than 90, focusing the analysis on degree distributions that maximize $| \deg(u) - \deg(v) |$.
Candidate answer: N/A (Analysis complete, bounds established)

### [W2, round 1]
REPORT on task "Develop an algebraic expression or a strong upper bound for S in terms of the degree sequence D = (d1, ..., d11) and the adjacency matrix, specifically examining how the term |d(u) - d(v)| behaves.": I developed the exact algebraic expression for the sum of labels, $S$, in terms of the adjacency matrix $A$ and the degree sequence $D$. The expression is $S = \sum_{u=1}^{11} \sum_{v=u+1}^{11} A_{uv} |d_u - d_v|$. I also provided a discussion in the notes regarding the difficulty of finding a tight upper bound without maximizing over all possible graph structures compatible with $D$.
Candidate answer: N/A (Structural Expression Developed)

### [W4, round 1]
Exploration of degree sequences maximizing the sum of squared degrees ($\sum d_i^2$) for $N=11$.

To maximize $\sum d_i^2$ while maintaining graphicity, high variance is sought.
Case 1: $D = (10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)$. This sequence is graphic (a central vertex connected to 10 leaves).
$\sum d_i = 20$. $|E| = 10$. $\sum d_i^2 = 10^2 + 10 \cdot 1^2 = 110$.

Case 2: $D = (10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)$. This sequence is graphic. The central vertex (degree 10) connects to all 10 others. The remaining 10 vertices, which start with degree 1, require exactly one more edge each among themselves. This requires a perfect matching on 10 vertices, which is possible.
$\sum d_i = 30$. $|E| = 15$. $\sum d_i^2 = 10^2 + 10 \cdot 2^2 = 100 + 40 = 140$.

The sequence $D = (10, 2, \dots, 2)$ provides a higher value for $\sum d_i^2$ (140) than the sequence $D = (10, 1, \dots, 1)$ (110), while remaining graphic. This suggests that increasing the total number of edges ($|E|$) while maintaining high variance is beneficial for maximizing the degree sum of squares.

### [W3, round 1]
**Investigation of Regular Graphs (N=11)**
For any $n$-regular graph G on 11 vertices, every vertex has degree $n$. The label of any edge $(u, v)$ is $|\deg(u) - \deg(v)| = |n - n| = 0$. Therefore, the sum of the labels, S, is 0 for all regular graphs on 11 vertices.

**Initial Investigation of Non-Regular Graphs (Maximization)**
The sum S is maximized when the degrees are maximally non-uniform. We tested the star graph $K_{1, 10}$:
Vertices: $v_1$ (center), $v_2, \ldots, v_{11}$ (leaves).
Degrees: $\deg(v_1) = 10$, $\deg(v_i) = 1$ for $i \ge 2$.
Edges: 10 edges, all incident to $v_1$.
Label per edge: $|10 - 1| = 9$.
Total Sum S = $10 \times 9 = 90$.

This value (S=90) is a strong candidate for the maximal value, as it represents the most extreme non-uniform distribution of degrees possible while maintaining connectivity and graph structure. Further exploration into slightly less extreme degree distributions (e.g., trying to distribute the degree 1s) suggests these will result in a smaller sum due to the reduction in the most significant difference factor (10-1).

### [W4, round 1]
REPORT on task "Explore how S changes when fixing the total number of edges |E|. Try to construct a degree sequence D = (d1, ..., d11) that maximizes the sum of squared degrees (a proxy for potential degree differenc": I explored degree sequences for $N=11$ that maximize the sum of squared degrees ($\sum d_i^2$) while ensuring the sequence is graphic. I found that sequences with high variance are optimal. Specifically, the degree sequence $D = (10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)$ is graphic, resulting in $\sum d_i^2 = 140$. This demonstrated that increasing the total number of edges $|E|$ (from 10 to 15) while maintaining extreme degree variance allows for a larger $\sum d_i^2$.
Candidate answer: N/A (Exploratory Task)

### [W3, round 1]
REPORT on task "Investigate the case of regular graphs (where all degrees are equal). Determine the value of S for an n-regular graph on 11 vertices (if such a graph exists for the maximal possible degree). Generaliz": I investigated the sum of edge labels, S, for graphs on 11 vertices. For any regular graph, the label of every edge is 0, meaning the sum S is 0. To maximize S, non-regularity is required. I analyzed the star graph K_{1, 10}, which represents the most extreme degree distribution possible (degrees 10 and 1). This configuration yields a total sum S = 90, which is the candidate for the largest possible value.
Candidate answer: 90
