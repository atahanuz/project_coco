### [W1, round 1]
Calculations for L_N = ∑_{\pi\in S_N}\frac{\sigma(\pi)}{v(\pi)+1}:

N=2:
S_2 = {(1, 2), (2, 1)}.
(1, 2): sigma=1, v=2. Term = 1/3.
(2, 1): sigma=-1, v=0. Term = -1/1.
L_2 = 1/3 - 1 = -2/3.

N=3:
S_3 has 6 permutations.
v=3 (Id): 1 perm, sigma=1. Term = 1/4.
v=1: 3 perms (transpositions). All sigma=-1. Term = 3 * (-1/2) = -3/2.
v=0: 2 perms (3-cycles). All sigma=1. Term = 2 * 1 = 2.
L_3 = 1/4 - 3/2 + 2 = 1/4 - 6/4 + 8/4 = 3/4.

N=4:
We sum contributions A_k / (k+1), where A_k = sum of signs of permutations with k fixed points.
k=4: A_4 = 1. Term = 1/5.
k=3: A_3 = 0. Term = 0.
k=2: 6 permutations (transpositions of the remaining 2). All sigma=-1. A_2 = -6. Term = -6/3 = -2.
k=1: 8 permutations (1 fixed point, 3-cycles on remaining 3). All sigma=1. A_1 = 8. Term = 8/2 = 4.
k=0: 9 derangements. 6 (4-cycles, sigma=-1) + 3 (two transpositions, sigma=1). A_0 = -6 + 3 = -3. Term = -3/1 = -3.
L_4 = 1/5 + 0 - 2 + 4 - 3 = 1/5 - 1 = -4/5.

Results:
L_2 = -2/3
L_3 = 3/4
L_4 = -4/5

### [W3, round 1]
Analysis of the sum A(N, k) = \sum_{\pi: v(\pi)=k} \sigma(\pi):
1. By decomposing permutations with k fixed points into choosing k elements ($\binom{N}{k}$) and deranging the remaining N-k elements, we established A(N, k) = \binom{N}{k} A'(N-k), where A'(m) is the sum of signs of all derangements of m elements.
2. By calculating small cases (m=0, 1, 2, 3, 4), we found the pattern for A'(m) to be A'(m) = (-1)^(m+1)(m-1) for all m >= 0.
3. Therefore, A(N, k) = \binom{N}{k} (-1)^{N-k+1}(N-k-1).
4. The original sum S = \sum_{\pi\in S}\frac{\sigma(\pi)}{v(\pi)+1} can be rewritten as S = \sum_{k=0}^{N} \frac{A(N, k)}{k+1}.

### [W2, round 1]
Finding the sum of signs $C_k = \sum_{\pi: v(\pi)=k} \sigma(\pi)$:

Let $N$ be the total number of elements. We group permutations by $k = v(\pi)$.
$C_k = \binom{N}{k} C'_{N-k}$, where $C'_m$ is the sum of signs over all derangements of $m$ elements.

We found $C'_m$ using the Principle of Inclusion-Exclusion on the alternating sum $a_j = \sum_{\pi \in S_j} \sigma(\pi)$, where $a_0=1, a_1=1, a_j=0$ for $j \ge 2$.
$C'_m = \sum_{j=0}^m (-1)^j \binom{m}{j} a_{m-j}$.

The results for $C'_m$ are:
1. If $m=0$: $C'_0 = 1$.
2. If $m=1$: $C'_1 = 0$.
3. If $m \ge 2$: $C'_m = (-1)^m (1-m)$.

Therefore, the required sum of signs $C_k$ is:
1. If $k=N$ (i.e., $m=0$): $C_N = \binom{N}{N} C'_0 = 1$.
2. If $k=N-1$ (i.e., $m=1$): $C_{N-1} = \binom{N}{N-1} C'_1 = N \cdot 0 = 0$.
3. If $0 \le k \le N-2$ (i.e., $m=N-k \ge 2$): $C_k = \binom{N}{k} (-1)^{N-k} (1 - (N-k)) = \binom{N}{k} (-1)^{N-k} (k - N + 1)$.

The specific value for $N=2024$ is derived using these formulas. The task requested determination of $C_k$.

### [W4, round 1]
Derived formula for $L_N = \sum_{\pi\in S_N}\frac{\sigma(\pi)}{v(\pi)+1}$.

1. Grouping by fixed points $k$: $L_N = \sum_{k=0}^{N} \frac{1}{k+1} S_k$, where $S_k = \sum_{\pi \in A_k} \sigma(\pi)$.
2. Relating $S_k$ to derangements $D_{N-k}$: $S_k = \binom{N}{k} D_{N-k}^{\sigma}$, where $D_M^{\sigma} = \sum_{\pi' \in D_M} \sigma(\pi')$.
3. Using $D_0^{\sigma}=1$, $D_1^{\sigma}=0$, and $D_M^{\sigma} = (-1)^{M+1}(M-1)$ for $M \ge 2$.
4. Substituting $M=N-k$ and simplifying the summation leads to:
$L_N = \sum_{M=0}^{N} \frac{1}{N-M+1} \binom{N}{M} D_M^{\sigma}$.
5. Expanding and separating terms for $M=0, 1, M \ge 2$ yields the closed form (in summation notation):
$L_N = \frac{1}{N+1} + \sum_{M=2}^{N} \frac{1}{N-M+1} \binom{N}{M} (-1)^{M+1}(M-1)$.
This formula was verified for $N=1, 2, 3$. No simpler closed form was found.

### [W3, round 2]
The conjecture $L_N = (-1)^{N+1} \frac{N}{N+1}$ was proven by substituting the derived formula for $C_k = \sum_{\pi: v(\pi)=k} \sigma(\pi)$ into the sum $L_N$. The crucial step involved rewriting the summation using $\frac{1}{k+1}\binom{N}{k} = \frac{1}{N+1}\binom{N+1}{k+1}$ and applying binomial identities related to $(1-1)^{N+1}$. The derivation yields $L_N = \frac{(-1)^{N+1} N}{N+1}$, confirming the conjectured closed form.
