### [W1, round 1]
Analysis of the specific case $A_{jk} = n/1000^2$:
Let $N=1000$ and $S=2014$. The quadratic form is $Q(x) = \sum_{j=1}^N \sum_{k=1}^N \frac{n}{N^2} x_j x_k = \frac{n}{N^2} (\sum x_j)^2 = \frac{n}{N^2} S^2$.
Since $Q(x)$ is constant for all valid $x$, $M(A) = \frac{n}{N^2} S^2$.
We require $M(A) \le S \cdot N$, which leads to:
$\frac{n}{1000^2} (2014)^2 \le 2014 \cdot 1000$.
Solving for $n$: $n \le \frac{1000^3}{2014} \approx 496524.329...$.
The maximum integer $n$ satisfying this bound is 496524.

### [W4, round 1]
The quadratic form $\sum_{i=1}^n x_{t_i}x_{s_i}$ can be written as $X^T A X$, where $A = \sum_{i=1}^n E_{t_i, s_i}$ and $E_{t_i, s_i}$ is the matrix with 1 at position $(t_i, s_i)$ and 0 elsewhere.
The constraint $\sum x_i = 2014$ allows substitution $x_i = 2014 y_i$ where $\sum y_i = 1$.
The maximum value $M(A)$ is thus $2014^2 \cdot \max_{Y \in \Delta_{1000}} (Y^T A Y)$.
The required condition $M(A) \le 2014 \cdot 1000$ reformulates to:
$\max_{Y \in \Delta_{1000}} (Y^T A Y) \le \frac{1000}{2014}$.
This relates the condition directly to the maximal value of the quadratic form associated with matrix $A$ over the standard simplex, which is related to the maximal eigenvalue of $A$.

### [W2, round 1]
**Investigation on the impact of diagonal entries ($A_{jj}$)**

Let $N=1000$ and $S=2014$. We are maximizing $n = \sum_{j,k} A_{j,k}$ subject to the constraint that for all non-negative $\mathbf{x}$ with $\sum x_i = S$:
$$Q(\mathbf{x}) = \sum_{j,k} A_{j,k} x_j x_k \le S N$$

Since $Q(\mathbf{x})$ is determined by the symmetric part of $A$, let $A_{sym} = (a_{jk})$ be the corresponding symmetric matrix, where $a_{jk} = A_{j,k} + A_{k,j}$. The constraint becomes:
$$\mathbf{x}^T A_{sym} \mathbf{x} \le S N$$

By setting $y_i = x_i/S$, we have $\sum y_i = 1$ and $y_i \ge 0$. The constraint is equivalent to finding $A_{sym}$ such that:
$$\max_{\mathbf{y} \in \Delta_N} \mathbf{y}^T A_{sym} \mathbf{y} \le \frac{N}{S}$$

We compare two cases:
1. **Case $A_{jj} > 0$ (Diagonal non-zero):** We can choose $A_{sym}$ to be proportional to the all-ones matrix $J$, i.e., $a_{jk} = \alpha$ for all $j, k$.
   $$\mathbf{y}^T A_{sym} \mathbf{y} = \alpha \sum y_j y_k = \alpha (\sum y_j)^2 = \alpha$$
   The constraint requires $\alpha \le N/S$. To maximize $n = \sum a_{jk} = N^2 \alpha$, we choose $\alpha = N/S$.
   $$n_{diag} = N^2 \frac{N}{S} = \frac{N^3}{S}$$

2. **Case $A_{jj} = 0$ (Diagonal zero):** We can choose $A_{sym}$ to be proportional to $J-I$, i.e., $a_{jj}=0$ and $a_{jk} = \alpha$ for $j \ne k$.
   $$\mathbf{y}^T A_{sym} \mathbf{y} = \alpha \left( (\sum y_j)^2 - \sum y_j^2 \right) = \alpha \left( 1 - \sum y_j^2 \right)$$
   The maximum value of this expression occurs when $\sum y_j^2$ is minimized, which happens at $y_j = 1/N$ for all $j$, giving a value $\alpha (1 - 1/N)$.
   The constraint requires $\alpha (1 - 1/N) \le N/S$.
   $$\alpha \le \frac{N/S}{1 - 1/N} = \frac{N^2}{S(N-1)}$$
   To maximize $n = \sum a_{jk} = N(N-1) \alpha$, we choose the maximal $\alpha$.
   $$n_{off-diag} = N(N-1) \frac{N^2}{S(N-1)} = \frac{N^3}{S}$$

