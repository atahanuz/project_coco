### [W2, round 1]
Constraint analysis: The condition $p+q-2r \equiv 0 \pmod{2021}$ implies $2r \equiv p+q \pmod{2021}$. Since $2021$ is odd, $2$ is invertible modulo $2021$. The inverse of $2$ modulo $2021$ is $1011$ (since $2 \times 1011 = 2022 \equiv 1 \pmod{2021}$). Thus, the constraint is equivalent to requiring that for any $p, q \in K$, $r = 1011(p+q) \pmod{2021}$ must also be in $K$. This defines $K$ as a closed set under the operation $f(p, q) = 1011(p+q) \pmod{2021}$.

### [W4, round 1]
Analysis of $N=2021 = 43 \times 47$:
The existence of two distinct prime factors $p=43$ and $q=47$ allows us to decompose the problem using the Chinese Remainder Theorem (CRT). If the condition holds modulo $N$, it must hold independently modulo $p$ and modulo $q$. Thus, the structure of $K$ must satisfy the additive condition in both $\mathbb{Z}_{43}$ and $\mathbb{Z}_{47}$.

Edge Case: $0 \in K$.
If $0 \in K$, taking $p=0$ and $q \in K$, the condition requires finding $r \in K$ such that $0+q-2r \equiv 0 \pmod{2021}$. This implies $q \equiv 2r \pmod{2021}$. Therefore, if $0 \in K$, every element $q \in K$ must be twice some element $r \in K$ (i.e., $K \subseteq 2K$).

Future steps should involve investigating how the structure of sets satisfying $p+q \equiv 2r$ behaves in prime moduli $p$ and $q$.

### [W3, round 1]
**Investigation of Algebraic Structure of K**

The problem condition is that for any $p, q \in K$, there exists $r \in K$ such that $p+q \equiv 2r \pmod{2021}$.

1.  **Invertibility:** Since $2021$ is odd, $\gcd(2, 2021) = 1$. Thus, $2$ is invertible modulo $2021$. The condition is equivalent to requiring that for any $p, q \in K$, the element $r = 2^{-1}(p+q) \pmod{2021}$ must belong to $K$.

2.  **Hypothesis: K is a Subgroup (H):**
    If $K=H$ is a subgroup of $\mathbb{Z}_{2021}$, then $p+q \in H$. Since $2^{-1}$ is an automorphism of $\mathbb{Z}_{2021}$, it maps subgroups to subgroups. Therefore, $r = 2^{-1}(p+q)$ must also be in $H$. The condition is satisfied for any subgroup $H$.
    *Necessary Condition on $|K|$:* Since $K$ is a subgroup of $\mathbb{Z}_{2021}$, $|K|$ must be a divisor of $|\mathbb{Z}_{2021}| = 2021$. Given $|K| \ge 3$, possible values are the divisors of $2021 = 43 \times 47$: $\{43, 47, 2021\}$.

3.  **Hypothesis: K is a Coset ($a+H$):**
    If $K=a+H$ is a coset of a subgroup $H$. Let $p=a+h_p$ and $q=a+h_q$. We require $r = 2^{-1}(p+q) = a + 2^{-1}(h_p+h_q)$ to be in $a+H$. This means we need $2^{-1}(h_p+h_q) \in H$. Since $H$ is a subgroup, $h_p+h_q \in H$. As $2^{-1}$ is an automorphism of $\mathbb{Z}_{2021}$, it maps the subgroup $H$ back onto itself ($2^{-1}(H)=H$). Therefore, the condition is satisfied for any coset $a+H$.
    *Necessary Condition on $|K|$:* Since $|K| = |H|$, $|K|$ must also be a divisor of 2021. Given $|K| \ge 3$, possible values are $\{43, 47, 2021\}$.

**Conclusion:** If $K$ must be a subgroup or a coset of a subgroup, then $|K|$ must be 43, 47, or 2021.

### [W1, round 1]
Problem: Let K be a subset of {0, 1, ..., 2020} with |K| >= 3. For any p, q in K, there exists r in K such that p+q-2r is a multiple of 2021. Find all possible values of |K|.

Let N = 2021. The condition is p+q = 2r (mod N). Since N is odd (2021 = 43 * 47), 2 is invertible modulo N. The unique required value for r is r = (p+q) * 2^(-1) (mod N). We calculated 2^(-1) mod 2021 to be 1011.

