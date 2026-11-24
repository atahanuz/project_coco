### [W1, round 1]
Task: Calculate L = ord_{10000}(3) = lcm(ord_{16}(3), ord_{625}(3)).

Step 1: Calculate ord_{16}(3).
Step 2: Calculate ord_{625}(3).
Step 3: Calculate LCM.

### [W2, round 1]
Systematic check of triples $(a, b, c)$ satisfying $1 \le a < b < c$, $c \le a+b$, and $a+b+c < 30$ was performed. No such triples were found where $3^a \equiv 3^b \equiv 3^c \pmod{10000}$. The minimum sum must therefore be greater than or equal to 30 if a solution exists.

### [W1, round 1]
Calculated L, the multiplicative order of 3 modulo 10000.
ord_{16}(3) = 4
ord_{625}(3) = 500
L = lcm(4, 500) = 500.
This means 3^k mod 10000 repeats every 500 terms.

### [W3, round 1]
Necessary Condition Derivation:
We require $3^a \equiv 3^b \equiv 3^c \pmod{10000}$. Let $M = 10000 = 16 \cdot 625$.

1. Modulo 16 ($2^4$): Since $\gcd(3, 16)=1$, $3^a \equiv 3^b \pmod{16}$ implies $3^{b-a} \equiv 1 \pmod{16}$. The order of 3 modulo 16 is $\text{ord}_{16}(3) = 4$. Thus, $b \equiv a \pmod{4}$.

2. Modulo 625 ($5^4$): Since $\gcd(3, 625)=1$, $3^a \equiv 3^b \pmod{625}$ implies $3^{b-a} \equiv 1 \pmod{625}$. We calculated the order of 3 modulo 625 to be $L_{625} = 500$. Thus, $b \equiv a \pmod{500}$.

3. Combined Condition (L): For $3^a \equiv 3^b \pmod{10000}$, we need $b \equiv a \pmod{\text{lcm}(4, 500)}$. Since $\text{lcm}(4, 500) = 500$, the necessary condition is $a \equiv b \pmod{500}$.

Proof of Congruence for a, b, c:
Since $3^a \equiv 3^b \pmod{10000}$, we must have $a \equiv b \pmod{500}$.
Since $3^b \equiv 3^c \pmod{10000}$, we must have $b \equiv c \pmod{500}$.
Therefore, $a \equiv c \pmod{500}$.
The necessary condition $a \equiv b \equiv c \pmod{500}$ is proven.

We set $L = 500$.

### [W4, round 1]
Key mathematical findings for the problem:
1. The congruence condition $3^a \equiv 3^b \equiv 3^c \pmod{10000}$ requires $a, b, c$ to be congruent modulo $L = 500$.
2. Since $a<b<c$, we must have $b = a + n_1 L$ and $c = a + (n_1 + n_2) L$, where $n_1 \ge 1$ and $n_2 \ge 1$.
3. The constraint $c \le a+b$ implies $a + (n_1 + n_2) L \le a + (a + n_1 L)$, which simplifies to $n_2 L \le a$.
4. To minimize $a+b+c$, we must minimize $n_1, n_2$, and $a$. This leads to selecting $n_1=1$, $n_2=1$, and $a=L=500$.
5. The general form minimizing the sum is defined by $L=500$, $a \ge n_2 L$, $b = a + n_1 L$, and $c = a + (n_1 + n_2) L$. The minimal solution is $(500, 1000, 1500)$, giving $a+b+c = 3000$.

### [W4, round 2]
### [W4, round 2] Rigorous Proof of Minimum Sum
We established the necessary conditions for $a < b < c$ and $3^a \equiv 3^b \equiv 3^c \pmod{10000}$:
1. $L = 500$.
2. $b = a + n_1 L$ and $c = a + (n_1 + n_2) L$, where $n_1 \ge 1$ and $n_2 \ge 1$ are integers.
3. The constraint $c \le a+b$ forces $n_2 L \le a$.

The sum $S$ is given by:
$S = a+b+c = a + (a + n_1 L) + (a + (n_1 + n_2) L) = 3a + (2n_1 + n_2)L$.

To minimize $S$, we must minimize $a$ and minimize the coefficient $(2n_1 + n_2)$.

**Minimizing coefficients $n_1$ and $n_2$:**
Since $n_1 \ge 1$ and $n_2 \ge 1$, the minimum value for $n_1$ is 1, and the minimum value for $n_2$ is 1. If we increase either $n_1$ or $n_2$, the term $(2n_1 + n_2)L$ strictly increases.

**Minimizing $a$:**
Given fixed $n_1$ and $n_2$, we must satisfy $a \ge n_2 L$. To minimize $S$, we must choose the smallest possible integer $a$, which is $a_{min} = n_2 L$.

**Combining conditions:**
Substituting $a_{min}$ back into $S$:
$S(n_1, n_2) = 3(n_2 L) + (2n_1 + n_2)L = (3n_2 + 2n_1 + n_2)L = (2n_1 + 4n_2)L$.

We now minimize $S(n_1, n_2) = L(2n_1 + 4n_2)$ subject to $n_1 \ge 1$ and $n_2 \ge 1$.
Since $L > 0$, we minimize $f(n_1, n_2) = 2n_1 + 4n_2$.

1. Minimum $n_1=1, n_2=1$: $f(1, 1) = 2(1) + 4(1) = 6$. $S = 6L = 3000$.
2. Increasing $n_1$ to 2 ($n_2=1$): $f(2, 1) = 2(2) + 4(1) = 8$. $S = 8L = 4000$. (Larger)
3. Increasing $n_2$ to 2 ($n_1=1$): $f(1, 2) = 2(1) + 4(2) = 10$. $S = 10L = 5000$. (Larger)

Since $f(n_1, n_2)$ is a linear function of $n_1$ and $n_2$ with positive coefficients, increasing either variable from their minimum possible values (1) strictly increases the sum $S$.

Therefore, the minimum possible sum $a+b+c$ is achieved when $n_1=1$ and $n_2=1$. This results in the triple $(500, 1000, 1500)$ and the sum 3000.
