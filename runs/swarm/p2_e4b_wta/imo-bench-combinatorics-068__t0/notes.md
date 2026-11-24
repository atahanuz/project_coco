### [W1, round 1]
Proof Sketch: Relating M1 and M2 using the number of occupied cells.
Let $N_{occ}$ be the number of occupied cells.
Initial state: $N_{occ, start} = 0$.
Final state: $N_{occ, end} = 1$.

Operation (1) (Insertion): Adds one number to an empty cell. This increases $N_{occ}$ by 1.
Operation (2) (Combination): Replaces two equal numbers ($2^j$) with one larger number ($2^{j+1}$) and empties the second cell. This decreases $N_{occ}$ by 1 (two occupied $\to$ one occupied).

The net change in the number of occupied cells is:
$\Delta N_{occ} = N_{occ, end} - N_{occ, start} = 1 - 0 = 1$.

This change must also equal the sum of changes from all operations:
$\Delta N_{occ} = (M_1 \times (+1)) + (M_2 \times (-1))$
$1 = M_1 - M_2$
Therefore, $M_2 = M_1 - 1$. This holds provided $M_1 \ge 1$ (which is guaranteed if we end with at least one occupied cell starting from zero).

### [W2, round 1]
Analysis of forming $2^{40}$ using only Move (2): Move (2) ($2^j + 2^j \to 2^{j+1}$) preserves the total sum of the numbers in the cells. To obtain a final single cell containing $2^{40}$, the initial total sum must be $2^{40}$. Since the initial inputs are $M_1$ copies of $2^0=1$, the total initial sum is $M_1$. Therefore, $M_1$ must be $2^{40}$. Since all operations require pairs of identical numbers, and $2^{40}$ is a power of 2, this number allows for a complete binary merging process to reach $2^{40}$. The minimum required $M_1$ is $2^{40}$.

### [W4, round 1]
Analysis of game mechanics:
Let M1 be the number of type (1) moves (placing numbers) and M2 be the number of type (2) moves (merging).
Each type (1) move increases the count of numbers by 1.
Each type (2) move decreases the count of numbers by 1 (consumes 2, produces 1).
Since the final state has 1 number, the total net change in count must be 1.
Initial count (0) + M1 * (+1) + M2 * (-1) = 1.
Thus, M1 - M2 = 1, or M2 = M1 - 1. This relationship holds generally for any sequence resulting in one final item.

Constraint on K (initial elements):
To end with a single number $2^{40}$, the initial set of $K=M_1$ numbers $\{2^{e_1}, \dots, 2^{e_K}\}$ must satisfy $2^{40} = \sum_{i=1}^K 2^{e_i}$.
For this sum to be a single power of two, $K$ must be a power of two, $K=2^p$, and all $e_i$ must be equal to some $e_0$.
We are constrained by the cell limit $N=9$, so $K \le 9$.
The maximum power of two $K \le 9$ is $K=8$.
If $K=8$, we need $8 \cdot 2^{e_0} = 2^{40}$, which means $2^3 \cdot 2^{e_0} = 2^{e_0+3} = 2^{40}$.
Thus, $e_0 = 37$.
The maximum number of moves $M = M_1 + M_2 = K + (K-1) = 2K - 1$.
For $K=8$, $M_{max} = 2(8) - 1 = 15$.

### [W3, round 1]
Investigated the maximum moves for target $2^8$ with $N=9$ cells. 
The relationship between moves $M$ and initial placements $M_1$ is $M = 2M_1 - 1$.
The cell constraint limits $M_1 \le 9$.
We verified that $2^8 = 256$ can be expressed as a sum of 9 powers of 2 (e.g., $2^7 + 8 \times 2^4$).
The maximum number of moves for $2^8$ is $M = 2(9) - 1 = 17$. This confirms the $N=9$ constraint is active for this test case.