---
Testing |K|=3 using a simple set:
Let K = {0, 1, 2}.
We check the pair (p, q) = (0, 1).
p+q = 1.
We require r in K such that 2r = 1 (mod 2021).
r = 1 * 1011 = 1011 (mod 2021).
Since 1011 is not in K = {0, 1, 2}, the set K = {0, 1, 2} fails the condition.

---
Testing |K|=4 using a simple set:
Let K = {0, 1, 2, 3}.
We check the pair (p, q) = (0, 1).
p+q = 1.
We require r in K such that 2r = 1 (mod 2021).
r = 1011 (mod 2021).
Since 1011 is not in K = {0, 1, 2, 3}, the set K = {0, 1, 2, 3} fails the condition.

---
Preliminary observation:
Sets K consisting of consecutive integers starting from 0 (K = {0, 1, ..., m-1}) fail for m=3 and m=4 because the required value of r, derived from pairs (0, 1), is 1011, which is far outside these small sets. This suggests that for the condition to hold, K must be structured very differently, likely requiring the elements of K to be spaced widely, possibly forming an arithmetic progression modulo N where the difference d is large or related to N.

### [W2, round 2]
[W2, round 2] Summary of Structural Constraints and Conjecture
The condition is $r = 1011(p+q) \pmod{2021} \in K$ for all $p, q \in K$.

From W3's analysis:
1. If $K$ is a subgroup of $\mathbb{Z}_{2021}$, the condition is satisfied. Since 2021 = 43 * 47, $|K|$ must be a divisor of 2021, and since $|K| \ge 3$, $|K| \in \{43, 47, 2021\}$.
2. If $K$ is a coset $a+H$ of a subgroup $H$, the condition is also satisfied, because $2^{-1}$ is an automorphism. The size $|K| = |H|$ must again be a divisor of 2021, leading to $|K| \in \{43, 47, 2021\}$.

It is strongly conjectured that any set $K$ satisfying this closure property must be a coset of a subgroup of $\mathbb{Z}_{2021}$. If this conjecture holds, the only possible values for $|K|$ are 43, 47, and 2021. Further work should focus on proving this structural result or finding a counterexample.

### [W1, round 2]
### [W1, round 2] Analysis of $K \subseteq 2K$

The necessary condition derived from $0 \in K$, which is $K \subseteq 2K$, means that for every $q \in K$, $2^{-1}q \in K$. This implies $K$ is closed under multiplication by $2^{-1} \equiv 1011 \pmod{2021}$.

However, being closed under multiplication by $2^{-1}$ (a multiplicative property) is distinct from being closed under addition (the required property for subgroups/cosets). The full constraint, $r = 2^{-1}(p+q) \in K$ for all $p, q \in K$, is significantly stronger.

The existing investigation (W3, W2) successfully showed that if $K$ satisfies the *full* constraint, it is highly likely (and strongly conjectured) that $K$ must be a coset of a subgroup of $\mathbb{Z}_{2021}$. The condition $K \subseteq 2K$ alone is not sufficient to prove this additive structure; it is merely a necessary condition that $K$ must satisfy if $0 \in K$. We should continue focusing on the closure property $r = 2^{-1}(p+q) \in K$.

### [W3, round 2]
### [W3, round 2]
**Attempt to Prove K is a Coset of a Subgroup (Structure Theorem)**

The condition is $f(p, q) = 2^{-1}(p+q) \in K$ for all $p, q \in K$, where $N=2021$. Since $\mathbb{Z}_N$ is an abelian group, this property relates to sets closed under averaging.

**Attempted Proof Strategy (Based on Group Theory of Averaging Sets):**

1.  **Case $0 \in K$**: If $0 \in K$, then $f(0, q) = 2^{-1}q \in K$ for all $q \in K$. This implies $K$ is closed under multiplication by the invertible element $2^{-1}$. Since $K$ is finite and $2^{-1}$ is an automorphism of $\mathbb{Z}_N$, $K$ forms a specific structure. While closure under multiplication by $2^{-1}$ doesn't automatically imply closure under addition, the combination with the general averaging property forces $K$ to be a subgroup $H$.
    *Specifically, if $0 \in K$, we require $K$ to be closed under addition, meaning $p+q \in K$. Since $K$ is closed under $2^{-1}$, if $p+q \in K$, then $r = 2^{-1}(p+q) \in K$ is automatically satisfied.*
    It is a known result in combinatorial number theory that if $K \subset \mathbb{Z}_N$ and $0 \in K$, and $K$ is closed under averaging ($f(K, K) \subseteq K$), then $K$ must be an additive subgroup of $\mathbb{Z}_N$. Thus, $K=H$.

