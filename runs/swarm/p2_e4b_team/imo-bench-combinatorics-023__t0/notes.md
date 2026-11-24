### [W2, round 1]
Analysis for the symmetric scenario ($C$ constant):
1. Necessary relationship: The total number of orders must be $2N$. Since there are $K$ entrées each ordered $C$ times, the relationship is $K \cdot C = 2N$. For $N=2017$, $K \cdot C = 4034$.
2. Combinatorial constraint: We require $\binom{K}{2} \ge N$, so $K(K-1) \ge 4034$. This requires $K \ge 65$.
3. Minimum $K$: Since $K$ must be a divisor of 4034, and $2017$ is prime, the divisors are $\{1, 2, 2017, 4034\}$. The smallest divisor satisfying $K \ge 65$ is $K=2017$.
4. Payment calculation: If $K=2017$, then $C = 4034 / 2017 = 2$. Since every entrée costs $C=2$, every mathematician's payment is 2. Total payment = $N \times 2 = 2017 \times 2 = 4034$.

### [W1, round 1]
Case N=3 analysis:
We aim to maximize the total payment $\sum_{i=1}^3 \min(C_{A_i}, C_{B_i})$. The total number of orders is $2N=6$.
The optimal configuration is achieved by using the minimum number of entrées ($K=3$) such that all pairs are distinct. Let the entrées be {1, 2, 3}.
The three mathematicians (M1, M2, M3) choose the complete set of possible pairs:
M1 orders {1, 2}.
M2 orders {1, 3}.
M3 orders {2, 3}.

Resulting Entrée Counts:
C1 (for entrée 1): Ordered by M1, M2. Count = 2.
C2 (for entrée 2): Ordered by M1, M3. Count = 2.
C3 (for entrée 3): Ordered by M2, M3. Count = 2.

Total University Payment:
M1 pays: min(C1, C2) = min(2, 2) = 2.
M2 pays: min(C1, C3) = min(2, 2) = 2.
M3 pays: min(C2, C3) = min(2, 2) = 2.
Total = 2 + 2 + 2 = 6.

Attempts with more entrées (e.g., K=4) resulted in unbalanced costs (e.g., counts (3, 1, 1, 1)), leading to a total payment of 3, which is less than 6.
The maximum total payment is 6.

### [W4, round 1]
ANALYSIS OF UPPER BOUND AND CONSTRAINTS:

1.  **Constraints:** We have $N=2017$ mathematicians, each ordering a pair of distinct entrées. The total number of ordered entrée instances is $2N = 4034$. Let $M$ be the total number of distinct entrées. The total count constraint is $\sum_{i=1}^M c_i = 2N = 4034$.
2.  **Pairing Constraint:** Since all pairs must be distinct, $M$ must satisfy $\binom{M}{2} \ge 2017$. We found the minimum required number of entrées is $M_{min} = 65$, since $\binom{65}{2} = 2080$.
3.  **Total Payment:** The total paid is $P = \sum_{\{i, j\} \text{ ordered}} \min(c_i, c_j)$.
4.  **Relationship to $2N$:** The total paid $P$ is a sum of minimums. To maximize $P$, we must maximize the values of $\min(c_i, c_j)$. This is generally achieved when the counts $c_i$ are distributed as evenly as possible among the available $M_{min}$ entrées.
5.  **Upper Bound Formulation:** If we could perfectly distribute the $2N$ counts among $M_{min}$ entrées, the average count would be $\bar{c} = 4034/65 \approx 62.06$. The optimal integer distribution found was 4 entrées with count 63, and 61 entrées with count 62. Assuming the pairings allow us to maximize the minimums (i.e., almost every pair is formed by entrées whose counts are both 62 or 63), the maximum total paid approaches $N \times \bar{c}$.

Upper Bound: $P \le N \cdot \lceil 2N / M_{min} \rceil$. Using $M_{min}=65$, this gives an upper bound based on the average count of the most frequent entrée type. A tighter theoretical upper bound assumes perfect pairing around the mean count: $P_{upper} \approx 2017 \times (4034/65) \approx 125274$.

### [W3, round 1]
Investigation into the role of K:
The problem aims to maximize the total university payment, $P_{total} = \sum_{M} \min(n_1, n_2)$, where $n_i$ is the count of mathematicians ordering entrée $i$. We have $N=2017$ mathematicians, so the total number of entrée selections is $2N = 4034$. Thus, the average order count across all $K$ dishes is $n_{avg} = 2N/K = 4034/K$.

To maximize $P_{total}$, we intuitively want to maximize the individual minimums, which means we want the counts $n_i$ to be as close to each other as possible (uniform distribution). For a fixed sum $\sum n_i = 2N$, the most uniform distribution occurs when $K$ is minimized, provided that a uniform distribution is achievable.

The minimum possible value for $K$ is $K_{min}=65$, which satisfies $\binom{65}{2} = 2080 \ge 2017$. This minimum value of $K$ forces the average order count $n_{avg}$ to be maximized: $n_{avg} = 4034/65 \approx 62.06$.

If $K$ is increased beyond $K_{min}$, $n_{avg}$ decreases proportionally. For example, if we choose $K=4034$ (the maximum possible relevant $K$ such that all $n_i \ge 1$ could theoretically exist), $n_{avg}=1$. In this case, every pair has $\min(1, 1) = 1$, yielding $P_{total}=N=2017$.

Since $P_{total}$ is strongly correlated with the average order count $n_{avg}$ (and we can expect $P_{total} \approx N \cdot n_{avg} \cdot C$ where $C$ is a factor close to 1), decreasing $K$ maximizes $n_{avg}$ and thus maximizes the potential total payment.

Conclusion: Restricting $K$ to the minimum possible value, $K=65$, appears to be optimal because it forces the highest possible average dish popularity ($n_{avg}$).

### [W1, round 2]
### [W1, Analysis of W2 vs Optimal Distribution]
W2's result of 4034 arose from imposing a strict symmetry constraint: that all $K$ dishes must have the same order count $C$. To satisfy this and the combinatorial constraint ($K \ge 65$), W2 was forced to use $K=2017$ dishes, resulting in $C=2$ for all of them. This uniformity limits the payment significantly: the university pays $\min(2, 2) = 2$ for every single mathematician, yielding a total payment of $2N = 4034$.

In contrast, the approach suggested by W3/W4 indicates that the optimal solution involves minimizing $K$ to $K_{min}=65$. This non-symmetric distribution allows the $2N=4034$ total orders to be spread across fewer dishes, maximizing the average popularity $\bar{c} = 4034/65 \approx 62.06$. When dish popularity is much higher, the minimum payment for each mathematician increases dramatically. The strict symmetry requirement of W2 prevents the system from concentrating popularity onto a smaller set of highly demanded entrées, thereby severely limiting the maximum possible total payment compared to an uneven but optimally balanced distribution using $K=65$.
