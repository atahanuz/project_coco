### [W1, round 1]
# Investigation: Prime Powers $n=p^a$

We seek positive integers $n=p^a$ such that $k^2 \equiv 1 \pmod{n}$ for all $k$ coprime to $n$. This means every element in the multiplicative group $(\mathbb{Z}/n\mathbb{Z})^*$ must have an order that divides 2 (i.e., the group must be elementary abelian of exponent 2).

## Case 1: $n=p$ (Prime)

The group $(\mathbb{Z}/p\mathbb{Z})^*$ has order $p-1$.
1. If $p=2$, $(\mathbb{Z}/2\mathbb{Z})^* = \{1\}$. $1^2 \equiv 1 \pmod{2}$. $n=2$ is a solution.
2. If $p$ is an odd prime, $(\mathbb{Z}/p\mathbb{Z})^*$ is cyclic of order $p-1$. For every element to satisfy $k^2 \equiv 1 \pmod{p}$, the maximum order must be 2. This implies $p-1 \le 2$.
   If $p-1 = 1$, then $p=2$ (covered above).
   If $p-1 = 2$, then $p=3$. $(\mathbb{Z}/3\mathbb{Z})^* = \{1, 2\}$. $1^2 \equiv 1$, $2^2 = 4 \equiv 1 \pmod{3}$. $n=3$ is a solution.
   If $p-1 > 2$ (i.e., $p>3$), the cyclic group contains elements of order greater than 2, so $n=p$ is not a solution.

Initial solutions found: $n=2, 3$.

## Case 2: $n=p^a$, where $a \ge 2$

### Subcase 2a: $p=2$, $n=2^a$ ($a \ge 2$)

We require $k^2 \equiv 1 \pmod{2^a}$ for all odd $k$.
1. $a=2$, $n=4$. Odd $k$ are $1, 3$. $1^2=1$, $3^2=9 \equiv 1 \pmod{4}$. $n=4$ is a solution.
2. $a=3$, $n=8$. Odd $k$ are $1, 3, 5, 7$. We check orders. $(\mathbb{Z}/8\mathbb{Z})^* = \{1, 3, 5, 7\}$. All elements squared are $1 \pmod{8}$. $n=8$ is a solution.
3. $a=4$, $n=16$. $(\mathbb{Z}/16\mathbb{Z})^*$. The element $5$ has order $2^{4-2} = 4$. $5^2 = 25 \equiv 9 \not\equiv 1 \pmod{16}$. $n=16$ is NOT a solution.
4. For $a \ge 4$, the group $(\mathbb{Z}/2^a\mathbb{Z})^*$ contains the element $5$, which has order $2^{a-2} \ge 4$. Thus $5^2 \not\equiv 1 \pmod{2^a}$. No solutions for $a \ge 4$.

Solutions found for $p=2$: $n=4, 8$.

### Subcase 2b: $p$ is an odd prime, $n=p^a$ ($a \ge 2$)

The group $(\mathbb{Z}/p^a\mathbb{Z})^*$ is cyclic of order $\phi(p^a) = p^{a-1}(p-1)$.
For all elements to have order dividing 2, the order of the group must be at most 2.
$\phi(p^a) \le 2$.

Since $p$ is an odd prime, $p \ge 3$. Since $a \ge 2$:
$\phi(p^a) = p^{a-1}(p-1) \ge p^1 (p-1) = p^2 - p$.
If $p=3$ and $a=2$, $\phi(9) = 3(2) = 6$. $6 > 2$.
If $p \ge 3$ and $a \ge 2$, then $\phi(p^a) \ge 6$.
Thus, the group $(\mathbb{Z}/p^a\mathbb{Z})^*$ must contain elements of order greater than 2.
No solutions exist for odd primes $p$ when $a \ge 2$.

## Conclusion for Prime Powers

The prime powers $n=p^a$ satisfying the condition are $n=2, 3, 4, 8$.
This concludes the investigation for prime powers.

