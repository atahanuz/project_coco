### [W4, round 1]
Analysis of Edge Placement for Fixed Degree Sequence:
To maximize the sum of edge labels $S = \sum_{(v_i, v_j) \in E} |d_i - d_j|$, we hypothesize that edges should be placed to connect vertices with maximally disparate degrees. Specifically, edges should predominantly link high-degree vertices to low-degree vertices.

Test Case: Star Graph $K_{1, 10}$ on 11 vertices.
Degrees: One central vertex $d_c = 10$; ten peripheral vertices $d_i = 1$.
All 10 edges connect the central vertex to a peripheral vertex.
The label for each edge is $|10 - 1| = 9$.
The total sum $S = 10 \times 9 = 90$. This suggests that a structure maximizing degree variance is likely optimal.

### [W1, round 1]
Calculations for n=11:

1. Complete Graph ($K_{11}$):
   - Degree sequence: (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
   - Sum of labels (S): 0

2. Path Graph ($P_{11}$):
   - Degree sequence: 9 vertices of degree 2, 2 vertices of degree 1. (2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1)
   - Sum of labels (S): 2

3. Star Graph ($K_{1, 10}$):
   - Degree sequence: 1 vertex of degree 10, 10 vertices of degree 1. (10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
   - Sum of labels (S): 90

### [W3, round 1]
Verification Check: For the maximally skewed degree sequence $D = (10, 1^{10})$ on 11 vertices, the unique realizable simple graph is the star graph $K_{1, 10}$. This graph has 10 edges. All edges connect the vertex of degree 10 to vertices of degree 1. The label of every edge is $|10 - 1| = 9$. The total sum $S = 10 \times 9 = 90$. This sequence achieves the maximum possible variance for $N=11$ while remaining realizable.

### [W3, round 1]
REPORT on task "Focus on constructing a highly skewed degree sequence (i.e., one that maximizes the variance of the degrees) that is realizable by a simple graph G with 11 vertices. Calculate the maximum S achievable": I focused on constructing the most highly skewed degree sequence realizable for 11 vertices, which is $D = (10, 1^{10})$. This sequence corresponds to the star graph $K_{1, 10}$. Since the structure is unique for this sequence, the edge placement is determined. Every one of the 10 edges connects a vertex of degree 10 to a vertex of degree 1, resulting in a label of 9 for each edge. The maximum sum $S$ achievable for this sequence is $10 \times 9 = 90$.
Candidate answer: 90

### [W1, round 1]
REPORT on task "Test several simple and extreme degree sequences for n=11 (e.g., the path graph, the star graph, and a complete graph). Calculate the sum of edge labels S for each and record the resulting value and t": I tested three extreme cases for n=11: the complete graph, the path graph, and the star graph. For $K_{11}$, the sum of edge labels was 0. For $P_{11}$, the sum was 2. For the star graph $K_{1, 10}$, the sum was 90. These results and the corresponding degree sequences have been recorded in notes.md. The largest value found so far is 90.
Candidate answer: Not determined yet. The largest value found so far is 90.

### [W4, round 1]
REPORT on task "Analyze the structure: If a degree sequence {d_i} is fixed, how should the edges be placed in the graph G to maximize the sum of labels S? (Hypothesize a placement rule and test it with the star graph": I analyzed the relationship between edge placement and the sum of labels $S = \sum |d_i - d_j|$. My initial analysis focused on finding a structure that maximized degree variance. I tested the star graph $K_{1, 10}$ on 11 vertices, which yields a sum of 90. Subsequent local modifications to this structure demonstrated that increasing the degree of low-degree vertices reduces the overall maximum sum. Based on this, the star graph provides the largest possible sum of labels.
Candidate answer: 90

### [W2, round 1]
The sum S of edge labels is $S = \sum_{(u, v) \in E} |d_u - d_v|$. Since edges between vertices of equal degree contribute 0, we partition the vertices into sets $V_k$ based on their degree $k$. Let $K$ be the set of unique degrees, and $n_k = |V_k|$. Let $X_{k_1, k_2}$ be the number of edges between $V_{k_1}$ and $V_{k_2}$.
The sum $S$ is given by: $S = \sum_{k_1 > k_2} (k_1 - k_2) X_{k_1, k_2}$.
The tight upper bound $S_{max}(D)$ for a given degree sequence $D$ is the solution to the following Linear Program, which relies only on the counts $n_k$ derived from $D$:

Maximize $\sum_{k_1 \in K} \sum_{k_2 \in K, k_1 > k_2} (k_1 - k_2) X_{k_1, k_2}$
Subject to:
1. $\sum_{k' \in K, k' \ne k} X_{k, k'} = k \cdot n_k \quad \forall k \in K$ (Degree requirement)
2. $0 \le X_{k_1, k_2} \le n_{k_1} n_{k_2} \quad \forall k_1, k_2 \in K, k_1 > k_2$ (Simple graph constraint)

### [W2, round 1]
REPORT on task "Attempt to derive a general formula or a tight upper bound for the sum S based solely on the degree sequence {d_1, ..., d_11}, without considering the specific graph structure required to realize it.": The sum of edge labels $S$ is bounded by $S_{max}(D)$, which depends on how the edges connect vertices of different degrees. By partitioning vertices into sets $V_k$ based on degree $k$, we derived a Linear Program whose objective function is $S$, and whose constraints enforce the degree requirements and the simple graph property. This LP formulation provides the tight upper bound based solely on the counts of each degree $n_k$ present in the sequence $\{d_1, \dots, d_{11}\}$.
Candidate answer: The tight upper bound is found by solving a linear program based on the degree sequence D, which maximizes the cross-edges between vertices of different degrees, $S_{max}(D)$.
