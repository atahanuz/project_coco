### [W1, round 1]
Calculated $\lambda = \operatorname{ord}_{10000}(3)$. Using Python, the smallest positive integer $\lambda$ such that $3^\lambda \equiv 1 \pmod{10000}$ is $\lambda = 500$.

### [W1, round 1]
REPORT on task "Calculate $\lambda = \operatorname{ord}_{10000}(3)$. Use Python to find the smallest positive integer $\lambda$ such that $3^\lambda \equiv 1 \pmod{10000}$.": I used a Python script to calculate the multiplicative order of 3 modulo 10000. The script iteratively computed powers of 3 modulo 10000 until the result was 1. The smallest positive integer $\lambda$ satisfying $3^\lambda \equiv 1 \pmod{10000}$ was found to be 500. This value has been recorded in the shared notes.
Candidate answer: 500

### [W2, round 1]
**Task 1: Proof that $b-a$ is a multiple of $\lambda$.**
Let $\lambda = \text{ord}_{10000}(3)$, which is the smallest positive integer such that $3^\lambda \equiv 1 \pmod{10000}$.
Since $3^a \equiv 3^b \pmod{10000}$ and $\gcd(3, 10000) = 1$, we can multiply by the inverse of $3^a$ modulo $10000$.
$3^a \cdot (3^a)^{-1} \equiv 3^b \cdot (3^a)^{-1} \pmod{10000}$
$1 \equiv 3^{b-a} \pmod{10000}$.
Since $\lambda$ is the order of $3$ modulo $10000$, $3^{b-a} \equiv 1 \pmod{10000}$ implies that $b-a$ must be a multiple of $\lambda$.

**Task 2: Confirmation that $a \ne 0$.**
The problem specifies non-negative integers $a<b<c$. If $a=0$, then $3^a = 1$.
The given condition $3^a \equiv 3^b \pmod{10000}$ becomes $1 \equiv 3^b \pmod{10000}$.
The constraints on $a, b, c$ include $a < b < c$ and $c \le a+b$.
If $a=0$, these constraints are $0 < b < c$ and $c \le 0+b$, which means $c \le b$.
The requirement $b < c$ and $c \le b$ is a contradiction. Therefore, $a$ cannot be zero.

### [W2, round 1]
REPORT on task "Prove rigorously that if $3^a \equiv 3^b \pmod{10000}$ (with $\gcd(3, 10000)=1$), then $b-a$ must be a multiple of $\lambda$. Also, confirm why $a$ cannot be zero.": I rigorously proved that if $3^a \equiv 3^b \pmod{10000}$, then $b-a$ must be a multiple of $\lambda = \text{ord}_{10000}(3)$ by utilizing the inverse element in modular arithmetic. I also confirmed that $a$ cannot be zero because assuming $a=0$ leads to a contradiction between the constraints $b < c$ and $c \le a+b$.
Candidate answer: N/A

### [W3, round 1]
**Investigation Summary for Minimization:**
The sum $S = a+b+c = 3a + (k_1 + k_2)\lambda$. The constraint $c \le a+b$ forces $a \ge (k_2 - k_1)\lambda$.
To minimize $S$, we minimize $k_2-k_1$ first. Since $k_2>k_1$, the minimum difference is $k_2-k_1=1$, leading to $k_2=k_1+1$. This choice results in $a \ge \lambda$.
Next, $S = 3a + (2k_1+1)\lambda$. To minimize $S$, we minimize $k_1$. Since $k_1 \ge 1$, we choose $k_1=1$. This confirms the conditions for minimizing $a+b+c$: minimizing $k_1$ and $k_2-k_1$, which leads to $a \ge \lambda$.

### [W3, round 1]
REPORT on task "Investigate the implications of the constraint $c \le a+b$ when $b=a+k_1\lambda$ and $c=a+k_2\lambda$. Show that minimizing $a+b+c$ requires minimizing $a$ and choosing $k_2=k_1+1$ and $k_1=1$, leadin": I investigated the implications of the constraint $c \le a+b$ on minimizing $a+b+c$. By substituting $b=a+k_1\lambda$ and $c=a+k_2\lambda$, I found that minimizing the sum $S = 3a + (k_1+k_2)\lambda$ requires minimizing the difference $k_2-k_1$, forcing $k_2=k_1+1$. Subsequently, minimizing $k_1$ (choosing $k_1=1$) and applying the constraint leads directly to $a \ge \lambda$.
Candidate answer: ""
