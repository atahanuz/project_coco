### [W1, round 1]
Calculated N(x) for x=1 to 100, where N(x) is the number of positive integers y such that 1/x + 1/y is a unit fraction.
N(x) = (tau(x^2) - 1) / 2, where tau is the divisor function.
Top 5 values found:
1. x = 60, N(x) = 22
2. x = 84, N(x) = 22
3. x = 90, N(x) = 22
4. x = 72, N(x) = 17
5. x = 96, N(x) = 16

### [W2, round 1]
Derivation of N(x):
We are counting pairs $(f_1, f_2)$ such that $d = f_1 f_2$ divides $x$, $f_1 > f_2 \ge 1$, and $\gcd(f_1, f_2) = 1$.

For a fixed divisor $d$ of $x$, the number of ways to write $d$ as a product of two coprime factors $f_1 f_2$ is determined by the number of distinct prime factors of $d$, denoted $\omega(d)$. Since $f_1$ and $f_2$ must be coprime, every prime power factor $p^a$ of $d$ must belong entirely to $f_1$ or entirely to $f_2$. This gives $2^{\omega(d)}$ ordered pairs $(f_1, f_2)$.

Since we require $f_1 > f_2 \ge 1$:
1. If $d=1$, then $(f_1, f_2) = (1, 1)$, which violates $f_1 > f_2$. Contribution is 0.
2. If $d>1$, then $f_1 \ne f_2$. The $2^{\omega(d)}$ pairs consist of $(f_1, f_2)$ and $(f_2, f_1)$. Exactly half satisfy $f_1 > f_2$. The count for $d>1$ is $2^{\omega(d)} / 2 = 2^{\omega(d)-1}$.

Therefore, $N(x)$ is the sum of these counts over all divisors $d$ of $x$:
$$N(x) = \sum_{d|x, d>1} 2^{\omega(d)-1}$$

Algorithm to calculate N(x):
1. Find all positive divisors $d$ of $x$.
2. For each $d > 1$, calculate $\omega(d)$ (the number of distinct prime factors of $d$).
3. Calculate the contribution $2^{\omega(d)-1}$.
4. Sum these contributions to find $N(x)$.

### [W4, round 1]
Derived formula for N(x): N(x) = (tau(x^2) - 1) / 2, where tau(n) is the number of positive divisors of n.
The number of divisors of x^2, tau(x^2), can be found by factoring x. If x = p1^a1 * p2^a2 * ..., then tau(x^2) = (2a1 + 1) * (2a2 + 1) * ...

Efficient Python function implemented to calculate N(x) using this property. The complexity is dominated by prime factorization of x, which is fast enough for x <= 1717.
The core function is calculate_N_x(x). Ready for comprehensive testing up to x=1717.

### [W3, round 1]
Analysis of the problem shows that $N(x)$, the number of positive integers $y$ such that $\frac{1}{x} + \frac{1}{y}$ is a unit fraction, is given by $N(x) = \frac{\tau(x^2) - 1}{2}$. To maximize $N(x)$, we must maximize $\tau(x^2)$. If $x = p_1^{a_1} \cdots p_k^{a_k}$, then $\tau(x^2) = (2a_1 + 1) \cdots (2a_k + 1)$.

Hypothesis: To maximize this product subject to $x \le 1717$, $x$ must be a highly composite number, relying exclusively on the smallest primes (2, 3, 5, 7, ...). The exponents $a_i$ should be chosen to maximize the product of $(2a_i+1)$, which generally implies favoring small primes and keeping the exponents balanced or slightly skewed towards the smallest prime (2).

Candidate Set Suggestion: Based on preliminary search (maximizing $\tau(x^2)$), the current best candidates are highly composite numbers close to 1717:
1. $x = 1680 = 2^4 \cdot 3^1 \cdot 5^1 \cdot 7^1$. ($\tau(x^2) = 9 \cdot 3^3 = 243$, $N(x)=121$)
2. $x = 1260 = 2^2 \cdot 3^2 \cdot 5^1 \cdot 7^1$. ($\tau(x^2) = 5 \cdot 5 \cdot 3^2 = 225$, $N(x)=112$)
3. $x = 1440 = 2^5 \cdot 3^2 \cdot 5^1$. ($\tau(x^2) = 11 \cdot 5 \cdot 3 = 165$, $N(x)=82$)
4. $x = 1080 = 2^3 \cdot 3^3 \cdot 5^1$. ($\tau(x^2) = 7 \cdot 7 \cdot 3 = 147$, $N(x)=73$)
