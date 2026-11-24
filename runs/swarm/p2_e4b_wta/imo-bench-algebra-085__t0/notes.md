### [W3, round 1]
Under the assumption that all $x_i$ are distributed equally among $D=1000$ variables ($x_i = 2014/1000$), the required inequality $\sum_{i=1}^n x_{t_i}x_{s_i} \le 2014 \cdot 1000$ simplifies to $n \cdot (2014/1000)^2 \le 2014 \cdot 1000$. Solving for $n$ yields $n \le 1000^3 / 2014 \approx 496524.33$. Thus, the largest integer $n$ in this specific case is 496524.

### [W1, round 1]
Proof attempt for the required condition: Assume there exists an index $i$ such that $t_i = s_i = k$ for some $k \in \{1, \ldots, 1000\}$. Let $N_k$ be the count of such terms involving index $k$. Consider setting $x_k = 2014$ and $x_j = 0$ for all $j \neq k$. This satisfies the constraint $\sum x_j = 2014$. The LHS of the inequality is $\sum_{i=1}^n x_{t_i}x_{s_i}$. For this choice of $x_j$, the LHS simplifies to $N_k \cdot x_k^2 = N_k \cdot 2014^2$. The required inequality is LHS $\le 2014 \cdot 1000$. If $N_k \ge 1$, then LHS $\ge 2014^2$. Since $2014^2 > 2014 \cdot 1000$ (as $2014 > 1000$), the inequality fails. Thus, we must have $t_i \neq s_i$ for all $i$.

### [W4, round 1]
The problem asks for the maximum integer $n$ such that $\sum_{i=1}^n x_{t_i}x_{s_i} \le 2014 \cdot 1000$ for all non-negative $x_i$ summing to 2014.

Let $N=1000$ be the dimension of the variables $X=(x_1, \ldots, x_N)$.
Let $C=2014$ be the sum constraint, $x_1 + \cdots + x_N = C$.
Let $M=1000$ be the dimension $N$.

The sum $\sum_{i=1}^n x_{t_i}x_{s_i}$ can be represented as a quadratic form $X^T A X$, where $A$ is an $N \times N$ symmetric matrix. $A_{j,k}$ counts the total number of times the index pair $\{j, k\}$ appears in the set $\{(t_i, s_i)\}_{i=1}^n$. Since $A$ must have non-negative integer entries, this construction holds.

The constraint requires that the maximum value of the quadratic form, subject to $\sum x_i = C$, must be less than or equal to $C \cdot M$.

We analyze the maximum of $X^T A X$ under the constraint $\sum x_i = C$.
A conservative upper bound is found by testing the vector $X$ proportional to the all-ones vector $\mathbf{1} = (1, 1, \ldots, 1)^T$.
Let $X = k \cdot \mathbf{1}$. Since $\sum x_i = C$, we must have $N k = C$, so $k = C/N = C/M$.
$X = (C/M) \cdot \mathbf{1}$.

We evaluate the quadratic form for this test vector:
$X^T A X = (C/M)^2 \cdot \mathbf{1}^T A \mathbf{1}$
$\mathbf{1}^T A \mathbf{1}$ is the sum of all entries in $A$, $\sum_{j, k} A_{jk}$. Since $A$ is derived from $n$ pairs $(t_i, s_i)$, and each pair contributes 2 to the total sum of entries (or $2$ if $t_i=s_i$), the total sum of entries is exactly $2n$.
(If $A$ is the symmetric count matrix, $\sum_{j,k} A_{jk} = 2n$).

Thus, $X^T A X = (C/M)^2 \cdot 2n$.

Applying the required inequality:
$(C/M)^2 \cdot 2n \le C \cdot M$

Solving for $n$:
$2n \le C M \cdot (M/C)^2$
$2n \le M^3 / C$
$n \le \frac{M^3}{2C}$

Substituting $M=1000$ and $C=2014$:
$n \le \frac{1000^3}{2 \cdot 2014} = \frac{1,000,000,000}{4028}$
$n \le 248268.59...$

The theoretical upper bound for $n$ is 248,268.
Note: This bound is derived by checking a specific vector $X$, which provides a sufficient condition for the inequality to hold, yielding an upper bound on $n$. The relationship to $\lambda_{max}(A)$ is implicitly established by bounding the quadratic form using a specific test vector, which in extremal cases often approaches the bound set by $\lambda_{max}(A)$ scaled by the constraint properties.

### [W3, round 2]
**Analysis of $\lambda_{max}(A)$ (Task requirement):**

We are asked to analyze the maximum eigenvalue $\lambda_{max}(A)$ for a matrix $A$ derived from $K_{1000}$ (so $N=1000$). The defining constraint for off-diagonal entries is $A_{k,l}+A_{l,k}=1$ for $k \neq l$.

We assume, based on standard graph matrix interpretations, that $A$ is symmetric, implying $A_{k,l} = 1/2$ for $k \neq l$. We also assume the diagonal entries are zero, $A_{k,k}=0$, consistent with the adjacency matrix of a simple graph $K_N$.

The matrix $A$ can be written as:
$A = \frac{1}{2}(J - I)$, where $J$ is the $1000 \times 1000$ all-ones matrix and $I$ is the identity matrix.

