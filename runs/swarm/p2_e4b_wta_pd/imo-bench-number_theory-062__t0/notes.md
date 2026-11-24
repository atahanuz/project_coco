### [W2, round 1]
Derivation for $\gcd(n, m) = 1$:
From condition (ii), $g(nm) + nm = ng(m) + mg(n)$.
Rearranging gives: $g(nm) = ng(m) + mg(n) - nm$.

Analysis of properties:
The function $g$ does not exhibit a simple multiplicative property ($g(nm) = g(n)g(m)$) or an additive property ($g(nm) = g(n) + g(m)$) when $\gcd(n, m) = 1$.
For example, using $n=2, m=3$: $g(2)=3, g(3)=4$. $g(6) = 2(4) + 3(3) - 6 = 11$.
Multiplicative check: $g(2)g(3) = 12 \neq 11$.
Additive check: $g(2) + g(3) = 7 \neq 11$.

### [W3, round 1]
Functional Equation for h(n):
Define $h(n) = g(n) - n$. Substituting $g(n) = h(n) + n$ into condition (ii) $g(nm) + nm = ng(m) + mg(n)$ yields:
$h(nm) + 2nm = n(h(m) + m) + m(h(n) + n)$
$h(nm) + 2nm = nh(m) + nm + mh(n) + mn$
$h(nm) = nh(m) + mh(n)$.

Value for primes p:
From condition (i), $g(p) = p + 1$. Thus, $h(p) = g(p) - p = (p+1) - p = 1$.

Value for prime powers p^k:
Using induction on $k$, based on $h(p^k) = h(p^{k-1} \cdot p) = p^{k-1} h(p) + p h(p^{k-1})$.
With $h(p)=1$, we find the pattern:
$h(p^k) = k p^{k-1}$.

### [W1, round 1]
Calculated g(n) for n up to 50 using the recurrence relation g(mp) = m + p * g(m), where p is the smallest prime factor of n and m = n/p.
The solutions found in the range 1 <= n <= 50 satisfying g(n) = 2n are n=4 and n=27.

### [W4, round 1]
Analysis of $g(n)=2n$:
Let $h(n) = g(n) - n$. The condition $g(n)=2n$ is equivalent to $h(n)=n$.
Using the functional equation (ii), $g(nm) + nm = ng(m) + mg(n)$, we derived the functional equation for $h$:
$h(nm) = h(n)m + h(m)n$.

From condition (i), $g(p) = p+1$ for prime $p$. Thus, $h(p) = g(p) - p = 1$.

Case 1: $n$ is a prime power, $n=p^a$.
By induction (or direct evaluation based on the derived functional equation), we find $h(p^a) = a p^{a-1}$.
We require $h(p^a) = p^a$.
$a p^{a-1} = p^a$. Dividing by $p^{a-1}$ gives $a = p$.
Thus, solutions must be of the form $n=p^p$.

Case 2: $n$ has at least two distinct prime factors, $n=n_1 n_2$ where $\gcd(n_1, n_2)=1$.
We found the condition $h(n) = n$ leads to $a_1 p_1 + a_2 p_2 = p_1 p_2$, where $n_1=p_1^{a_1}$ and $n_2=p_2^{a_2}$. This Diophantine equation has no solutions for positive exponents $a_1, a_2$ and distinct primes $p_1, p_2$.

Conclusion: All solutions must be of the form $n=p^p$.
We check the constraint $n \le 4000$:
1. $p=2$: $n=2^2 = 4$. (Valid)
2. $p=3$: $n=3^3 = 27$. (Valid)
3. $p=5$: $n=5^5 = 3125$. (Valid)
4. $p=7$: $n=7^7 > 4000$. (Invalid)
The set of solutions is $\{4, 27, 3125\}$.

### [W3, round 2]
[W3, Verification]
Verification of g(3125) = 2 * 3125:
We have $3125 = 5^5$. Using the established pattern for prime powers $h(p^k) = k p^{k-1}$, we calculate $h(3125)$:
$h(5^5) = 5 \cdot 5^{5-1} = 5 \cdot 5^4 = 5^5 = 3125$.
Since $h(n) = g(n) - n$, we have $g(3125) - 3125 = 3125$, which confirms $g(3125) = 2 \cdot 3125$. This aligns with the general solution form $n=p^p$ found earlier.

