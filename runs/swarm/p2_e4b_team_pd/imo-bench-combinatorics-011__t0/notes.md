### [W1, round 1]
Investigation for N=4:
If Ronaldo chooses a fixed direction for all steps (e.g., all clockwise, $d_i = +1$), the total distance covered along the circle is $D = \sum_{i=1}^4 c_i$.
If $D < 1$, then there is guaranteed to be a continuous arc of length $1 - D$ that is never visited or run across, regardless of the specific values of $c_i$, as long as they are positive.
This establishes a pattern: when the sum of step lengths is small compared to the circumference (1), a guaranteed gap exists.

The problem asks what happens when $c_i < C$ for *all* $i$. If we choose $C < 1/4$, then $\sum c_i < 1$, and Ronaldo can guarantee a gap by always moving in the same direction. This suggests the critical constant $C$ must be at least $1/4$. Further investigation is needed for cases where $\sum c_i \ge 1$ but $c_i < C$.

### [W4, round 1]
The critical constant C is related to 1/2. If C > 1/2, it is possible to construct sequences $c_i$ (e.g., constant $c_i = 1/2$) that force the entire circle to be covered, regardless of Ronaldo's strategy. Therefore, the constraint that $C$ must satisfy to prevent total coverage is $C \le 1/2$.

### [W3, round 1]
Conjecture/Finding: The largest constant C for which avoidance is possible is $C=1/2$.

Derivation attempt:
Ronaldo can ensure avoidance if he can keep his net displacement $S_N = \sum_{i=1}^N d_i c_i$ (where $d_i = \pm 1$) bounded by $M < 1/2$. If $|S_N| \le M$, then the path is confined to an arc of length at most $2M$, which is less than the circumference 1, guaranteeing an unvisited point.

Ronaldo can achieve this boundedness using a greedy strategy: At step $N$, choose $d_N$ to minimize $|S_N| = |S_{N-1} + d_N c_N|$. This optimal strategy ensures that $|S_N| \le \max(|S_{N-1}|, c_N)$.

If we require that $|S_N|$ remains strictly less than $1/2$ for all $N$, we must choose directions such that $|S_{N-1}|$ and $c_N$ are both less than $1/2$.

If $c_i < 1/2$ for all $i$, then by the greedy strategy, $|S_N| < 1/2$ for all $N$. Thus, the property holds if $C \le 1/2$.

Since $C=1/2$ guarantees the property (by considering $c_i < 1/2$), a lower bound for $C$ is $1/2$.

### [W2, round 1]
Analysis of Uncrossed Point Constraint:
Let $s_i \in \{-1, 1\}$ represent the choice of direction for the $i$-th run ($s_i=1$ for CCW, $s_i=-1$ for CW). Let $c_i$ be the distance.
The position after $k$ steps is $P_k = \sum_{i=1}^k s_i c_i \pmod{1}$. We assume the starting point is $P_0=0$.

A point $x$ on the circle is never visited or crossed if the entire path of Ronaldo remains confined to an arc strictly shorter than the circumference (i.e., an arc of length $L < 1$).

The condition on the sequence of signs $\{s_i\}$ that ensures the path remains confined to an arc of length $L < 1$ (and thus guarantees the existence of an unvisited/uncrossed point $x$) is:
$$\max_{k \ge 0} \left( \sum_{i=1}^k s_i c_i \right) - \min_{k \ge 0} \left( \sum_{i=1}^k s_i c_i \right) < 1$$
(Where the sum for $k=0$ is 0).

This constraint bounds the total displacement range in the unwrapped real line $\mathbb{R}$. If this range is less than 1, all positions $P_k$ fall into an arc of length less than 1 on the circle, meaning there must be points outside that arc which are never visited or crossed.