The eigenvalues of $J$ are $N$ (with eigenvector $\mathbf{1}$) and $0$ (with multiplicity $N-1$).
The eigenvalues of $J-I$ are $N-1$ (for $\mathbf{1}$) and $-1$ (for other eigenvectors).

Thus, the eigenvalues of $A = \frac{1}{2}(J-I)$ are:
1. $\lambda_1 = \frac{1}{2}(N-1)$ (corresponding to $\mathbf{1}$)
2. $\lambda_{k} = -\frac{1}{2}$ (with multiplicity $N-1$)

Since $N=1000$, the maximum eigenvalue is:
$\lambda_{max}(A) = \frac{1000 - 1}{2} = \frac{999}{2} = 499.5$.

We need to determine if $\lambda_{max}(A) \le M=1000$.
Since $499.5 \le 1000$, the condition is satisfied.

### [W1, round 2]
[W1, round 2]
The task requires maximizing $n$ such that the underlying matrix $A$ is a simple adjacency matrix of a graph on $N=1000$ vertices, subject to the constraint $A_{k,l} + A_{l,k} \le 1$. This constraint implies that between any two distinct vertices $k$ and $l$, there can be at most one directed edge (either $k \to l$ or $l \to k$, but not both).
Since $A$ is a simple adjacency matrix, $A_{k,l} \in \{0, 1\}$ and $A_{k,k}=0$.
The number $n$ corresponds to the total number of edges in this directed graph, $n = \sum_{k \neq l} A_{k,l}$.
To maximize $n$, we must orient every possible edge between pairs of distinct vertices. The number of pairs of vertices is $\binom{N}{2}$.
Thus, the maximum possible value for $n$ is $\binom{1000}{2} = \frac{1000 \times 999}{2} = 499,500$.
The resulting matrix $A$ is the adjacency matrix of a complete asymmetric digraph (a tournament graph oriented such that $A_{k,l} + A_{l,k} = 1$ for all $k \neq l$). A simple construction is to define $A_{k,l} = 1$ if $k < l$, and $A_{k,l} = 0$ otherwise.

### [W2, round 2]
### Verification of W2's Single Pair Constraint Proof

**Goal:** Rigorously prove that if $A_{k,l} + A_{l,k} \ge 2$ for $k \neq l$, the inequality $\sum_{i=1}^n x_{t_i}x_{s_i} \le 2014 \cdot 1000$ fails for the test vector $X$ where $x_k=x_l=C/2$ and $x_j=0$ for $j \neq k, l$.

**Definitions:**
1. $N=1000$, $C=2014$.
2. The quadratic form is $Q(X) = \sum_{i=1}^n x_{t_i}x_{s_i} = X^T A X$.
3. $A_{j,m}$ is the coefficient matrix. Since $k \neq l$, the coefficient of $x_k x_l$ is $A_{k,l} + A_{l,k}$.
4. The condition given is $A_{k,l} + A_{l,k} \ge 2$.

**Proof Steps:**

1. **Analyze the Test Vector:**
   The test vector $X$ is defined such that $x_k = C/2$ and $x_l = C/2$. This vector satisfies the constraint $\sum x_i = C/2 + C/2 = C$.

2. **Calculate the Quadratic Form $Q(X)$:**
   $Q(X) = X^T A X = \sum_{j, m} A_{j, m} x_j x_m$.
   Since $x_j$ is zero unless $j \in \{k, l\}$, only terms involving $k$ or $l$ contribute.
   $Q(X) = A_{k,k} x_k^2 + A_{l,l} x_l^2 + A_{k,l} x_k x_l + A_{l,k} x_l x_k$.
   $Q(X) = A_{k,k} (C/2)^2 + A_{l,l} (C/2)^2 + (A_{k,l} + A_{l,k}) (C/2)^2$.

3. **Establish the Failure Condition (Minimum Case):**
   To demonstrate the inequality fails, we find the minimum value of $Q(X)$ subject only to the condition $A_{k,l} + A_{l,k} \ge 2$. This minimum occurs when the diagonal terms $A_{k,k}$ and $A_{l,l}$ are zero.
   Assuming $A_{k,k} = 0$ and $A_{l,l} = 0$, the quadratic form simplifies to:
   $Q(X)_{min} = (A_{k,l} + A_{l,k}) (C/2)^2$.

4. **Apply the Constraint:**
   Since $A_{k,l} + A_{l,k} \ge 2$, we must have:
   $Q(X) \ge 2 \cdot (C/2)^2 = 2 \cdot C^2 / 4 = C^2 / 2$.

5. **Compare with the Upper Bound:**
   The inequality requires $Q(X) \le C N$.
   We need to check if the minimum value $C^2/2$ is greater than the required upper bound $C N$.
   We compare $C^2/2$ vs $C N$. Since $C > 0$, we compare $C/2$ vs $N$.

   Substitute the values: $C = 2014$ and $N = 1000$.
   $C/2 = 2014 / 2 = 1007$.
   Since $1007 > 1000$, we have $C/2 > N$.
   Multiplying by $C$: $C^2/2 > C N$.

**Conclusion:**
Since $Q(X) \ge C^2/2$, and $C^2/2 > C N$, we have $Q(X) > C N$. Therefore, the required inequality fails whenever $A_{k,l} + A_{l,k} \ge 2$, provided we can find a configuration where $A_{k,k}=0$ and $A_{l,l}=0$. This rigorously verifies W2's finding.
