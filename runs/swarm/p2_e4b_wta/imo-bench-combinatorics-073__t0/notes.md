### [W3, round 1]
Analysis of Condition 2: Exactly two rows ($R_1, R_2$) have $m$ reserved seats.

1. Constraints on Column Usage for $R_1$ and $R_2$:
    *   Consider two seats $S_a = (1, j_a)$ and $S_b = (2, j_b)$. Since $R_1 = R_2 = m$, Condition 1 requires that it is NOT the case that [$C_{j_a} = C_{j_b}$].
    *   If $j_a = j_b$, the two seats are stacked. $R_1=R_2=m$ and $C_{j_a}=C_{j_a}$. This pair violates Condition 1. Therefore, the $m$ reserved seats in $R_1$ and the $m$ reserved seats in $R_2$ must occupy $2m$ entirely distinct columns.
    *   Furthermore, if $j_a \neq j_b$, since $R_1=R_2=m$, Condition 1 mandates that $C_{j_a} \neq C_{j_b}$. This means the set of $m$ column counts associated with $R_1$ must be disjoint from the set of $m$ column counts associated with $R_2$.

2. Constraints on Remaining Rows ($R_i, i \ge 3$):
    *   By Condition 2, for $i=3, \ldots, 200$, we must have $R_i \neq m$.
    *   The distribution $\{R_3, \ldots, R_{200}\}$ must ensure that when combined with $R_1$ and $R_2$, Condition 1 is never violated. For example, if $R_3 = m'$ and $R_4 = m'$, then any seat in $R_3$ must be in a column $j$ such that $C_j$ is unique among all seats in $R_4$.

3. Constraints on Column Distribution ($C_j$):
    *   Due to the requirement imposed by $R_1$ and $R_2$, at least $2m$ distinct column count values must be present among the columns involved in $R_1$ and $R_2$.
    *   The overall distribution of $\{C_j\}$ must be complex enough to accommodate $2m$ distinct column counts, while ensuring that any potential duplicate counts in $C_j$ do not correspond to rows having the same reserved seat count.

### [W4, round 1]
Research Summary: The constraint "No two reserved seats can be in rows that have the same number of reserved seats while also being in columns that have the same number of reserved seats" translates to a strong structural requirement on the incidence matrix A. Let $k_R$ be the number of distinct row sums and $k_C$ be the number of distinct column sums. For any pair of distinct row sum $r$ and column sum $c$, the submatrix defined by the set of rows $I_r$ (rows with sum $r$) and the set of columns $J_c$ (columns with sum $c$) must contain at most one reserved seat (entry of 1). This implies that the total number of reserved seats, $N$, is bounded by $N \le k_R k_C$. Condition 2 requires at least two rows to have the same sum $m$, meaning $k_R \le 199$. Maximizing $m$ requires finding configurations that approach this bound while maintaining the required multiplicity $d_m \ge 2$.

### [W2, round 1]
Analysis of Constraint 1 and Constraint 2:
Let $r_i$ be the number of reserved seats in row $i$, and $c_j$ be the number of reserved seats in column $j$.
Constraint 2 requires the existence of two distinct rows, $i_a$ and $i_b$, such that $r_{i_a} = r_{i_b} = m$.

Constraint 1 states that for any two distinct reserved seats $S_1=(i_1, j_1)$ and $S_2=(i_2, j_2)$, it cannot be the case that $r_{i_1} = r_{i_2}$ AND $c_{j_1} = c_{j_2}$.

Consider two reserved seats in the same column $j$, say $S_1=(i_a, j)$ and $S_2=(i_b, j)$. Since $i_a \neq i_b$ and $j_1=j_2=j$, Constraint 1 requires that $r_{i_a} \neq r_{i_b}$.
Since we assume $r_{i_a} = r_{i_b} = m$, this means that it is impossible to have reserved seats at both $(i_a, j)$ and $(i_b, j)$ for any column $j$.
Thus, for all $j \in \{1, \dots, 200\}$, $R_{i_a, j} + R_{i_b, j} \le 1$.

The total number of reserved seats in row $i_a$ is $m = \sum_{j=1}^{200} R_{i_a, j}$.
The total number of reserved seats in row $i_b$ is $m = \sum_{j=1}^{200} R_{i_b, j}$.

The sum of reserved seats in these two rows combined is:
$r_{i_a} + r_{i_b} = 2m = \sum_{j=1}^{200} (R_{i_a, j} + R_{i_b, j})$.
Since $R_{i_a, j} + R_{i_b, j} \le 1$ for all $j$, we have:
$2m \le \sum_{j=1}^{200} 1 = 200$.
This yields the necessary upper bound: $m \le 100$.

### [W1, round 1]
SUMMARY:
The combination of Condition 2 (existence of two rows $R_a, R_b$ with $r_a=r_b=m$) and Constraint 1 imposes a severe limitation on column usage. For any column $j$, $R_{a, j} + R_{b, j} \le 1$. Summing over all $N=200$ columns, $r_a + r_b = 2m \le 200$. Thus, the largest possible value for $m$ is bounded by $m \le 100$. Small configurations test suggest that finding feasible arrangements requires significant column sum heterogeneity, but $m=2$ and $m=3$ are likely feasible provided the higher-order constraints (internal row sum distinctness) can be met.
