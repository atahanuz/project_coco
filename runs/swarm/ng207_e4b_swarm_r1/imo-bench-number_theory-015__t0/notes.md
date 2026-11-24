### [W2, round 1]
Analysis Modulo p (assuming p does not divide a and p does not divide b):
The equations are:
1) $a^{p-1} + b = p^x$
2) $b^{p-1} + a = p^y$

Since $p > 2$ and $p \nmid a$, by Fermat's Little Theorem, $a^{p-1} \equiv 1 \pmod{p}$.
From (1), $p^x \equiv 0 \pmod{p}$ (since $a^{p-1}+b \ge 1+1=2$, we must have $x \ge 1$).
Thus, $1 + b \equiv 0 \pmod{p}$, which implies $b \equiv -1 \equiv p-1 \pmod{p}$.

Similarly, since $p \nmid b$, $b^{p-1} \equiv 1 \pmod{p}$.
From (2), $p^y \equiv 0 \pmod{p}$ (since $b^{p-1}+a \ge 2$, we must have $y \ge 1$).
Thus, $1 + a \equiv 0 \pmod{p}$, which implies $a \equiv -1 \equiv p-1 \pmod{p}$.

Conclusion for this case: If $p \nmid a$ and $p \nmid b$, then both $a$ and $b$ must satisfy $a \equiv p-1 \pmod{p}$ and $b \equiv p-1 \pmod{p}$.

### [W2, round 1]
REPORT on task "Analyze the system modulo p. Since p > 2, use Fermat's Little Theorem. Consider the case where p does not divide a and p does not divide b. Deduce constraints on a and b based on the equations a^(p-1)": I analyzed the system of equations modulo $p$ under the assumption that $p$ does not divide $a$ and $p$ does not divide $b$. Using Fermat's Little Theorem, I found that both $a^{p-1} \equiv 1 \pmod{p}$ and $b^{p-1} \equiv 1 \pmod{p}$. By analyzing the original equations modulo $p$, I deduced that both $a$ and $b$ must satisfy $a \equiv -1 \pmod{p}$ and $b \equiv -1 \pmod{p}$. These constraints must hold for any solution where $p \nmid a$ and $p \nmid b$.
Candidate answer: ""

### [W1, round 1]
Computational Search Results:

1. Search for p=3 (1 <= a <= b <= 10):
   One solution found: (p, a, b) = (3, 2, 5).
   Exponents: a^(p-1) + b = 3^2 (x=2), b^(p-1) + a = 3^3 (y=3).

2. Search for p=5 (1 <= a <= b <= 5):
   No solutions found.

### [W1, round 1]
REPORT on task "Perform a computational search for small solutions. Start by checking prime p=3 for a <= b <= 10. Then check p=5 for a <= b <= 5. Record all triples (p, a, b) and the corresponding exponents x and y t": I performed a computational search for small solutions. For p=3 with a<=b<=10, I found one solution: (3, 2, 5), which yields the exponents (x, y) = (2, 3). For p=5 with a<=b<=5, no solutions were found in the specified range. The findings have been recorded in the team notes.
Candidate answer: (3, 2, 5)

### [W3, round 1]
### [W3, round 2]
Analysis of Exponents $x$ and $y$ assuming $a < b$.

We are given:
1) $p^x = a^{p-1} + b$
2) $p^y = b^{p-1} + a$

**1. Proof that $y > x$ (and thus $y \ge x$)**
We compare $p^y$ and $p^x$ by examining their difference:
$$p^y - p^x = (b^{p-1} + a) - (a^{p-1} + b) = (b^{p-1} - a^{p-1}) - (b - a)$$

Since $b > a > 0$, we can factor the difference of $(p-1)$-th powers:
$$b^{p-1} - a^{p-1} = (b-a) \sum_{k=0}^{p-2} b^{p-2-k} a^k$$

