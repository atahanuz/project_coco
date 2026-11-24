### [W3, round 1]
Invariant Quantity Investigation:
The move replaces two box sizes $m_i, m_j$ with $m_{new} = m_i + m_j - 2k$.
The total sum of marbles $S$ changes by $m_{new} - m_i - m_j = (m_i + m_j - 2k) - m_i - m_j = -2k$.
Since $2k$ is even, the parity of the total sum of marbles, $S \pmod{2}$, is invariant.
Initial state: $2025$ boxes of size 1. $S_{initial} = 2025$.
$S_{initial} \equiv 1 \pmod{2}$.
Any final state must have an odd total number of marbles.

### [W1, round 1]
Analysis of the game for small initial numbers $N$, starting with $N$ boxes each containing 1 marble.
The move is interpreted as replacing two selected boxes ($B_i, B_j$) with a single new box ($B_{new}$) containing $(m_i - k) + (m_j - k)$ marbles, where $k \le \min(m_i, m_j)$. The two original boxes are discarded after modification.

For the initial state $M = \{1, 1, \ldots, 1\}$, any move must use $k=1$ on any pair of boxes, resulting in $m_i' = 0, m_j' = 0$, and $m_{new} = 0$. Since we only count non-empty boxes, this move effectively reduces the number of boxes by 2 (discarding the two original boxes and the new 0-marble box).

Results for small N:
N=3: {1, 1, 1} $\to$ {1}. Minimum non-empty boxes: 1.
N=4: {1, 1, 1, 1} $\to$ {1, 1} $\to$ {}. Minimum non-empty boxes: 0.
N=5: {1, 1, 1, 1, 1} $\to$ {1, 1, 1} $\to$ {1}. Minimum non-empty boxes: 1.

Conjecture based on these results: If all initial marbles are 1, the minimum number of non-empty boxes is 1 if N is odd, and 0 if N is even.

### [W2, round 1]
Initial state: 2025 boxes, all containing 1 marble.
Move: Select (m_A, m_B), choose k = min(m_A, m_B). New box size = (m_A - k) + (m_B - k).
For the initial state (1, 1), choosing k=1 results in a new box size of 0.
Since 2025 is odd, we can pair up 2024 boxes into 1012 pairs. Each pair results in an empty box (size 0).
We are left with 1012 empty boxes and 1 box containing the original 1 marble.
The minimum number of non-empty boxes (N_min) is 1.
