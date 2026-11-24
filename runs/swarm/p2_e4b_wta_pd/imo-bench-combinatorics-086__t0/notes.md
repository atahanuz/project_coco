### [W3, round 1]
1. Analysis of $g(n) = n^2 - n + 1$:
$g(n) = n(n-1) + 1$. Since $n$ and $n-1$ are consecutive integers, their product $n(n-1)$ is always even. Therefore, $g(n) = n(n-1) + 1$ is always odd.

2. Analysis of $f$:
The condition $f(x_1, y_1) > f(x_2, y_2) \implies f(x_1+1, y_1) > f(x_2+1, y_2)$ implies that $f$ is strictly increasing in $x$. If $x_1 > x_2$, then $f(x_1, y) > f(x_2, y)$ for any $y$.
Similarly, $f$ is strictly increasing in $y$. If $y_1 > y_2$, then $f(x, y_1) > f(x, y_2)$ for any $x$.
Since $f$ is a bijection from $\mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0}$ to $\mathbb{Z}_{\geqslant 0}$, it is a specific way of enumerating the non-negative integers using a 2D grid where the ordering is controlled by $f$.

3. Potential connection to $g$:
The function $g(n)$ generates a sequence of all odd numbers (if we disregard $g(0)=g(1)=1$, but since $g(n)$ is always odd, it is certainly constrained to odd values). This suggests that if $f$ is "simple" or "maximal" in some sense, it might favor odd values, similar to how $g(n)$ always yields an odd value. Further investigation into parity patterns of $f$ based on its coordinates is needed.

### [W4, round 1]
The problem asks for the minimum (a) and maximum (b) number (N) of odd values in the set $\{f(x, y) : 0 \le x, y < 100\}$. The total number of pairs is $100^2 = 10000$. Since $f$ is a bijection, the values form an ordered sequence of 10000 distinct non-negative integers. The monotonicity constraint ensures that the inputs map to values in strictly increasing order according to a fixed index ordering, but it does not restrict the parity pattern of the resulting values. By choosing the range of $f$ to be $\{0, 1, \dots, 9999\}$, the set contains exactly 5000 odd numbers and 5000 even numbers. Since the function $f$ must map the 10000 inputs to these 10000 values, the count $N$ must be exactly 5000, regardless of how the index ordering is realized. Therefore, $a = 5000$ and $b = 5000$. The product $ab = 25,000,000$.

### [W2, round 1]
Analysis of the strict monotonicity condition: If $f(x_1, y_1) > f(x_2, y_2)$, then $f(x_1+1, y_1) > f(x_2+1, y_2)$ and $f(x_1, y_1+1) > f(x_2, y_2+1)$.
This condition implies that the function $f$ must preserve the relative order of values when coordinates are shifted, making it a highly structured enumeration of $\mathbb{Z}_{\geqslant 0}^2$. Functions satisfying this property, such as $f(x, y) = Ax+By$ where $\gcd(A, B)=1$, are guaranteed to be bijections onto $\mathbb{Z}_{\geqslant 0}$.

We examine the parity of $f(x, y)$ for $0 \le x, y < 100$. The domain size is $100 \times 100 = 10000$.
1. If $f(x, y) = x+y$ (A=1, B=1, $\gcd(1, 1)=1$), $f(x, y)$ is odd when $x+y$ is odd. Since there are 50 even and 50 odd numbers in $\{0, \dots, 99\}$, $N = 50 \times 50 + 50 \times 50 = 5000$.
2. If $f(x, y) = 2x+y$ (A=2, B=1, $\gcd(2, 1)=1$), $f(x, y)$ is odd when $y$ is odd. There are 100 choices for $x$ and 50 choices for odd $y$. $N = 100 \times 50 = 5000$.

These simple linear forms satisfy the constraints and yield $N=5000$. Due to the extreme structural constraints imposed by the monotonicity condition, it is strongly expected that any valid bijection $f$ must distribute the parities almost uniformly over the given square, meaning $a=b=5000$.

### [W3, round 1]
4. Determining the bounds $a$ and $b$:
$N$ is the count of odd values $f(x, y)$ for $0 \le x, y < 100$. Since $f$ is a bijection onto $\mathbb{Z}_{\geqslant 0}$ and must satisfy strong monotonicity, the parity of $f(x, y)$ is determined by the specific ordering $f$.

Minimum $a$: To minimize $N$, we want $f(x, y)$ to be even for all $10000$ pairs in the domain. Although $f$ must be globally surjective onto $\mathbb{Z}_{\geqslant 0}$ (meaning it must hit odd numbers somewhere), we can construct a bijection $f$ where the $100 \times 100$ block maps exclusively to even numbers (e.g., $f(x, y) = 2k(x, y)$ for $0 \le x, y < 100$, where $k(x, y)$ is a standard increasing bijection, and the remaining odd numbers are covered elsewhere). Thus, the smallest possible value is $a=0$.

Maximum $b$: To maximize $N$, we want $f(x, y)$ to be odd for all $10000$ pairs. Similarly, we can construct a bijection $f$ where the $100 \times 100$ block maps exclusively to odd numbers (e.g., $f(x, y) = 2k(x, y) + 1$ for $0 \le x, y < 100$, and the remaining even numbers are covered elsewhere). Thus, the largest possible value is $b=10000$.

The product $ab$ is $0 \times 10000 = 0$.

### [W1, round 1]
FINAL CONCLUSION: The monotonicity constraint ensures a globally consistent enumeration $f: \mathbb{Z}_{\geqslant 0}^2 \to \mathbb{Z}_{\geqslant 0}$, but it does not strictly enforce a balanced parity distribution within the finite square $S = [0, 99)^2$. By carefully constructing the enumeration order $f$, we can prioritize mapping $S$ entirely to even numbers to achieve $a=0$ (minimum N), or entirely to odd numbers to achieve $b=10000$ (maximum N). The required product $ab = 0 \times 10000 = 0$.
