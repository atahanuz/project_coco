### [W2, round 1]
Analysis of Condition 1:
Let $R_k$ be the set of rows with $k$ reserved seats ($|R_k| = N_k$). Let $J_i$ be the set of $k$ columns containing reserved seats in row $i \in R_k$.
Condition 1 implies that for any two distinct rows $i_1, i_2 \in R_k$, the set of column sums $\{c_j\}_{j \in J_{i_1}}$ must be disjoint from the set of column sums $\{c_j\}_{j \in J_{i_2}}$.

Since the maximum possible column sum is 200 (and 0 is possible), there are 201 distinct possible values for the column sums $\{c_j\}$.
If $N_k$ rows have $k$ reserved seats, these rows collectively use $N_k$ disjoint sets of column sums. Since each of the $N_k$ rows contributes at least one column sum value to its respective set, and assuming the most restrictive case where each of the $k$ seats in a row uses a distinct column sum value (i.e., $|S_{i}| = k$), we must have:
$N_k \cdot k \le 201$.
Thus, $N_k \le \lfloor 201/k \rfloor$. This is a structural constraint on the maximum number of rows sharing the same reservation count $k$.

### [W1, round 1]
Analysis of Constraint 1 on a small grid (N=4):
Condition 1 states that no two reserved seats $(i, j)$ and $(k, l)$ can exist such that $R_i = R_k$ AND $C_j = C_l$.
This implies a very severe restriction: If two rows share the same reserved count $m$ (e.g., $R_i = R_k = m$), then for any reserved seat in row $i$ (say $(i, j)$) and any reserved seat in row $k$ (say $(k, l)$), their corresponding column counts must be different ($C_j \neq C_l$).

Testing for m=2 (N=4):
Let $R_1=2$ and $R_2=2$. The remaining rows $R_3, R_4$ must be $\neq 2$.
If we place seats $(1, j_1), (1, j_2)$ and $(2, k_1), (2, k_2)$, then we must ensure that $C_{j_1}, C_{j_2}, C_{k_1}, C_{k_2}$ are all distinct.
If $C_j$ includes contributions from $R_1, R_2, R_3, R_4$, it is difficult to achieve this distinctness, especially when $m$ is large relative to $N$.

Example Failure (N=4, m=2 attempt):
R1: (1, 1), (1, 2). C = (1, 1, 0, 0).
R2: (2, 3), (2, 4). C = (1, 1, 1, 1).
Check pair (1, 1) and (2, 3): R1=2, R2=2. C1=1, C3=1. Since C1=C3, this configuration VIOLATES Condition 1.

Conclusion: Constraint 1 forces an extreme separation of column usage when multiple rows share the same reservation count $m$. For small $N$, $m$ appears highly restricted, suggesting $m$ might be small even in the large grid. The maximum $m$ found in this small case is currently 1 (if $R_1=1, R_2=1$ and they use distinct columns and the resulting column counts are distinct). Further optimization is required to find the true maximum $m$.

### [W4, round 1]
Global Upper Bound Derivation (Task):
Condition 1 states that no two reserved seats $(i_1, j_1)$ and $(i_2, j_2)$ can exist such that $r_{i_1} = r_{i_2}$ AND $c_{j_1} = c_{j_2}$.

Condition 2 requires the existence of $K \ge 2$ rows (let $I_m$ be this set) such that $r_i = m$ for all $i \in I_m$.
The total number of reserved seats contributed by these $K$ rows is $S_m = K \cdot m$.

Let $J_l$ be the set of columns whose reserved seat count is $l$. There are $201$ possible values for $l$ (from 0 to 200).
The constraint implies that for any fixed column sum value $l$, there can be at most one reserved seat $(i, j)$ such that $i \in I_m$ and $j \in J_l$.
Therefore, the total number of seats $S_m$ is bounded by the number of possible column sum values:
$S_m \le |\{0, 1, \dots, 200\}| = 201$.

Substituting $S_m = K \cdot m$:
$K \cdot m \le 201$.

Since Condition 2 guarantees $K \ge 2$, we have:
$2m \le 201$
$m \le 100.5$.

The global upper bound on $m$ is $100$. This bound holds regardless of the assignments of seats in rows outside of $I_m$.
