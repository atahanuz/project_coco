### [W3, round 1]
Baseline Finding (Non-intersecting diagonals): The maximum size of a set of pairwise non-intersecting diagonals in a regular N-gon is N-3. For N=109, the maximum size is 106.

### [W3, round 1]
Next Steps Strategy: The baseline for non-intersecting diagonals is 106. The exploration now hinges on determining the maximum size of a set $S$ where intersections are restricted to perpendicular pairs. This requires establishing the exact algebraic condition for two diagonals in a regular 109-gon to be perpendicular. If this condition allows for a highly structured set where intersections are dense but orthogonal, the size might exceed 106. I need to find a known theorem or geometric property relating perpendicular diagonals in an odd-sided regular polygon to determine an upper bound for $|S|$.

### [W4, round 1]
Investigating sets $S_k$ of diagonals in a regular 109-gon where all diagonals have constant span $k$.
Since N=109 is a prime number, the structure of these diagonals is highly symmetric.
For any fixed span $k$ (where $1 < k < 54$), the set $S_k$ consists of N diagonals.
Geometric analysis suggests that if two diagonals in $S_k$ intersect, they are generally not perpendicular unless $k$ is related to $N$ in a very specific way, which is unlikely for generic $k$ and prime $N$.
Therefore, the set $S_k$ is likely NOT good unless all pairs happen to be non-intersecting.
The maximum possible size of a subset of $S_k$ that is guaranteed to be good is achieved by finding a maximal set of non-intersecting diagonals of span $k$.
A set of size 1 is always good. If we can find $k$ and a non-intersecting set of size $M > 1$, then $M$ is a candidate answer based on this constraint.
The difficulty lies in proving the perpendicularity condition for intersecting pairs in $S_k$.
I will proceed by focusing on the non-intersecting subset problem under the constraint of constant span $k$.

### [W4, round 1]
Summary of the investigation based on constant span $k$:
For $N=109$ (a prime number), the full set $S_k$ of all diagonals with span $k$ is highly unlikely to be 'good' because intersecting diagonals of the same length/span are generally not perpendicular in a regular polygon unless specific conditions relating $k$ and $N$ are met, which is rare.
Any maximal 'good' set derived from $S_k$ must therefore be a non-intersecting subset. The largest possible guaranteed good subset is of size 1. Finding a larger non-intersecting subset requires complex combinatorial geometry to determine the maximum packing density given the fixed span $k$.
Since this approach does not yield a large guaranteed maximum size, the investigation for this specific constraint is concluded.

### [W1, round 1]
Analysis for N=8 (Octagon):
1. Definitions: A 'good' set of diagonals requires any two diagonals to either not intersect in the interior OR be perpendicular.
2. Baseline: The maximum size of a set of pairwise non-intersecting diagonals is $N-3$. For $N=8$, this size is $8-3=5$. Any such set is automatically a 'good' set.
3. Construction: We can construct a set of size 5 by choosing all diagonals originating from a single vertex, say $v_0$: $S_5 = \{v_0v_2, v_0v_3, v_0v_4, v_0v_5, v_0v_6\}$. These diagonals do not intersect in the interior since they share the endpoint $v_0$. Thus, the maximum size is at least 5.
4. Perpendicularity Check: We investigated the possibility of including intersecting diagonals. We found that two specific intersecting diagonals, $v_0v_3$ and $v_1v_4$, were not perpendicular, meaning they cannot both be in the set.
5. Conclusion: Given the strong constraint imposed by the perpendicularity requirement on intersecting pairs, the maximum size appears to be limited by the maximum non-crossing set size, $N-3=5$. The maximum size of a good set for the octagon is 5.

### [W2, round 1]
## Perpendicularity Condition Derivation

The vertices of a regular N-gon are represented by $V_k = e^{i 2\pi k/N}$ (assuming unit radius). A diagonal connects $V_i$ and $V_j$. The direction of the chord $V_i V_j$ is perpendicular to the vector $W_{ij} = V_i + V_j$.

Let $D_1$ connect $V_i, V_j$ and $D_2$ connect $V_k, V_l$. $D_1 \perp D_2$ if and only if $W_{ij} \perp W_{kl}$.

The direction of $W_{ij}$ corresponds to the angle $\alpha = \frac{\pi(i+j)}{N}$. The direction of $W_{kl}$ corresponds to $\beta = \frac{\pi(k+l)}{N}$.
$W_{ij} \perp W_{kl}$ implies $\alpha - \beta = \pm \frac{\pi}{2} + 2m\pi$.

This leads to the general condition for perpendicularity:
$$2(i+j - k - l) = N \cdot M$$
where $M$ is an odd integer.

## Application for N=109

Since $N=109$ is odd, $N \cdot M$ must be odd (as $M$ is odd).
However, $2(i+j - k - l)$ is always an even integer.
Since an even integer cannot equal an odd integer, there are **no** pairs of diagonals in a regular 109-gon that are perpendicular.

This implies that for a set to be "good," every pair must not intersect in the interior. The maximum size of a good set is thus the maximum size of a set of pairwise non-intersecting diagonals, which is $N-3 = 106$.
