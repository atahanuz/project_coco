### [W1, round 1]
The maximum size of a set of non-crossing diagonals in an $n$-gon is $n-3$. For a regular 109-gon ($n=109$), the maximum size of a non-crossing set of diagonals is $109 - 3 = 106$. This set forms a triangulation of the polygon.

### [W3, round 1]
A constructive lower bound is found by considering the set of all diagonals originating from a single vertex, say $V_0$.
Let $n=109$. The diagonals from $V_0$ connect $V_0$ to $V_k$ for $k \in \{2, 3, \dots, 107\}$. The size of this set is $n-3 = 106$.
Any two diagonals $d_1$ and $d_2$ in this set share the common endpoint $V_0$. Since $V_0$ is a vertex of the polygon, it lies on the boundary, not in the interior of the polygon. Therefore, any pair of these diagonals satisfies the condition "do not intersect in the interior."
This means the set of 106 diagonals is a good set. Thus, the maximum size is at least 106.

### [W2, round 1]
Geometric Condition for Perpendicular Diagonals in a Regular 109-gon (N=109):
Let a diagonal be defined by two vertices $V_i$ and $V_j$, and another diagonal by $V_k$ and $V_l$. Since N=109 is odd, the diagonals $V_i V_j$ and $V_k V_l$ are perpendicular if and only if the sum of their endpoint indices satisfy:
i + j \equiv k + l \pm 55 \pmod{109}
where 55 = (N+1)/2.

### [W4, round 1]
### Analysis of the Good Set Constraint for $N=109$ (Prime)

1.  **Non-Crossing Sets:** A set of diagonals that do not intersect in the interior (a non-crossing set) automatically satisfies the "good set" condition because the first clause ("either do not intersect in the interior") is met for all pairs. The maximum size of a non-crossing set is $N-3 = 106$. The set of all diagonals originating from a single vertex provides a constructive example of size 106.

2.  **Perpendicularity Constraint:** The constraint only becomes restrictive when diagonals *do* intersect in the interior. If we seek a size greater than 106, we must introduce at least one crossing pair, and that pair must be perpendicular.

3.  **Structural Invariants for $N=109$ (Odd Prime):** Since $N=109$ is odd, there are no diagonals that pass through the center of the regular 109-gon. This eliminates the simplest case of perfect symmetry often used in finding maximal perpendicular sets (as seen in $N=4$ or $N=6$ where central diagonals exist). The perpendicularity relationship between chords in a regular $N$-gon with odd $N$ is highly dependent on the angular separation defined by vertex indices, and finding a set of multiple mutually perpendicular crossing chords is generally very difficult unless specific geometric structures force it.

4.  **Next Steps:** To improve upon the lower bound of 106, we must investigate whether a diagonal $D$ can be added to the existing good set $S_{106}$ (all diagonals from $V_0$) such that $D$ is perpendicular to *all* diagonals in $S_{106}$ that it crosses. This seems geometrically improbable given the structure of $S_{106}$.

### [W2, round 1]
Current State and Next Steps:
1. The maximum size of a good set is at least 106, demonstrated by the set of 106 diagonals originating from a single vertex (which are non-crossing).
2. The geometric condition for two diagonals $V_i V_j$ and $V_k V_l$ to be perpendicular in a regular 109-gon is $i+j \equiv k+l \pm 55 \pmod{109}$.
3. To find the maximum size, we must investigate if using the perpendicularity condition allows us to construct a good set $S$ such that $|S| > 106$. This requires analyzing how intersection occurs for general diagonals and how the perpendicularity condition interacts with the intersection geometry. The current upper bound based on non-intersection is 106.

### [W2, round 2]
### [W2, round 2] Summary of Constraints and Verification

Based on W2's derivation and W4's analysis, we confirm that the maximum size is at least 106 (non-crossing set from a single vertex). To exceed 106, we need crossing pairs that are perpendicular.

The perpendicularity condition $i+j \equiv k+l \pm 55 \pmod{109}$ must hold for any crossing pair $\{V_i V_j, V_k V_l\}$ that we introduce. The combinatorial density of diagonals satisfying this strict condition while simultaneously respecting the alternation required for intersection, and maintaining the constraint for *all* other pairs, suggests that achieving $|S| > 106$ is highly improbable for an odd prime $N$. We should focus on proving that the introduction of any crossing pair forces a violation of the good set condition for another pair, thereby maintaining 106 as the maximum.