### [W1, round 2]
Verification of $h(p_1 p_2) = p_1 p_2$ for distinct primes $p_1, p_2$:
Using the derived functional equation for $h$: $h(nm) = nh(m) + mh(n)$ (valid for coprime $n, m$).
Set $n=p_1$ and $m=p_2$. Since $p_1$ and $p_2$ are distinct primes, $\gcd(p_1, p_2) = 1$.
$h(p_1 p_2) = p_1 h(p_2) + p_2 h(p_1)$.
Since $h(p) = 1$ for any prime $p$, we have $h(p_1) = 1$ and $h(p_2) = 1$.
$h(p_1 p_2) = p_1(1) + p_2(1) = p_1 + p_2$.
Conclusion: The equation $h(p_1 p_2) = p_1 p_2$ is FALSE, as $p_1 + p_2 \neq p_1 p_2$ for distinct primes (e.g., $2+3=5 \neq 2\cdot 3=6$). This verifies that Case 2 in W4, where $h(n)=n$ for $n=p_1 p_2$, has no solutions, which confirms the previous analysis.

### [W4, round 2]
### [W4, Round 2] Formalizing the Composite Case Proof

**Goal:** Prove that if $n$ is a composite number with at least two distinct prime factors, $h(n) \neq n$.

**Setup:** Let $n = n_1 n_2$, where $\gcd(n_1, n_2) = 1$, $n_1 > 1$, and $n_2 > 1$.
Let $n_1 = p_1^{a_1}$ and $n_2 = p_2^{a_2}$, where $p_1 \neq p_2$ are prime and $a_1, a_2 \ge 1$.

**Known Results:**
1. $h(n_1 n_2) = n_1 h(n_2) + n_2 h(n_1)$.
2. $h(p^a) = a p^{a-1}$.

**Substitution:**
$$h(n) = h(p_1^{a_1} p_2^{a_2}) = p_1^{a_1} h(p_2^{a_2}) + p_2^{a_2} h(p_1^{a_1})$$
$$h(n) = p_1^{a_1} (a_2 p_2^{a_2-1}) + p_2^{a_2} (a_1 p_1^{a_1-1})$$
$$h(n) = a_2 p_1^{a_1} p_2^{a_2-1} + a_1 p_2^{a_2} p_1^{a_1-1}$$

**Condition $h(n) = n$:**
We set $h(n) = p_1^{a_1} p_2^{a_2}$:
$$p_1^{a_1} p_2^{a_2} = a_2 p_1^{a_1} p_2^{a_2-1} + a_1 p_2^{a_2} p_1^{a_1-1}$$

**Algebraic Simplification:**
Divide the entire equation by $p_1^{a_1-1} p_2^{a_2-1}$:
$$p_1 p_2 = a_2 p_1 + a_1 p_2$$

**Solving the Diophantine Equation:**
We rearrange the equation to solve for $a_1$:
$$p_1 p_2 - a_2 p_1 = a_1 p_2$$
$$p_1 (p_2 - a_2) = a_1 p_2$$

Since $p_1$ and $p_2$ are distinct primes, $\gcd(p_1, p_2) = 1$. For the equality to hold, $p_2$ must divide $p_1 (p_2 - a_2)$. As $\gcd(p_1, p_2) = 1$, we must have $p_2$ dividing $(p_2 - a_2)$.
If $p_2 | (p_2 - a_2)$, then $p_2 | (-a_2)$, which implies $p_2 | a_2$.
Let $a_2 = k p_2$ for some positive integer $k$ (since $a_2 \ge 1$).

Substitute this back:
$$p_1 (p_2 - k p_2) = a_1 p_2$$
$$p_1 p_2 (1 - k) = a_1 p_2$$

Divide by $p_2$:
$$a_1 = p_1 (1 - k)$$

Since $a_1$ is an exponent, we require $a_1 \ge 1$. Since $p_1 > 0$, we must have $1 - k > 0$, so $k < 1$.
However, since $a_2 \ge 1$ and $p_2 \ge 2$, we have $k = a_2/p_2 > 0$. Since $k$ must be an integer, $k \ge 1$.
The requirement $k < 1$ contradicts $k \ge 1$.

**Conclusion:** No solutions exist for $a_1, a_2 \ge 1$ when $p_1 \neq p_2$. Therefore, if $n$ has two or more distinct prime factors, $h(n) \neq n$, meaning $g(n) \neq 2n$.
