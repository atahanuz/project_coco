### [W3, round 1]
## Problem Analysis and Condition Formulation

**1. Cube and Pillars:**
The cube is $N \times N \times N$ where $N=18$. Pillars are $1 \times 1 \times 18$. A configuration $S$ is defined by the set of $xy$-coordinates $L_S$ of the base of the chosen pillars. $L_S \subset \{1, \dots, 18\}^2$.

**2. Constraints on Configurations ($\mathcal{S}$):**
Let $L$ be a set of base locations. $L$ must satisfy:
a) $|L| \ge 2$.
b) **No adjacency constraint:** For any two distinct locations $l_1, l_2 \in L$, the Chebyshev distance $d_\infty(l_1, l_2) = \max(|x_1 - x_2|, |y_1 - y_2|)$ must be $\ge 2$. (This prevents sharing any vertex or side, as $d_\infty=1$ means shared side/vertex).
Let $\mathcal{S}$ be the set of all valid configuration sets $L$.

**3. Sampling and Identification:**
Berta chooses a set of unit cubes $C$. When a pillar configuration $L_S$ is chosen, a cube $c$ is black if and only if its $(x, y)$ projection $l_c$ belongs to $L_S$.
Let $P_C$ be the set of projected $xy$-locations of the cubes in $C$.

Berta can uniquely determine the configuration $L_S$ if and only if the set $L_S$ is uniquely identifiable from the observations $L_S \cap P_C$.

**4. Necessary and Sufficient Condition:**
The set of sampled locations $C$ is sufficient to distinguish all distinct configurations in $\mathcal{S}$ if and only if, for every pair of distinct valid configurations $L_1, L_2 \in \mathcal{S}$ ($L_1 \neq L_2$), there exists at least one location $l$ in the symmetric difference $L_1 \Delta L_2 = (L_1 \setminus L_2) \cup (L_2 \setminus L_1)$ such that $l$ is covered by the sample locations $C$ (i.e., $l \in P_C$).

This condition ensures that $L_1$ and $L_2$ generate different color readings on at least one sampled cube.

### [W4, round 1]
**Proof/Analysis for Task:**
The problem requires proving that for any location $p$ on the $18 \times 18$ base grid, there exists a valid base configuration $P_{base}$ of size $|P_{base}| \ge 2$ such that $p$ does not conflict with any pillar in $P_{base}$. A conflict occurs if two pillars share a vertex or a side, meaning their base locations must be separated by a distance of at least 2 in both the x and y directions.

Let $p = (x_p, y_p)$ be any chosen location. We need to find $q_1, q_2$ such that:
1. $|x_p - x_{q_i}| \ge 2$ and $|y_p - y_{q_i}| \ge 2$ for $i=1, 2$.
2. $|x_{q_1} - x_{q_2}| \ge 2$ and $|y_{q_1} - y_{q_2}| \ge 2$.

Since the grid is $18 \times 18$, for any given $p$, there is always ample space far away from $p$ to place $q_1$ and $q_2$.

**Case 1: p is central (e.g., $p=(9, 9)$).** We can choose $q_1=(1, 1)$ and $q_2=(1, 3)$.
*   $\{q_1, q_2\}$ is valid: $|1-1|=0 < 2$ (Side sharing, this setup is invalid).
*   Let's choose $q_1=(1, 1)$ and $q_2=(3, 3)$. $\{q_1, q_2\}$ is valid: $|1-3|=2 \ge 2$ and $|1-3|=2 \ge 2$.
*   $p=(9, 9)$ is far from $q_1=(1, 1)$ and $q_2=(3, 3)$.
*   We set $P_{base} = \{(1, 1), (3, 3)\}$.
*   $S_1 = P_{base} \cup \{p\}$ is valid.
*   $S_2 = P_{base}$ is valid.
*   If Berta avoids sampling $p$, $S_1$ and $S_2$ are indistinguishable.

**Case 2: p is near a corner (e.g., $p=(1, 1)$).** We can choose $q_1=(18, 18)$ and $q_2=(18, 16)$.
*   $\{q_1, q_2\}$ is valid: $|18-18|=0 < 2$ (Side sharing, invalid).
*   Let's choose $q_1=(18, 18)$ and $q_2=(16, 16)$. $\{q_1, q_2\}$ is valid.
*   $p=(1, 1)$ is far from $q_1=(18, 18)$ and $q_2=(16, 16)$.
*   We set $P_{base} = \{(18, 18), (16, 16)\}$.
*   $S_1 = P_{base} \cup \{p\}$ is valid.
*   $S_2 = P_{base}$ is valid.
*   If Berta avoids sampling $p$, $S_1$ and $S_2$ are indistinguishable.

Since the grid is large enough to always find a set $P_{base}$ of size $\ge 2$ separated from $p$ by at least a distance of 2 in both coordinates, the configurations $S_1$ and $S_2$ exist.

**Conclusion:** Failing to sample any single location $p$ in $P$ guarantees the existence of two indistinguishable configurations $S_1$ and $S_2$. The statement is TRUE.

### [W1, round 1]
The task is to find the maximum size of a set of pillars $P$ on an $18 \times 18$ grid such that no two pillars share a vertex or side. A pillar at $(i_1, j_1)$ and one at $(i_2, j_2)$ share a vertex or side if and only if $\max(|i_1 - i_2|, |j_1 - j_2|) \le 1$. Therefore, we seek the maximum set $P$ such that the $L_\infty$ distance between any two points in $P$ is at least 2. This maximum size is achieved by selecting pillars at coordinates $(i, j)$ where both $i$ and $j$ are odd. For $N=18$, there are $\lceil 18/2 \rceil = 9$ possible odd values for $i$ (1, 3, ..., 17) and 9 for $j$. The maximum size $|P|$ is $9 \times 9 = 81$.

### [W2, round 1]
The maximum number of mutually separated pillar locations on an 18x18 grid is 81 (9x9 checkerboard pattern separated by 2 units). The set of all valid configurations S is the power set of these 81 locations, excluding the empty set and singletons. To uniquely determine which subset P was chosen from a space of size 2^81, Berta needs at least 81 queries, one for each potential location.
