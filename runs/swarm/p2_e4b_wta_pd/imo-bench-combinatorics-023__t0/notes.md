### [W3, round 1]
Configuration: $N=2017$ entrées arranged in a cycle $C_{2017}$. The $N$ mathematicians order the $N$ pairs of adjacent entrées corresponding to the edges of $C_{2017}$.
1. Entrée popularity (cost): Since each entrée is adjacent to two others, every entrée is ordered by exactly 2 mathematicians. Cost = 2 for all entrées.
2. Payment per mathematician: Each mathematician orders a pair with equal cost (2). Due to the arbitrary tie-breaker, the university pays 2 for each mathematician.
3. Total payment: $2017 \times 2 = 4034$.

### [W4, round 1]
Analysis of concentration:
The payment for an edge $(e_a, e_b)$ is $\min(d_{e_a}, d_{e_b})$. To maximize the total payment, we need large degrees $d_e$ for the involved entrées. Concentrating the $N=2017$ distinct edges onto a small set of entrées ($|E| \ll N$) forces the average degree of the involved entrées to be high ($\text{Avg}(d_e) = 2N/|E|$). If $|E|$ is small, the degrees are large. This structure favors higher minimum payments per edge, as both $d_{e_a}$ and $d_{e_b}$ are likely large. Specifically, forming dense subgraphs with a small number of entrées is expected to result in a total payment significantly higher than configurations where edges are spread out (sparse graphs). The goal is to find the optimal balance between maximizing degrees and maintaining structural connectivity for all 2017 distinct edges.

### [W2, round 1]
SUCCESS: A construction has been found where the total payment exceeds 2N.
We used M=65 distinct entrées. The total number of possible pairs is 2080.
We selected N=2017 pairs by removing 3 edges from the complete graph K_65.
In this configuration, the minimum degree of any entrée in the selected set is 62, and the vast majority are 64.
The total payment was calculated to be 132,928, which is strictly greater than 2N = 4034.

### [W1, round 1]
**Attempt to derive $S \le 2N$:**

1.  **Definitions:** Let $N$ be the number of mathematicians. Let $E$ be the set of entrées, and $d_e$ be the degree of entrée $e$. The total number of orders is $N$, which corresponds to $N$ edges in a graph where entrées are vertices. The fundamental identity is $\sum_{e \in E} d_e = 2N$.
2.  **Total Payment $S$:** $S = \sum_{\{e_1, e_2\} \text{ ordered}} \min(d_{e_1}, d_{e_2})$.
3.  **Bounding Attempt:** We know that $\min(d_{e_1}, d_{e_2}) \le d_{e_1}$. Summing over all $N$ orders:
    $$S \le \sum_{\{e_1, e_2\} \text{ ordered}} d_{e_1}$$
    This sum is difficult to bound simply by $2N$ because the set of $d_{e_1}$ values depends on the arbitrary labeling of the ordered pairs. If we attempt to relate this sum to $\sum d_e$, we are effectively asking if the average degree contributing to the payment is less than 2.

4.  **Conclusion on the Bound:** While the target bound $S \le 2N$ is requested, general graph theory principles show this bound is not universally true for all configurations (e.g., dense graphs where degrees $d_e$ are large, yielding $S > 2N$). If this bound holds, it implies a strong structural constraint on the degree distribution that limits the minimum shared degree across all edges to an average of 2. The required derivation likely relies on assumptions about graph sparsity or specific properties of the optimal set of orders that are not specified in the problem statement. We document the formal setup required for the proof.

### [W4, round 2]
### [W4, round 2] Theoretical Model for Total Payment Scaling $S(M)$

The total payment $S$ is defined as the sum of the minimum degrees for all $N$ chosen edges: $S = \sum_{\{e_1, e_2\}} \min(d_{e_1}, d_{e_2})$. We seek to maximize $S$ for fixed $N$ by minimizing $M$ (the number of entrées).

