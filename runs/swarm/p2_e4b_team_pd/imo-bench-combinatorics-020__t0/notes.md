### [W1, round 1]
Foundational Calculations for the 40-team tournament:
1. Total number of possible unique games (pairs) among 40 teams: $\binom{40}{2} = 780$.
2. In each round, 20 games are played.
3. The theoretical maximum number of rounds, $a_{max}$, before all possible games must have been played is $\lfloor 780 / 20 \rfloor = 39$. This represents the maximum possible length of a round-robin tournament under the given constraints.

### [W2, round 1]
The problem asks for the smallest integer $a$ such that if we have $a$ edge-disjoint perfect matchings $M_1, M_2, \ldots, M_a$ in $K_{40}$, the graph $G = \bigcup_{i=1}^a M_i$ is such that its complement $\bar{G} = K_{40} \setminus G$ does not contain any perfect matching. This ensures that any $(a+1)$-th round must reuse an edge already played.

### [W4, round 1]
Investigation of the case $a=39$:
The tournament involves $N=40$ teams. Each round consists of 20 games.
The total number of possible games between 40 teams is $\binom{40}{2} = 780$.
After 39 rounds, the total number of games played is $39 \times 20 = 780$.
Since the maximum number of games between any two teams is 1, after 39 rounds, every possible pair of teams must have played exactly one game.
The graph $G_{39}$ representing the played games is therefore the complete graph $K_{40}$.

Condition check: If one more round is taken, it requires forming a perfect matching $M_{40}$ on $K_{40}$. Since $G_{39} = K_{40}$, every edge in $M_{40}$ is an edge present in $G_{39}$. Thus, every pair in the hypothetical 40th round has already played a game. The condition is met for $a=39$.

### [W3, round 1]
Investigating a=38: We are looking for a schedule of 38 rounds such that the 20 unplayed matchups form a perfect matching. The total number of matchups in K_40 is 780. 38 rounds cover 760 matchups, leaving 20 needed. Since K_40 (where N=40 is even) possesses a 1-factorization consisting of N-1 = 39 perfect matchings, we can schedule 38 rounds such that the 39th perfect matching remains unplayed. Therefore, such a schedule exists, and a=38 is too small.
