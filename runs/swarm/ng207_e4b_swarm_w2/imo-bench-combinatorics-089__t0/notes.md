### [W1, round 1]
For a $4 \times 4$ lattice, the maximum possible number of colors ($C$) is 4, as any $2 \times 2$ subgrid has only 4 cells.
We sought to construct a coloring using $C=4$ colors that satisfies the constraint: in every $2 \times 2$ subgrid, at least two squares share the same color (i.e., no $2 \times 2$ subgrid can use 4 distinct colors).

A successful pattern was found using colors $\{1, 2, 3, 4\}$, based on the formula $c(i, j) = (i+j) \pmod 4 + 1$ (using 1-based indexing $i, j \in \{1, 2, 3, 4\}$).

The resulting coloring pattern is:
$$
\begin{pmatrix}
1 & 2 & 3 & 4 \\
2 & 3 & 4 & 1 \\
3 & 4 & 1 & 2 \\
4 & 1 & 2 & 3
\end{pmatrix}
$$
This pattern guarantees that every $2 \times 2$ subgrid contains at most 3 distinct colors, thus satisfying the constraint.
Therefore, the maximum number of colors $C$ for a $4 \times 4$ lattice is 4.

### [W1, round 1]
REPORT on task "Systematically determine the maximum number of colors (C) that can be used in a small $4 \times 4$ lattice while satisfying the constraint (in every $2 \times 2$ subgrid, at least two squares share th": I systematically searched for the maximum number of colors ($C$) usable in a $4 \times 4$ lattice. Since a $2 \times 2$ subgrid has only 4 cells, $C$ cannot exceed 4. I constructed a coloring pattern using 4 colors, defined by the rule $c(i, j) = (i+j) \pmod 4 + 1$. This pattern was verified to ensure that every $2 \times 2$ subgrid contains at most 3 distinct colors, thereby satisfying the constraint. The maximum number of colors found is 4.
Candidate answer: 4

### [W2, round 1]
Theoretical Upper Bound: The maximum number of colors is 199.
Justification: By examining the constraint propagation between adjacent rows of width $L=100$, it is possible to construct a coloring such that $R_{i+1}$ introduces a new color relative to $R_i$ while maintaining the $2\times 2$ constraint everywhere. Starting with $R_1$ using 100 distinct colors, we can sequentially introduce one new color in each of the remaining 99 rows. Thus, the total number of distinct colors used is $100 + 99 = 199$. This is achieved by setting $R_i = (C_1, C_2, \dots, C_{100})$ and $R_{i+1} = (C_{new}, C_1, C_2, \dots, C_{99})$, where $C_{new}$ is a new color, and verifying that the resulting $2\times 2$ blocks satisfy the constraint.

### [W2, round 1]
REPORT on task "Attempt to find a theoretical upper bound on the total number of colors used in the entire $100 \times 100$ lattice based solely on the $2 \times 2$ constraint. Investigate how the coloring of a $2 \t": I investigated the constraint propagation between adjacent rows to find the theoretical maximum number of colors. By demonstrating a construction where $R_{i+1}$ can introduce a new color while satisfying the $2\times 2$ constraint, starting with a row of 100 distinct colors, I found that the maximum number of colors increases linearly. For a $100 \times 100$ grid, this results in a total maximum of $100 + (100 - 1) = 199$ distinct colors.
Candidate answer: 199
