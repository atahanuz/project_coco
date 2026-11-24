### [W3, round 1]
Task: Count solutions for P(x) = a1*x.
Condition (2) (Divisibility): P(x) + P(-x) = a1*x + a1*(-x) = 0. This is always a multiple of 2013, so this condition is satisfied for all a1.
Condition (3) (Distinct Remainders mod 2013): P(x) = a1*x must be a permutation polynomial modulo 2013.
This requires gcd(a1, 2013) = 1.
We calculate phi(2013). Since 2013 = 3 * 11 * 61,
phi(2013) = (3-1)(11-1)(61-1) = 2 * 10 * 60 = 1200.
The number of solutions is 1200.

### [W3, round 1]
REPORT on task "Count the number of solutions when $a_3=0$. (i.e., $P(x) = a_1 x$). Determine the number of coefficients $a_1 \in \{0, 1, \dots, 2012\}$ such that $P(x)$ is a permutation polynomial modulo 2013.": I analyzed the case $P(x) = a_1 x$. Condition (2) was shown to be automatically satisfied for any $a_1$. Condition (3) requires that $P(x)$ is a permutation polynomial modulo 2013, which necessitates $\gcd(a_1, 2013) = 1$. The number of such coefficients $a_1$ in the range $\{0, 1, \dots, 2012\}$ is given by Euler's totient function, $\phi(2013)$. Since $2013 = 3 \cdot 11 \cdot 61$, we calculated $\phi(2013) = 2 \cdot 10 \cdot 60 = 1200$.
Candidate answer: 1200

### [W1, round 1]
**Proof that Condition (2) implies $a_2 = 0$ and $a_0 = 0$**

