### [W2, round 1]
Analysis of P(k) \equiv 0 \pmod n:
1.  **Constraint on the constant term $a_0$**: Since $P(k) \equiv 0 \pmod n$ for all positive integers $k$, this must hold for $k=n$.
    $$P(n) = a_n n^n + a_{n-1} n^{n-1} + \dots + a_1 n + a_0$$
    Since $n>1$, all terms except $a_0$ are divisible by $n$. Thus, $P(n) \equiv a_0 \pmod n$.
    Since $P(n) \equiv 0 \pmod n$, we must have $a_0 \equiv 0 \pmod n$.
    As $a_0$ is a coefficient, $a_0 \in \{1, -1, 0\}$. Since $n>1$, the only possibility is $a_0 = 0$.
    This means the polynomial must be divisible by $x$.

2.  **Constraints on other values**: We require $P(k) \equiv 0 \pmod n$ for $k=1, 2, \dots, n-1$.
    Specifically, $P(1) = \sum_{i=1}^n a_i$. Thus, the sum of all non-zero coefficients must be a multiple of $n$.

3.  **Structural Restriction**: The condition $P(k) \equiv 0 \pmod n$ for all $k$ strongly restricts $P$. We have established $a_0=0$. For $n=2$, we found that $a_0$ must be even, which contradicted $a_0 \in \{1, -1\}$, suggesting no solution exists for $n=2$. Further investigation into specific $n$ (e.g., prime vs composite) is needed to find the minimum number of non-zero coefficients.

### [W3, round 1]
Case m=2: P(x) = c_a x^a + c_b x^b, where c_a, c_b in {-1, 1}. The modulus must be the degree, $n = \max(a, b)$. Assume $a > b$. We require P(k) = c_a k^a + c_b k^b to be divisible by $n=a$ for all $k \ge 1$.

Consider the case where coefficients are opposite: c_a = -c_b. P(x) = c_a (x^a - x^b).
We require k^a - k^b \equiv 0 \pmod a for all k.

If we choose b=1, P(x) = c_a (x^a - x). We require k^a \equiv k \pmod a for all k.
If we choose a prime number p, Fermat's Little Theorem states k^p \equiv k \pmod p.
Thus, any prime degree $n=p$ works, provided the lower exponent $b=1$.

The smallest degree $n>1$ is $n=2$. If $n=2$, we choose $a=2, b=1$.
P(x) = x^2 - x (or -x^2 + x).
P(k) = k^2 - k = k(k-1). Since $k$ and $k-1$ are consecutive integers, $k(k-1)$ is always even, hence a multiple of 2.
Therefore, such an integer $n$ exists, and the smallest such $n$ is 2.

### [W1, round 1]
Investigation of the problem for n=2 and n=3.

Case n=2:
P(x) is of degree 2, so P(x) = a_2 x^2 + a_1 x + a_0, with a_2 != 0. All non-zero coefficients must be +/- 1.
1. P(2) must be divisible by 2. P(2) = a_2 2^2 + a_1 2 + a_0. Modulo 2, P(2) = a_0. Thus, a_0 must be 0.
2. P(1) must be divisible by 2. P(1) = a_2 + a_1 + a_0 = a_2 + a_1. Since a_i are +/- 1 (if non-zero), and a_0=0, m = number of non-zero coefficients = 1 + (1 if a_1 != 0). P(1) = a_2 + a_1. Since a_2, a_1 are +/- 1, a_2+a_1 is even only if a_1 = -a_2, or if a_1=0.
3. If a_1=0, m=1. P(1) = a_2 = +/- 1, not divisible by 2. So m >= 2.
4. If m=2, we must have a_1 != 0. P(1) = a_2 + a_1. This is even if a_1 = -a_2.
We test P(x) = x^2 + x (i.e., a_2=1, a_1=1, a_0=0, but wait, we need a_1 = -a_2 if we use the constraint P(1) = 0 mod 2, which is only true if a_1=-a_2. Let's recheck P(1) mod 2 requirement).
P(1) = a_2 + a_1. If a_2=1, a_1=1, P(1)=2, which is 0 mod 2.
P(k) = a_2 k^2 + a_1 k. Modulo 2, P(k) = k^2 + k = k(k+1) = 0 mod 2 for all k.
Thus, for n=2, the minimum number of non-zero coefficients is m=2. (e.g., P(x) = x^2 + x).

Case n=3:
P(x) is of degree 3, so P(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0, with a_3 != 0.
1. P(3) must be divisible by 3. P(3) = a_3 3^3 + a_2 3^2 + a_1 3 + a_0. Modulo 3, P(3) = a_0. Thus, a_0 must be 0.
2. We try minimum m. m >= 1 (since a_3 != 0).
3. Try m=1: P(x) = a_3 x^3. P(1) = a_3. a_3 != 0 mod 3. Fails. So m >= 2.
4. Try m=2. We need two non-zero coefficients among {a_3, a_2, a_1}.
Test P(x) = x^3 - x (a_3=1, a_1=-1, a_2=0, a_0=0). m=2.
P(k) = k^3 - k = k(k^2 - 1) = (k-1)k(k+1). This is the product of three consecutive integers, which is always divisible by 3.
Thus, for n=3, the minimum number of non-zero coefficients is m=2.

### [W4, round 1]
Initial investigation of the problem: $P(x)$ is a polynomial of degree $n>1$ with coefficients $\in \{0, 1, -1\}$, such that $P(k) \equiv 0 \pmod n$ for all positive integers $k$.

If we consider $P(x)$ over $\mathbb{Z}_n$, the condition implies that $P(x)$ must be identically zero when evaluated at all $x \in \mathbb{Z}_n$.

Case Study: $n=2$. We require $P(k) \equiv 0 \pmod 2$ for all $k$. We found $P(x) = x^2 + x$ satisfies this. $P(x)$ has degree 2, and 2 non-zero coefficients (1 and 1).

Case Study: $n=3$. We require $P(k) \equiv 0 \pmod 3$ for all $k$. We found $P(x) = x^3 - x$ satisfies this. $P(x)$ has degree 3, and 2 non-zero coefficients (1 and -1).

Case Study: $n=4$. We require $P(k) \equiv 0 \pmod 4$ for all $k$. We need $\deg(P)=4$. We found $P(x) = x^4 - x^2$ satisfies this. $P(x)$ has degree 4, and 2 non-zero coefficients (1 and -1).

Conjecture: The minimum possible number of non-zero coefficients is 2, provided such a polynomial of degree $n$ exists. These polynomials appear to be of the form $P(x) = x^n - x^j$ (or $x^j - x^n$) for some $j$. This requires $k^n \equiv k^j \pmod n$ for all $k$.

### [W2, round 1]
Further investigation suggests the minimum possible number of non-zero coefficients is 2.
We tested $n=3$ and found a solution with 2 non-zero coefficients:
Let $P(x) = x^3 - x$. The coefficients are $a_3=1, a_2=0, a_1=-1, a_0=0$.
The number of non-zero coefficients is 2.
We verified this works for $n=3$:
$P(1) = 1 - 1 = 0 \equiv 0 \pmod 3$.
$P(2) = 8 - 2 = 6 \equiv 0 \pmod 3$.
$P(3) = 27 - 3 = 24 \equiv 0 \pmod 3$.
Since $a_0$ must be 0, and $a_n \ne 0$, at least two coefficients are needed to satisfy $P(1) \equiv 0 \pmod n$ unless $n=1$ (which is excluded). Thus, 2 is the minimum possible number.
