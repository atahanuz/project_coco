### [W1, round 1]
**Intermediate Goal: Minimum $n$ such that $2023 \mid n!$**

1.  Factorization of 2023: $2023 = 7 \cdot 17^2$.
2.  We require $n!$ to be divisible by 7 and $17^2$.
3.  For $7 \mid n!$, we need $n \ge 7$.
4.  For $17^2 \mid n!$, we need $v_{17}(n!) \ge 2$. Using Legendre's Formula, $v_{17}(n!) = \sum_{k=1}^{\infty} \lfloor \frac{n}{17^k} \rfloor$.
    *   If $n < 34$, $v_{17}(n!) \le 1$.
    *   If $n=34$, $v_{17}(34!) = \lfloor 34/17 \rfloor + \lfloor 34/289 \rfloor = 2 + 0 = 2$.
5.  The minimum $n$ satisfying both conditions is $n=34$. This justifies $v_{17}(34!) = 2 \ge 2$.

### [W3, round 1]
Based on the required analysis involving $v_{17}(n!)$ and assuming the implied relationship $k = v_{17}(n!)$, we sought the largest integer $n$ such that $v_{17}(n!) \le 11$. Using Legendre's formula, we found that $v_{17}(203!) = 11$ and $v_{17}(204!) = 12$. Therefore, the largest integer $n$ satisfying the condition is $n=203$.

### [W2, round 1]
Derivation for $k = \omega(n!/2023)$:
Let $D = 2023 = 7^1 \cdot 17^2$. We seek $k = \omega(n!/D)$.
The distinct prime factors of $n!/D$ are determined by the primes $p \le n$.

1. Primes $p \notin \{7, 17\}$: These primes divide $n!/D$ if and only if $p \le n$. There are $\pi(n) - \mathbb{I}(7 \le n) - \mathbb{I}(17 \le n)$ such primes.

2. Prime $p=7$: 7 divides $n!/D$ if and only if $v_7(n!) - v_7(D) > 0$. Since $v_7(D)=1$, this requires $v_7(n!) \ge 2$.

3. Prime $p=17$: 17 divides $n!/D$ if and only if $v_{17}(n!) - v_{17}(D) > 0$. Since $v_{17}(D)=2$, this requires $v_{17}(n!) \ge 3$.

The precise formula for $k$ is:
$k = \pi(n) - \mathbb{I}(7 \le n) - \mathbb{I}(17 \le n) + \mathbb{I}(v_7(n!) \ge 2) + \mathbb{I}(v_{17}(n!) \ge 3)$,
where $v_p(n!) = \sum_{i=1}^{\infty} \lfloor \frac{n}{p^i} \rfloor$ and $\mathbb{I}(\cdot)$ is the indicator function.

This formula relates $k$ directly to $\pi(n)$ and the conditions on the exponents of 7 and 17 in $n!$.
Specific conditions:
- $v_7(n!) \ge 2$ holds iff $n \ge 14$.
- $v_{17}(n!) \ge 3$ holds iff $n \ge 51$.

### [W4, round 1]
ANALYSIS OF THE PROBLEM:
1. Let $g = \gcd(a, b) = 2023$ and $L = \text{lcm}(a, b) = n!$.
2. We write $a = g a'$ and $b = g b'$, where $\gcd(a', b') = 1$.
3. The LCM condition implies $L = g a' b'$.
   $n! = 2023 a' b'$.
4. Let $K = n! / 2023$. We seek the number of ordered pairs $(a', b')$ such that $a' b' = K$ and $\gcd(a', b') = 1$.
5. The number of such pairs is $2^k$, where $k$ is the number of distinct prime factors of $K$.
6. The condition is $2^k \le 4000$. Since $2^{11} = 2048$ and $2^{12} = 4096$, we must have $k \le 11$.
7. Factorization: $2023 = 7 \cdot 17^2$.
8. For $K$ to be an integer, $n!$ must be divisible by 2023. This requires $v_7(n!) \ge 1$ (i.e., $n \ge 7$) and $v_{17}(n!) \ge 2$ (i.e., $n \ge 34$). We must check $n \ge 34$.
9. $k$ is the count of primes $p \le n$ such that $v_p(n!) > v_p(2023)$.
   - If $p \notin \{7, 17\}$, $v_p(2023)=0$, so $p$ contributes to $k$ if $p \le n$.
   - If $p=7$, $v_7(2023)=1$. $p=7$ contributes if $v_7(n!) \ge 2$. Since $n \ge 34$, $v_7(n!) \ge 4$. 7 contributes to $k$.
   - If $p=17$, $v_{17}(2023)=2$. $p=17$ contributes if $v_{17}(n!) \ge 3$. This requires $n \ge 51$.
10. Case $34 \le n < 51$: $p=17$ does not contribute. $k = \pi(n) - 1$. We need $\pi(n) - 1 \le 11$, so $\pi(n) \le 12$. $\pi(37) = 12$. $\pi(41) = 13$. Thus $34 \le n \le 40$.
11. Case $n \ge 51$: $p=17$ contributes. $k = \pi(n)$. We need $\pi(n) \le 11$. Since $\pi(51) \ge 16$, there are no solutions in this range.
12. The valid integers $n$ are $\{34, 35, 36, 37, 38, 39, 40\}$.
13. The sum is $34+35+36+37+38+39+40 = 259$.