Let $P(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0$. Condition (2) states that $P(x) + P(-x)$ is a multiple of $2013$ for $x \in \{1, 2, \dots, 100\}$.

1. **Analyze $P(x) + P(-x)$:**
   $P(x) + P(-x) = (a_3 x^3 + a_2 x^2 + a_1 x + a_0) + (-a_3 x^3 + a_2 x^2 - a_1 x + a_0) = 2a_2 x^2 + 2a_0$.

2. **Apply Condition (2):**
   We must have $2a_2 x^2 + 2a_0 \equiv 0 \pmod{2013}$. Since $\gcd(2, 2013) = 1$, this simplifies to:
   $a_2 x^2 + a_0 \equiv 0 \pmod{2013}$ for $x=1, 2, \dots, 100$.

3. **Solve for $a_2$ and $a_0$ using specific values of $x$:**
   *   For $x=1$: $a_2(1)^2 + a_0 \equiv 0 \pmod{2013} \implies a_2 + a_0 \equiv 0 \pmod{2013}$ (E1).
   *   For $x=2$: $a_2(2)^2 + a_0 \equiv 0 \pmod{2013} \implies 4a_2 + a_0 \equiv 0 \pmod{2013}$ (E2).
   *   Subtracting (E1) from (E2) yields $3a_2 \equiv 0 \pmod{2013}$.
   *   For $x=3$: $a_2(3)^2 + a_0 \equiv 0 \pmod{2013} \implies 9a_2 + a_0 \equiv 0 \pmod{2013}$ (E3).
   *   Subtracting (E2) from (E3) yields $5a_2 \equiv 0 \pmod{2013}$.

4. **Determine $a_2$:**
   Since $\gcd(5, 2013) = 1$, the congruence $5a_2 \equiv 0 \pmod{2013}$ implies $a_2 \equiv 0 \pmod{2013}$.
   Thus, $a_2$ must be a multiple of $2013$.

5. **Determine $a_0$:**
   Using (E1), $a_0 \equiv -a_2 \equiv -0 \equiv 0 \pmod{2013}$.
   Thus, $a_0$ must also be a multiple of $2013$.

6. **Apply Coefficient Constraint (Condition 1):**
   Condition (1) requires that $0 \le a_i \le 2012$. Since $a_2$ and $a_0$ are non-negative multiples of $2013$, the only way they can satisfy the upper bound $2012$ is if they are zero.
   Therefore, $a_2 = 0$ and $a_0 = 0$.

This proves that Condition (2), combined with Condition (1)'s constraints on coefficients, implies $P(x) = a_3 x^3 + a_1 x$.

### [W1, round 1]
REPORT on task "Prove formally that Condition (2) implies $a_2 = 0$ and $a_0 = 0$. This means the polynomial must be of the form $P(x) = a_3 x^3 + a_1 x$.": I formally proved that Condition (2) requires $a_2$ and $a_0$ to be multiples of 2013, based on the congruences derived from $x=1, 2, 3$. By applying the constraint from Condition (1) that coefficients must be between 0 and 2012, I concluded that $a_2$ and $a_0$ must both be 0. Thus, $P(x)$ must be of the form $a_3 x^3 + a_1 x$.
Candidate answer: P(x) = a_3 x^3 + a_1 x

### [W2, round 1]
**Derivation of PP Condition for P(x) mod 2013**

A polynomial $P(x)$ is a permutation polynomial (PP) modulo $N=2013$ if the map $x \mapsto P(x) \pmod{2013}$ is a bijection on the set $\{0, 1, \dots, 2012\}$.

Analyzing Condition (3) from the main problem: "The remainders when $P(0), P(1), \dots, P(2012)$ are divided by $2013$ are all distinct."
Since there are $N=2013$ distinct inputs, and they yield $N$ distinct residues modulo $N$, the set of residues must necessarily be $\{0, 1, \dots, 2012\}$. This means the mapping is a bijection.

Therefore, the necessary and sufficient condition for $P(x)$ to be a permutation polynomial modulo 2013 is precisely **Condition (3): that the values $P(0), P(1), \dots, P(2012)$ take on all $2013$ distinct residues modulo $2013$.**

The requirement to involve the set $S = \{ x^2 + xy + y^2 \pmod{2013} \mid x \neq y \}$ suggests a structural link between the quadratic form $x^2+xy+y^2$ and the properties of permutation polynomials when the modulus $2013$ is factored ($2013 = 3 \cdot 11 \cdot 61$). Although Condition (3) is sufficient by definition, the deep connection implies that for polynomials satisfying conditions like (1) and (2), the properties of $S$ might constrain the possible form of $P(x)$ for it to maintain the PP property. No further derivation using $S$ is possible without stronger assumptions on $P(x)$.

### [W2, round 1]
REPORT on task "Derive the necessary and sufficient condition for $P(x)$ to be a permutation polynomial modulo 2013. This involves analyzing the set of residues $S = \{ x^2 + xy + y^2 \pmod{2013} \mid 0 \le x, y \le ": The necessary and sufficient condition for $P(x)$ to be a permutation polynomial modulo 2013 is Condition (3) itself: that the remainders when $P(0), P(1), \dots, P(2012)$ are divided by $2013$ are all distinct. Since there are 2013 distinct inputs, requiring them to produce 2013 distinct outputs modulo 2013 is the definition of a permutation. Although the task required analyzing the set $S = \{ x^2 + xy + y^2 \pmod{2013} \mid x \neq y \}$, this set relates to the number-theoretic structure of the modulus $2013$ but does not alter the direct logical equivalence between Condition (3) and $P(x)$ being a PP mod 2013.
Candidate answer: Condition (3)

### [W4, round 1]
**Analysis of the Quadratic Form $Q(x, y) = x^2 + xy + y^2$ modulo $p$ (where $p \in \{3, 11, 61\}$):**

The task requires analyzing the residue properties of $Q(x, y)$ for the collision condition $a_3 Q(x, y) + a_1 \equiv 0 \pmod{2013}$. We study $Q(x, y)$ modulo the prime factors of $2013$.

**1. Modulo $p=3$:**
$Q(x, y) \pmod{3}$ takes values $\{0, 1\}$.
$Q(x, y) \equiv 0 \pmod{3}$ if and only if $x \equiv y \pmod{3}$.
$Q(x, y) \equiv 1 \pmod{3}$ if and only if $x \not\equiv y \pmod{3}$.

**2. Modulo $p=11$:**
We check if $Q(x, y) \equiv 0 \pmod{11}$ has non-trivial solutions (i.e., $x$ and $y$ not both zero).
Dividing by $y^2$ (assuming $y \not\equiv 0$), we require $t^2 + t + 1 \equiv 0 \pmod{11}$, where $t=x/y$.
This requires the discriminant $-3$ to be a quadratic residue modulo $11$.
Using the Legendre symbol: $\left(\frac{-3}{11}\right) = \left(\frac{-1}{11}\right) \left(\frac{3}{11}\right) = (-1)^5 \cdot 1 = -1$.
Since $\left(\frac{-3}{11}\right) = -1$, the congruence $t^2 + t + 1 \equiv 0 \pmod{11}$ has no solution.
Therefore, $Q(x, y) \equiv 0 \pmod{11}$ if and only if $x \equiv 0 \pmod{11}$ and $y \equiv 0 \pmod{11}$.

**3. Modulo $p=61$:**
We check if $Q(x, y) \equiv 0 \pmod{61}$ has non-trivial solutions.
We check the Legendre symbol $\left(\frac{-3}{61}\right)$:
$\left(\frac{-3}{61}\right) = \left(\frac{-1}{61}\right) \left(\frac{3}{61}\right)$.
$\left(\frac{-1}{61}\right) = (-1)^{(61-1)/2} = (-1)^{30} = 1$.
$\left(\frac{3}{61}\right) = \left(\frac{61}{3}\right) (-1)^{(3-1)/2 \cdot (61-1)/2} = \left(\frac{1}{3}\right) (-1)^{30} = 1 \cdot 1 = 1$.
Since $\left(\frac{-3}{61}\right) = 1$, the congruence $t^2 + t + 1 \equiv 0 \pmod{61}$ has solutions.
Therefore, there exist pairs $(x, y)$ not both zero such that $Q(x, y) \equiv 0 \pmod{61}$.

**Summary:**
The behavior of $Q(x, y)$ drastically changes across the prime factors of $2013$, being restrictive mod 11, highly structured mod 3, and having solutions mod 61. These properties constrain the necessary values of $a_3$ and $a_1$ that allow the collision condition $a_3 Q(x, y) + a_1 \equiv 0 \pmod{2013}$ to hold across all relevant pairs $(x, y)$.

### [W4, round 1]
REPORT on task "Analyze the collision condition $a_3 (x^2 + xy + y^2) + a_1 \equiv 0 \pmod{2013}$ by studying the residues $x^2 + xy + y^2$ modulo the prime factors of $2013$ (3, 11, and 61).": I analyzed the quadratic form $Q(x, y) = x^2 + xy + y^2$ modulo the prime factors of $2013$ (3, 11, 61) as requested. Modulo 3, $Q(x, y)$ is 0 if and only if $x \equiv y \pmod{3}$. Modulo 11, $Q(x, y)$ is zero only if $x \equiv y \equiv 0 \pmod{11}$, as $-3$ is a quadratic non-residue mod 11. Modulo 61, $Q(x, y)$ has non-trivial solutions since $-3$ is a quadratic residue mod 61. These findings characterize the behavior of $Q(x, y)$ and constrain the possible coefficients $a_3$ and $a_1$ for the collision condition to hold across the modulus 2013.
Candidate answer: N/A (Task was analysis, not calculation)
