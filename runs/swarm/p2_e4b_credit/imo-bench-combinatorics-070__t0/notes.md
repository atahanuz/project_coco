### [W3, round 1]
ANALYSIS START: Queenie's restriction strategy.

The game's core is finding the maximum independent set (MIS) in the knight's graph ($G_{40 \times 60}$). The theoretical maximum MIS size ($\alpha(G)$) is 1200 (half the board). Queenie's goal is to place queens ($Q_W$) such that the MIS in the remaining graph ($G'$) is minimized.

1.  **Mechanism of Restriction:** Queens do not directly attack knights; they cover empty squares. By covering squares, Queenie eliminates potential knight placement sites. Furthermore, she aims to cover 'critical' squares—those that are highly connected to other potential knight sites, thereby breaking up large, independent sets.

2.  **Estimation Strategy (Coverage):** Since the board is large ($N=3600$), a small number of queens cannot cover everything. We estimate the number of queens ($Q$) required to reduce the available square count drastically.
    *   A single queen placed centrally on a $40 \times 60$ board can cover roughly $40 + 60 - 1$ (row + column) plus diagonal coverage. A conservative estimate for average coverage, $C_{avg}$, might be around 50-60 squares, accounting for overlaps and boundary effects.
    *   To significantly restrict the space, Queenie must aim to eliminate a substantial fraction of the 3600 potential knight spots. If she successfully eliminates 50% of the board (1800 squares), the knight count $K$ is potentially halved to 600.
    *   Required Queens: $Q \approx 1800 / C_{avg}$. Using $C_{avg} \approx 50$, we estimate $Q \approx 36$ queens.

3.  **Focus on Criticality:** While pure coverage is important, Queenie's most effective strategy is to place queens such that they isolate large sections of the board, specifically targeting squares that bridge components of the largest possible independent set. This focuses the density requirement on creating 'holes' in the connectivity map.

CONCLUSION: To maximally restrict the space for knights, Queenie must aim for a high-density placement strategy, targeting approximately 35-40 queens to eliminate half the available squares and severely degrade the graph structure required for a large independent set. This estimation provides the necessary scale for future search for the precise value of K.
ANALYSIS END

### [W1, round 1]
Simulation on 8x8 board (10 turns):
Observation: Queenie's role is primarily to eliminate squares from the set of available placements for Horst. Since Horst's constraint is purely based on knight attacks between knights, Queenie's presence (a White Queen on a square) does not change the attack pattern between knights, only the availability of the square itself.
Queenie's worst-case strategy is thus equivalent to a vertex removal strategy on the knight's graph: she removes the most critical empty vertices (squares) that would contribute to the Maximum Independent Set (MIS) of the board.
In the simulated runs, Queenie targeted central squares, a reasonable heuristic for maximizing board disruption.
Conclusion for small boards: The problem boils down to finding the MIS of the Knight's graph, minus the vertices occupied by Queenie.
The simulation placed 10 knights before exhausting options. This suggests a significant, but not dominating, effect from Queenie's blocking.

### [W2, round 1]
### [W2, round 1] MIS Calculation for 40x60 Knight's Graph
The task is to determine the Maximum Independent Set ($\alpha(G)$) of the Knight's Graph on a $40 \times 60$ board.
1.  **Graph Properties:** The Knight's Graph on any standard chessboard grid is bipartite. The squares can be colored black and white (W and B), and a knight always moves between squares of different colors.
2.  **Board Size:** The total number of vertices is $|V| = 40 \times 60 = 2400$.
3.  **Partitions:** Since $N$ and $M$ are both even, the two partitions ($W$ and $B$) are perfectly balanced: $|W| = |B| = 1200$.
4.  **Maximum Independent Set:** Since the graph is bipartite, the size of the MIS, $\alpha(G)$, is related to the size of the maximum matching, $\mu(G)$, by $\alpha(G) = |V| - \mu(G)$.
5.  **Perfect Matching:** For large boards with even dimensions (like $40 \times 60$), it is known that the Knight's Graph admits a perfect matching, meaning $\mu(G) = |V|/2 = 1200$.
6.  **Result:** Therefore, $\alpha(G) = 2400 - 1200 = 1200$.

The theoretical maximum number of non-attacking knights is 1200. This answers the specific graph theory task provided.
