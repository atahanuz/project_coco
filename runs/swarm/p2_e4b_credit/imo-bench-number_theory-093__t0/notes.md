### [W1, round 1]
Determining k = ord_10000(3):
1. ord_16(3) = 4.
2. ord_625(3) = 500.
3. k = lcm(4, 500) = 500.

### [W4, round 1]
Investigation of constraints $a<b<c$ and $3^a \equiv 3^b \equiv 3^c \pmod{10000}$.
1. The modulus is $M=10000$. Since $\gcd(3, 10000)=1$, the exponents must be congruent modulo $\lambda = \text{ord}_{10000}(3)$.
2. Calculation shows $\lambda = \text{lcm}(\text{ord}_{16}(3), \text{ord}_{625}(3)) = \text{lcm}(4, 500) = 500$.
3. Thus, $b-a = k\lambda$ and $c-a = n\lambda$, where $0 < k < n$ are positive integers.
4. Applying the inequality $c \le a+b$:
   $a + n\lambda \le a + (a + k\lambda)$
   $n\lambda \le a + k\lambda$
   $a \ge (n-k)\lambda$
5. Checking the edge case $a=0$: If $a=0$, then $0 \ge (n-k)500$. Since $n>k$, $n-k \ge 1$, so $500(n-k) \ge 500$. This leads to a contradiction ($0 \ge 500$). Therefore, $a=0$ is impossible.
6. General Case ($a>0$): The constraint derived is $a \ge 500(n-k)$. The minimum required value for $n-k$ is 1. Setting $n-k=1$ and $k=1$ (the smallest possible positive integer), we require $n=2$. The minimum possible $a$ is $500$.
7. Minimum candidate solution: $a=500, b=1000, c=1500$. This satisfies $c=a+b$ and the modular condition.

### [W2, round 1]
Calculated the order of 3 modulo 10000, denoted k, to be k=500.
The condition $3^a \equiv 3^b \equiv 3^c \pmod{10000}$ implies that $b-a$ and $c-a$ must be multiples of $k$.
To minimize $a+b+c$, we choose the smallest positive differences: $b-a = k$ and $c-a = 2k$.
These constraints lead to $a < b < c$ where $b = a+k$ and $c = a+2k$.
The problem constraint $c \le a+b$ requires $a+2k \le a + (a+k)$, which simplifies to $a \ge k$.
The minimum sum occurs when $a$ is minimized, so we set $a = k$.
The minimum triplet is $(k, 2k, 3k)$, and the minimum sum is $6k$.

### [W3, round 1]
Step 1: Analyze the modular condition.
The requirement $3^a \equiv 3^b \equiv 3^c \pmod{10000}$ implies that the differences $(b-a)$ and $(c-b)$ must be multiples of the order of 3 modulo 10000, denoted $L = \text{ord}_{10000}(3)$.
Computational check found $L = 500$.

Step 2: Relate differences to $L$.
Let $k_1 = b-a$ and $k_2 = c-b$. We must have $k_1 = j_1 L$ and $k_2 = j_2 L$, where $j_1, j_2 \ge 1$.
Thus, $b = a + j_1 L$ and $c = a + (j_1 + j_2) L$.

Step 3: Apply the inequality constraint.
We require $c \le a+b$.
Substituting the forms: $a + (j_1 + j_2) L \le a + (a + j_1 L)$
$a + j_1 L + j_2 L \le 2a + j_1 L$
$j_2 L \le a$.

Step 4: Minimize the sum.
We want to minimize $S = a+b+c = 3a + 2j_1 L + j_2 L$.
To minimize $S$, we must minimize $a$, $j_1$, and $j_2$.

The minimum possible values for $j_1$ and $j_2$ are $j_1=1$ and $j_2=1$.
The constraint $j_2 L \le a$ requires $1 \cdot 500 \le a$, so the minimum possible value for $a$ is $a_{\min} = 500$.

Using these minimum values:
$a = 500$
$j_1 = 1 \implies k_1 = 500 \implies b = 500 + 500 = 1000$
$j_2 = 1 \implies k_2 = 500 \implies c = 1000 + 500 = 1500$

The minimum sum is $a+b+c = 500 + 1000 + 1500 = 3000$.
This solution satisfies all conditions: $500 < 1000 < 1500$, $1500 \le 500+1000$, and $3^{500}, 3^{1000}, 3^{1500}$ are all congruent to $1 \pmod{10000}$.