**Conclusion:** Both configurations yield an achievable maximum $n$ of $N^3/S$. Therefore, choosing $A$ with non-zero diagonal elements does not allow for a strictly larger $n$ than choosing an $A$ where all diagonal elements are zero.

### [W3, round 1]
Analysis for N=2 (S=2014):
We seek the largest integer $n = A+B+C$ such that $A x_1^2 + B x_2^2 + C x_1x_2 \le 2S$ for all $x_1+x_2=S=2014$.
1. Testing the endpoint $(S, 0)$: Requires $A S^2 \le 2S$, so $A \le 2/S \approx 0.00099$. Thus $A=0$.
2. Testing the endpoint $(0, S)$: Requires $B S^2 \le 2S$, so $B \le 2/S \approx 0.00099$. Thus $B=0$.
3. Testing the midpoint $(S/2, S/2)$: Requires $n (S/2)^2 \le 2S$, so $n \le 8/S \approx 0.00397$. Thus $n=0$.
The largest integer $n$ satisfying the constraint is $n=0$. Since the problem asks for the largest *positive* integer $n$, no such integer exists under the specified conditions ($S=2014$).

### [W4, round 2]
### [W4, round 2] Formal Argument for $A_{sym} = 0$

The problem requires finding the largest integer $n = \sum_{j,k} A_{jk}$ such that for $N=1000$ and $S=2014$, we have:
$$\max_{\mathbf{y} \in \Delta_N} \mathbf{y}^T A_{sym} \mathbf{y} \le \frac{N}{S} = \frac{1000}{2014}$$
Since $A$ has non-negative integer entries, $A_{sym}$ has non-negative integer entries, denoted $a_{jk} = A_{jk} + A_{kj}$.

**Step 1: Analyzing Diagonal Entries ($a_{kk}$)**
Let $\mathbf{y}$ be a standard basis vector $\mathbf{e}_k$, where $y_k=1$ and all other components are zero. Since $\mathbf{e}_k \in \Delta_N$, the maximum must satisfy:
$$\mathbf{e}_k^T A_{sym} \mathbf{e}_k = a_{kk} \le \frac{1000}{2014}$$
Since $1000/2014 \approx 0.4965$, and $a_{kk}$ must be a non-negative integer, the only possibility is $a_{kk} = 0$ for all $k=1, \ldots, N$.

**Step 2: Analyzing Off-Diagonal Entries ($a_{jk}, j \ne k$)**
Assume there exists an off-diagonal entry $a_{jk} \ge 1$. We test a specific vector $\mathbf{y}$ concentrated on indices $j$ and $k$. Let $y_j = 1/2$, $y_k = 1/2$, and $y_i = 0$ for $i \ne j, k$. This vector $\mathbf{y}$ is in $\Delta_N$.
The quadratic form evaluated at $\mathbf{y}$ is:
$$\mathbf{y}^T A_{sym} \mathbf{y} = a_{jj} y_j^2 + a_{kk} y_k^2 + 2 a_{jk} y_j y_k$$
Using $a_{jj}=0$ and $a_{kk}=0$ (from Step 1):
$$\mathbf{y}^T A_{sym} \mathbf{y} = 0 + 0 + 2 a_{jk} (1/2)(1/2) = \frac{a_{jk}}{2}$$
The required condition dictates that this value must be less than or equal to the bound:
$$\frac{a_{jk}}{2} \le \frac{1000}{2014}$$
$$a_{jk} \le \frac{2000}{2014} \approx 0.993$$
Since $a_{jk}$ is a non-negative integer, the only possibility is $a_{jk} = 0$ for all $j \ne k$.

