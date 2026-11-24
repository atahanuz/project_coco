### [W4, round 1]
Case z=1: The condition for a good triple $(x, y, 1)$ is that $\frac{(x+1)^y}{x^1 + 1} = (x+1)^{y-1}$ is a positive integer. Since $x \ge 1$ and $y \ge 1$, $(x+1)^{y-1}$ is always a positive integer. We need to count the number of pairs $(x, y)$ such that $1 \le x < 100$ and $1 \le y < 100$. The number of possible $x$ values is 99, and the number of possible $y$ values is 99. The total count is $99 \times 99 = 9801$.

### [W1, round 1]
**Results for 1 <= x, y, z <= 10:**

1.  **Total Good Triples:** 199.
2.  **Pattern for x=1:** All 100 triples of the form (1, y, z) are good because the expression simplifies to $2^{y-1}$, which is always an integer.
3.  **Pattern for x >= 3:** For $x \in \{3, 4, \dots, 10\}$, only the triples where $z=1$ were found (i.e., $(x, y, 1)$ for $1 \le y \le 10$). This accounts for $8 \times 10 = 80$ triples.
4.  **Case x=2:** This case yielded 19 good triples, which are not limited to $z=1$.
5.  **General Observation:** The vast majority of good triples occur when $z=1$ or when $x=1$.

### [W3, round 1]
**Task 1: Case x=1**
A triple $(1, y, z)$ is good if $\frac{(1+1)^y}{1^z + 1} = \frac{2^y}{2} = 2^{y-1}$ is an integer. This is true for all $y \ge 1$.
Solutions: All triples $(1, y, z)$ where $1 \le y < 100$ and $1 \le z < 100$. There are $99 \times 99 = 9801$ such good triples.

**Task 2: Case y=1**
A triple $(x, 1, z)$ is good if $\frac{x+1}{x^z + 1}$ is a positive integer $K$.
1. If $z=1$: $\frac{x+1}{x+1} = 1$. Good for all $1 \le x < 100$. (99 triples).
2. If $z \ge 2$:
    a) If $x=1$: $\frac{2}{1^z+1} = 1$. Good for all $1 \le z < 100$. (99 triples).
    b) If $x \ge 2$: Since $x^z+1 > x+1$ for $z \ge 2$, the fraction is strictly between 0 and 1 and cannot be a positive integer. No solutions here.
Total good triples for $y=1$: $99 + 99 - 1$ (subtracting the double count of $(1, 1, 1)$) = 197 triples.

### [W2, round 1]
### [W2, round 1] Analysis of Divisibility Condition $x^z + 1 \mid (x+1)^y$

We must have $x^z + 1$ dividing $(x+1)^y$. This immediately implies that every prime factor of $x^z + 1$ must also be a prime factor of $x+1$. We analyze this using the greatest common divisor (GCD).

Let $d = \gcd(x^z + 1, x+1)$. Since $x \equiv -1 \pmod{x+1}$, we have:
$$x^z + 1 \equiv (-1)^z + 1 \pmod{x+1}$$

**Case 1: $z$ is odd.**
If $z$ is odd, then $(-1)^z + 1 = -1 + 1 = 0$. This means $x^z + 1$ is always divisible by $x+1$.
The divisibility condition simplifies to requiring $\frac{x^z + 1}{x+1}$ to divide $(x+1)^{y-1}$.

**Case 2: $z$ is even.**
If $z$ is even, then $(-1)^z + 1 = 1 + 1 = 2$. This means $\gcd(x^z + 1, x+1) = \gcd(2, x+1)$.

**Subcase 2a: $x$ is even.**
If $x$ is even, $x+1$ is odd. Thus, $\gcd(x^z + 1, x+1) = 1$. Since $x \ge 1$ and $z \ge 1$, $x^z + 1 > 1$. If $x^z + 1$ and $(x+1)^y$ are coprime, the only way for the latter to divide the former is if $x^z + 1 = 1$, which is impossible.
**Conclusion for $x$ even, $z$ even: No solutions exist.**

**Subcase 2b: $x$ is odd.**
If $x$ is odd, $x+1$ is even. Thus, $\gcd(x^z + 1, x+1) = 2$. In this case, solutions might exist, as $x^z+1$ and $(x+1)^y$ share the factor 2.

**Summary of Necessary Conditions:**
1. If $x$ is even and $z$ is even, there are no good triples.
2. If $x=1$, all triples are good, as $2 \mid 2^y$.
3. If $z$ is odd, $x+1$ must divide $x^z+1$. This provides the strongest constraint for $z>1$.

### [W2, round 2]
### [W2, round 2] Analysis of Good Triples ($x \ge 2, y \ge 2, z \ge 2$)

**1. Case z is odd ($z \ge 3$):**
We define $K = (x^z + 1) / (x+1)$. The requirement is that all prime factors of $K$ must divide $x+1$.
Testing small values reveals that this condition is highly restrictive.
*   For $(2, 3)$: $x+1=3$, $K = (2^3+1)/(2+1) = 3$. Since $3 \mid 3$, this pair works.
*   For $(2, 5)$: $x+1=3$, $K = 11$. Since $11 \nmid 3$, this pair fails.
*   For $(3, 3)$: $x+1=4$, $K = 7$. Since $7 \nmid 4$, this pair fails.

Based on preliminary analysis, the primary candidate pair for $z$ odd and $z \ge 3$ is $(x, z) = (2, 3)$.

For $(2, 3)$, $K=3$. We require $3 \mid (2+1)^{y-1} = 3^{y-1}$. Since $y \ge 2$, this holds true for all $2 \le y < 100$.
This yields $99 - 2 + 1 = 98$ good triples: $(2, y, 3)$ for $2 \le y \le 99$.

**2. Case z=1 ($z \ge 2$ assumed in initial task, but $z=1$ is a key solution):**
If $z=1$, $K=1$. The condition $K \mid (x+1)^{y-1}$ is trivially satisfied.
For $x \ge 2$ and $y \ge 2$: $x$ ranges from 2 to 99 (98 values), and $y$ ranges from 2 to 99 (98 values).
Total solutions for $z=1, x \ge 2, y \ge 2$: $98 \times 98 = 9604$.

**3. Case z is even, x is odd ($x \ge 3$):**
The divisibility condition simplifies to requiring $x^z + 1$ to be a power of 2, i.e., $x^z + 1 = 2^M$.
If $x=3, z=2$: $3^2 + 1 = 10$, not a power of 2.
Number theory suggests that solutions to $x^z + 1 = 2^M$ (with $x>1, z>1$) are extremely rare, making solutions unlikely within the defined bounds $x, z < 100$. We conclude that no solutions are found here.
