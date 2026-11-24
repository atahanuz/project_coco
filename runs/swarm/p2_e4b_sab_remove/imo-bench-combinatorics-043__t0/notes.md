### [W3, round 1]
Global Counting Argument Derivation:
Let $n_i$ be the size of study group $G_i$. Since $n_i = 2m_i + 1$, we have $m_i = (n_i - 1)/2$.
1. By counting pairs of students (Constraint i), we found: $\sum (n_i^2 - n_i) = N(N-1)$.
2. By counting student-lab memberships (Constraints ii and iii), we found: $\sum n_i m_i = kN$.
Substituting $m_i$: $\sum n_i \left(\frac{n_i - 1}{2}\right) = kN$.
This simplifies to the algebraic equation linking $k$ and the group sizes:
$$\sum_{i} (n_i^2 - n_i) = 2kN$$
Equating the results from both counting methods:
$$N(N-1) = 2kN$$
Since $N=579$, we solve for $k$: $k = (N-1)/2 = (579-1)/2 = 289$.
