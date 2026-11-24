### [W1, round 1]
The multiplicative order of 3 modulo 10000, $k = \text{ord}_{10000}(3)$, was calculated. Using properties of modular arithmetic, it was determined that $k = \text{lcm}(\text{ord}_{16}(3), \text{ord}_{625}(3))$. We found $\text{ord}_{16}(3) = 4$ and $\text{ord}_{625}(3) = 500$. Therefore, $k = \text{lcm}(4, 500) = 500$. This was verified by computation: $3^{500} \equiv 1 \pmod{10000}$ and $3^{250} \not\equiv 1 \pmod{10000}$.

### [W2, round 1]
Case c = a+b:
The conditions $3^a \equiv 3^b \equiv 3^{a+b} \pmod{10000}$ simplify to two requirements due to $\gcd(3, 10000) = 1$:
1. $3^a \equiv 1 \pmod{10000}$
2. $3^{b-a} \equiv 1 \pmod{10000}$

Let k = ord_{10000}(3). Both conditions require that $k$ divides $a$ and $k$ divides $b-a$.
Therefore, the necessary constraints are that both $a$ and $b$ must be multiples of k:
$a = m \cdot k$
$b = n \cdot k
where m, n are positive integers, and $m < n$ (since $a < b$). Also, since $a>0$ (otherwise $c=b$ violating $b<c$), we must have $m \ge 1$.

### [W3, round 1]
### [W3, round 1]
Task: Derive the condition relating $a$ to the smallest possible positive integers $m, n$ given $k=500$.

We start with the setup:
$b = a + mk$
$c = a + (m+n)k$
where $m \ge 1$ and $n \ge 1$ since $a<b<c$ and $k>0$.

We apply the constraint $c \le a+b$:
$a + (m+n)k \le a + (a + mk)$
$a + mk + nk \le 2a + mk$
$nk \le a$

The condition relating $a$ to $m$ and $n$ is $a \ge nk$.
To find the condition related to the *smallest possible positive integers* $m, n$, we choose $m=1$ and $n=1$.
This yields the condition $a \ge k$. Since $k=500$ (from W1's finding), the smallest possible value for $a$ under the constraint $c \le a+b$ with minimum $m, n$ is $a=500$.

### [W4, round 1]
The order of 3 modulo 10000 is L=500.
The constraint $3^a \equiv 3^b \equiv 3^c \pmod{10000}$ requires $b-a = 500 n_1$ and $c-b = 500 n_2$ for $n_1, n_2 \ge 1$.
The constraint $c \le a+b$ implies $a \ge 500 n_2$.
The minimum sum $S = 3a + 1000 n_1 + 500 n_2$ is achieved when $n_1=1, n_2=1$, leading to $a_{min}=500$, $b=1000$, $c=1500$, and $S_{min}=3000$.