The sum contains $p-1$ positive terms. Since $p > 2$, $p-1 \ge 2$. Since $b>a\ge 1$, the sum is strictly greater than $p-1$. Thus,
$$b^{p-1} - a^{p-1} > (b-a) \cdot 1 = b-a$$

Substituting back:
$$p^y - p^x > (b-a) - (b-a) = 0$$
Since $p^y > p^x$, we conclude that $y > x$.

**2. Relating Magnitude using $b^p - a^p$**
We relate the structure of the exponents to the difference of the $p$-th powers, $b^p - a^p$.

From the defining equations, we have lower bounds on $p^x$ and $p^y$:
$$p^x > a^{p-1}$$
$$p^y > b^{p-1}$$

Since $a \ge 1$ and $b \ge 1$, we can establish upper bounds for $b^p - a^p$:
$$b^p = b \cdot b^{p-1} < b \cdot p^y$$
$$a^p = a \cdot a^{p-1} < a \cdot p^x$$

Therefore,
$$b^p - a^p < b \cdot p^y$$

This demonstrates that the difference $b^p - a^p$ grows substantially faster than $p^y$ (as $b^p$ vs $b^{p-1}$) and places strict constraints on the required relationship between $a, b,$ and $p$. For $b^p - a^p$ to be bounded by $b \cdot p^y$, $a$ and $b$ must be constrained relative to $p$.

### [W4, round 1]
Investigating $a=b$ case: $a^{p-1} + a = p^k$.
1. If $a=1$, $1^{p-1} + 1 = 2 = p^k$. Since $p>2$, this is impossible. So $a \ge 2$.
2. If $p | a$, then $a = mp$. $a^{p-1} + a = p^{p-1}m^{p-1} + mp$. This is divisible by $p$. If $k=1$, $p^{p-2}m^{p-1} + m = 1$. This has no positive integer solutions for $m$ when $p \ge 5$, and we verified it fails for $p=3$. Thus, $p \nmid a$.
3. By Fermat's Little Theorem, since $p \nmid a$, $a^{p-1} \equiv 1 \pmod p$. The equation $a^{p-1} + a = p^k$ implies $1 + a \equiv 0 \pmod p$, so $a \equiv -1 \pmod p$. We set $a = mp - 1$ for some integer $m \ge 1$.

Initial numerical checks for $a=mp-1$:
- $p=3$: $a=2$ ($m=1$). $2^2 + 2 = 6$. $3^k=6$. No solution.
- $p=5$: $a=4$ ($m=1$). $4^4 + 4 = 260$. $5^k=260$. No solution.
- $p=7$: $a=6$ ($m=1$). $6^6 + 6 = 46662$. $7^k=46662$. No solution ($7^5 < 46662 < 7^6$).
- $p=5$: $a=24$ ($m=5$). $24^4 + 24 = 331800$. $5^k=331800$. No solution.
The equation is highly constrained and appears to have no solutions for small primes and corresponding values of $a$.

### [W4, round 1]
REPORT on task "Investigate the special case where a = b. The problem reduces to finding primes p > 2 and positive integers a such that a^(p-1) + a is a power of p. Analyze this Diophantine equation fully.": I investigated the special case $a=b$, reducing the problem to solving $a^{p-1} + a = p^k$. I established that $a$ must satisfy $a \equiv -1 \pmod p$. By testing small primes ($p=3, 5, 7$) and corresponding values of $a$ (including $a=p-1$ and $a=p^2-1$), I found no solutions. The analysis shows that the equation imposes very strong constraints on $a$ relative to $p$, and based on the initial investigation, no solutions appear to exist.
Candidate answer: None found.

### [W3, round 1]
REPORT on task "Analyze the structure of the exponents x and y. Assume a < b. Show that y must be greater than or equal to x. Use bounds to relate the magnitude of p^x and p^y to a and b, specifically focusing on how": "I analyzed the system of equations assuming $a < b$. By comparing $p^y$ and $p^x$ using the difference $p^y - p^x = (b^{p-1
Candidate answer: ""
