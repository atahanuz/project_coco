### [W2, round 1]
Algebraic Analysis of $F = |x+y-a-b| + |y+z-b-c| + |z+x-c-a|$:

Let $D_1 = x+y-a-b$, $D_2 = y+z-b-c$, $D_3 = z+x-c-a$.
$F = |D_1| + |D_2| + |D_3|$.

1. Simplification when signs are consistent:
   - If $D_1, D_2, D_3 \ge 0$, then $F = D_1 + D_2 + D_3 = 2(x+y+z - a-b-c)$.
   - If $D_1, D_2, D_3 \le 0$, then $F = -D_1 - D_2 - D_3 = -2(x+y+z - a-b-c)$.
   In both cases, $F = 2|x+y+z - a-b-c|$. This occurs if the relative sums $x+y$ vs $a+b$, etc., are consistently greater than or less than.

2. Simplification when signs are mixed:
   - Consider the case $D_1 \ge 0, D_2 \ge 0, D_3 < 0$:
     $F = (x+y-a-b) + (y+z-b-c) - (z+x-c-a)$
     $F = 2y - 2b$. (The dependence on $x$ and $z$ cancels out.)
   - Considering other mixed sign cases will yield similar simplifications, potentially isolating a single variable or leading to expressions dependent only on $a, b, c$.

Conclusion: The function $F$ simplifies drastically when the signs of the arguments are consistent, or when a specific combination of signs causes variables to cancel out algebraically. Maria must design questions $(a, b, c)$ to force these simplifications.

### [W1, round 1]
Brute-Force Testing Results:
We tested three triples (x, y, z) against two questions (a, b, c).
Response R = |x+y-a-b| + |y+z-b-c| + |z+x-c-a|.

Test Set 1:
Triple (1, 0, 0) -> Responses against Q1=(0, 0, 0) and Q2=(5, 5, 5) are [2, 28].
Triple (1, 1, 0) -> Responses against Q1=(0, 0, 0) and Q2=(5, 5, 5) are [4, 26].
Triple (2, 2, 2) -> Responses against Q1=(0, 0, 0) and Q2=(5, 5, 5) are [12, 18].

Observation: The three tested triples produced unique pairs of responses. This suggests that multiple questions might be enough to distinguish between triples, but more tests are needed to confirm the minimum number.

### [W3, round 1]
Structural Analysis Findings:
1. Case x=y=z=k:
   The function value is F = |2k - (a+b)| + |2k - (b+c)| + |2k - (c+a)|.
   If Maria chooses (a, b, c) = (k, k, k), the resulting F is 0, which determines k=x=y=z.

2. Case {x, y, z} = {0, 1, 2} (specifically (0, 1, 2)):
   F = |1 - a - b| + |3 - b - c| + |2 - c - a|.
   For (a, b, c) = (0, 0, 0), F = 6.
   For (a, b, c) = (1, 1, 1), F = 2.
   For (a, b, c) = (0, 1, 0), F = 4.

### [W4, round 1]
Sensitivity Analysis Findings:
The function F = |x+y-a-b| + |y+z-b-c| + |z+x-c-a| is highly dependent on the choice of question parameters (a, b, c) for a fixed target triple (x, y, z).

Case 1: (x, y, z) = (0, 0, 0). F simplifies to 2(a+b+c).
- Minimal F (F=0) is uniquely achieved when (a, b, c) = (0, 0, 0).
- Maximal F (F=54) is uniquely achieved when (a, b, c) = (9, 9, 9).

Case 2: (x, y, z) = (3, 5, 7). A simulation over all 1000 choices for (a, b, c) showed:
- Minimal F (F=0) is achieved by exactly 1 choice of (a, b, c). This represents the unique parameter set that minimizes the observable value.
- Maximal F (F=30) is achieved by exactly 1 choice of (a, b, c). This represents the unique parameter set that maximizes the observable value.
- There are 16 unique F values in this case, indicating that many different question settings lead to the same observed value, limiting Maria's ability to uniquely determine (x, y, z) from a single response.

### [W1, round 2]
""
### [W1,round 2]
Discriminability Check against Q1=(0, 0, 0) and Q2=(9, 9, 9):We tested 5 challenging triples against the reference questions Q1 and Q2 to assess their distinct responses (discriminability).

