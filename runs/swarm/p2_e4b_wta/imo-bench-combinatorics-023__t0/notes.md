### [W1, round 1]
K=4 entrées (E1, E2, E3, E4) are available. There are $\binom{4}{2} = 6$ possible distinct pairs of entrées. Since the goal is to maximize the total university payment, we should use all 6 possible pairs, meaning $N=6$ mathematicians.
Let $n_i$ be the popularity (number of orders) of entrée $E_i$.
In a complete graph $K_4$ (which corresponds to using all 6 pairs), each entrée $E_i$ is paired with the other 3 entrées. Thus, $n_1 = n_2 = n_3 = n_4 = 3$.
For any mathematician ordering $\{E_i, E_j\}$, the university pays $\min(n_i, n_j) = \min(3, 3) = 3$.
Since there are 6 mathematicians, the total maximum payment is $6 \times 3 = 18$.

### [W2, round 1]
--- Initial Constraints and Definitions ---

Let $M=2017$ be the number of mathematicians.
Let $E$ be the set of entrées, and $n_i$ be the popularity count for entrée $i$.

1.  **Total Order Constraint:** $\sum_{i \in E} n_i = 2M = 4034$.
2.  **Total Payment Definition:** $P = \sum_{(i, j) \in O} \min(n_i, n_j)$, where $O$ is the set of 2017 chosen pairs.
3.  **Target Investigation:** Constraints relating $P$ to $S_2 = \sum n_i^2$.

The maximization of $P$ is dependent on both the distribution of $\{n_i\}$ and the structure of the set of pairs $O$.

### [W3, round 1]
We aim to find the distribution of entrée counts $n_i$ closest to uniform, subject to $\sum_{i=1}^{65} n_i = 2 \times 2017 = 4034$.

The average count is $4034 / 65 \approx 62.06$.
The closest integer distribution is:
4 entrées with count 63.
61 entrées with count 62.

Let $C_{63}$ be the set of 4 entrées (count 63) and $C_{62}$ be the set of 61 entrées (count 62).
The university pays $\min(n_i, n_j)$ for each of the 2017 chosen pairs.
The possible payment values are 63 (if both are in $C_{63}$), 62 (if one is in $C_{63}$ and one in $C_{62}$, or both in $C_{62}$).

Let $N_{63, 63}$ be the number of pairs chosen entirely from $C_{63}$.
Total Payment $P = 63 \cdot N_{63, 63} + 62 \cdot (2017 - N_{63, 63})$
$P = 62 \cdot 2017 + N_{63, 63}$

To maximize $P$, we must maximize $N_{63, 63}$.
Since $|C_{63}| = 4$, the maximum number of distinct pairs possible from $C_{63}$ is $\binom{4}{2} = 6$.
Assuming this configuration is achievable while satisfying the degree constraints (which is standard practice for this type of optimization problem when dealing with uniform distributions), $N_{63, 63}^{\max} = 6$.

Maximum Payment Estimate:
$P_{\max} = 62 \times 2017 + 6$
$P_{\max} = 124954 + 6$
$P_{\max} = 124960$.

### [W2, round 1]
--- Theoretical Investigation: P vs. $\sum n_i^2$ ---

The quantity $P$ sums the minimum popularity counts over all chosen pairs. To relate this to the sum of squared popularities, $S_2 = \sum n_i^2$, we must consider how the pairing structure $O$ interacts with the distribution $\{n_i\}$.

1.  **Upper Bound on P (General observation):**
    Since $\min(n_i, n_j) \le n_i$ and $\min(n_i, n_j) \le n_j$, we have $\min(n_i, n_j) \le \frac{n_i + n_j}{2}$.
    $$P = \sum_{(i, j) \in O} \min(n_i, n_j) \le \sum_{(i, j) \in O} \frac{n_i + n_j}{2}$$
    Let $D_i$ be the degree of entrée $i$ (the number of times $i$ appears in the chosen pairs $O$). $D_i$ is not necessarily $n_i$, but $D_i \le n_i$. In fact, $\sum D_i = 2M$.
    $$P \le \frac{1}{2} \sum_{i \in E} D_i n_i$$
    Since $D_i \le n_i$ is not guaranteed (we only know $D_i$ is the count *within* the chosen set $O$), this bound isn't strong enough yet without knowing the optimal structure.

2.  **Relationship involving $S_2$ and Average Payment:**
    We know $S_2 = \sum n_i^2$. If we assume all $n_i$ are close to the average $\bar{n} = 2M/|E|$, then $S_2 \approx |E| \bar{n}^2$.

3.  **Investigating Maximization:**
    To maximize $P$ relative to $S_2$, we should look for distributions $\{n_i\}$ where the cost $\min(n_i, n_j)$ remains high, even when $S_2$ is large. High $S_2$ suggests large disparities in $n_i$.
    *   *Case 1: Uniform Distribution* ($n_i = C$). $S_2$ is minimized for a fixed sum $2M$. $P$ is maximized for a fixed $|E|$ if all chosen pairs are uniform, $P = M \cdot C$.
    *   *Case 2: Highly Skewed Distribution* ($n_1 \gg n_2, n_3, \dots$). $S_2$ is maximized. If $n_1$ is huge, most pairs involving $n_1$ will have the minimum determined by the smaller $n_j$. If all pairs involve $n_1$, $P \approx \sum \min(n_1, n_j) \approx \sum n_j$.

**Conjecture based on maximization:** P tends to be maximized when the popularity counts are relatively uniform, which *minimizes* $S_2$ for a fixed $|E|$. Therefore, maximizing $P$ *relative* to $S_2$ suggests finding conditions where $P$ is large while $S_2$ is constrained or low.

The immediate theoretical constraint we can state is the connection between $P$ and the sum of the chosen degrees: $P \le \frac{1}{2} \sum D_i n_i$. Since $D_i$ is fixed by the selection of $O$, this is the primary theoretical link. Further constraints require fixing $O$ or deriving bounds independent of $O$.

### [W2, round 1]
--- Summary of Theoretical Constraint ---

We derived the following primary inequality that relates the total university payment $P$ to the popularity counts $\{n_i\}$ and the structure of the chosen pairs $O$:

Let $D_i$ be the degree of entrée $i$ (i.e., the number of times $i$ appears in the $M=2017$ chosen pairs $O$).
$$P = \frac{1}{2} \left( \sum_{i \in E} D_i n_i - \sum_{(i, j) \in O} |n_i - n_j| \right)$$

**Conditions for Maximization relative to $\sum n_i^2$:**
To maximize $P$ relative to $S_2 = \sum n_i^2$, the configuration must minimize the penalty term $\sum |n_i - n_j|$ while maintaining a high $\sum D_i n_i$. This strongly suggests that the optimal configuration requires the popularity counts $\{n_i\}$ to be as uniform as possible (minimizing $S_2$) and the chosen pairs $O$ to ensure that the degrees $D_i$ are structured to maximize the weighted sum $\sum D_i n_i$ under the uniformity constraint. High variance in $n_i$ (high $S_2$) tends to increase the penalty term $\sum |n_i - n_j|$ significantly, thus reducing $P$ relative to the increase in $S_2$.
