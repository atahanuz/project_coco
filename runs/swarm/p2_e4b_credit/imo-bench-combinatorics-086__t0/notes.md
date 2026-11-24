### [W3, round 1]
Analysis of $g(n)$: The function $g(n) = n^2 - n + 1$ is always odd for all $n \in \mathbb{Z}_{\ge 0}$, since $n^2 - n = n(n-1)$ is always even. This suggests a structural bias towards odd numbers if $f$ were related to $g$.

Hypothesis for Extremes ($a, b$):
The domain size is $100 \times 100 = 10000$. The minimum ($a$) and maximum ($b$) of $N$ are sought.
1. Maximum ($b$): Since $f$ is a bijection, it must eventually take on even numbers. However, the strong monotonic ordering allows for high flexibility in parity distribution. We hypothesize that a bijection $f$ can be constructed such that the first 10000 values it assigns to the grid points are all odd, leading to $b = 10000$.
2. Minimum ($a$): Conversely, we hypothesize that $f$ can be constructed such that the first 10000 values assigned are all even, leading to $a = 0$.

Assuming these extreme distributions are possible under the given constraints, the product $ab$ would be $0 \times 10000 = 0$. Further research would be required to definitively prove the existence of such bijections $f$.

### [W1, round 1]
Investigated the condition that $f$ must be strictly increasing in both $x$ and $y$. The standard Cantor pairing function $C(x, y) = \frac{(x+y)(x+y+1)}{2} + y$ satisfies this condition and is a bijection. Calculated $N$, the number of pairs $(x, y)$ with $0 \le x, y < 100$ where $C(x, y)$ is odd. The calculation yielded $N=5000$. Given that the constraints impose a very strong structural property on $f$ (compatibility with the product order), it is conjectured that all such monotone bijections yield the same count $N$, meaning $a=b=5000$.

### [W2, round 1]
Analysis of the strict monotonicity condition: The property states that the relative ordering of values is preserved when translating both coordinate pairs by (1, 0) or (0, 1). This condition is characteristic of functions $f$ that preserve the product order structure of $\mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0}$ when mapped to $\mathbb{Z}_{\ge 0}$. This strongly suggests that $f$ must be strictly increasing in both $x$ and $y$, i.e., $f(x+1, y) > f(x, y)$ and $f(x, y+1) > f(x, y)$ for all $x, y$. If this strict monotonicity holds, and since $f$ is a bijection to $\mathbb{Z}_{\ge 0}$, the set of the first $100 \times 100 = 10000$ values $\{f(x, y) \mid 0 \le x, y < 100\}$ must be $\{0, 1, \dots, 9999\}$. In this case, exactly half of these values are odd, implying $N = 5000$. This suggests that $a=b=5000$, leading to $ab = 25,000,000$.
