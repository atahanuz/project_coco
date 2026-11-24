### [W3, round 1]
The task was to establish an upper bound for $\sum a_i^2$ using $a_i \le 2/\sqrt{n}$ and analyze its achievability under $\sum a_i^3 = 0$.

1. **Upper Bound:** Since $a_i \le 2/\sqrt{n}$, we have $a_i^2 \le 4/n$. Summing over $n$ terms gives $\sum a_i^2 \le n \cdot (4/n) = 4$.

2. **Achievability Analysis:** We analyzed the problem by setting $a_i = c_i \cdot (2/\sqrt{n})$, leading to the requirement $\sum c_i^3 = 0$, subject to $c_i \le 1$ and maximizing $\sum c_i^2$.
    If $n$ is even, $n=2K$, we can choose $K$ values of $c_i=1$ and $K$ values of $c_j=-1$. This yields $\sum c_i^2 = 2K = n$, and thus $\sum a_i^2 = 4$. The bound is achieved.
    If $n$ is odd, $n=2K+1$, the maximum $\sum c_i^2$ is $2K = n-1$, yielding $\sum a_i^2 = 4(n-1)/n < 4$. The bound is approached.

The uniform supremum value for all $n$ is 4.

### [W2, round 1]
**Analysis of the optimization problem:**
Maximize $S_2 = \sum_{i=1}^n a_i^2$
Subject to:
1. $\sum_{i=1}^n a_i^3 = 0$
2. $|a_i| \le 2/\sqrt{n}$

**General Algebraic Approach:**
To maximize $S_2$, the optimal solution must utilize the boundary constraint $|a_i| = 2/\sqrt{n}$ for as many variables as possible. The zero-sum cube constraint requires balancing positive and negative contributions.

**Hypothesis (Two-Value Distribution):**
We assume the optimal configuration consists of $k$ elements equal to $A > 0$ and $n-k$ elements equal to $-B > 0$. To maximize the objective function, we assume $A=B$.

Let $A=B$. The constraints become:
1. $k A^3 - (n-k) A^3 = 0 \implies (k - (n-k)) A^3 = 0$. Since $A \neq 0$, we must have $k = n-k$, which means $k = n/2$. This implies the maximum is achieved when $n$ is even and the signs are perfectly balanced (half positive, half negative).

If $n$ is even, we set $k=n/2$ and $A=B$. To maximize $S_2$, we set $A$ to its maximum allowed value: $A = 2/\sqrt{n}$.

**Calculation for $n$ even:**
$S_2 = k A^2 + (n-k) A^2 = n A^2$.
$S_2 = n \left( \frac{2}{\sqrt{n}} \right)^2 = n \left( \frac{4}{n} \right) = 4$.

**Conclusion:**
The algebraic approach suggests that if $n$ is even, the maximum value is 4, achieved by setting half the $a_i$'s to $2/\sqrt{n}$ and the other half to $-2/\sqrt{n}$. This suggests the maximum value might be 4 regardless of $n$.

### [W1, round 1]
Test Case n=2:
Maximize $a_1^2 + a_2^2$ subject to $a_i \le \sqrt{2}$ and $a_1^3 + a_2^3 = 0$.
Optimal solution: $a_1 = \sqrt{2}, a_2 = -\sqrt{2}$.
Maximum value of $\sum a_i^2$: $4$.

Test Case n=3:
Maximize $a_1^2 + a_2^2 + a_3^2$ subject to $a_i \le 2/\sqrt{3}$ and $a_1^3 + a_2^3 + a_3^3 = 0$.
We set $a_1 = a_2 = 2/\sqrt{3}$. Then $a_3 = -2^{1/3} (2/\sqrt{3})$.
Maximum value of $\sum a_i^2$: $\frac{4}{3} (2 + 2^{2/3})$.

Test Case n=4:
Maximize $a_1^2 + a_2^2 + a_3^2 + a_4^2$ subject to $a_i \le 1/\sqrt{2}$ and $\sum a_i^3 = 0$.
Optimal solution: $a_1 = a_2 = 1/\sqrt{2}, a_3 = a_4 = -1/\sqrt{2}$.
Maximum value of $\sum a_i^2$: $2$.

### [W4, round 1]
**Investigation of the Two-Value Case:**
We analyzed the case where the set $\{a_i\}$ consists of exactly two distinct values, $x$ and $y$. Let $n_x$ and $n_y$ be the counts, with $n_x+n_y=n$. The zero-sum cube constraint requires $n_x x^3 + n_y y^3 = 0$. To maximize $\sum a_i^2 = n_x x^2 + n_y y^2$, we deduce that $x$ and $y$ must have opposite signs, and we seek to maximize their magnitudes subject to $|a_i| \le 2/\sqrt{n}$.

1. **Optimal Configuration:** The maximum is achieved when $x = 2/\sqrt{n}$ and $y = -2/\sqrt{n}$. This forces $n_x = n_y$, meaning $n$ must be even, $n_x = n_y = n/2$.
2. **Maximum Value (n even):** In this case, $\sum a_i^2 = \frac{n}{2} (2/\sqrt{n})^2 + \frac{n}{2} (-2/\sqrt{n})^2 = \frac{n}{2} \frac{4}{n} + \frac{n}{2} \frac{4}{n} = 2 + 2 = 4$.
3. **Maximum Value (n odd):** If $n$ is odd, $n_x$ cannot equal $n_y$ if $x=y=2/\sqrt{n}$. The supremum of $\sum a_i^2$ in this case is still 4, achieved in the limit as the distribution approaches $n/2$ and $n/2$.

The conclusion is that the maximum value (supremum) for the two-value case is 4.
