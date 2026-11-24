### [W3, round 1]
Investigation complete for non-uniform distribution $a_i \in \{2, 3\}$ in Round 1.
If all initial pebble counts $a_i$ are 2 or 3, the safety condition is always met for Round 1, regardless of Bob's split $k$ or Alice's choice, as the minimum resulting count is $2-1=1$.
To minimize the total sum $n = \sum a_i$ while satisfying $a_i \in \{2, 3\}$ and requiring at least one box to have 3 pebbles ($N_3 \ge 1$), we set $N_3=1$ and $N_2=99$.
The smallest $n$ satisfying these constraints is $n = 99(2) + 1(3) = 198 + 3 = 201$.

### [W2, round 1]
Analysis of Round 3 transition from state A^(2) (where all a_i in {1, 3}):
Let S_1 be the set of indices i where a_i = 1.
Bob wins if he can choose a split k' such that regardless of Alice's choice, a 0 pebble count is forced.

1. If Alice chooses G_L' (Add 1 to left, Subtract 1 from right): A zero count occurs if and only if there exists i > k' such that a_i = 1. (i.e., S_1 intersects {k'+1, ..., 100}).
2. If Alice chooses G_R' (Subtract 1 from left, Add 1 to right): A zero count occurs if and only if there exists i <= k' such that a_i = 1. (i.e., S_1 intersects {1, ..., k'}).

Bob forces a win if and only if he can choose k' such that S_1 is split by k'. That is, k' must satisfy:
a) min(S_1) <= k'
b) max(S_1) > k'

If the '1's are all located at indices $i \le k'$ for all $k'$, or $i > k'$ for all $k'$, Bob cannot guarantee a win. If the 1s are split across the board, Bob wins.

### [W1, round 1]
Analysis of $A^{(0)} = (4, 4, \ldots, 4)$ across three rounds:

Initial state (after Round 1): $A^{(0)} = (4, 4, \ldots, 4)$. Minimum pebble count = 4.

Round 2 (Transition $A^{(0)} \to A^{(1)}$):
Bob chooses a split $k$. Since $A^{(0)}$ is uniform, Alice can choose either side to add 1 pebble and subtract 1 pebble from the other. The minimum pebble count in $A^{(1)}$ is 3, regardless of Bob's choice $k$.

Round 3 (Transition $A^{(1)} \to A^{(2)}$):
The minimum in $A^{(1)}$ is 3. If Bob chooses a split $k'$ such that boxes with 3 pebbles are split between the active and inactive groups, Alice cannot save them all. The minimum pebble count in $A^{(2)}$ is 2.

Round 4 (Transition $A^{(2)} \to A^{(3)}$):
The minimum in $A^{(2)}$ is 2. If Bob chooses a split $k''$ such that boxes with 2 pebbles are split between the active and inactive groups, Alice cannot save them all. The minimum pebble count in $A^{(3)}$ is 1.

Conclusion: Since the minimum count in $A^{(1)}, A^{(2)},$ and $A^{(3)}$ is $3, 2,$ and $1$ respectively, no box contains zero pebbles across these three rounds. The guarantee holds for the specified timeframe.

### [W4, round 1]
Theoretical Lower Bound Analysis:
For Alice to prevent Bob from winning indefinitely, she must ensure that the minimum number of pebbles in any box, $m = \min(p_i)$, never drops to 0.
If $m=1$, let $B_j$ be a box with 1 pebble. Bob can choose a cut $k$ such that $B_j$ is in the group losing a pebble. If Alice selects that group, $p_j$ becomes $1-1=0$, and Bob wins immediately.
Therefore, a necessary condition for sustained play is that $p_i \ge 2$ for all $i$ in every round.

To ensure $p_i^{(1)} \ge 2$ after the first round, consider the worst-case scenario for Alice's initial distribution $P^{(0)}$. Bob chooses $k$. Alice must pick a group $G_{chosen}$ such that all boxes in the losing group $G_{other}$ satisfy $p_i^{(0)} - 1 \ge 2$, meaning $p_i^{(0)} \ge 3$ for all $i \in G_{other}$. Since Bob chooses $k$ arbitrarily, he can always define a $G_{other}$ of size $100-k$. To guarantee survival, Alice must ensure that for any $k$, the boxes in $G_{other}$ start with at least 3 pebbles. This forces $p_i^{(0)} \ge 3$ for all $i=1, \ldots, 100$.

The smallest $n$ satisfying this requirement is when all boxes are initialized to 3 pebbles: $n = 100 \times 3 = 300$. This establishes a theoretical lower bound $C=300$.

### [W1, round 2]
### [W1, Characterization of $S_1$ Survival]
Based on the analysis in [W2, round 1], a necessary condition for the set of 'weak' boxes $S_1$ (where pebble count $a_i=1$) to survive indefinitely is that $S_1$ must be clustered.
Formally, for any split $k \in \{1, \ldots, 99\}$, $S_1$ must satisfy $S_1 \subseteq \{B_1, \ldots, B_k\}$ or $S_1 \subseteq \{B_{k+1}, \ldots, B_{100}\}$.
If $S_1$ is split by $k$ (i.e., $\min(S_1) \le k < \max(S_1)$), Bob can force a win:
1. If $S_1$ intersects $\{B_{k+1}, \ldots, B_{100}\}$, Bob chooses Alice to add pebbles to the left group ($G_L$). Then, for any $j \in S_1 \cap G_R$, $a_j$ becomes $1-1=0$.
2. Conversely, if $S_1$ intersects $\{B_1, \ldots, B_k\}$, Bob chooses Alice to add pebbles to the right group ($G_R$). Then, for any $j \in S_1 \cap G_L$, $a_j$ becomes $1-1=0$.
Therefore, clustering of $S_1$ is necessary to prevent Bob from winning.

### [W4, round 2]
Re-analysis of $A^{(0)}=(3, \ldots, 3)$ for Round 3 transition:

W2 established that Bob forces a win in Round 3 if and only if the set $S_1$ (indices where $a_i=1$ in $A^{(2)}$) is split by Bob's chosen cut $k'$. If $S_1$ is split, Bob wins regardless of Alice's choice.

To prevent Bob from forcing a win, Alice must ensure that $S_1$ is either empty or non-splittable (i.e., all $1$s are contiguous, and the total set size is 100, or $S_1$ is empty). However, even if $S_1$ is contiguous, Bob can choose a cut $k'$ that splits it, leading to a forced win for Bob according to W2's criterion.

Therefore, the necessary and sufficient condition for Alice to avoid Bob forcing a win in Round 3 is that $S_1$ must be empty.

Starting from $A^{(0)}=(3, \ldots, 3)$:
Round 1 transition $A^{(0)} \to A^{(1)}$ creates a boundary between regions of 4s and 2s, based on Bob's $k_1$ and Alice's choice.
Round 2 transition $A^{(1)} \to A^{(2)}$ creates 1s if the losing group $G_{other}$ contains any boxes with 2 pebbles.
Since $A^{(1)}$ always contains boxes with 2 pebbles (unless $k_1=99$ and Alice chooses $G_L$, or $k_1=1$ and Alice chooses $G_R$, both of which leave the other side fully intact, but Bob controls $k_1$), Bob can always choose $k_2$ to make $G_{other}$ include at least one 2-pebble box, thus ensuring $S_1$ is non-empty.

Since Bob can always force $S_1$ to be non-empty, and any non-empty $S_1$ can be split by a strategically chosen $k'$, it is impossible for Alice to guarantee that $S_1$ is not split in Round 3.

### [W3, round 2]
Analysis of Round 2 for n=201:
The initial state $P^{(0)}$ after Round 1 contains 99 boxes with 2 pebbles and one box with 3 pebbles.
For Bob to win in Round 2, he needs to force a state $P^{(1)}$ such that the set $S_1$ (boxes with 1 pebble) satisfies $|S_1| \ge 2$.
Since there are 99 boxes starting at 2 pebbles, Bob can always choose a split $k$ (e.g., $k=50$) such that both resulting groups ($G_L, G_R$) contain at least two boxes starting at 2 pebbles.
If Alice chooses $G_I$ (the inactive group), it must contain at least two boxes starting at 2 pebbles, making their count 1 in $P^{(1)}$. Thus, $|S_1| \ge 2$ is forced.
If $|S_1| \ge 2$, Bob can choose a cut $k'$ in Round 2 that splits $S_1$. Alice is then forced to lose a pebble from at least one box $i \in S_1$, resulting in $P_i^{(2)} = 0$.
Conclusion: For $n=201$, Bob can choose a split $k$ in Round 2 that guarantees a zero pebble count, given the state derived from Round 1.

### [W2, round 3]
Claim verification: Starting from $A^{(0)}=(3, \ldots, 3)$, Alice can guarantee that the resulting state $A^{(2)}$ has a set $S_1$ (boxes with 1 pebble) that is entirely clustered.

We analyze the transitions $A^{(0)} \xrightarrow{k_1, G_{R1}} A^{(1)} \xrightarrow{k_2, G_{R2}} A^{(2)}$.

1. Round 1 ($A^{(0)} \to A^{(1)}$):
Bob chooses a cut $k_1$. Alice chooses $G_{R1}$ (the group she adds 1 pebble to). The boxes in the other group, $G_{O1}$, lose 1 pebble.
If $A^{(0)} = (3, \ldots, 3)$, then $A^{(1)}$ must be of the form $(\underbrace{4, \ldots, 4}_{k_1}, \underbrace{2, \ldots, 2}_{100-k_1})$ or $(\underbrace{2, \ldots, 2}_{k_1}, \underbrace{4, \ldots, 4}_{100-k_1})$, depending on whether Alice chooses the left or right group, and $k_1$ determines the boundary index. In either case, $A^{(1)}$ has exactly one boundary between 2s and 4s.

2. Round 2 ($A^{(1)} \to A^{(2)}$):
Bob chooses a cut $k_2$. Alice chooses $G_{R2}$ (the group she adds 1 pebble to). The boxes in $G_{O2}$ lose 1 pebble.
$S_1$ in $A^{(2)}$ consists of boxes that were in $G_{O2}$ and had a count of 2 in $A^{(1)}$.

We analyze the structure based on the position of the R1 boundary ($k_1$) relative to the R2 boundary ($k_2$):

Case 1: $k_1$ is the boundary index of $A^{(1)}$, and $A^{(1)}$ is $4^{k_1} 2^{100-k_1}$.
    a) $k_2 < k_1$: $G_L'$ is $4^{k_2}$. $G_R'$ is mixed ($4^{k_1-k_2}, 2^{100-k_1}$).
        If Alice chooses $G_L'$: $G_{O2}=G_R'$. The 2s in $G_R'$ drop to 1. $S_1 = \{k_1+1, \ldots, 100\}$. (Clustered).
        If Alice chooses $G_R'$: $G_{O2}=G_L'$. All boxes in $G_L'$ are 4s, so $S_1$ is empty. (Clustered).
    b) $k_2 \ge k_1$: $G_L'$ is mixed ($4^{k_1}, 2^{k_2-k_1}$). $G_R'$ is $2^{100-k_2}$.
        If Alice chooses $G_L'$: $G_{O2}=G_R'$. The 2s in $G_R'$ drop to 1. $S_1 = \{k_2+1, \ldots, 100\}$. (Clustered).
        If Alice chooses $G_R'$: $G_{O2}=G_L'$. The 2s in the segment $k_1+1$ to $k_2$ drop to 1. $S_1 = \{k_1+1, \ldots, k_2\}$. (Clustered).