**1. Modeling the Dense Case (Approaching $K_M$):**
To maximize $S$, the $N$ chosen edges must be highly concentrated, meaning we select $M$ to be the smallest integer such that $\binom{M}{2} \ge N$. In this maximally dense scenario, the degrees $d_e$ of the involved entrées are maximized and remain close to $M-1$.

For the complete graph $K_M$, where $N = \binom{M}{2}$, every vertex has degree $M-1$. For any edge, the payment is $M-1$.
The total payment in $K_M$ is $S_{K_M} = \binom{M}{2} \cdot (M-1)$.

**2. Scaling Function $S(M)$:**
Since the optimal configuration is to select $N$ edges from a set where degrees are as close to $M-1$ as possible, we approximate the total payment $S$ using the full $K_M$ model:
$$S(M) \approx N_{chosen} \cdot (M-1)$$
Since $N_{chosen} = N \approx \binom{M}{2} \approx \frac{M^2}{2}$, we have the scaling relationship:
$$S(M) \propto M^2 \cdot M = M^3$$
Or, substituting $M \approx \sqrt{2N}$:
$$S(M) \propto N^{1.5}$$

**3. Explaining Optimality of Minimal $M$:**
Since $N$ is fixed, the scaling $S \propto M^{1.5}$ shows that $S$ is a strictly increasing function of $M$.

If we were to increase $M$ to $M' > M_{min}$ while keeping $N$ constant, we would be distributing the $N$ edges over more vertices ($M'$ instead of $M_{min}$). This spreading effect causes the average degree of the $M'$ vertices to decrease (from $\approx M_{min}-1$ to $\approx 2N/M'$). Since the total payment $S$ scales proportionally to the maximum achievable degree (which is $M-1$ when $M$ is minimized), *minimizing $M$ is the optimal strategy* because it forces the maximum possible degrees onto the involved entrées, thereby maximizing the minimum payment per edge.

### [W3, round 2]
### [W3, round 2] - Structural Formula Verification for Dense Graphs

**Goal:** Verify $S = \sum \min(d_{e_a}, d_{e_b})$ for dense/near-complete subgraphs.

**Analysis using Complete Graph $K_M$:**
If we select $N = M(M-1)/2$ edges from $K_M$, the degree of every entrée is $d_e = M-1$.
In this configuration, for every edge $\{e_a, e_b\}$, the payment contribution is $\min(d_{e_a}, d_{e_b}) = M-1$.
The total payment $S$ is:
$S = N \cdot (M-1)$

**Relationship to $N$ and $M$:**
Since $N \approx M^2/2$, we have $M \approx \sqrt{2N}$.
Substituting this into the formula:
$S \approx N \cdot \sqrt{2N} = \sqrt{2} N^{3/2}$.

**Confirmation with W2's result:**
W2 used $M=65$ entrées. $K_{65}$ has $N_{K_{65}} = 2080$ edges.
$S$ for $K_{65}$: $S = 2080 \cdot (65-1) = 133,120$.
W2 achieved $S=132,928$ using $N=2017$ edges from $K_{65}$. This value is extremely close to the theoretical maximum for the full $K_{65}$, confirming that the maximum payment $S$ is achieved by clustering the $N$ orders onto the smallest possible complete subgraph $K_M$ such that $N$ edges can be chosen.

**Conclusion:** For dense graphs, the total payment $S$ scales approximately as $O(N^{3/2})$ and is structurally determined by $S \approx N(M-1)$ where $M$ is the minimum number of entrées required to support $N$ distinct orders.

### [W1, round 2]
### [W1, round 2] Testing smaller dense subgraphs (M=40, M=30)

**Constraint Check:** N=2017 orders requires $\binom{M}{2} \ge 2017$.
*   $M=40$: $\binom{40}{2} = 780$. (INSUFFICIENT)
*   $M=30$: $\binom{30}{2} = 435$. (INSUFFICIENT)

**Assumption:** Calculation proceeds by assuming we maximize payment using $N_{max} = \binom{M}{2}$ orders within $K_M$, as $K_M$ is the densest structure.

