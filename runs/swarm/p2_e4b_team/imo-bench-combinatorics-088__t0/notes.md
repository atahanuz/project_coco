### [W1, round 1]
Calculated sum of edge labels for the graph structure where one vertex has degree 10 and all others have degree 1 (N=11).
Degrees: $\deg(v_1) = 10$, $\deg(v_i) = 1$ for $i=2, \ldots, 11$.
Edges exist only between $v_1$ and $v_i$ ($i \geq 2$).
For each edge, the label is $|\deg(v_1) - \deg(v_i)| = |10 - 1| = 9$.
There are 10 such edges.
Total sum of labels = $10 \times 9 = 90$.

### [W3, round 1]
Goal: Maximize S = sum(|d(u) - d(v)|) for N=11. This requires maximizing the variance of the degree sequence $\{d_i\}$, concentrating degrees at extremes (0 and 10).

Key Observation: If a vertex $v$ has degree $d(v)=0$, it contributes nothing to the sum S, nor does it affect the degrees of other vertices. We should aim for minimal $n_0$ unless necessary, as isolated vertices waste vertices that could otherwise contribute to edge labels.

Hypothesis: The maximum S will occur when the degree sequence $\{d_i\}$ is as close as possible to containing only 0s and 10s, while satisfying the graphicality conditions ($\sum d_i$ is even, and the sequence is graphical).

Test Case Strategy: Test scenarios where $n_{10}$ is large and the remaining degrees are minimized (e.g., 1 or 2) to maintain graphicality and high variance. A sequence consisting purely of 0s and 10s is extremely restrictive and might be impossible for $N=11$. We will investigate sequences close to this ideal structure.

### [W2, round 1]
The problem asks for the theoretical upper bound of $S = \sum_{(i, j) \in E} |d_i - d_j|$ for a simple graph $G$ on $n=11$ vertices, given $0 \le d_i \le 10$ and $\sum d_i$ is even.

To maximize $S$, we aim to choose a degree sequence $D$ that is highly polarized (containing many low and high degrees) and construct a graph $G$ that connects the vertices with these extreme degrees as much as possible.

We tested the structure of a complete bipartite graph $K_{k, 11-k}$, where $k$ vertices have degree $11-k$ and $11-k$ vertices have degree $k$. The edges only exist between these two sets, so the difference $|d_i - d_j|$ is constant for all edges: $|(11-k) - k| = |11 - 2k|$.
The sum is $S(k) = k(11-k) \cdot |11 - 2k|$.

We tested values of $k$:
k=1: $S(1) = 1 \cdot 10 \cdot |9| = 90$.
k=2: $S(2) = 2 \cdot 9 \cdot |7| = 126$. (Sequence $D=(9^2, 2^9)$, sum = 36, even).
k=3: $S(3) = 3 \cdot 8 \cdot |5| = 120$.
k=4: $S(4) = 4 \cdot 7 \cdot |3| = 84$.
k=5: $S(5) = 5 \cdot 6 \cdot |1| = 30$.

The maximum value achieved by the complete bipartite construction is $S=126$ for $K_{2, 9}$. Since this structure maximally connects the polarized degree groups, it is conjectured to be the theoretical upper bound. Any deviation from $K_{k, n-k}$ (e.g., adding edges within the partitions) tends to equalize the degrees and thus reduce $S$.

### [W3, round 2]
Found a non-bipartite sequence D' = (10^2, 2^9) for N=11. This sequence corresponds to taking K_{2, 9} and adding one edge between the two vertices of degree 9. The resulting sum of labels S is 144, which exceeds the maximum of 126 found in the complete bipartite constructions.

### [W2, round 3]
---
**Task 1: Rigorous calculation for $D'=(10^2, 2^9)$**

The degree sequence $D' = (10^2, 2^9)$ is realized by starting with a complete bipartite graph $K_{2, 9}$, where the two vertices in partition A ($a_1, a_2$) have degree 9, and the nine vertices in partition B ($b_1, \ldots, b_9$) have degree 2. Then, an edge $(a_1, a_2)$ is added within partition A.

Let $d_i$ be the degree of vertex $v_i$. After adding $(a_1, a_2)$:
$d(a_1) = 9 + 1 = 10$
$d(a_2) = 9 + 1 = 10$
$d(b_j) = 2$ for $j=1, \ldots, 9$.

The sum of labels $S$ is calculated over the total set of edges $E'$. $E'$ consists of $E_{A,B}$ (18 edges) and $E_{A,A}$ (1 edge).

1. Contribution from $E_{A,B}$: All 18 edges connect a vertex of degree 10 to a vertex of degree 2.
   Label contribution: $18 \times |10 - 2| = 18 \times 8 = 144$.

2. Contribution from $E_{A,A}$: The single edge $(a_1, a_2)$ connects two vertices of degree 10.
   Label contribution: $1 \times |10 - 10| = 1 \times 0 = 0$.

Total sum $S = 144 + 0 = 144$. This confirms the target value.

**Task 2: Systematic investigation for $S > 144$**

The goal is to maximize $S = \sum_{(u, v) \in E} |d(u) - d(v)|$ for $N=11$. This requires maximizing the variance of the degree sequence while maximizing the connectivity between high-degree and low-degree vertices.

The sequence $(10^2, 2^9)$ achieved $S=144$ using 19 edges.

*Case 1: Increasing the number of $d=10$ vertices ($n_{10} > 2$).*
Consider $D'' = (10^3, 1^8)$. This sequence is graphical ($\sum d_i = 38$, even). To maximize $S$, we would strive for a structure where the three $d=10$ vertices are fully connected to all eight $d=1$ vertices (24 edges). The theoretical maximum contribution would be $24 \times |10 - 1| = 216$.
However, since $d(v)=10$ requires connection to all 10 other vertices, any vertex $v_i$ with $d(v_i)=10$ is connected to $v_j$ with $d(v_j)=1$. This connection forces $d(v_j) \ge 3$ (as $v_j$ must connect to all three $d=10$ vertices), contradicting $d(v_j)=1$. Thus, $D''$ is not realizable in a way that maintains the intended polarization.

*Case 2: Modifying the low-degree vertices ($n_{10}=2, n_2 < 9$).*
If we increase one low degree, say $D^* = (10^2, 4^1, 2^8)$. The two $d=10$ vertices ($v_1, v_2$) must connect to all 10 other vertices.
$d(v_3)$ (where $d(v_3)=4$) is automatically at least 2 (from $v_1, v_2$). To reach 4, $v_3$ needs 2 more connections, which must come from the $d=2$ vertices $\{v_4, \ldots, v_{11}\}$. If $v_3$ connects to $v_4$ and $v_5$, then $d(v_4)$ and $d(v_5)$ become 3, violating the target sequence $D^*$.

**Conclusion of Investigation:**
The highest sum $S=144$ is achieved by the realizable degree sequence $(10^2, 2^9)$ constructed by maximizing the difference across the entire graph while adhering strictly to the degree constraints. Attempts to achieve higher variance or more edges by increasing $n_{10}$ or altering $n_2$ fail because the necessary connections required by the high-degree vertices inherently violate the low-degree constraints of the sequence.
---