Case 2: $k_1$ is the boundary index of $A^{(1)}$, and $A^{(1)}$ is $2^{k_1} 4^{100-k_1}$.
    a) $k_2 < k_1$: $G_L'$ is $2^{k_2}$. $G_R'$ is mixed ($2^{k_1-k_2}, 4^{100-k_1}$).
        If Alice chooses $G_L'$: $G_{O2}=G_R'$. The 2s in the segment $k_2+1$ to $k_1$ drop to 1. $S_1 = \{k_2+1, \ldots, k_1\}$. (Clustered).
        If Alice chooses $G_R'$: $G_{O2}=G_L'$. The 2s in $G_L'$ drop to 1. $S_1 = \{1, \ldots, k_2\}$. (Clustered).
    b) $k_2 \ge k_1$: $G_L'$ is mixed ($2^{k_1}, 4^{k_2-k_1}$). $G_R'$ is $4^{100-k_2}$.
        If Alice chooses $G_L'$: $G_{O2}=G_R'$. $S_1$ is empty (as $G_R'$ contains only 4s). (Clustered).
        If Alice chooses $G_R'$: $G_{O2}=G_L'$. The 2s in $G_L'$ drop to 1. $S_1 = \{1, \ldots, k_1\}$. (Clustered).

Conclusion: For any combination of Bob's choices $k_1$ and $k_2$, Alice can always select a group such that $S_1$ (if non-empty) is a single contiguous block. Therefore, the claim is PROVEN TRUE.