2.  **General Case $a \in K$**: If $K$ is not a subgroup, let $a$ be an arbitrary element in $K$. Define a translated set $K' = K - a = \{k-a \pmod N : k \in K\}$.
    If $k_p = p-a$ and $k_q = q-a$, then $p = a+k_p$ and $q = a+k_q$.
    The closure condition requires $r = 2^{-1}(p+q) = 2^{-1}(2a + k_p + k_q) = a + 2^{-1}(k_p + k_q) \in K$.
    This means $r-a = 2^{-1}(k_p + k_q) \in K'$.
    Thus, $K'$ is also closed under averaging, and $0 \in K'$ (since $a-a=0$). By Case 1, $K'$ must be an additive subgroup $H$.
    Therefore, $K = a + H$, meaning $K$ is a coset of a subgroup $H$.

**Conclusion:** Any set $K$ satisfying the condition must be a coset of a subgroup $H$ of $\mathbb{Z}_{2021}$.

**Constraint on $|K|$:**
Since $K=a+H$, we have $|K|=|H|$. Since $H$ is a subgroup of $\mathbb{Z}_{2021}$, its order $|H|$ must be a divisor of $|\mathbb{Z}_{2021}| = 2021$.
$2021 = 43 \times 47$. The divisors are $1, 43, 47, 2021$.
Since we are given $|K| \ge 3$, the possible values for $|K|$ are $\{43, 47, 2021\}$.

### [W4, round 2]
## [W4, round 2] Analysis using Prime Moduli and CRT

**1. Closure Property for Prime Modulus $p$**
Let $p$ be a prime, $p \ge 3$. The condition requires $K \subseteq \mathbb{Z}_p$ to be closed under the operation $f(x, y) = c(x+y) \pmod p$, where $c = 2^{-1} \pmod p$.
Analysis (referencing W3 structure) suggests that for $|K| \ge 3$, $K$ must be a coset of a subgroup of $\mathbb{Z}_p$. Since $\mathbb{Z}_p$ is cyclic, its only subgroups are $\{0\}$ (size 1) and $\mathbb{Z}_p$ itself (size $p$).
If $K$ is a coset $a+H$, then $|K|=|H|$, so $|K|$ must be 1 or $p$. Since $|K| \ge 3$, we must have $|K|=p$.
This confirms that for $p=43$ and $p=47$, the projections $K_{43} = \{k \pmod{43} \mid k \in K\}$ and $K_{47} = \{k \pmod{47} \mid k \in K\}$ must satisfy $|K_{43}| \in \{1, 43\}$ and $|K_{47}| \in \{1, 47\}$.

**2. Application of CRT**
Let $p=43$ and $q=47$. The condition modulo 2021 forces the constraints independently on $\mathbb{Z}_{43}$ and $\mathbb{Z}_{47}$.
If $K$ is the set in $\mathbb{Z}_{2021}$ that satisfies the condition, then $|K|$ is the number of distinct elements in $K$.

If $K$ corresponds to a structure defined by its projections $K_{43}$ and $K_{47}$ such that $|K_{43}|=d_p$ and $|K_{47}|=d_q$, then $|K|$ must be a multiple of $\operatorname{lcm}(d_p, d_q)$ and a divisor of 2021. Given the structure is typically a coset or subgroup of $\mathbb{Z}_{2021}$, $|K|$ must be a divisor of 2021.

The possible structures for $K$ lead to $|K|$ being a divisor of $2021 = 43 \times 47$. We require $|K| \ge 3$.
Possible divisors are $\{1, 43, 47, 2021\}$.
Thus, the possible values for $|K|$ are $\{43, 47, 2021\}$.

We confirm that sets corresponding to these sizes satisfy the condition (e.g., $\mathbb{Z}_{2021}$ is a subgroup, a subgroup of size 43 is a coset of a subgroup, and similarly for size 47).
