### [W3, round 1]
The maximum size of a set of non-intersecting diagonals (a triangulation) in a regular $n$-gon is $n-3$. For $n=109$, this gives a lower bound for the maximum size of a good set: $|S| \ge 106$. If the good set $S$ consists entirely of non-intersecting diagonals, the maximum size is 106.

### [W3, round 1]
Structural analysis suggests that while the 'good set' condition permits intersecting diagonals if they are perpendicular, the strong constraints imposed by perpendicularity in a regular $n$-gon with odd $n$ (like $n=109$) are unlikely to allow for a set larger than the maximal non-crossing set. A set of non-intersecting diagonals forms a triangulation, achieving $|S| = n-3 = 106$. Any introduction of an intersection forces a rigid geometric relationship (perpendicularity), which generally limits the ability to pack more diagonals into the structure while maintaining the "good" property. Therefore, 106 is conjectured to be the maximum size.

### [W2, round 1]
Perpendicularity condition derivation:
Let the vertices of a regular n-gon be $V_0, \dots, V_{n-1}$ inscribed in a circle of radius R centered at the origin. A diagonal $D_{ij}$ connects $V_i$ and $V_j$. Using coordinates and the sum-to-product identities, the direction vector of $D_{ij}$ is proportional to $(-\sin S_{ij}, \cos S_{ij})$, where $S_{ij} = (i+j)\pi/n$.
Two diagonals $D_{ij}$ and $D_{kl}$ are perpendicular if and only if the dot product of their direction vectors is zero:
$\cos(S_{ij} - S_{kl}) = 0$.
Substituting $S_{ij} = (i+j)\pi/n$ and $S_{kl} = (k+l)\pi/n$:
$\cos\left(\frac{\pi}{n} ((i+j) - (k+l))\right) = 0$.
This requires the argument of the cosine to be an odd multiple of $\pi/2$:
$\frac{\pi}{n} ((i+j) - (k+l)) = (2m+1)\frac{\pi}{2}$ for some integer $m$.
The general condition is: $(i+j) - (k+l) = n \frac{2m+1}{2}$.

Application to n=109:
For $n=109$, the condition becomes $(i+j) - (k+l) = 109 \frac{2m+1}{2}$.
Since $i, j, k, l$ are integers, the left-hand side (LHS) is an integer.
$2((i+j) - (k+l)) = 109 (2m+1)$.
Since 109 is a prime number and does not divide 2, 109 must divide the LHS. Let $L = (i+j) - (k+l)$. Then $L = 109 q$ for some integer $q$.
Substituting this: $2(109 q) = 109 (2m+1)$, which simplifies to $2q = 2m+1$.
This equation requires an even integer ($2q$) to equal an odd integer ($2m+1$), which is impossible.
Therefore, for a regular 109-gon, there are no pairs of diagonals that are perpendicular in the interior.

### [W4, round 1]
Theoretical Upper Bound Analysis:
A good set S must satisfy: if d1 intersects d2, then d1 is perpendicular to d2.
We consider the families Di of parallel diagonals. Di is a good set.
If we find two mutually perpendicular families, Di and Dj, their union Si U Dj is a good set.
For n=109 (odd), there are 54 distinct directions, each containing 109 diagonals.
While true perpendicularity is difficult for odd n, the theoretical maximum is bounded by the sum of the sizes of the two largest near-perpendicular families.
The size of the largest family is n=109. Thus, the maximal theoretical bound derived from the parallel structure is 2 * floor(n/2) = 2 * 54 = 108.

### [W1, round 1]
## Analysis for Regular Octagon (n=8)

**1. Non-intersecting Diagonals (Lower Bound):**
The maximum number of non-intersecting diagonals (a triangulation) is $n-3 = 5$.
A set achieving this size is $S_{5} = \{(V_0, V_2), (V_0, V_3), (V_0, V_4), (V_0, V_5), (V_0, V_6)\}$. Since all diagonals share the vertex $V_0$, no pair intersects in the interior. This is a good set of size 5.

**2. Intersecting Diagonals (Test Cases):**
*   **Diameters:** The four diameters, $D = \{V_0V_4, V_1V_5, V_2V_6, V_3V_7\}$, all intersect at the center $O$. A subset of $D$ must consist only of perpendicular pairs.
    *   $S_A = \{V_0V_4, V_2V_6\}$: Size 2. Both intersect at $O$ and are perpendicular (x-axis and y-axis). Good set.
    *   $S_B = \{V_1V_5, V_3V_7\}$: Size 2. Both intersect at $O$ and are perpendicular ($y=x$ and $y=-x$). Good set.
    *   No set of size 3 or 4 from $D$ is a good set, as shown by pairs like $(V_0V_4, V_1V_5)$ which intersect at $O$ but are not perpendicular.
*   **General Intersecting Pairs:** Tested $d_1 = V_0V_3$ and $d_2 = V_1V_4$. These diagonals intersect in the interior, but their calculated slopes confirm they are NOT perpendicular. Thus, $S=\{V_0V_3, V_1V_4\}$ is NOT a good set.

**3. Conclusion for n=8:**
The maximum size found is 5, achieved by selecting a triangulation. Due to the restrictive nature of the perpendicularity requirement for intersecting diagonals in a regular octagon, it is conjectured that no set of size 6 or more exists. The maximum size is 5.