### [W1, round 2]
### [W1, round 2] Analysis of Perpendicular Diagonals to $V_0 V_k$
Focusing on the perpendicularity condition: $D_{new} = V_i V_j$ is perpendicular to $D_{ref} = V_0 V_k$ if $i+j \equiv k+0 \pm 55 \pmod{109}$.
For any fixed pair $(i, j)$, this equation yields exactly two solutions for $k$:
$k_1 \equiv i+j - 55 \pmod{109}$
$k_2 \equiv i+j + 55 \pmod{109}$
Therefore, the maximum number of values for $k$ is 2, provided $k_1$ and $k_2$ correspond to valid diagonals $V_0 V_k$ (i.e., $k \in \{2, 3, \dots, 107\}$).

To ensure both $k_1$ and $k_2$ are valid indices, we must avoid $k \equiv 0, 1, 108 \pmod{109}$.
Let $S = i+j$.
1. $S - 55 \not\equiv 0, 1, 108 \implies S \not\equiv 55, 56, 54 \pmod{109}$
2. $S + 55 \not\equiv 0, 1, 108 \implies S \not\equiv 54, 55, 53 \pmod{109}$

Combining these, the sum $S = i+j$ must satisfy $S \not\in \{53, 54, 55, 56\} \pmod{109}$. The range of index pairs $(i, j)$ that maximizes the number of $k$ values (which is 2) are those where $i, j \in \{2, 3, \dots, 107\}$, $i \neq j$, and $i+j \not\equiv 53, 54, 55, 56 \pmod{109}$.

### [W3, round 2]
### [W3, round 2] Analysis of $S_{106} + D_{new}$

We assume $S_{106}$ is the good set of 106 diagonals originating from $V_0$, $S_{106} = \{ V_0 V_k \mid k=2, \dots, 107 \}$. We seek $D_{new} = V_i V_j$ ($i<j$) such that $S_{106} \cup \{D_{new}\}$ is a good set, meaning $D_{new}$ must be perpendicular to every $V_0 V_k$ it crosses.

1.  **Intersection Condition:** Assuming $0 < i < j < 109$, $D_{new} = V_i V_j$ intersects $D_k = V_0 V_k$ if and only if $i < k < j$. The set of crossed indices is $K = \{i+1, i+2, \dots, j-1\}$.

2.  **Perpendicularity Condition (W2):** $D_k$ and $D_{new}$ are perpendicular iff $k \equiv i + j \pm 55 \pmod{109}$.

3.  **Constraint Implication:** For $S_{106} \cup \{D_{new}\}$ to be good, every index $k \in K$ must satisfy the perpendicularity condition. This means $K$ must be a subset of $\{i+j+55 \bmod 109, i+j-55 \bmod 109\}$, which has a maximum size of 2.
    Therefore, $D_{new}$ can cross at most 2 diagonals from $S_{106}$. The requirement of crossing a "sufficiently large fraction" of $S_{106}$ (which has size 106) is mathematically impossible under the constraints of perpendicularity.

4.  **Constructive Examples (Size 107):** We found solutions where $j-i=2$ or $j-i=3$:
    *   Case $j-i=2$ (1 crossed diagonal): $D_{53} V_{55}$. It crosses $D_{54}$. $54 \equiv 53+55+55 \bmod 109$. Set size is 107.
    *   Case $j-i=2$ (1 crossed diagonal): $D_{54} V_{56}$. It crosses $D_{55}$. $55 \equiv 54+56-55 \bmod 109$. Set size is 107.
    *   Case $j-i=3$ (2 crossed diagonals): $D_{53} V_{56}$. It crosses $D_{54}$ and $D_{55}$. Required indices are $\{54, 55\}$. $54 \equiv 53+56-55 \bmod 109$ and $55 \equiv 53+56+55 \bmod 109$. Set size is 107.

Conclusion: We successfully increased the size of the good set to 107. The maximum size is at least 107.

### [W4, round 2]
### [W4, round 2] Analysis of $|S| > 106$ augmentation

Rigorous analysis shows that if a new diagonal $D_{new}$ is added to $S_{106}$ (the set of 106 diagonals from vertex $V_0$), $D_{new}$ can cross at most one diagonal $D_k$ from $S_{106}$ while maintaining the good set property. This is because two distinct diagonals from $S_{106}$ (sharing $V_0$) cannot be parallel, yet if $D_{new}$ is perpendicular to both, they must be parallel. Therefore, the maximum possible size of $S$ achievable by augmenting $S_{106}$ is 107. Since $107 > 106$, it is possible to construct a good set larger than 106 under the specified conditions.
