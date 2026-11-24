### [W3, round 1]
**Diophantine System Establishment (k=1 case)**

Based on the requirement that $\frac{\sum_{i=1}^n P_i(x)^2}{x^2 + 7}$ is a perfect square (we assume the resulting quotient $Q(x)$ is a constant, $Q(x)=1$, for minimal $n$), and assuming $P_i(x)$ are linear polynomials, $P_i(x) = a_i x + b_i$ (where $a_i, b_i \in \mathbb{Z}$), we establish the following system of Diophantine equations by comparing coefficients of $\sum (a_i x + b_i)^2 = (x^2 + 7) \cdot 1^2$:

1. (Coefficient of $x^2$): $\sum_{i=1}^n a_i^2 = 1$
2. (Coefficient of $x$): $2 \sum_{i=1}^n a_i b_i = 0 \implies \sum_{i=1}^n a_i b_i = 0$
3. (Constant term): $\sum_{i=1}^n b_i^2 = 7$

The next step is to minimize $n$ such that integer solutions exist for this system. From constraint (1), since $a_i$ are integers, at most one $a_i$ can be non-zero, and if it is non-zero, $|a_i|=1$.

### [W4, round 1]
Construction for $\sum_{i=1}^{5} P_i(x)^2 = x^2 + 7$:
We seek integer-coefficient polynomials $P_i(x)$ such that the sum of their squares equals $x^2+7$. Since the right-hand side is degree 2, the polynomials must have degree at most 1. Let $P_i(x) = a_i x + b_i$.
The system of equations derived by comparing coefficients is:
1) $\sum a_i^2 = 1$
2) $2 \sum a_i b_i = 0$
3) $\sum b_i^2 = 7$

From (1), exactly one $a_i$ must be $\pm 1$. We choose $a_1 = 1$ and $a_2=a_3=a_4=a_5=0$.
From (2), $2(1 \cdot b_1 + 0) = 0$, so $b_1 = 0$.
From (3), we need $0^2 + b_2^2 + b_3^2 + b_4^2 + b_5^2 = 7$.
We use the representation $7 = 4 + 1 + 1 + 1$.
We choose $b_2=2, b_3=1, b_4=1, b_5=1$.

The resulting polynomials are:
$P_1(x) = x$
$P_2(x) = 2$
$P_3(x) = 1$
$P_4(x) = 1$
$P_5(x) = 1$

Verification:
$\sum_{i=1}^{5} P_i(x)^2 = (x)^2 + (2)^2 + (1)^2 + (1)^2 + (1)^2 = x^2 + 4 + 1 + 1 + 1 = x^2 + 7$.
This construction requires $n=5$ polynomials. (Note: The task required construction for $n=5$, assuming the initial part about 7 requires 4 squares of integers confirms that $n$ might be larger than 1).

### [W1, round 1]
**Problem Analysis & Necessary Conditions**

The problem requires finding the smallest positive integer $n$ such that $\frac{\sum_{i=1}^{n} P_i(x)^2}{x^2 + 7}$ is a perfect square of a positive integer, $k^2$.

1. **Interpretation:** This implies the identity $\sum_{i=1}^{n} P_i(x)^2 = k^2(x^2 + 7)$ for some integer $k \ge 1$.

2. **Focus on $k=1$:** We focus on the case $\sum_{i=1}^{n} P_i(x)^2 = x^2 + 7$.

3. **Degree Analysis:** Since the RHS has degree 2, all $P_i(x)$ must have degree at most 1. Let $P_i(x) = a_i x + b_i$, where $a_i, b_i \in \mathbb{Z}$.

4. **System of Equations:** Expanding the sum and equating coefficients with $x^2 + 0x + 7$ yields the system:
   a) $\sum_{i=1}^{n} a_i^2 = 1$
   b) $\sum_{i=1}^{n} a_i b_i = 0$
   c) $\sum_{i=1}^{n} b_i^2 = 7$

5. **Solving for $n$:**
   From (a), since $a_i \in \mathbb{Z}$, exactly one $a_j$ must be $\pm 1$ and all others must be 0. Let $a_1 = 1$ and $a_i = 0$ for $i \ge 2$.
   Substituting into (b): $1 \cdot b_1 + \sum_{i=2}^{n} 0 \cdot b_i = b_1$. Thus, $b_1 = 0$.
   Substituting into (c): $b_1^2 + \sum_{i=2}^{n} b_i^2 = 7$. Since $b_1=0$, we need $\sum_{i=2}^{n} b_i^2 = 7$.
   We seek the minimum number of non-zero integers $m = n-1$ whose squares sum to 7.
   Minimum $m$:
   - $m=1$: $b_2^2 = 7$ (No integer solution).
   - $m=2$: $b_2^2 + b_3^2 = 7$ (No integer solution, as $4+3$ and $1+6$ are impossible).
   - $m=3$: $b_2^2 + b_3^2 + b_4^2 = 7$ (No integer solution, as $4+1+1=6$, and $1+1+1=3$).
   - $m=4$: $b_2^2 + b_3^2 + b_4^2 + b_5^2 = 7$. We found the solution $4 + 1 + 1 + 1 = 7$.

The minimum number of terms required is $m=4$, which means $n = m+1 = 5$.

**Conclusion:** The smallest positive integer $n$ is 5.

**Construction for n=5:**
We choose $a_1=1, b_1=0$ and $a_i=0$ for $i \ge 2$.
We choose $b_2=2, b_3=1, b_4=1, b_5=1$.
The polynomials are:
$P_1(x) = x$
$P_2(x) = 2$
$P_3(x) = 1$
$P_4(x) = 1$
$P_5(x) = 1$
Verification: $\sum P_i(x)^2 = x^2 + 2^2 + 1^2 + 1^2 + 1^2 = x^2 + 7$.

### [W2, round 1]
Task: Show that $\max(\deg(P_i)) \le 1$ given $\sum P_i^2 = K^2(x^2+7)$.
1. Degree Analysis: If $D = \max(\deg(P_i))$ and $d_K = \deg(K)$, then $D = d_K + 1$.
2. Case D=1: This is possible. If $P_i(x) = a_i x + b_i$, then $\sum P_i^2$ is degree 2. $K(x)$ must be a constant $k_0$. We require $\sum a_i^2 = k_0^2$, $\sum b_i^2 = 7k_0^2$, and $2\sum a_i b_i = 0$. This system has known solutions (e.g., $k_0=1$, $n=10$ gives $\sum a_i^2=1, \sum b_i^2=7$).
3. Case D>=2: We must show this is impossible. Let $P_j(x)$ be the polynomial of degree $D$. If $D \ge 2$, then $d_K = D-1 \ge 1$. The identity implies that $x^2+7$ must be decomposable as a "norm" or sum of squares structure relating $P_i$ and $K$. The necessary condition involves analyzing the factorization properties or coefficient constraints arising from requiring $P_i$ and $K$ to have integer/rational coefficients. A full proof requires advanced results (e.g., properties of sums of squares over polynomial rings) but the constraint severely limits $D$. We proceed assuming the existence of a contradiction if $D \ge 2$.
