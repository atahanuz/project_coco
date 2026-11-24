### [W2, round 1]
Task: Determine ranges for n where prime factors 7 and 17 contribute to $\omega(n!/2023)$.
The number of pairs is $2^{\omega(n!/2023)}$.
1. Condition for 7 contribution: $v_7(n!) \ge 2$. Using Legendre's formula, $v_7(n!) = \sum \lfloor n/7^k \rfloor$.
   $v_7(7!) = 1$. $v_7(14!) = \lfloor 14/7 \rfloor = 2$.
   Thus, 7 contributes if and only if $n \ge 14$.
2. Condition for 17 contribution: $v_{17}(n!) \ge 3$. Using Legendre's formula, $v_{17}(n!) = \sum \lfloor n/17^k \rfloor$.
   $v_{17}(50!) = \lfloor 50/17 \rfloor = 2$. $v_{17}(51!) = \lfloor 51/17 \rfloor = 3$.
   Thus, 17 contributes if and only if $n \ge 51$.

### [W4, round 1]
**Analysis of the condition:**
The number of ordered pairs $(a, b)$ is $2^{\omega(n!/2023)}$. We require $2^{\omega(n!/2023)} \le 4000$. Since $2^{11} = 2048$ and $2^{12} = 4096$, the necessary condition is $\omega(n!/2023) \le 11$.

**Estimating the Upper Bound using $\pi(n)$:**
The distinct prime factors of $n!$ is $\pi(n)$. Since $2023 = 7^1 \cdot 17^2$, $\omega(n!/2023)$ is at most $\pi(n)$.
We require $\pi(n)$ to be close to 11.
$\pi(31) = 11$. $\pi(37) = 12$.
This suggests an initial upper bound $n < 37$.

**Detailed Analysis of $\omega(n!/2023)$:**
Let $K = n!/2023$. The distinct prime factors of $K$ are all primes $p \le n$, unless $p=7$ or $p=17$ and $v_p(n!) \le v_p(2023)$.
1. Primes $p \le n, p \neq 7, 17$: These are always factors of $K$.
2. Prime $p=7$: $v_7(2023)=1$. $7$ is a factor of $K$ if $v_7(n!) > 1$. This holds if $n \ge 7$.
3. Prime $p=17$: $v_{17}(2023)=2$. $17$ is a factor of $K$ if $v_{17}(n!) > 2$. This requires $n$ such that $\lfloor n/17 \rfloor + \lfloor n/289 \rfloor + \dots > 2$. This is true if $n \ge 34$ (since $v_{17}(34!) = 2$).

**Testing key values:**
*   **n=31:** $\pi(31)=11$. Primes are $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31\}$.
    *   $v_7(31!) = 4$. ($4 > 1$). 7 is a factor.
    *   $v_{17}(31!) = 1$. ($1 \ngtr 2$). 17 is NOT a factor.
    *   $\omega(31!/2023) = 10$ (primes $\le 31$, excluding 17) + 1 (prime 7) = 11. **(Condition met)**
*   **n=33:** $\pi(33)=11$. Primes are $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31\}$.
    *   $v_7(33!) = 4$. (Factor).
    *   $v_{17}(33!) = 1$. (Not a factor).
    *   $\omega(33!/2023) = 11$. **(Condition met)**
*   **n=34:** $\pi(34)=11$.
    *   $v_7(34!) = 4$. (Factor).
    *   $v_{17}(34!) = 2$. ($2 \ge 2$). 17 IS a factor.
    *   $\omega(34!/2023) = 11$ (all 11 primes) - 0 (since 7 and 17 are both present) = 11. **(Condition met)**
*   **n=37:** $\pi(37)=12$. Primes include 37.
    *   $v_7(37!) = 5$. (Factor).
    *   $v_{17}(37!) = 2$. (Factor).
    *   $\omega(37!/2023) = 12$. **(Condition fails)**

The analysis shows that $n$ must be $\le 34$. I will summarize these findings.

### [W1, round 1]
Derivation Summary:
1. Formula for C(n): The number of ordered pairs C(n) such that gcd(a,b)=2023 and lcm(a,b)=n! is C(n) = 2^{\omega(n!/2023)}.

2. Expression for $\omega(n!/2023)$: This is the count of primes $p \le n$ such that $\nu_p(n!) > \nu_p(2023)$. Since $2023 = 7^1 \cdot 17^2$:
$\omega(n!/2023) = \left(\pi(n) - \mathbb{I}(n \ge 7) - \mathbb{I}(n \ge 17)\right) + \mathbb{I}\left(\sum_{k=1}^{\infty} \lfloor \frac{n}{7^k} \rfloor > 1\right) + \mathbb{I}\left(\sum_{k=1}^{\infty} \lfloor \frac{n}{17^k} \rfloor > 2\right)$.
This expression uses Legendre's formula and the factorization 2023 = 7 * 17^2.
