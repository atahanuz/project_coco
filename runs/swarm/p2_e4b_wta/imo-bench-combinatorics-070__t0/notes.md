### [W1, round 1]
Maximum independent set size of Knight's graph on M x N board is known. For M=40, N=60, total squares = 2400. Since both dimensions are even, the board has exactly 1200 squares of each color. As a knight always moves between colors, placing knights only on squares of the same color yields an independent set of size 1200, which is the maximum possible size. K = 1200.

### [W4, round 1]
[W4 analysis] The maximum number of non-attacking knights on the $40 \times 60$ board is 1200 (by placing them all on squares of the same color partition, since $40$ and $60$ are both even). Queenie's objective is to reduce this achievable number $K$ by placing queens on squares that Horst might otherwise use for his maximal independent set.

The key invariant to search for is how many squares of a given color partition (say, White) a single Queen can cover or occupy, relative to the geometry of the board. A Queen attacks across rows, columns, and diagonals. Since the knight placement is governed by color, we must analyze how effectively a Queen can target squares of a single color.

Hypothesis: The problem reduces to finding the minimum number of squares in one color partition that must remain unoccupied by queens, while still allowing for a guaranteed independent set of size $K$.

Next step: Analyze the worst-case scenario for Queenie: determining the maximum number of squares of one color partition she can "disable" with a small number of strategically placed queens. This will define the upper bound on $M_Q$ relative to $K$.

### [W3, round 1]
Investigation into Knight's Graph Bipartiteness (40x60 Board):
The chessboard coloring provides a natural bipartition of the $40 \times 60$ board into two sets of squares, $C_W$ (White) and $C_B$ (Black). Since $40 \times 60 = 2400$ (even), $|C_W| = |C_B| = 1200$.
In the Knight's graph, any independent set (a set of mutually non-attacking knights) must satisfy the condition that no two knights are adjacent. A set consisting entirely of squares of the same color is automatically an independent set.
Horst's optimal strategy, relying purely on the bipartite structure, is to commit all his knights to one color class, say $C_W$.
Queenie's worst-case strategy to minimize $K$ is to prioritize placing her queens on squares within $C_W$.
Since Horst and Queenie alternate turns, if both players focus their moves solely on $C_W$ (1200 available spots), they effectively split this pool. Horst gets one spot, Queenie gets one spot, and so on.
In this worst-case scenario, Horst can guarantee $K = \lceil 1200 / 2 \rceil = 600$ knights. This bound is independent of Queenie's move type (Queen vs. Knight) as long as she is constrained by the board state and her turn order.

### [W2, round 1]
Analysis for 10x10 board:
1. Maximum independent set ($K_{max}$) for the knight graph on 10x10 is 50 (by selecting all squares of one color, as knights must form a set of one color to be independent).
2. Queenie (minimizer) plays optimally by targeting one of the two maximal independent sets (e.g., all 50 white squares, $V_W$).
3. If Horst (maximizer) commits to $V_W$, and Queenie dedicates all her $Q$ moves to removing squares from $V_W$, the total number of squares used or blocked in $V_W$ is $K + Q$. Since $Q=K-1$, we have $K + (K-1) \le 50$, leading to $2K - 1 \le 50$, or $K \le 25.5$.
4. The maximal guaranteed number of knights Horst can place ($K$) is 25.
5. The minimum number of squares Queenie needs to occupy ($Q_{min}$) to force this outcome is $Q = K-1 = 24$.
Relationship recorded: $K=25$ achieved when $Q=24$ is played optimally by Queenie.