### [W1, round 1]
REPORT on task "Investigate the condition $k^2 \equiv 1 \pmod{n}$ for all $k$ coprime to $n$ when $n$ is a prime power ($n=p^a$). Determine all such prime powers $n$.": I investigated the condition $k^2 \equiv 1 \pmod{n}$ for all $k$ coprime to $n$ when $n$ is a prime power $p^a$. For prime $p$, only $p=2$ and $p=3$ satisfy the condition. For $n=2^a$, the condition holds for $a=1, 2, 3$, yielding $n=2, 4, 8$, but fails for $a \ge 4$. For odd primes $p$ and $a \ge 2$, the multiplicative group $(\mathbb{Z}/p^a\mathbb{Z})^*$ is cyclic and has order greater than 2, meaning it contains elements whose order is greater than 2. Thus, the complete set of prime power solutions is $\{2, 3, 4, 8\}$.
Candidate answer: 2, 3, 4, 8

### [W2, round 1]
### [W2, round 1]
# Investigation of $n=2^a 3^b$ for $a \le 4, b \le 1$

The condition requires $k^2 \equiv 1 \pmod{n}$ for all $k$ coprime to $n$. Since $n = 2^a 3^b$, this is equivalent to:
1. $k^2 \equiv 1 \pmod{2^a}$ for all odd $k$.
2. $k^2 \equiv 1 \pmod{3^b}$ for all $k$ coprime to $3^b$.

**Analysis of Modulo $3^b$ ($b \le 1$):**
*   If $b=1$, $n$ is divisible by 3. $(\mathbb{Z}/3\mathbb{Z})^* = \{1, 2\}$. $1^2 \equiv 1 \pmod 3$ and $2^2 = 4 \equiv 1 \pmod 3$. This condition always holds for $b=1$.
*   If $b \ge 2$, $(\mathbb{Z}/3^b\mathbb{Z})^*$ is cyclic of order $2 \cdot 3^{b-1} \ge 6$, so it contains elements of order $> 2$. This fails the condition.
Since we are restricted to $b \le 1$, we must have $b=1$.

**Analysis of Modulo $2^a$ ($a \le 4$):**
*   $a=1$ ($n$ divisible by 2): $k^2 \equiv 1 \pmod 2$. True for all odd $k$.
*   $a=2$ ($n$ divisible by 4): $k^2 \equiv 1 \pmod 4$. True for all odd $k$.
*   $a=3$ ($n$ divisible by 8): $k^2 \equiv 1 \pmod 8$. True for all odd $k$.
*   $a=4$ ($n$ divisible by 16): $k^2 \equiv 1 \pmod{16}$. Fails for $k=3$, since $3^2 = 9 \not\equiv 1 \pmod{16}$.

**Testing composite $n = 2^a 3^b$ (where $b=1$ and $a \ge 1$):**
We test $a=1, 2, 3$.
*   $a=1, b=1 \implies n=6$. Works since $2^1$ and $3^1$ both satisfy the respective conditions.
*   $a=2, b=1 \implies n=12$. Works.
*   $a=3, b=1 \implies n=24$. Works.
*   $a=4, b=1 \implies n=48$. Fails because $2^4=16$ fails the condition.

The investigation shows that for $n=2^a 3^b$ with $a \le 4$ and $b \le 1$, the possible values are $n=6, 12, 24$.

### [W2, round 1]
REPORT on task "Investigate the condition for composite numbers $n$, specifically starting with $n = 2^a 3^b$. Test $n$ for small values of $a$ and $b$ (e.g., $a \le 4, b \le 1$) and look for restrictions on $a$ and ": I investigated composite numbers of the form $n=2^a 3^b$ subject to $a \le 4$ and $b \le 1$. The condition $k^2 \equiv 1 \pmod n$ requires that $b=1$ and that $2^a$ is a solution to $k^2 \equiv 1 \pmod{2^a}$ for odd $k$. These restrictions limit $a$ to be 1, 2, or 3. Testing these cases confirmed that $n=6, 12, 24$ satisfy the condition, while $n=48$ fails.
Candidate answer: $n \in \{6, 12, 24\}$ (within the tested constraints $a \le 4, b \le 1$)
