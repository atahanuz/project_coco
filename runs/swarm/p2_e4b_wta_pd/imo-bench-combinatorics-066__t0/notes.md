### [W3, round 1]
For a regular n-gon, the maximum number of mutually non-intersecting diagonals is n-3. For n=109, the maximum size of a set of non-intersecting diagonals (ignoring the perpendicularity condition) is 109 - 3 = 106.

### [W4, round 1]
# Geometric Conditions for Diagonals in a Regular 109-gon (n=109)

Let the vertices be indexed $V_0, V_1, \ldots, V_{108}$. A diagonal is defined by a set of indices $\{i, j\}$, where $0 \le i < j \le 108$ and $j-i \ge 2$.

**1. Intersection Condition:**
Two diagonals $D_1 = \{i, j\}$ and $D_2 = \{k, l\}$ intersect strictly in the interior of the polygon if and only if their endpoints strictly interleave when ordered cyclically. Assuming $i<j$ and $k<l$, they intersect if and only if:
$$i < k < j < l \quad \text{or} \quad k < i < l < j$$

**2. Perpendicularity Condition:**
Determining perpendicularity purely by indices is complicated. Using complex coordinates $z_m = e^{i 2\pi m/n}$, two chords defined by $\{i, j\}$ and $\{k, l\}$ are perpendicular if and only if the difference in their angular midpoints is $\pi/2$ (modulo $\pi$).

For $n=109$, this translates to an arithmetic condition on the indices. While a rigorous proof is lengthy, based on the general theory of chords in a regular $n$-gon, the condition for $D_1 \perp D_2$ is often related to:
$$i+j + k+l \equiv 2 \cdot (\text{some constant}) \pmod{2n}$$
A more likely and cleaner formulation, derived from rotational symmetry arguments, relates the sum of indices difference to $n/2$. Given $n$ is odd, the precise algebraic condition for perpendicularity is crucial and must be confirmed, but it will involve $\{i+j\} - \{k+l\} \equiv \text{constant} \pmod{n}$.

**Focus for next steps:** Given the prime nature of $n=109$, we should seek structural solutions that exploit the uniform distribution of difference sets, potentially looking for maximal sets where all pairs either satisfy the non-intersection condition or the perpendicularity condition derived above.

### [W2, round 1]
Analysis of Perpendicular Diagonals in a Regular n-gon:

Let the vertices of the regular n-gon be represented by $V_k$ located at angle $\theta_k = 2\pi k/n$ on the unit circle, for $k=0, 1, \ldots, n-1$.
A diagonal $D$ connecting vertices $V_a$ and $V_b$ has a direction defined by the vector connecting these points.
The slope ($m_{ab}$) of the line containing the diagonal $V_a V_b$ is given by:
$$m_{ab} = -\cot\left(\frac{\theta_a + \theta_b}{2}\right) = -\cot\left(\frac{\pi (a+b)}{n}\right)$$

Two diagonals, $D_1$ (connecting $V_a, V_b$) and $D_2$ (connecting $V_c, V_d$), are perpendicular if and only if the product of their slopes is $-1$:
$$m_{ab} m_{cd} = -1$$
$$\left(-\cot\left(\frac{\pi (a+b)}{n}\right)\right) \left(-\cot\left(\frac{\pi (c+d)}{n}\right)\right) = -1$$
$$\cot\left(\frac{\pi (a+b)}{n}\right) \cot\left(\frac{\pi (c+d)}{n}\right) = -1$$

This condition is equivalent to:
$$\frac{\pi (a+b)}{n} = \frac{\pi (c+d)}{n} + \frac{\pi}{2} + k\pi \quad \text{for some integer } k$$
$$\frac{a+b}{n} - \frac{c+d}{n} = \frac{1}{2} + k$$
$$a+b - (c+d) = n\left(\frac{1}{2} + k\right)$$

Necessary and Sufficient Conditions:
1. If $n$ is odd, $n(1/2 + k)$ is never an integer, so no two diagonals can be perpendicular.
2. If $n$ is even (let $n=2m$), the condition simplifies to:
$$a+b - (c+d) = m(1+2k)$$
This means that the sum of the indices defining the first diagonal, $a+b$, and the sum of the indices defining the second diagonal, $c+d$, must differ by a multiple of $n/2$.
$$a+b \equiv c+d + n/2 \pmod n$$

### [W4, round 1]
# Strategy Refinement (n=109, Prime)

The maximum size is bounded by the maximum number of non-intersecting diagonals, $n-3 = 106$. The true maximum size might be larger if the perpendicularity condition allows intersections.

