### [W4, round 1]
Initial case analysis for $n=0, 1, 2, 3, 4$ yields solutions $n \in \{0, 1, 2, 4\}$.
For $n=0, E(0) = -9$.
For $n=1, E(1) = 21$.
For $n=2, E(2) = 25$.
For $n=3, E(3) = 363/5$ (Not integer).
For $n=4, E(4) = 309$.
The problem reduces to $2n-1 \mid 3((n+2)! + 1)$. If $2n-1$ divides $(n+2)!$, then we require $2n-1 \mid 3$. This only happens for $n=1, 2$. For $n \ge 5$, if $2n-1$ is prime, we require $(n+2)! \equiv -1 \pmod{2n-1}$, which suggests further investigation into modular arithmetic.

### [W2, round 1]
The condition is $2n-1 \mid 3((n+2)! + 1)$.

**Analysis Modulo 3:**
1. If $3 \nmid (2n-1)$ (i.e., $n \not\equiv 2 \pmod 3$), the condition simplifies to $2n-1 \mid (n+2)! + 1$.
2. If $3 \mid (2n-1)$ (i.e., $n \equiv 2 \pmod 3$), let $2n-1 = 3k$. The condition simplifies to $k \mid (n+2)! + 1$, where $k = (2n-1)/3$.

**Analysis Modulo Prime Factors $p$ of $2n-1$:**
Let $p$ be a prime divisor of $2n-1$.
If $p \ne 3$, then $p \mid 3((n+2)! + 1)$ implies $(n+2)! \equiv -1 \pmod p$.

If $p > n+2$, this strong condition suggests $p$ must be related to $(p-1)! \equiv -1 \pmod p$ by Wilson's theorem. If $2n-1$ is prime $P$ and $P > n+2$, we require $(n+2)! \equiv -1 \pmod P$. This holds if $n+2 = P-1$, which implies $n+2 = 2n-2$, or $n=4$.
If $n=4$, $2n-1=7$. $6! \equiv -1 \pmod 7$. (Verified solution).

If $p \le n+2$, then $(n+2)! \equiv 0 \pmod p$. The condition $(n+2)! \equiv -1 \pmod p$ becomes $0 \equiv -1 \pmod p$, which implies $p \mid 1$, a contradiction.
Therefore, any prime factor $p$ of $2n-1$ that is not 3 must satisfy $p > n+2$. This means $2n-1$ must be greater than $n+2$, so $n>3$.
If $n \le 3$, the only prime factor $p$ of $2n-1$ must satisfy $p \le n+2$.
For $n=0$, $2n-1=-1$. Trivial.
For $n=1$, $2n-1=1$. Trivial.
For $n=2$, $2n-1=3$. Prime factor $p=3$. Covered by Case 2.
For $n=3$, $2n-1=5$. $p=5$. $n+2=5$. $p=n+2$. Condition requires $5! \equiv -1 \pmod 5$, i.e., $0 \equiv -1 \pmod 5$, false. (Verified $n=3$ fails).

The constraints are:
1. $n=0, 1, 2$ are solutions.
2. For $n > 3$, if $2n-1$ has any prime factor $p \ne 3$, then $p$ must be greater than $n+2$.
3. If $3 \mid (2n-1)$, then $(2n-1)/3 \mid (n+2)! + 1$.

### [W3, round 1]
Investigation Summary: Condition is $2n-1 \mid 3((n+2)! + 1)$.

1. Small Solutions Found: $n \in \{0, 1, 2, 4, 12\}$.

2. Structural Analysis by Divisibility: Let $D = 2n-1$.

   a) Case $D$ is divisible by 3 (i.e., $n \equiv 2 \pmod 3$):
      The condition simplifies to $D/3 \mid (n+2)! + 1$.
      Testing $n=11$ ($D=21$, $D/3=7$): We require $7 \mid 13! + 1$. Since $13 \ge 7$, $13! \equiv 0 \pmod 7$. Thus $13!+1 \equiv 1 \pmod 7$. $n=11$ is not a solution. This strongly suggests that for $n \ge 11$ where $2n-1$ is divisible by 3, the condition fails because $n+2$ will likely be large enough compared to the prime factors of $2n-1$.

   b) Case $\gcd(D, 3) = 1$:
      The condition simplifies to $D \mid (n+2)! + 1$.
      If $D$ is a prime $p > 3$, we require $p \mid (n+2)! + 1$.
      For this to hold, we *must* have $n+2 < p$.
      Since $p = 2n-1$, this imposes the necessary condition $n+2 < 2n-1$, which simplifies to $n > 3$.
      If $n \le 3$ and $2n-1$ is prime ($n=2$ gives $3$, $n=3$ gives $5$):
      - $n=3$: $D=5$. $n+2=5$. Since $n+2 \ge D$, $5 \mid 5!$. $5!+1 \equiv 1 \pmod 5$. $n=3$ is not a solution (Confirmed earlier).

3. Conclusion for Large $n$: If $2n-1 = p$ (prime) and $p>3$, then $n>3$ is necessary. If $n+2 \ge p$, the condition fails immediately. The focus should now be on finding cases where $n+2 < 2n-1$ holds, or investigating the specific cases where $2n-1$ is composite but not divisible by 3.

### [W1, round 1]
Calculations for the expression $E(n) = \frac{3((n+2)! + 1)}{2n - 1}$ for $n=0$ to $n=15$ using modular arithmetic:
The expression is an integer for $n \in \{0, 1, 2, 4, 12\}$.

Checked values:
n=0: Integer (-9)
n=1: Integer (21)
n=2: Integer (25)
n=3: Not Integer
n=4: Integer
n=5: Not Integer
n=12: Integer

Patterns observed: Solutions are sparse. Small values $n=0, 1, 2, 4$ worked. $n=12$ was the next solution found.

### [W2, round 2]
[W2, round 2] Generalized Prime Case Analysis (p = 2n-1, p != 3)
A necessary condition for $n>3$ is that the prime divisor $p$ of $2n-1$ must satisfy $p > n+2$.
If $2n-1 = p$ (prime), the condition simplifies to $p \mid (n+2)! + 1$.
In terms of $p$: $n = (p+1)/2$ and $n+2 = (p+5)/2$.
The required congruence is:
$$\left(\frac{p+5}{2}\right)! \equiv -1 \pmod p$$
This has been verified for $p=23$ (n=12). This serves as the primary test case for large prime divisors.

### [W3, round 2]
Investigation completed for composite $2n-1$ (not divisible by 3) in $5 \le n \le 25$. The candidates were $n=13, 18, 25$. In all cases, $2n-1$ divided $(n+2)!$, leading to the requirement $2n-1 | 1$, which is impossible. No new solutions were found in this range.
