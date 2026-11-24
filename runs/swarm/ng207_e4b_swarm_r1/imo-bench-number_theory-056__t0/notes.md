### [W3, round 1]
Case $n$ is prime:
The condition $P(k) \equiv 0 \pmod n$ for all positive integers $k$ implies that $P(x) \equiv 0 \pmod n$ for all $x \in \mathbb{Z}_n$.
Since $n$ is prime, by Fermat's Little Theorem, $x^n - x \equiv 0 \pmod n$.
A polynomial vanishing for all $x \in \mathbb{Z}_n$ must be a multiple of $x^n - x$ in $\mathbb{Z}_n[x]$.
We seek a polynomial $P(x)$ such that $P(x) \equiv 0 \pmod n$ for all $x \in \mathbb{Z}_n$, and $P(x)$ has coefficients $a_i \in \{1, -1, 0\}$.

Consider $P(x) = x^n - x$.
1. Degree: $\deg(P) = n$. Since $n$ is prime, $n>1$. (Satisfied)
2. Coefficients: The non-zero coefficients are $a_n=1$ and $a_1=-1$. These are in $\{1, -1\}$. (Satisfied)
3. Divisibility: By Fermat's Little Theorem, $k^n - k \equiv 0 \pmod n$ for any integer $k$. Thus $P(k)$ is a multiple of $n$. (Satisfied)

$P(x) = x^n - x$ is a valid solution and has exactly 2 non-zero coefficients. Since the degree is $n>1$, we must have at least two non-zero coefficients ($a_n \ne 0$ and $a_1 \ne 0$ if we assume the simplest form), so 2 is the minimum possible number.

Conjecture for prime $n$: The minimum number of non-zero coefficients is 2.

### [W3, round 1]
REPORT on task "Consider the case where $n$ is prime. Since $P(k) \equiv 0 \pmod n$ for all $k$, explore the relationship between $P(x)$ and $x^n - x$ (or related polynomials) in $\mathbb{Z}_n[x]$, and how this restr": For the case where $n$ is prime, we analyzed the condition $P(k) \equiv 0 \pmod n$ for all integers $k$. This forces $P(x)$ to be congruent to a multiple of $x^n - x$ modulo $n$. We constructed the polynomial $P(x) = x^n - x$. This polynomial satisfies all constraints: its degree is $n$, its coefficients are only $1, -1,$ or $0$, and $P(k) \equiv 0 \pmod n$ by Fermat's Little Theorem. Since the polynomial must have degree $n>1$, it requires at least two non-zero coefficients (for $x^n$ and $x$), establishing that the minimum possible number of non-zero coefficients for prime $n$ is 2.
Candidate answer: 2

### [W2, round 1]
Analysis of $P(k) \equiv 0 \pmod n$ for all $k \in \mathbb{Z}^+$:
The condition is equivalent to stating that the polynomial $P(x)$ must evaluate to zero for every element $x$ in the ring $\mathbb{Z}_n$. That is, $P(x) \in \text{Ann}(\mathbb{Z}_n)$ where $\text{Ann}(\mathbb{Z}_n)$ is the set of functions from $\mathbb{Z}_n$ to $\{0\}$.

Necessary Condition: $P(x)$ must be in the ideal of polynomials that vanish on $\mathbb{Z}_n$.

If $n$ is prime, $n=p$, $\mathbb{Z}_p$ is a field. A polynomial of degree $p$ vanishing for all $p$ inputs must be a multiple of $x^p - x$ in $\mathbb{Z}_p[x]$. Since $P(x)$ must have degree $n$, the minimum number of non-zero coefficients is achieved when $P(x) = \pm(x^n - x)$, giving 2 non-zero coefficients.

If $n$ is composite, the structure is determined by the least common multiple of polynomials $(x^{p_i^{e_i}} - 1)$ or similar constructs derived from the Chinese Remainder Theorem, but the core necessary condition remains that $P(x)$ must vanish on all of $\mathbb{Z}_n$.

Small case verification suggests that the minimum number of non-zero coefficients is 2 for $n=2, 3, 4$.

### [W1, round 1]
**Findings for specific degrees (Task Requirement):**

**Case n=2:**
Minimum number of non-zero coefficients: 2.
Corresponding polynomial structure: $P(x) = x^2 + x$.
(Checked: $P(1)=2\equiv 0 \pmod 2$, $P(2)=6\equiv 0 \pmod 2$, $P(3)=12\equiv 0 \pmod 2$.)

**Case n=3:**
Minimum number of non-zero coefficients: 2.
Corresponding polynomial structure: $P(x) = x^3 - x$.
(Checked: $P(1)=0\equiv 0 \pmod 3$, $P(2)=6\equiv 0 \pmod 3$, $P(3)=18\equiv 0 \pmod 3$.)

**Case n=4:**
Minimum number of non-zero coefficients: 2.
Corresponding polynomial structure: $P(x) = -x^4 + x^2$.
(Checked: $P(1)=0\equiv 0 \pmod 4$, $P(2)=-12\equiv 0 \pmod 4$, $P(3)=-72\equiv 0 \pmod 4$.)