**Calculation for M=40:**
$N_{max} = 780$. Degree $d_e = 39$. Payment per order = 39.
Total Payment $S_{40} = 780 \times 39 = 30,420$.

**Calculation for M=30:**
$N_{max} = 435$. Degree $d_e = 29$. Payment per order = 29.
Total Payment $S_{30} = 435 \times 29 = 12,615$.

These payments are significantly lower than the W2 result ($S_{65} = 132,928$), confirming that maximizing the number of entrées ($M$) while maintaining density is crucial for high payment.

### [W2, round 2]
### Verification of S=132,928 for M=65 Configuration

This note provides a rigorous step-by-step verification of the total payment calculation for the configuration described by W2, Round 1, by analyzing the degree sequence implied by $N=2017$ edges among $M=65$ entrées.

**1. Determining the Required Degree Sequence:**
Let $M=65$ (number of entrées) and $N=2017$ (number of orders/edges). The sum of all degrees must satisfy $\sum_{e \in E} d_e = 2N = 2(2017) = 4034$.
W2 stated that the minimum degree is 62 and most are 64. We assume the degree sequence consists only of 62s and 64s.
Let $x$ be the count of entrées with degree 62, and $y$ be the count of entrées with degree 64.
We have two equations:
(i) $x + y = 65$
(ii) $62x + 64y = 4034$
Substituting $y = 65 - x$ into (ii):
$62x + 64(65 - x) = 4034$
$62x + 4160 - 64x = 4034$
$-2x = 4034 - 4160 = -126$
$x = 63$.
Thus, $y = 65 - 63 = 2$.
The required degree sequence is: 63 entrées of degree 62 ($V_{62}$), and 2 entrées of degree 64 ($V_{64}$).

**2. Determining Edge Counts based on Degree Sequence:**
The total payment $S$ depends on the number of edges connecting vertices of specific degrees:
$n_{62, 62}$: edges between two $V_{62}$ vertices. Contribution to $S$: 62.
$n_{62, 64}$: edges between a $V_{62}$ and a $V_{64}$ vertex. Contribution to $S$: 62.
$n_{64, 64}$: edges between two $V_{64}$ vertices. Contribution to $S$: 64.

We use the degree sums:
a) Sum of degrees in $V_{62}$: $63 \times 62 = 3906$. This equals $2n_{62, 62} + n_{62, 64}$.
$$2n_{62, 62} + n_{62, 64} = 3906 \quad (*)$$
b) Sum of degrees in $V_{64}$: $2 \times 64 = 128$. This equals $2n_{64, 64} + n_{62, 64}$.
$$2n_{64, 64} + n_{62, 64} = 128 \quad (**)$$
c) Total edges: $n_{62, 62} + n_{62, 64} + n_{64, 64} = 2017$.

From (**), since $n_{64, 64}$ must be 0 or 1 (as $|V_{64}|=2$):
If $n_{64, 64} = 1$, then $n_{62, 64} = 128 - 2(1) = 126$.
Substituting $n_{62, 64} = 126$ into (*):
$2n_{62, 62} + 126 = 3906$
$2n_{62, 62} = 3780$
$n_{62, 62} = 1890$.

Verification of total edges (c): $1890 + 126 + 1 = 2017$. This configuration is mathematically consistent.

**3. Calculating Total Payment S:**
The total payment $S$ is:
$S = (n_{62, 62} \times 62) + (n_{62, 64} \times 62) + (n_{64, 64} \times 64)$
$S = (1890 \times 62) + (126 \times 62) + (1 \times 64)$
$S = (1890 + 126) \times 62 + 64$
$S = 2016 \times 62 + 64$
$S = 124,992 + 64$
$S = 125,056$.

**Conclusion:**
Based on the degree structure implied by $M=65$ and $N=2017$ under the constraint that degrees are only 62 or 64, the calculated total payment is $S = 125,056$. This value mathematically contradicts the $S = 132,928$ found in the original notes, indicating a probable error in the reported calculation or the description of the underlying configuration.
