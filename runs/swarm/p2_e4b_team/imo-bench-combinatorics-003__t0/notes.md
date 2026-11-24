### [W3, round 1]
Derivation for the position of the $k$-th flip, $P_k$.

Let $N = 2n+1$ be the total number of coins, indexed $0, 1, \dots, N-1$. Let $P_k$ be the position of the $k$-th coin flipped.

1. Initialization: We assume the process starts by flipping the coin at position 0. So, $P_1 = 0$.

2. Pattern Analysis: The procedure describes a pattern of skips followed by a flip.
    - From $P_1$ to $P_2$: "one coin is flipped [P1], the next coin is skipped, the next coin is flipped [P2]". This implies a skip of 1 coin. The step size is $1 (\text{skip}) + 1 (\text{flip}) = 2$. $P_2 = P_1 + 2 \pmod N$.
    - From $P_2$ to $P_3$: "the next two coins are skipped, the next coin is flipped [P3]". This implies a skip of 2 coins. The step size is $2 (\text{skip}) + 1 (\text{flip}) = 3$. $P_3 = P_2 + 3 \pmod N$.
    - Generally, from $P_{k-1}$ to $P_k$ (for $k \ge 2$): The number of skips is $s_{k-1} = k-1$. The step size is $(k-1) + 1 = k$.

3. Recurrence Relation:
The position $P_k$ satisfies the recurrence relation:
$P_1 = 0$
$P_k = P_{k-1} + k \pmod{2n+1}, \quad \text{for } k \ge 2$.

4. Closed Form Formula:
Summing the steps:
$P_k = \sum_{j=2}^{k} j + P_1 \pmod{2n+1}$
$P_k = \left( \sum_{j=1}^{k} j \right) - 1 \pmod{2n+1}$
$P_k = \left( \frac{k(k+1)}{2} - 1 \right) \pmod{2n+1}$.