**Conclusion:**
Since all diagonal entries ($a_{kk}$) and all off-diagonal entries ($a_{jk}$) must be zero, $A_{sym}$ must be the zero matrix. Since $A$ has non-negative integer entries, $A_{sym}=0$ implies $A$ is the zero matrix. Consequently, the total sum $n = \sum A_{jk} = 0$. This formally proves that the largest integer $n$ satisfying the condition must be 0.

### [W2, round 2]
**Formal Proof: $A_{sym}$ must be zero for $N=1000, S=2014$.**

The condition requires that for the symmetric matrix $A_{sym}$, where $a_{jk}$ are non-negative integers derived from the counts $t_i, s_i$, the following holds for the standard simplex $\Delta_{1000}$:
$$\max_{\mathbf{y} \in \Delta_{1000}} \mathbf{y}^T A_{sym} \mathbf{y} \le \frac{N}{S} = \frac{1000}{2014}$$

1.  **Diagonal Entries ($a_{jj}$):**
    Consider the basis vector $\mathbf{e}_j$, which is in $\Delta_{1000}$.
    The quadratic form evaluated at $\mathbf{e}_j$ is:
    $$\mathbf{e}_j^T A_{sym} \mathbf{e}_j = a_{jj}$$
    Since $a_{jj}$ is a non-negative integer, we must have $a_{jj} \le 1000/2014$. Since $1000/2014 < 1$, the only non-negative integer satisfying this is $a_{jj} = 0$. Thus, all diagonal entries must be zero.

2.  **Off-Diagonal Entries ($a_{jk}, j \ne k$):**
    Consider a point $\mathbf{y}$ supported on two coordinates, $y_j = 1/2$ and $y_k = 1/2$ (and $y_i=0$ otherwise). This point is in $\Delta_{1000}$.
    The quadratic form evaluated at $\mathbf{y}$ is:
    $$\mathbf{y}^T A_{sym} \mathbf{y} = \frac{1}{2} a_{jj} y_j^2 + \frac{1}{2} a_{kk} y_k^2 + a_{jk} y_j y_k$$
    Since $a_{jj}=0$ and $a_{kk}=0$, this simplifies to:
    $$\mathbf{y}^T A_{sym} \mathbf{y} = a_{jk} (1/2)(1/2) = \frac{a_{jk}}{4}$$
    Wait, there is an error in the generic formula I just wrote down.
    Let $\mathbf{y} = (0, \dots, 1/2, \dots, 1/2, \dots, 0)$ where $1/2$ is at $j$ and $k$.
    $$\mathbf{y}^T A_{sym} \mathbf{y} = \sum_{i, l} a_{il} y_i y_l$$
    The only non-zero terms are when $i, l \in \{j, k\}$.
    $$\sum_{i, l \in \{j, k\}} a_{il} y_i y_l = a_{jj} y_j^2 + a_{kk} y_k^2 + a_{jk} y_j y_k + a_{kj} y_k y_j$$
    Since $a_{jj}=0, a_{kk}=0$ and $a_{kj} = a_{jk}$:
    $$0 + 0 + a_{jk} (1/4) + a_{jk} (1/4) = a_{jk}/2$$
    We require $a_{jk}/2 \le 1000/2014$, which means $a_{jk} \le 2000/2014$.
    Since $2000/2014 < 1$, and $a_{jk}$ is a non-negative integer, we must have $a_{jk} = 0$.

**Conclusion:** Since all diagonal and off-diagonal entries of $A_{sym}$ must be zero, $A_{sym}$ is the zero matrix.

### [W1, round 2]
Review of integer constraint: For N=1000, S=2014, the condition requires the largest eigenvalue of $A_{sym}$ to be $\le 1000/2014 \approx 0.4965$. Since $A_{sym}$ must have non-negative integer entries derived from $A = \sum E_{t_i, s_i}$, any non-zero $A_{sym}$ will have $\lambda_{max} \ge 1$. Thus, the only solution satisfying the integer constraint is $A_{sym}=0$, meaning $n=0$. Consequently, there is no positive integer $n$ that satisfies the condition.
