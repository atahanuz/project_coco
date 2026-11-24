### [W1, round 1]
**Task: Maximum non-attacking pillars (M) on an 18x18 grid.**

1.  **Constraint Interpretation:** Two pillars at $(i_1, j_1)$ and $(i_2, j_2)$ are non-attacking if they do not share a vertex or side. This means the maximum coordinate difference must be strictly greater than 1: $\max(|i_1 - i_2|, |j_1 - j_2|) \ge 2$.
2.  **1D Maximum:** In a 1D sequence of length $N=18$, the maximum number of points separated by at least 2 units is achieved by selecting points $1, 3, 5, \dots, 2k-1$. For $N=18$, this yields $k = (18/2) = 9$ possible positions (i.e., $\{1, 3, 5, 7, 9, 11, 13, 15, 17\}$).
3.  **2D Maximum (M):** Since the constraint separates along both axes, the maximum number of pillars $M$ is the product of the 1D maximums: $M = 9 \times 9 = 81$.
4.  **Structure Characterization:** The valid placements form a regular grid pattern. Specifically, pillars must be placed at coordinates $(i, j)$ where both $i$ and $j$ are odd integers, i.e., $i, j \in \{1, 3, 5, \dots, 17\}$.

### [W4, round 1]
Calculated the King's graph for the 18x18 grid. The number of valid pillar locations is $N=324$. The number of configurations with exactly $k=2$ pillars ($N_2$) was determined by calculating the total number of pairs and subtracting pairs that share a vertex or side (edges $E=1190$). $N_2 = \binom{324}{2} - 1190 = 52326 - 1190 = 51136$. As a theoretical lower bound for the total number of configurations $C$ (where $C = \sum_{k=2}^{81} N_k$), we use $C \ge N_2$. The required number of probes $P$ satisfies $2^P \ge C$, leading to a lower bound $P \ge \lceil \log_2 51136 \rceil = 16$.

### [W3, round 1]
Investigated the pillar placement constraint for the $N \times N$ grid ($L_\infty$ distance must be $\ge 2$). This implies that any chosen pillar locations must belong entirely to one of the four mutually disjoint sets $S_X$ defined by the parity of their coordinates $(x \pmod 2, y \pmod 2)$.

For $N=4$, the grid size is $4 \times 4$. The four sets $S_X$ partition the grid, and each set has size 4. The total number of possible valid configurations (subsets of $S_X$ with size $\ge 2$) is $4 \times (2^4 - 1 - 4) = 44$. Since these 44 possibilities are derived from 4 disjoint sets of locations, Berta must probe every single location on the $N \times N$ grid to uniquely distinguish between all possible scenarios.

Structural insight: For a cube of size $N$, the minimum number of required probes scales as $N^2$, as Berta must probe all $N^2$ base locations to ensure unique identification of the pillar set.

### [W1, round 2]
### [W1, round 2]
**Proof of necessity to probe all 81 locations.**

**Context:**
1. The set of all possible pillar bases is $S$, which consists of $9 \times 9 = 81$ specific locations on the $18 \times 18$ grid (i.e., coordinates where both $x$ and $y$ are odd).
2. The constraint dictates that the chosen set of pillars $C$ must satisfy $|C| \ge 2$.
3. **Crucial Premise (as given):** We assume that every subset $C \subseteq S$ such that $|C| \ge 2$ is a valid configuration.

**Argument by Contradiction:**
Suppose Berta can uniquely determine the set $C$ by probing a proper subset of locations, $P \subset S$ ($P \neq S$).
Since $P$ is a proper subset, there must exist at least one location $s \in S$ such that $s \notin P$.

We now construct two distinct possible configurations, $C_1$ and $C_2$, such that they generate the identical observation when Berta probes $P$.

1. **Configuration $C_2$**: Let $C_2 = P$. Since $P$ is a non-empty subset of $S$ and $P \neq \emptyset$, we assume $|P| \ge 2$ (If $|P|<2$, Berta could not determine the configuration since the game requires $|C| \ge 2$). Since we assume all subsets of size $\ge 2$ are valid, $C_2$ is a valid configuration.
2. **Configuration $C_1$**: Let $C_1 = P \cup \{s\}$. Since $s \in S$ and $P \subseteq S$, $C_1 \subseteq S$. Since $|P| \ge 2$, $|C_1| = |P| + 1 \ge 3$. Thus, $C_1$ is also a valid configuration under the crucial premise.

$C_1$ and $C_2$ are distinct because $s \in C_1$ but $s \notin C_2$.

When Berta probes the set $P$, she observes the colors of the unit cubes located at $P$.
*   The observed set for $C_2$ is $C_2 \cap P = P \cap P = P$.
*   The observed set for $C_1$ is $C_1 \cap P = (P \cup \{s\}) \cap P$. Since $s \notin P$, this intersection simplifies to $P$.

Since $C_1 \neq C_2$ but they yield the same observed color pattern on $P$, Berta cannot uniquely distinguish between $C_1$ and $C_2$.

**Conclusion:**
The assumption that $P$ could be a proper subset of $S$ leads to a contradiction. Therefore, Berta must probe every single one of the 81 possible locations in $S$ to ensure that every distinct configuration yields a unique observation.
