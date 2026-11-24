### [W1, round 1]
Task verification for small n:
1. Case n=1: If we choose $t_1 \ne s_1$, the inequality is $x_{t_1}x_{s_1} \le 2014000$. The maximum value of the LHS occurs when $x_{t_1} = x_{s_1} = 1007$, giving LHS = 1014049. Since $1014049 \le 2014000$, $n=1$ is possible.
2. Test Case (Constant Distribution): If $x_i = 2014/1000$ for all $i$, the inequality simplifies to $n (2014/1000)^2 \le 2014 \cdot 1000$. Solving for $n$ yields $n \le 1000^3 / 2014 \approx 496524.26$.
The maximum integer $n$ satisfying the inequality under this specific distribution is $n = 496524$.

### [W2, round 1]
### Derivation of Upper Bound on n

**1. Quadratic Form Representation:**
Let $X = (x_1, \ldots, x_M)^T$ where $M=1000$. We define the $M \times M$ symmetric matrix $A$ such that $A_{jk}$ is the number of pairs $(t_i, s_i)$ from the given $n$ pairs such that $\{t_i, s_i\} = \{j, k\}$.
The sum is $Q = \sum_{i=1}^n x_{t_i}x_{s_i} = X^T A X$.
$A$ is a non-negative integer matrix. The sum of all entries in $A$ is $\sum_{j, k} A_{jk} = n$.

**2. Constraint and Necessary Condition:**
We are given that $Q \le S \cdot M$ must hold for all non-negative $X$ such that $\sum x_i = S$ ($S=2014, M=1000$).
To find a necessary condition on $n$ (which is related to $\lambda_{max}(A)$), we consider the maximum value of $Q$ under the constraint $\sum x_i = S$.

The maximum of the quadratic form $X^T A X$ subject to $\sum x_i = S$ (even when allowing $x_i$ to be general real numbers, which gives a tight necessary bound) is bounded by $S^2 \lambda_{max}(A)$ if we normalize the vector $X$ differently, or more commonly, if we analyze the worst-case distribution of $x_i$.

Using the standard bounding technique for maximizing a quadratic form over a hyperplane (ignoring the $x_i \ge 0$ restriction for the necessary condition), the maximum value is related to $\lambda_{max}(A)$. To satisfy $Q \le S \cdot M$, we must have:
$$ \max_{X: \sum x_i = S} X^T A X \le S M $$
A necessary condition derived from spectral analysis suggests that if the inequality is to hold universally, the matrix $A$ must satisfy:
$$ S^2 \lambda_{max}(A) \le S M $$

**3. Formal Upper Bound:**
Solving for $\lambda_{max}(A)$:
$$ \lambda_{max}(A) \le \frac{M}{S} $$
Since $A$ is a non-negative matrix, the largest eigenvalue $\lambda_{max}(A)$ is bounded below by the maximum row sum (or column sum), $R_{max} = \max_j \sum_k A_{jk}$. Since $\sum A_{jk} = n$, the average row sum is $n/M$.
Thus, $n/M \le R_{max} \le \lambda_{max}(A)$.
Combining these bounds provides the upper bound on $n$:
$$ \frac{n}{M} \le \lambda_{max}(A) \le \frac{M}{S} $$
Therefore, a necessary condition on $n$ is:
$$ n \le \frac{M^2}{S} $$

### [W4, round 1]
## Investigation into Matrix Configuration for Maximizing n

**Goal:** To investigate sparse, structured, or block matrix configurations $A$ that might allow $n = \sum A_{ij}$ to exceed the maximum derived from the uniform density case, while respecting the necessary condition $\lambda_{max}(A) \le M/S = 1000/2014$. ($M=1000, S=2014$).

**1. Theoretical Baseline (Uniform Case):**
The maximum theoretical sum of entries $n$ for a non-negative matrix $A$ constrained by its spectral radius $\rho(A) \le C$ is generally achieved when $A$ is proportional to the all-ones matrix $J$. In this case, $A_{ij} = C/M = 1/2014$ (for real values), yielding $n = M^2/S \approx 496.5$.

**2. Sparse Configurations:**
Sparse matrices (matrices with many zero entries) inherently reduce $n$ (the sum of entries) since $n$ is defined as the total count of pairs chosen. Therefore, sparse configurations cannot yield a larger $n$ than the densest possible matrix satisfying the constraint.

**3. Structured/Block Configurations:**
We investigate block matrices $A$. Let $A$ be divided into $k \times k$ blocks of size $m \times m$, where $km=M=1000$.
If we aim to maximize $n$, we attempt to maintain the average density while distributing the entries.