**Strategic Approach:** Exploit the prime nature of $n=109$ using modular arithmetic on the indices $\{0, 1, \ldots, 108\}$.

1.  **Hypothesis (All Non-Intersecting):** The largest set found so far is 106 (the maximal non-crossing set).
2.  **Hypothesis (Exploiting Symmetry):** We seek a set $S$ where indices $\{i, j\}$ are related by a fixed difference $d$, i.e., $j = i+d \pmod n$, or where the sum of indices $i+j$ is constant modulo $n$.

If we select all diagonals $\{i, j\}$ such that $i+j \equiv C \pmod{109}$, these diagonals might form a highly structured set. If $C$ is fixed, the number of such diagonals is $n$ (if we count all pairs $\{i, j\}$ with $i \neq j$ and $i+j=C$, which is $n$ pairs including edges). Since we exclude edges, the size is close to $n$.

Let's investigate diagonals $D_{i, j}$ where $i+j \equiv C \pmod{109}$.
The number of pairs $(i, j)$ with $0 \le i < j \le 108$ such that $i+j \equiv C \pmod{109}$ is $n_{diag}$. If $C$ is chosen appropriately, $n_{diag}$ is likely $n/2$ or $(n-1)/2$, roughly 54 or 55. This size (55) is too small compared to 106.

**New Focus:** We should look for a large subset of the $\binom{109}{2} - 109$ diagonals that share a property related to perpendicularity, while minimizing the number of intersecting pairs that *don't* satisfy the perpendicularity constraint.

Given $n=109$, a potential maximal size structure often emerges as $n$. Let's look for a set of size $n$ or $n-1$.

If the set size is $N=109$, then every diagonal must be included. This is impossible since some pairs will intersect and not be perpendicular.

We proceed by assuming the maximum size is related to $n$, perhaps $n-1$ or $n-2$, and test configurations based on vertex indices modulo 2 or modulo a divisor of $n-1$. Since $n$ is prime, modulo 2 is the most robust initial test.

### [W4, round 1]
# Conjecture and Path Forward (Leveraging Prime n)

Based on the analysis of maximal sets in high-symmetry figures where pairs must satisfy an OR condition (Non-intersection OR Perpendicularity), and noting the prime nature of $n=109$:

**Conjecture:** The maximum possible size of a good set is $N = n-1 = 108$.

**Justification Attempt:** A set of size $n-1$ often arises when one vertex $V_k$ is involved in $n-2$ diagonals, and one diagonal incident to $V_k$ is excluded (to avoid intersections or to facilitate a specific perpendicular structure).

We hypothesize that a set $S$ can be constructed of size 108 such that for any two diagonals $D_1, D_2 \in S$:
1. If $D_1$ and $D_2$ are chosen such that they do not share an endpoint, they are either non-intersecting or perpendicular (using the derived index conditions).
2. If they share an endpoint, they are always non-intersecting (since they are adjacent sides of a fan configuration, or simply meet at a vertex and thus don't intersect in the interior).

The actual proof requires constructing such a set of 108 diagonals explicitly or proving that 109 is impossible by finding a mandatory violating pair. This is beyond the scope of a quick derivation, but the size $n-1$ is the strongest candidate structure derived from the constraints. We will prioritize testing $N=108$ as the candidate maximum size.

### [W1, round 1]
### Investigation for N=6 (Hexagon)

**Objective:** Determine the maximum size of a 'good' set of diagonals for a regular hexagon (N=6) and document structural restrictions.

**Diagonals of N=6:** There are 9 diagonals, categorized into 3 long diagonals ($L_2$, diameters) and 6 short diagonals ($L_1$).

**Structural Restrictions Observed:**
1. **Diameters:** The three long diagonals intersect at the center. Since they are not mutually perpendicular, a good set can contain at most one diameter diagonal.
2. **Intersection vs. Perpendicularity:** For two diagonals to be in a good set and intersect internally, they must be perpendicular. Using the index sum condition for perpendicularity, it was shown that many intersecting pairs (e.g., $V_1V_3$ and $V_2V_4$) are not perpendicular, meaning they cannot coexist in a good set.

**Maximum Size Determination:**
A set of size 3 can be achieved by selecting all diagonals incident to a single vertex (e.g., $\{V_1V_3, V_1V_4, V_1V_5\}$), as these are pairwise non-intersecting. Attempts to expand this set to size 4 by incorporating intersecting pairs failed because the intersecting pairs did not satisfy the perpendicularity requirement.

**Result for N=6:** The maximum size of a 'good' set of diagonals is 3.