Test Results (Triple (x,y, z) -> [Response Q1, Response Q2]):1. (0,9, 0) -> [18, 36]
2. (1, 5, 8) -> [28, 26]
3. (3, 3, 7) -> [26, 28]
4. (9, 0, 9) -> [36, 18]
5. (5, 5, 5) -> [30, 24]

Observation:All 5 tested triples produce unique pairs of responses when measured against Q1 and Q2

### [W2, round 2]
Candidate questions selected: Q1 = (0, 0, 0) and Q2 = (9, 9, 9).

Reasoning:
1.  To guarantee unique identification of $S_{xyz} = x+y+z$, we must force the function $F = |x+y-a-b| + |y+z-b-c| + |z+x-c-a|$ to simplify consistently to $F = 2|S_{xyz} - S_{abc}|$.
2.  Choosing Q1=(0, 0, 0) ensures that for any valid $(x, y, z)$, the arguments of the absolute values ($x+y, y+z, z+x$) are all non-negative, forcing a consistent sign pattern (all $\ge 0$), leading to $F_1 = 2(x+y+z)$. This maps $S_{xyz}$ directly to $F_1/2$.
3.  Choosing Q2=(9, 9, 9) ensures that for any valid $(x, y, z)$, the arguments of the absolute values ($x+y-18, y+z-18, z+x-18$) will either all be negative (if $x+y < 18$, etc.) or at least consistent enough that the simplification $F_2 = 2|S_{xyz} - 27|$ holds, which is the worst-case scenario for the subtraction term.
4.  This choice maximizes the range of the comparison value $S_{abc}$ (from 0 to 27), maximizing the discriminative power of the two measurements $F_1$ and $F_2$ regarding $S_{xyz}$.

### [W3, round 2]
**Permutation Investigation (W3):**
We analyzed the structural implications of knowing the solution $\{x, y, z\}$ only up to permutation, rather than the specific ordered triple $(x, y, z)$.

1.  **State Space Reduction:** The total number of possible solutions reduces significantly from $N_{ordered} = 1000$ (all ordered triples) to $N_{unordered} = 220$ (all unordered multisets of three digits from 0 to 9). If the measurement function $F$ were fully symmetric with respect to $(x, y, z)$, the required minimum number of questions ($k$) would decrease drastically, as $k$ would now need only satisfy $M^k \ge 220$ instead of $M^k \ge 1000$ (where $M$ is the number of distinguishable outcomes per question).

2.  **Symmetry of the Measurement Function:** Our initial analysis shows that $F = |x+y-a-b| + |y+z-b-c| + |z+x-c-a|$ is generally *not* symmetric in $(x, y, z)$ for an arbitrary question $(a, b, c)$. For example, swapping $x$ and $y$ typically changes the value of $F$ because the coefficients $a, b, c$ are assigned specifically to the pairs $(x, y), (y, z), (z, x)$ in the argument differences.

3.  **Conclusion:** For Maria to *be sure* of determining the set $\{x, y, z\}$ under the permutation constraint, she must choose a set of questions $Q_1, \dots, Q_k$ such that for *any* multiset $S=\{x, y, z\}$, the resulting response vector $\vec{R}(S) = (F(S; Q_1), \dots, F(S; Q_k))$ is unique, AND crucially, this vector must be identical for all $3!/p$ permutations of $S$. Since $F$ is generally non-symmetric, this imposes a much stricter constraint on the set of questions $\{Q_i\}$ than simply reducing the state space from 1000 to 220. The reduction in the required number of questions is conditional upon finding a set of highly specific, symmetry-enforcing questions.

### [W1, round 3]
**[W1, round 3] Collision Verification: (0, 0, 1), (0, 1, 0), (1, 0, 0)**
Re-verification of the collision noted previously using Q1=(0, 0, 0) and Q2=(9, 9, 9):

1. Triple (0, 0, 1) [x=0, y=0, z=1]:
   - Q1: F = |0| + |1| + |1| = 2.
   - Q2: F = |0+0-18| + |0+1-18| + |1+0-18| = 18 + 17 + 17 = 52.
   -> Response: (2, 52).

