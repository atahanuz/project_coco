### [W3, round 1]
Characterization of pentagons with exactly two acute angles in a regular 101-gon:

1.  **Angle Condition:** For a pentagon whose vertices partition the 101 edges into arc lengths $d_1, d_2, d_3, d_4, d_5$, the interior angle $\theta_i$ corresponding to arc length $d_i$ is given by $\theta_i = (101 - d_i) \frac{180^\circ}{101}$.
2.  **Acute Angle Criterion:** An angle $\theta_i$ is acute ($\theta_i < 90^\circ$) if and only if $d_i > 101/2$. Since $d_i$ is an integer, this requires $d_i \ge 51$.
3.  **Classification Requirement:** We seek partitions where exactly two of the arc lengths, say $d_i$ and $d_j$, satisfy $d_i \ge 51$ and $d_j \ge 51$, while the remaining three satisfy $d_k, d_l, d_m \le 50$.
4.  **Conclusion:** If two arc lengths are both $\ge 51$, their sum is at least $51 + 51 = 102$. Since the total sum of all five arc lengths must be exactly 101 ($\sum d_i = 101$), it is impossible for two arc lengths to simultaneously be $\ge 51$.
5.  **Characterization:** The set of partitions $(d_1, d_2, d_3, d_4, d_5)$ satisfying the required geometric condition is the empty set.

### [W4, round 1]
Analysis of Acute Angles in Inscribed Polygons:

Let $N$ be the number of vertices of the regular polygon. A pentagon is formed by choosing 5 vertices, which defines 5 gaps $g_1, g_2, g_3, g_4, g_5$, where $g_i \ge 1$ and $\sum_{i=1}^5 g_i = N$. $g_i$ represents the number of edges along the perimeter between two consecutive chosen vertices.

The interior angle $\theta_i$ at a vertex is subtended by the arc defined by the remaining $N - g_i - g_{i+1}$ edges. Specifically, if the angle is between segments defined by gaps $g_i$ and $g_{i+1}$, the angle $\theta$ is acute if the sum of the gaps *opposite* to it, $g_{i+2} + g_{i+3} + g_{i+4}$ (indices mod 5), is less than $N/2$.

Using $g_{i+2} + g_{i+3} + g_{i+4} = N - g_i - g_{i+1}$, the condition for $\theta_i$ being acute is:
$$N - (g_i + g_{i+1}) < N/2$$
$$N/2 < g_i + g_{i+1}$$

We require exactly two acute angles. This means exactly two of the five sums $g_i + g_{i+1}$ must be greater than $N/2$.

General Formula Formulation:
The problem reduces to finding the number of ordered compositions $(g_1, g_2, g_3, g_4, g_5)$ of $N$ into 5 parts (where $g_i \ge 1$) such that exactly two of the five cyclic sums $g_i + g_{i+1}$ exceed $N/2$.

Let $C(N)$ be this count. Due to the cyclic nature, we count distinct solutions first and then account for rotational symmetry. Since $N$ is prime (like 101), there are no non-trivial rotational symmetries of the polygon, so $C(N)$ is related to $N$ times the number of solutions found up to rotation.

Asymptotic Approach:
For large $N$, this counting problem requires sophisticated methods (like lattice point counting or generating functions for restricted compositions). Since $N/2$ acts as a strict threshold, the asymptotic growth rate of $C(N)$ will likely be polynomial in $N$. Given the constraints, $C(N)$ is expected to be much smaller than the total number of pentagons, $\binom{N}{5} \sim O(N^5)$.

For the specific case $N=101$, the calculation requires finding all integer solutions $(g_1, \ldots, g_5)$ to $\sum g_i = 101$ such that exactly two adjacent sums $g_i+g_{i+1}$ are $\ge 51$.
This is a hard enumeration problem, and a closed-form general formula is not readily available without advanced combinatorial tools.

We proceed by defining the required counting function. We must select which two adjacent pairs $(i, j)$ satisfy the acute condition, which is $\binom{5}{2}=10$ ways. Due to rotational symmetry, we only need to count the pattern starting with $(g_1, g_2)$ acute, $(g_3, g_4)$ acute, and the others obtuse, and multiply by 5 (the number of possible starting points).

The counting task is: Find the number of solutions to $g_1+g_2+g_3+g_4+g_5=N$ such that:
1. $g_1+g_2 > N/2$
2. $g_3+g_4 > N/2$
3. $g_2+g_3 \le N/2$
4. $g_4+g_5 \le N/2$
5. $g_5+g_1 \le N/2$

This framework provides the general methodology required. For $N=101$, this is the concrete starting point for computation.

### [W2, round 1]
Derivation of Angle Conditions for Inscribed Pentagon in Regular N-gon:

