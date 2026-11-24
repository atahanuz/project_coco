### [W4, round 1]
Simulation Results: Testing $P(x) = a_3 x^3 + a_1 x$ modulo 61.

We tested $a_3 \in \{1, 2, 3\}$ against all $a_1 \in \{0, 1, \dots, 60\}$.
For all tested values, the polynomial $P(x)$ was NOT a permutation polynomial modulo 61.
Specifically, for $a_3=1, 2,$ and $3$, the total count of $a_1$ values yielding a bijective map was 0.
This suggests that cubic polynomials of the form $a_3 x^3 + a_1 x$ may not be permutations modulo 61.

### [W4, round 1]
REPORT on task "Use Python simulation to test the permutation property of $P(x) = a_3 x^3 + a_1 x$ modulo 61 for several small non-zero values of $a_3$ (e.g., $a_3=1, 2, 3$) and various $a_1$. Document observations r": I conducted a Python simulation to test the permutation property of polynomials of the form $P(x) = a_3 x^3 + a_1 x$ modulo 61, specifically for $a_3 \in \{1, 2, 3\}$ and all $a_1 \in \{0, 1, \dots, 60\}$. The simulation showed that for these tested values of $a_3$, no choice of $a_1$ resulted in $P(x)$ being a permutation polynomial modulo 61. I documented this observation in the team notes.
Candidate answer: ""

### [W1, round 1]
### Analysis of $P(x) = a_1 x$ (Case $a_3=0, a_2=0, a_0=0$)

**Condition (3) Analysis:**
For $P(x) = a_1 x$ to satisfy Condition (3) modulo 2013, the values $\{a_1 k \pmod{2013} \mid k=0, \dots, 2012\}$ must be distinct. This requires $a_1$ to be coprime to 2013, i.e., $\gcd(a_1, 2013) = 1$.
$2013 = 3 \cdot 11 \cdot 61$.
The number of such coefficients $a_1 \in \{1, 2, \dots, 2012\}$ is $\phi(2013)$.
$\phi(2013) = 2013 \left(1 - \frac{1}{3}\right) \left(1 - \frac{1}{11}\right) \left(1 - \frac{1}{61}\right) = 1200$.

**Modulo 3 Check:**
If $\gcd(a_1, 2013) = 1$, then $a_1$ cannot share any prime factor with 2013. Since 3 is a prime factor of 2013, any $a_1$ satisfying Condition (3) must satisfy $a_1 \not\equiv 0 \pmod 3$. Thus, all 1200 such values satisfy this sub-requirement of Condition (1).

**Condition (2) Analysis and Conflict Summary:**
For $P(x) = a_1 x$, Condition (2) requires $P(x) + P(-x) = 0 \equiv 0 \pmod{2013}$, which is trivially satisfied for any $a_1$.
In the general case, Condition (2) implies $2a_2 x^2 + 2a_0 \equiv 0 \pmod{2013}$ for $x=1, \dots, 100$. This forces $a_0 \equiv 0 \pmod{2013}$ and $a_2 \equiv 0 \pmod{2013}$. Therefore, Condition (2) forces the polynomial to be of the form $P(x) = a_3 x^3 + a_1 x$ (an odd function). Since $a_3$ is unconstrained by Condition (2), the conflict mentioned likely refers to the fact that if Condition (2) were to constrain $a_3$, it would require $a_3=0$ or restrict $a_3$ severely, but it does not. For this specific case $a_3=0$, the constraints are met.

### [W1, round 1]
REPORT on task "Analyze the case where $a_3=0$. Determine the number of coefficients $a_1 \in \{1, 2, ..., 2012\}$ such that $P(x)=a_1 x$ satisfies Condition (3) for modulo 2013. Additionally, check if any such $a_1$": I analyzed the case $P(x) = a_1 x$, where $a_3=0$. Condition (3) requires $a_1$ to be coprime to $2013$, meaning $\gcd(a_1, 3 \cdot 11 \cdot 61) = 1$. The number of such values for $a_1$ in the range $\{1, \dots, 2012\}$ is $\phi(2013) = 1200$. All 1200 such values satisfy $a_1 \not\equiv 0 \pmod 3$, as being coprime to 2013 prevents divisibility by 3. Condition (2) is trivially satisfied for this form of $P(x)$, but generally requires $a_0=0$ and $a_2=0$, forcing $P$ to be an odd function, which is consistent with $a_3=0$.
Candidate answer: 1200

### [W3, round 1]
The task asks to count pairs $(a_3, a_1)$ constrained by Conditions (1) and (2) only, subject to $a_3 \not\equiv 0 \pmod{11}$ and $a_3 + a_1 \not\equiv 0 \pmod 3$.