2. Triple (0, 1, 0) [x=0, y=1, z=0]:
   - Q1: F = |1| + |1| + |0| = 2.
   - Q2: F = |0+1-18| + |1+0-18| + |0+0-18| = 17 + 17 + 18 = 52.
   -> Response: (2, 52).

3. Triple (1, 0, 0) [x=1, y=0, z=0]:
   - Q1: F = |1| + |0| + |1| = 2.
   - Q2: F = |1+0-18| + |0+0-18| + |0+1-18| = 17 + 18 + 17 = 52.
   -> Response: (2, 52).

Conclusion: The collision is confirmed. The three permutations (0, 0, 1), (0, 1, 0), and (1, 0, 0) all map to the same response pair (2, 52) when using Q1 and Q2. This highlights that knowledge of the sum $x+y+z=1$ is insufficient to distinguish between these specific permutations using only these two questions.

### [W2, round 3]
### [W2, round 3]
**Analysis of Symmetry in F:**
The function is $F(x, y, z; a, b, c) = |(x+y) - (a+b)| + |(y+z) - (b+c)| + |(z+x) - (c+a)|$.
For $F$ to be symmetric with respect to permutations of $(x, y, z)$, $F(x, y, z; a, b, c)$ must equal $F(\pi(x, y, z); a, b, c)$ for any permutation $\pi$.

The required condition for achieving general symmetry is that the target sums must be equal across all pairs defined by the cyclical structure of the problem.
If we set $a=b=c=k$, then $a+b = b+c = c+a = 2k$.
The function simplifies to $F = |(x+y) - 2k| + |(y+z) - 2k| + |(z+x) - 2k|$.
If we permute $(x, y, z)$, say to $(y, x, z)$:
$F' = |(y+x) - 2k| + |(x+z) - 2k| + |(z+y) - 2k|$.
Since addition is commutative, $F' = F$. The function is symmetric.

The required structure for $(a, b, c)$ is $a=b=c$.

### [W4, round 3]
### [W4, round 2]
**Task Execution: Testing Q3 for distinguishing {(0, 0, 1), (0, 1, 0), (1, 0, 0)}**

I designed the third question $Q_3 = (0, 0, 1)$ aiming to exploit the asymmetry in the arguments of the absolute value function $F = |x+y-a-b| + |y+z-b-c| + |z+x-c-a|$.

The required function evaluations are:
1. $Q_1=(0, 0, 0)$: $F_1(x, y, z) = |x+y| + |y+z| + |z+x|$
2. $Q_2=(9, 9, 9)$: $F_2(x, y, z) = |x+y-18| + |y+z-18| + |z+x-18|$
3. $Q_3=(0, 0, 1)$: $F_3(x, y, z) = |x+y| + |y+z-1| + |z+x-1|$

**Results Calculation:**

*   **For $(0, 0, 1)$:**
    *   $R_1 = |0| + |1| + |1| = 2$
    *   $R_2 = | -18| + | -17| + | -17| = 52$
    *   $R_3 = |0| + |1-1| + |1-1| = 0$
*   **For $(0, 1, 0)$:**
    *   $R_1 = |1| + |1| + |0| = 2$
    *   $R_2 = | -17| + | -17| + | -18| = 52$
    *   $R_3 = |1| + |0-1| + |0| = 1 + 1 + 0 = 2$
*   **For $(1, 0, 0)$:**
    *   $R_1 = |1| + |0| + |1| = 2$
    *   $R_2 = | -17| + | -18| + | -17| = 52$
    *   $R_3 = |1| + |0-1| + |1-1| = 1 + 1 + 0 = 2$

**Summary Table (Response Signature $(R_1, R_2, R_3)$):**
*   (0, 0, 1) $\rightarrow$ (2, 52, 0)
*   (0, 1, 0) $\rightarrow$ (2, 52, 2)
*   (1, 0, 0) $\rightarrow$ (2, 52, 2)

The question $Q_3=(0, 0, 1)$ successfully distinguishes the triple $(0, 0, 1)$ from the other two, but $(0, 1, 0)$ and $(1, 0, 0)$ still collide based on the responses from $Q_1, Q_2, Q_3$. This provides a strong path forward for finding a complete solution.