### [W2, round 1]
REPORT on task "Analyze the condition $P(k) \equiv 0 \pmod n$ for all $k \in \mathbb{Z}^+$. Investigate what this implies about the polynomial $P(x)$ when viewed as an element of $\mathbb{Z}_n[x]$. Specifically, cons": I analyzed the condition $P(k) \equiv 0 \pmod n$ by reformulating it as $P(x)$ vanishing for all $x \in \mathbb{Z}_n$. This requires $P(x)$ to belong to the ideal of polynomials that vanish on $\mathbb{Z}_n$. For prime $n$, this implies $P(x)$ must be a multiple of $x^n - x$. Choosing $P(x) = x^n - x$ provides a valid polynomial satisfying the constraints with exactly 2 non-zero coefficients. Numerical checks for $n=2, 3, 4$ also confirm that 2 is achievable. Therefore, the minimum possible number of non-zero coefficients appears to be 2.
Candidate answer: 2

### [W1, round 1]
REPORT on task "Examine small degrees $n=2, 3, 4$. For each $n$, find the minimum number of non-zero coefficients (which must be 1 or -1) such that $P(k)$ is a multiple of $n$ for $k=1, 2, 3$. Record the minimum coun": I examined the constraints for degrees $n=2, 3,$ and $4$. For $n=2$, the minimum count is 2, exemplified by $P(x)=x^2+x$. For $n=3$, the minimum count is 2, exemplified by $P(x)=x^3-x$. For $n=4$, the minimum count is 2, exemplified by $P(x)=-x^4+x^2$. In all examined cases, the minimum number of non-zero coefficients found was 2.
Candidate answer: The minimum count is 2 for $n=2, 3, 4$.

### [W4, round 1]
### [W4, round 1] Deriving constraints on $n$ for small $m$

Based on the existing findings, it appears $m=2$ is achievable for many $n$. We derive the necessary structural constraints on $n$ by assuming the minimum possible number of non-zero coefficients, $m=2$.

Let $P(x) = a_n x^n + a_j x^j$, where $n > j \ge 0$ and $a_n, a_j \in \{1, -1\}$. The condition is $P(k) \equiv 0 \pmod n$ for all positive integers $k$.

1. Constraint from $k=1$:
$P(1) = a_n + a_j$. We require $a_n + a_j \equiv 0 \pmod n$.
Since $a_n, a_j \in \{1, -1\}$, $a_n + a_j \in \{-2, 0, 2\}$.
If $n > 2$, then $n$ must divide $a_n + a_j = 0$, which implies $a_n = -a_j$.
If $n=2$, $a_n+a_j$ can be 0 or $\pm 2$. If $a_n=a_j=1$, $P(x)=x^2+x$. $P(1)=2\equiv 0 \pmod 2$. This holds.

Assuming $n>2$ (or treating the $n=2$ case separately, which we know works), we must have $a_j = -a_n$.
$P(x)$ must be of the form $a_n (x^n - x^j)$.

2. Constraint from $k=2$:
$P(2) = a_n (2^n - 2^j)$. We require $a_n (2^n - 2^j) \equiv 0 \pmod n$.
Since $a_n = \pm 1$, we must have:
$$2^n \equiv 2^j \pmod n$$
This is a necessary structural constraint on $n$ if a solution exists with $m=2$ and $n>2$.

**Summary of Constraints (for $m=2, n>2$):**
A polynomial $P(x)$ with only two non-zero coefficients ($a_n$ and $a_j$) satisfying $P(k) \equiv 0 \pmod n$ for all $k$ requires that $n$ and $j$ satisfy the congruence $2^n \equiv 2^j \pmod n$. This condition is satisfied when $n$ is prime and $j=1$ (by Fermat's Little Theorem), as seen previously.

### [W4, round 1]
REPORT on task "Assume $P(x)$ has a small fixed number of non-zero coefficients, say $m$. Derive structural constraints on $n$ that must be satisfied for such a polynomial to exist and satisfy $P(k) \equiv 0 \pmod n$": I assumed $P(x)$ has exactly $m=2$ non-zero coefficients, $P(x) = a_n x^n + a_j x^j$. Applying the condition $P(k) \equiv 0 \pmod n$ for $k=1$ and $k=2$ led to necessary structural constraints on $n$. For $n>2$, the condition $P(1) \equiv 0 \pmod n$ forces $a_n = -a_j$. The condition $P(2) \equiv 0 \pmod n$ then forces the necessary constraint $2^n \equiv 2^j \pmod n$ for some $j < n$. This confirms that solutions exist for prime $n$ (where $j=1$) and some composite $n$ (like $n=4$ where $j=2$).
Candidate answer: The existence of such a polynomial requires $n$ to satisfy specific congruences related to the exponents of 2 modulo $n$ when assuming the minimum possible number of non-zero coefficients $m=2$.