*   **Hypothesis:** For non-negative matrices, structural partitioning (e.g., block-diagonal or circulant structures) generally tends to reduce the total sum of entries $n$ relative to the uniform case, unless the structure specifically allows for highly optimized eigenvalue distribution (e.g., highly correlated sub-blocks).
*   **Block-Diagonal Example:** If $A = \text{diag}(A_1, \ldots, A_k)$, then $\lambda_{max}(A) = \max_j \lambda_{max}(A_j)$. To maximize $n = \sum \sum A_{ij}$, we maximize the density within each block $A_j$ while keeping $\lambda_{max}(A_j) \le C$. If $A_j$ is uniform, $A_j = c_j J_m$, then $m c_j \le C$. The total contribution is $k \cdot m^2 c_j \approx k m (C) = M C$. This structure does not exceed the uniform bound $MC$.

**Conclusion of Investigation:**
Based on standard matrix theory for non-negative matrices, the uniform configuration $A_{ij} \propto J$ appears to maximize the total sum $n$ given the spectral radius constraint $\lambda_{max}(A) \le M/S$. Alternative structured configurations, such as block matrices, do not mathematically offer a pathway to achieving $n > M^2/S$. The task requirement suggests seeking alternatives, but the analysis indicates that the optimal configuration is the densest one possible, which is the uniform matrix.

### [W2, round 2]
### [W2, round 2] Verification of Constant Distribution Bound

I rigorously tested the necessary condition using the constant distribution $x_i = S/M$.
Let $M=1000$ and $S=2014$. The constraint is $\sum x_i = S$.
The LHS of the inequality is $Q = \sum_{i=1}^n x_{t_i}x_{s_i}$.
For the constant distribution, $x_{t_i}x_{s_i} = (S/M)^2$.
Thus, $Q = n (S/M)^2$.
The required inequality $Q \le S M$ becomes:
$$ n \left(\frac{S}{M}\right)^2 \le S M $$
Solving for $n$:
$$ n \le S M \cdot \frac{M^2}{S^2} = \frac{M^3}{S} $$
This confirms that the necessary condition derived from the uniform distribution is $n \le M^3/S$. This contrasts with the $n \le M^2/S$ derived via spectral radius analysis in previous notes, suggesting the spectral bound used might not be tight or directly applicable here, or that the constant distribution provides a tighter necessary bound. The current bound is $n \le 1000^3 / 2014 \approx 496524$.

### [W4, round 2]
[W4, round 2]
Assessment of the theoretical maximum n = 496524 against the necessary spectral bound.

1. Necessary Condition Review: The inequality requires $Q = X^T A X \le S M$ for all $X$ such that $\sum x_i = S$. This implies a necessary condition on the maximum eigenvalue of the symmetric matrix $A$: $\lambda_{max}(A) \le M/S = 1000/2014 \approx 0.496524$.

2. Spectral Bound on n: For any non-negative matrix $A$, the maximum eigenvalue is bounded below by the maximum row sum $R_{max} = \max_j \sum_k A_{jk}$. Since $\sum_{j,k} A_{jk} = n$, the average row sum is $n/M$. Thus, $\lambda_{max}(A) \ge n/M$. Combining these bounds yields $n/M \le M/S$, or $n \le M^2/S \approx 496.524$.

3. Contradiction: The stated premise assumes $n$ can be as high as 496524. However, if $n=496524$, then the required row sum average is $n/M = 496.524$. This forces $\lambda_{max}(A) \ge 496.524$. This violates the necessary condition $\lambda_{max}(A) \le 0.496524$ by a large margin. The bound $n \le 496524$ only satisfies the inequality for the specific uniform distribution $x_i = S/M$, but it does not satisfy the necessary condition for all choices of $X$.

4. Addressing the Task Question (Structural Difference): If we hypothetically assume a matrix $A$ exists with $\sum A_{ij} = 496524$, any such matrix must have a very large $\lambda_{max}(A) \ge 496.524$.
For a fixed sum $n$, the largest eigenvalue $\lambda_{max}(A)$ is generally optimized when the matrix is as close to uniform as possible (i.e., $A_{ij} \approx n/M^2$). Non-uniform configurations typically cause the eigenvalues to disperse, potentially *reducing* the largest eigenvalue relative to the uniform case, but only up to the constraint set by $n/M$. Since the uniform configuration already yields the absolute minimum possible value for $\lambda_{max}(A)$ given the total sum $n$, no non-uniform configuration can make $\lambda_{max}(A)$ smaller, and thus no non-uniform configuration can *prevent* the quadratic form from exceeding the required bound more than the uniform configuration already does.

Conclusion: The premise leads to a necessary failure of the required inequality. Theoretically, for a fixed sum $n$, the uniform configuration does not allow for a *smaller* maximum quadratic form than any non-uniform configuration, and thus cannot invalidate the necessary bound $n \le M^2/S$ by allowing a larger Q than the uniform case. The uniform case $A_{ij} = n/M^2$ achieves the minimum possible $\lambda_{max}(A)$ for the sum $n$.
