### [W1, round 1]
Checked the property $k^2 \equiv 1 \pmod n$ for $1 \le k < n$ and $\gcd(k, n) = 1$ for $n=2$ to $n=15$.
The values of $n$ that satisfy the condition in this range are $n \in \{2, 3, 4, 6, 8, 12\}$.

### [W3, round 1]
For $n=pq$ with distinct primes $p$ and $q$, the condition $k^2 \equiv 1 \pmod n$ for all $\gcd(k, n)=1$ is equivalent to the system of congruences:
1. $k^2 \equiv 1 \pmod p$
2. $k^2 \equiv 1 \pmod q$
This must hold for all $k$ coprime to $p$ and $q$.
The condition $k^2 \equiv 1 \pmod p$ for all $k$ coprime to $p$ implies that the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^\times$ must be an elementary abelian 2-group. Since this group is cyclic of order $p-1$, its order must be 1 or 2.
If $p-1=1$, then $p=2$.
If $p-1=2$, then $p=3$.
Thus, $p$ must be 2 or 3. Similarly, $q$ must be 2 or 3. Since $p$ and $q$ are distinct, the only possibility is $\{p, q\} = \{2, 3\}$, meaning $n=6$.

### [W2, round 1]
The problem asks for all $n \ge 2$ such that $k^2 \equiv 1 \pmod n$ for all $k$ coprime to $n$.
We are analyzing the case where $n$ is a prime power, $n=p^a$.

---
**Case 1: $n=p$, where $p$ is an odd prime.**

The condition requires that for every $k$ such that $\gcd(k, p)=1$, we must have $k^2 \equiv 1 \pmod p$.
The multiplicative group $(\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic of order $\phi(p) = p-1$.
If $k^2 \equiv 1 \pmod p$ for all $k$, then every element in this group must have order dividing 2. This means the exponent of the group must be 2.
Since the group is cyclic, its exponent is equal to its order, $p-1$.
We require $p-1 \le 2$.

1.  $p-1 = 1 \implies p=2$. (Excluded by the prompt condition that $p$ is an odd prime).
2.  $p-1 = 2 \implies p=3$.

Let's verify $p=3$: $(\mathbb{Z}/3\mathbb{Z})^\times = \{1, 2\}$. $1^2 \equiv 1 \pmod 3$ and $2^2 = 4 \equiv 1 \pmod 3$. So $n=3$ works.

For any odd prime $p>3$, $p-1 > 2$. The cyclic group $(\mathbb{Z}/p\mathbb{Z})^\times$ contains elements of order $p-1 > 2$. Therefore, there exists a $k$ such that $k^2 \not\equiv 1 \pmod p$.
Conclusion for Case 1: The only odd prime $n$ satisfying the condition is $n=3$.

### [W2, round 1]
**Case 2: $n=p^a$, where $a \ge 2$.**

**Subcase 2a: $p$ is an odd prime.**
The multiplicative group $(\mathbb{Z}/p^a\mathbb{Z})^\times$ has order $\phi(p^a) = p^{a-1}(p-1)$.
For $a \ge 2$ and $p \ge 3$, we have $\phi(p^a) \ge 3(3-1) = 6 > 2$.
Since the group size is greater than 2, and for $a \ge 2$, the group structure (being cyclic) ensures the exponent is $\phi(p^a)$, there must exist elements $k$ such that the order of $k$ is greater than 2. Thus, $k^2 \not\equiv 1 \pmod{p^a}$.
Conclusion for odd primes: No solutions for $a \ge 2$.

**Subcase 2b: $p=2$.**
We examine $n=2^a$ for $a \ge 2$.

1.  **$n=4$ ($a=2$):** $(\mathbb{Z}/4\mathbb{Z})^\times = \{1, 3\}$. $1^2 \equiv 1 \pmod 4$ and $3^2 = 9 \equiv 1 \pmod 4$. $n=4$ works.
2.  **$n=8$ ($a=3$):** $(\mathbb{Z}/8\mathbb{Z})^\times = \{1, 3, 5, 7\}$. All elements squared are $1 \pmod 8$. $n=8$ works.
3.  **$n=16$ ($a=4$):** $(\mathbb{Z}/16\mathbb{Z})^\times$ has order 8. It is not cyclic. The element $3$ has order 4 ($3^2=9$, $3^4=81 \equiv 1 \pmod{16}$). Since $3^2 \not\equiv 1 \pmod{16}$, $n=16$ fails.
4.  **$n=2^a, a \ge 4$:** For $a \ge 4$, the multiplicative group $(\mathbb{Z}/2^a\mathbb{Z})^\times$ contains elements of order $2^{a-2} > 2$. Thus, $k^2 \not\equiv 1 \pmod{2^a}$ for all units $k$. $n=2^a$ fails for $a \ge 4$.

**Summary of Prime Power Solutions:** The solutions when $n$ is a prime power are $n=3, 4, 8$.

### [W4, round 1]
**General Structure Constraint:** The condition that $k^2 \equiv 1 \pmod n$ for all $k \in (\mathbb{Z}/n\mathbb{Z})^\times$ is equivalent to requiring that the exponent of the multiplicative group, $\lambda(n)$, must divide 2.

**Constraints on Prime Power Factors $p^a$:**
We require $\lambda(p^a) \mid 2$.
1. **Odd Primes $p$**: $\lambda(p^a) = \phi(p^a) = p^{a-1}(p-1)$. This must divide 2. This forces $a=1$ and $p-1 \mid 2$, meaning $p=3$. Thus, the only allowable odd prime power factor is $3^1=3$.
2. **$p=2$**: $\lambda(2^a)$ is $1, 2, 2, 4, 8, \ldots$ for $a=1, 2, 3, 4, 5, \ldots$. This must divide 2. This forces $a \in \{1, 2, 3\}$. The allowable factors are $2^1=2, 2^2=4, 2^3=8$.

**Structure of $n$:** Since $n$ must be a product of coprime prime powers, $n$ must be of the form $2^a 3^b$.
Based on the constraints:
- $a \in \{0, 1, 2, 3\}$ (if $a=0$, $2^a=1$).
- $b \in \{0, 1\}$.

The solutions $n \ge 2$ are:
- $b=0$: $n \in \{2, 4, 8\}$.
- $b=1$: $n \in \{3, 6, 12, 24\}$.

Total solutions: $n \in \{2, 3, 4, 6, 8, 12, 24\}$.

### [W2, round 2]
### [W2, round 2]
Verification of the proposed solution set N = {2, 3, 4, 6, 8, 12, 24}:
A Python script was run to check the condition $k^2 \equiv 1 \pmod n$ for all positive integers $k$ coprime to $n$, for every $n$ in N.
The results confirmed that all values in N satisfy the condition:
$n=2, 3, 4, 6, 8, 12, 24$ all satisfy the requirement. This verifies the structure derived in [W4, round 1].
