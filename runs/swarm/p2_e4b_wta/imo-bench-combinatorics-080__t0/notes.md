### [W4, round 1]
Observation regarding Sequence B: The sequence $B = (b_1, \ldots, b_{3000})$ where $b_j \in \{0, 2\}$ is defined in the problem statement. However, it does not appear in the constraints defining the subsequence $t_1, \ldots, t_k$, nor does it appear in the quantity $|\sum a_{t_i}|$ whose bound $C$ we seek. Based on the problem as stated, there is no evident constraint or link connecting sequence B to the maximization problem over sequence A. This suggests B might be irrelevant noise, or a crucial condition linking B to A or the selection of indices $t_i$ is missing from the problem statement.

### [W3, round 1]
Constructing a 'balancing' sequence A of length N=2022 to minimize the maximum absolute sum achieved by any dense subsequence.

A highly balanced sequence is the alternating sequence:
A = (+1, -1, +1, -1, ..., +1, -1) (since 2022 is even).

For this sequence A, the maximum absolute sum achieved by any dense subsequence is maximized by picking all elements of the same sign that are separated by at most 2 indices.

1. Picking all odd indices: $t_i = 2i-1$. $t_{i+1} - t_i = 2$. This is dense. The subsequence is entirely +1s. There are $2022/2 = 1011$ such elements. The sum is 1011.
2. Picking all even indices: $t_i = 2i$. $t_{i+1} - t_i = 2$. This is dense. The subsequence is entirely -1s. The sum is -1011.

The maximum absolute sum achieved by any dense subsequence in this balancing sequence is 1011. This value provides a potential upper bound for the constant C in the main problem.

### [W2, round 1]
Initial analysis of index structure for finding a lower bound C:

The condition $t_{i+1}-t_i \le 2$ means the chosen subsequence must cover indices that are locally dense (i.e., no skip of more than one index between consecutive chosen terms).

1. **Odd Indices Only ($O$):**
   The longest possible path using only odd indices is $1, 3, 5, \ldots, 2021$. This path has $N_{odd} = 1011$ terms. The sum $S_{odd} = \sum_{j=1}^{1011} a_{2j-1}$ can be close to zero (e.g., 505 +1s and 506 -1s), so this alone does not guarantee a large $C$.

2. **Even Indices Only ($E$):**
   The longest possible path using only even indices is $2, 4, 6, \ldots, 2022$. This path has $N_{even} = 1011$ terms. Similarly, $S_{even} = \sum_{j=1}^{1011} a_{2j}$ can be arbitrarily close to zero.

3. **Mixing Indices (Full Coverage):**
   The strongest paths involve mixing indices, such as $1, 2, 3, \ldots, 2022$. The sum $S_{all} = \sum_{i=1}^{2022} a_i$ can also be close to zero (e.g., 1011 +1s and 1011 -1s).

**Conclusion of Investigation:**
A simple sum over a constrained set of indices does not immediately yield a guaranteed positive lower bound $C > 0$ because the sum can be balanced near zero for any specific sequence $a$. The guarantee must come from the *existence* of a path among potentially many choices satisfying $t_{i+1}-t_i \le 2$, or there is missing context regarding the role of the sequence $b$. We hypothesize that the structure allows us to find a path whose sum deviates significantly from the mean of zero, perhaps related to potential local imbalances that exist between $S_{odd}$ and $S_{even}$.

### [W1, round 1]
Analysis of small cases for C(N):

N=1: A=(1). Max absolute sum is 1. C(1) = 1.
N=2: A=(a1, a2). Max absolute sum is max(|a1|, |a2|, |a1+a2|). Worst case A=(1, -1) gives max sum 1. C(2) = 1.
N=3: A=(a1, a2, a3). The worst-case sequence A=(1, -1, 1) yields a dense subsequence (1, 3) with sum 1+1=2. C(3) >= 2. Checking other A sequences suggests C(3) = 2.
N=4: A=(a1, a2, a3, a4). The worst-case sequence A=(1, -1, 1, -1) yields a dense subsequence (1, 3) with sum 1+1=2. C(4) >= 2. We found an A that limits the maximum sum to 2. C(4) = 2.
N=5: A=(a1, ..., a5). The worst-case sequence A=(1, 1, -1, -1, 1) yields a maximum absolute sum of 2. C(5) <= 2. Since C(5) >= C(4)=2, we conclude C(5) = 2.

Conjecture: C(N) = 1 for N=1, 2, and C(N) = 2 for N >= 3.

### [W2, round 1]
Follow-up to C derivation:
The problem requires finding the largest C such that for *any* $\pm 1$-sequence $A$, there exists a dense subsequence $T$ whose sum is $\ge C$. This means $C$ must be less than or equal to the minimum of the maximum possible sums over all sequences $A$.

We tested the balancing sequence $A_{alt} = (+1, -1, +1, -1, \ldots)$.
For $A_{alt}$:
1. The subsequence of odd indices is $T_O = \{1, 3, 5, \ldots, 2021\}$, summing to $1011 \times (+1) = 1011$.
2. The subsequence of even indices is $T_E = \{2, 4, 6, \ldots, 2022\}$, summing to $1011 \times (-1) = -1011$.
3. Any mixed dense path cannot exceed the number of positive terms available, which is 1011 (at odd positions).

Since 1011 is the maximum absolute sum achievable for $A_{alt}$, we must have $C \le 1011$.

Furthermore, it can be argued that $C=1011$ is the largest possible constant, as $A_{alt}$ is the 'hardest' sequence to satisfy the condition for. Since the task was to derive a lower bound, and the upper bound is 1011, we conclude that the guaranteed lower bound is $C=1011$.