Let the chosen vertices of the pentagon be $A_{i_1}, A_{i_2}, A_{i_3}, A_{i_4}, A_{i_5}$, ordered sequentially around the perimeter of the regular N-gon.

Define the arc lengths $d_j$ (in terms of the number of polygon edges) between consecutive chosen vertices, where $j \in \{1, 2, 3, 4, 5\}$ and $A_{i_6} = A_{i_1}$.
$d_j = (i_{j+1} - i_j) \pmod N$. (More formally, if $i_{j+1} \ge i_j$, $d_j = i_{j+1} - i_j$; otherwise $d_j = N + i_{j+1} - i_j$).
We must have $\sum_{j=1}^5 d_j = N$.

Consider the internal angle $\theta_k$ at vertex $A_{i_k}$. This angle intercepts the arc defined by the vertices $A_{i_{k-1}}$ and $A_{i_{k+1}}$ (indices are mod 5).
The total number of edges spanned by the intercepted arc $S_k$ is $S_k = N - (d_{k-1} + d_k)$, where $d_{k-1}$ and $d_k$ are the edge counts of the two sides meeting at $A_{i_k}$.

By the Inscribed Angle Theorem, the angle measure is $\theta_k = S_k \cdot \frac{180^\circ}{N}$.

The condition for $\theta_k$ being acute, right, or obtuse depends on comparing $S_k$ to $N/2$:

1.  **Right Angle ($\theta_k = 90^\circ$):**
    $S_k = N/2 \implies N - (d_{k-1} + d_k) = N/2$
    Necessary and sufficient condition: $d_{k-1} + d_k = N/2$.

2.  **Acute Angle ($\theta_k < 90^\circ$):**
    $S_k < N/2 \implies N - (d_{k-1} + d_k) < N/2$
    Necessary and sufficient condition: $d_{k-1} + d_k > N/2$.

3.  **Obtuse Angle ($\theta_k > 90^\circ$):**
    $S_k > N/2 \implies N - (d_{k-1} + d_k) > N/2$
    Necessary and sufficient condition: $d_{k-1} + d_k < N/2$.

### [W1, round 1]
### Investigation of Small Cases (N=7, 9, 11)

The problem reduces to finding the number of compositions $(d_1, d_2, d_3, d_4, d_5)$ of $N$ into 5 parts ($d_i \ge 1$) such that exactly two of the five cyclic sums $d_i + d_{i+1}$ exceed $N/2$.

**Case N=7:**
1. Total pentagons: $\binom{7}{5} = 21$.
2. Condition for acute angle: $d_i + d_{i+1} > 3.5$, i.e., $d_i + d_{i+1} \ge 4$.
3. Partitions of 7 into 5 parts:
    a. Type (3, 1, 1, 1, 1) and its 5 cyclic permutations.
        Check: Adjacent sums are (4, 2, 2, 2, 4). Exactly 2 sums are $\ge 4$. **Result: 2 acute angles.**
    b. Type (2, 2, 1, 1, 1) and its 10 cyclic permutations.
        Check: The only adjacent sum $\ge 4$ is $2+2=4$. This occurs only once per cycle. **Result: 1 acute angle.**
4. **Pattern observed:** For $N=7$, only compositions of type (3, 1, 1, 1, 1) yield exactly two acute angles. There are 5 such ordered compositions.

**Case N=9:**
1. Total pentagons: $\binom{9}{5} = 126$.
2. Condition for acute angle: $d_i + d_{i+1} > 4.5$, i.e., $d_i + d_{i+1} \ge 5$.
3. Partitions of 9 into 5 parts:
    a. Type (5, 1, 1, 1, 1): 5 permutations. Adjacent sums include $5+1=6$ and $1+5=6$. **Result: 2 acute angles.**
    b. Type (3, 3, 1, 1, 1): 10 permutations. Adjacent sums include $3+3=6$. **Result: 2 acute angles.**
    c. Other types (e.g., (4, 2, 1, 1, 1) or (2, 2, 2, 2, 1)) generally result in 2 or fewer acute angles, depending on the configuration.
4. **Pattern observed:** Two structural types (5, 1, 1, 1, 1) and (3, 3, 1, 1, 1) yield exactly two acute angles. The total number of ordered compositions for these types is $5 + 10 = 15$.

**Case N=11:**
1. Total pentagons: $\binom{11}{5} = 462$.
2. Condition for acute angle: $d_i + d_{i+1} > 5.5$, i.e., $d_i + d_{i+1} \ge 6$.
3. Calculation required: Enumerating compositions of 11 into 5 parts that satisfy the required adjacency conditions is complex and is the next step.
4. **Tentative Pattern:** The required configurations appear when the largest arc lengths are distributed such that exactly two adjacent pairs sum to $\ge \lceil N/2 \rceil$.
