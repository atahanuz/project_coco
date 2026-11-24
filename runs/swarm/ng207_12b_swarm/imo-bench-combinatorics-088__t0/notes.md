### [W1, round 1]
REPORT on task "Use Python to compute small cases / brute-force search, record data and patterns in notes.md, and propose a candidate answer.": I used a search algorithm to find the maximum sum of edge labels $|d_i - d_j|$ in a simple graph with 11 vertices. The sum is maximized when the vertices are partitioned into two sets of degrees $D$ and $d$, connected by as many edges as possible. I tested various values for $k$ (number of vertices with degree $D$) and found that for $k=4, D=10, d=4$, the number of edges between the sets is $m_{12} = 28$, leading to a sum of $28 \times (10 - 4) = 168$. Another configuration with $k=3, D=10, d=3$ also yielded 168. Checking other configurations, 168 remains the maximum.
Candidate answer: 168

### [W4, round 1]
The problem asks for the largest sum of edge labels in a graph with 11 vertices, where each edge label is the difference of the degrees of its endpoints.
Let the degrees of the vertices be d_1, d_2, ..., d_11 sorted in non-increasing order.
The sum of the labels is S = sum_{i<j, (i,j) \in E} (d_i - d_j).
This can be rewritten as S = sum_{v \in V} (d_v * (y_v - x_v)), where y_v is the number of neighbors of v with larger degree and x_v is the number of neighbors with smaller degree.
Wait, my previous Python code used a different formula S = 2 * sum d_i y_i - sum d_i^2. Let's re-check.
If d_1 >= d_2 >= ... >= d_n, let y_i be the number of neighbors of vertex i in {i+1, ..., n}.
The degree d_i = y_i + (number of neighbors in {1, ..., i-1}).
Let x_i be the number of neighbors of vertex i in {1, ..., i-1}.
So d_i = y_i + x_i.
The sum of labels S = sum_{i<j, (i,j) \in E} (d_i - d_j).
Let E_i be the set of edges (i,j) such that i < j. For each (i,j) \in E_i, the label is d_i - d_j.
S = sum_{i < j, (i,j) \in E_i} (d_i - d_j)
S = sum_{i=1}^n \sum_{j=i+1, (i,j) \in E_i}^n (d_i - d_j)
S = sum_{i=1}^n (y_i d_i - sum_{j \in Neighbors(i), j>i} d_j).
Also, d_j = y_j + x_j, where x_j is the number of neighbors of j in {1, ..., j-1}.
So sum_{j \in Neighbors(i), j>i} d_j is hard to simplify directly.
Let's use the property: sum_{j \in Neighbors(i), j>i} d_j = sum_{j \in Neighbors(i), j>i} (y_j + x_j).
Note that sum_{j > i, (i,j) \in E} x_j is the number of edges (k,j) such that k < j and j > i.
This is getting complicated. Let's use the other way:
S = sum_{i < j, (i,j) \in E} (d_i - d_j)
S = sum_{i < j, (i,j) \in E} d_i - sum_{i < j, (i,j) \in E} d_j
Sum_{i < j, (i,j) \in E} d_i: For each vertex i, it is counted for every neighbor j > i. This is y_i.
So sum_{i < j, (i,j) \in E} d_i = sum_{i=1}^n y_i d_i.
Sum_{i < j, (i,j) \in E} d_j: For each vertex j, it is counted for every neighbor i < j. This is x_j.
So sum_{i < j, (i,j) \in E} d_j = sum_{j=1}^n x_j d_j.
Thus S = sum y_i d_i - sum x_i d_i.
Since d_i = y_i + x_i, we have x_i = d_i - y_i.
S = sum y_i d_i - sum (d_i - y_i) d_i = sum y_i d_i - sum d_i^2 + sum y_i d_i = 2 * sum y_i d_i - sum d_i^2.
This matches my Python code.
The code computed the maximum S for n=11 to be 168.
Let's double check the values:
n=3: 2
n=4:

### [W4, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": I calculated the maximum sum of edge labels by modeling the problem as maximizing S = 2 * sum y_i d_i - sum d_i^2, where d_i are the sorted degrees and y_i are the number of neighbors of vertex i with a higher index. I used a greedy approach to find the optimal edge set for each graphic degree sequence. For n=11, the maximum sum was found to be 168.
Candidate answer: 168

### [W3, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": (no report: step or token limit reached)

### [W2, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": (no report: step or token limit reached)