1. Coefficients $a_i$ must satisfy $0 \le a_i \le 2012$.
2. Condition (2) relates to $P(x) + P(-x) = 2a_2 x^2 + 2a_0$. This imposes constraints on $a_2$ and $a_0$ (specifically, $a_2$ must be a multiple of 671, etc.), but it places *no* constraints on $a_3$ or $a_1$.
3. Constraints on $a_3$: $0 \le a_3 \le 2012$ and $a_3 \not\equiv 0 \pmod{11}$. The number of multiples of 11 in $[0, 2012]$ is $183$. Thus, the number of valid choices for $a_3$ is $2013 - 183 = 1830$.
4. Constraints on $a_1$: $0 \le a_1 \le 2012$ and $a_1 \not\equiv -a_3 \pmod 3$. Since $2013$ is divisible by 3, there are exactly $2013/3 = 671$ values of $a_1$ for any given residue modulo 3. The number of choices for $a_1$ that satisfy the condition is $2013 - 671 = 1342$.
5. Since the choice of $a_1$ is independent of the specific valid value of $a_3$, the total number of pairs $(a_3, a_1)$ is $1830 \times 1342 = 2,455,860$.

### [W3, round 1]
REPORT on task "Calculate the total number of pairs $(a_3, a_1)$ satisfying the constraints derived from Conditions (1) and (2) only: $a_3 \not\equiv 0 \pmod{11}$ and $a_3 + a_1 \not\equiv 0 \pmod 3$. This gives a co": I analyzed Conditions (1) and (2) to find constraints on $(a_3, a_1)$. Condition (2) only restricts $a_2$ and $a_0$, leaving $a_3$ and $a_1$ subject only to the task's specific criteria. The number of valid choices for $a_3$ (not divisible by 11) is 1830. For any valid $a_3$, the number of valid choices for $a_1$ (such that $a_3+a_1$ is not divisible by 3) is 1342. The total number of pairs is $1830 \times 1342 = 2,455,860$.
Candidate answer: 2455860

### [W2, round 1]
Analysis of $f(x) = a_3 x^3 + a_1 x$ modulo 61:
A polynomial $f(x)$ is a permutation polynomial (PP) modulo 61 if and only if the equation $a_3 (x^2 + xy + y^2) + a_1 \equiv 0 \pmod{61}$ has no solutions $(x, y)$ such that $x \ne y$.

We examined the equation $x^2 + xy + y^2 \equiv C \pmod{61}$, where $C = -a_1 a_3^{-1}$. Since $61$ is prime and $61 \equiv 1 \pmod 3$, the quadratic form $x^2 + xy + y^2$ represents all residues modulo 61. Thus, for any $a_3, a_1$ with $a_3 \ne 0$, solutions $(x, y)$ always exist.

We analyzed the condition $x=y$, which requires $3x^2 \equiv C \pmod{61}$.
1. If $C$ is a quadratic residue modulo 61 (or $C=0$), solutions where $x=y$ exist, but the total number of solutions $|S|$ is strictly greater than the number of diagonal solutions $|S_{diag}|$ (e.g., $|S| \ge 60$, $|S_{diag}| \le 2$), guaranteeing solutions with $x \ne y$.
2. If $C$ is a non-residue modulo 61, no solutions with $x=y$ exist ($|S_{diag}|=0$), but since solutions always exist, all solutions must satisfy $x \ne y$.

Conclusion: For any choice of $a_3 \ne 0$ and $a_1$, the equation always has solutions $(x, y)$ with $x \ne y$. Therefore, $f(x) = a_3 x^3 + a_1 x$ is never a permutation polynomial modulo 61 if $a_3 \ne 0$.

### [W2, round 1]
REPORT on task "Focus on Condition (3) modulo 61 for $a_3 \ne 0$. Determine the necessary and sufficient conditions on the pair $(a_3, a_1)$ for $f(x) = a_3 x^3 + a_1 x$ to be a permutation polynomial modulo 61. Spec": I focused on the condition for $f(x) = a_3 x^3 + a_1 x$ to be a permutation polynomial modulo 61. This requires that the equation $a_3 (x^2 + xy + y^2) + a_1 \equiv 0 \pmod{61}$ has no solutions $(x, y)$ with $x \ne y$. By analyzing the quadratic form $x^2 + xy + y^2 \pmod{61}$, I proved that for any $a_3 \ne 0$ and $a_1$, solutions always exist where $x \ne y$. Thus, $f(x)$ is never a permutation polynomial modulo 61 when $a_3 \ne 0$.
Candidate answer: No necessary and sufficient conditions exist for $a_3 \ne 0$.
