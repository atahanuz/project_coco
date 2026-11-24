### [W4, round 1]
Problem investigation initiated using optimization techniques.
The goal is to find $C = \sup_A \left\{ \min \left( \max_i |R_i|, \max_j |C_j| \right) \right\}$ for a $230 \times 230$ matrix $A$.

This leads to a Max-Min Optimization problem. We seek to maximize $X$ such that there exists a valid matrix A where both $\max_i |R_i| \ge X$ and $\max_j |C_j| \ge X$.

Formal setup:
Maximize $X$
Subject to:
1. $-1 \le a_{ij} \le 1$ for all $i, j$.
2. $\sum_{i,j} a_{ij} = 0$.
3. $\exists k$: $\sum_j a_{kj} \ge X$ OR $\sum_j a_{kj} \le -X$ (For $\max_i |R_i| \ge X$)
4. $\exists l$: $\sum_i a_{il} \ge X$ OR $\sum_i a_{il} \le -X$ (For $\max_j |C_j| \ge X$)

Due to the complexity of the $\max$ constraints, a direct linear programming formulation is not immediately apparent. Further investigation into bounds from discrepancy theory or semidefinite programming might be required if standard LP/Flow methods fail to simplify the goal function.

### [W3, round 1]
## Analysis for Small N
The problem seeks the least integer $C$ such that for any matrix $A$ of size $N \times N$ (with $|A_{ij}| \le 1$ and $\sum A_{ij} = 0$), at least one row sum or column sum has an absolute value no greater than $C$. This means we are looking for $C = \sup_A (\min_{s \in S(A)} |s|)$.

**Case N=2:**
Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. We require $a+b+c+d=0$.
Consider the matrix $A_2 = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$.
Constraints check: $|A_{ij}| \le 1$. Sum = 0.
Row sums: $R_1 = 2$, $R_2 = -2$.
Column sums: $C_1 = 0$, $C_2 = 0$.
The set of sums $S(A_2) = \{2, -2, 0, 0\}$. The minimum absolute sum is 0.

**Case N=3:**
Let $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & -1 \\ -1 & -1 & 0 \end{pmatrix}$.
Constraints check: $|A_{ij}| \le 1$. Sum = 0.
Row sums: $R_1 = 3$, $R_2 = -1$, $R_3 = -2$.
Column sums: $C_1 = 1$, $C_2 = -1$, $C_3 = 0$.
The set of sums $S(A) = \{3, -1, -2, 1, -1, 0\}$. The minimum absolute sum is 0.

**Initial Conclusion:**
In both tested cases ($N=2$ and $N=3$), we were able to construct matrices where at least one row sum or column sum is exactly 0. This strongly suggests that the required bound $C$ might be 0, meaning that the zero-sum constraint forces at least one line sum to be zero (or very close to zero, if entries were real numbers not restricted to $\pm 1$). Since we found instances where the minimum absolute sum is 0, $C$ must be at least 0. We hypothesize $C=0$.

### [W1, round 1]
Analysis of the upper bound C:
The problem requires finding an upper bound C such that at least one row sum ($R_i$) or column sum ($K_j$) has an absolute value $\le C$. We aim to prove $C \le N/2$ where $N=230$.

1. Row Sums: Since the total sum of entries is zero, the sum of all row sums must be zero: $\sum_{i=1}^N R_i = 0$.
2. Contradiction Argument: Assume, for contradiction, that $|R_i| > N/2$ for all $i=1, \dots, N$.
3. Since $N=230$ is even, let $P$ be the set of rows with $R_i > N/2$ and $M$ be the set of rows with $R_i < -N/2$. $P \cup M = \{1, \dots, N\}$.
4. For the sum to be zero, we must have roughly $|P| \approx |M| \approx N/2$. However, because we use strict inequality $|R_i| > N/2$, even if $|P|=|M|=N/2$, the sum is strictly positive:
$\sum R_i > \sum_{i \in P} (N/2) + \sum_{i \in M} (-N/2) = |P| \cdot (N/2) - |M| \cdot (N/2) = N/2 \cdot N/2 - N/2 \cdot N/2 = 0$.
5. Since $\sum R_i$ must be exactly 0, the initial assumption that $|R_i| > N/2$ for all $i$ is false.
6. Conclusion: There must exist at least one row $i$ such that $|R_i| \le N/2$.
7. Column Sums: The same logic applies to the column sums $K_j$.

Therefore, the condition required by the problem is satisfied by the row sums alone, proving that $C \le N/2$.

### [W2, round 1]
Constructed matrix M for N=230: M is a 2x2 block matrix where blocks are 115x115.
M = [[J, 0], [0, -J]], where J is the matrix of all ones.
This construction satisfies all constraints (entries in [-1, 1], sum=0).
The minimum of the absolute row and column sums for this matrix is 115. This provides a lower bound C >= 115.
