### [W2, round 1]
ANALYSIS OF PRIME FACTORS MODULO P:
The problem requires that for any $k$ coprime to $n$, $k^2 \equiv 1 \pmod n$.
Let $p$ be an odd prime dividing $n$. The condition implies that for any $k$ such that $p \nmid k$, we must have $k^2 \equiv 1 \pmod p$.
This congruence holds if and only if $k \equiv 1 \pmod p$ or $k \equiv -1 \equiv p-1 \pmod p$.
For this to hold for *all* non-zero residues $k \pmod p$, the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^*$ must have only two elements (1 and $p-1$).
The order of this group is $p-1$. We require $p-1 = 2$, which forces $p=3$.
Therefore, if $n$ has any odd prime factor, that factor must be 3.

### [W3, round 1]
### [W3, round 1] Analysis of $(\mathbb{Z}/n\mathbb{Z})^\times$ structure

The condition that $k^2 \equiv 1 \pmod n$ for all $k \in (\mathbb{Z}/n\mathbb{Z})^\times$ means that the group $(\mathbb{Z}/n\mathbb{Z})^\times$ must be an elementary abelian 2-group (every element has order dividing 2).

Using the Chinese Remainder Theorem (CRT), if $n = p_1^{e_1} p_2^{e_2} \cdots p_r^{e_r}$, then
$(\mathbb{Z}/n\mathbb{Z})^\times \cong (\mathbb{Z}/p_1^{e_1}\mathbb{Z})^\times \times \cdots \times (\mathbb{Z}/p_r^{e_r}\mathbb{Z})^\times$.
For the overall group to be an elementary abelian 2-group, every factor $(\mathbb{Z}/p_i^{e_i}\mathbb{Z})^\times$ must also be an elementary abelian 2-group.

1. Odd prime powers $p^e$ ($p > 2$):
As noted in the current files, $(\mathbb{Z}/p^e\mathbb{Z})^\times$ is cyclic of order $\phi(p^e) = p^{e-1}(p-1)$. For it to be an elementary abelian 2-group (which must be $C_2$ since it is cyclic), we require $\phi(p^e) = 2$. This only holds when $p=3$ and $e=1$.
Thus, the only allowed odd prime power factor is $3$.

2. Powers of 2 ($2^e$):
We examine $(\mathbb{Z}/2^e\mathbb{Z})^\times$:
- $e=1$: $n=2$. $(\mathbb{Z}/2\mathbb{Z})^\times \cong \{1\}$. Elementary abelian 2-group. Allowed.
- $e=2$: $n=4$. $(\mathbb{Z}/4\mathbb{Z})^\times \cong C_2$. Elementary abelian 2-group. Allowed.
- $e=3$: $n=8$. $(\mathbb{Z}/8\mathbb{Z})^\times \cong C_2 \times C_2$. Elementary abelian 2-group. Allowed.
- $e \ge 4$: $(\mathbb{Z}/2^e\mathbb{Z})^\times \cong C_2 \times C_{2^{e-2}}$. Since $e \ge 4$, $e-2 \ge 2$, so $C_{2^{e-2}}$ has order at least 4. This group is not elementary abelian 2-group. Not allowed.

3. Combining factors (CRT):
Since the factors must be $3$ or one of $\{2, 4, 8\}$, $n$ must be of the form $3^a \cdot 2^b$, where $a \in \{0, 1\}$ and $b \in \{0, 1, 2, 3\}$. We must ensure $n \ge 2$.

Possible values for $n$:
- $a=0$: $n \in \{2, 4, 8\}$ (since $b \ge 1$)
- $a=1$: $n \in \{3, 6, 12, 24\}$ (since $b \ge 0$, and $b=0$ gives $n=3$).

The complete set of solutions is $n \in \{2, 3, 4, 6, 8, 12, 24\}$.

### [W1, round 1]
Test results for 2 <= n <= 20:
The solutions are n = 2, 3, 4, 6, 8, 12.
All solutions found are of the form $2^a 3^b$, meaning they are restricted to products involving only the small primes 2 and 3.

### [W4, round 1]
Investigating the case where n has two distinct odd prime factors, p and q.
We want to show that if n is divisible by pq, the required condition fails.
The condition requires that for all k coprime to n, k^2 = 1 (mod n). This means the exponent of the multiplicative group (Z/nZ)* must divide 2.

Let p and q be two distinct odd prime factors of n.
Since p and q are distinct odd primes, at least one of them must be greater than or equal to 5. Let us assume, without loss of generality, that q >= 5.

Since q >= 5, the multiplicative group (Z/qZ)* has order q-1 >= 4. Therefore, there exists an element b in (Z/qZ)* such that b^2 is not congruent to 1 modulo q.

We construct a counterexample k using the Chinese Remainder Theorem (CRT):
1. k = 1 (mod p)
2. k = b (mod q)

Since gcd(1, p) = 1 and gcd(b, q) = 1, k is coprime to pq, and thus coprime to n.

We check k^2 modulo pq:
1. k^2 = 1^2 = 1 (mod p)
2. k^2 = b^2 (mod q). By choice of b, b^2 != 1 (mod q).

Since k^2 is not congruent to 1 modulo q, it cannot be congruent to 1 modulo pq.
Therefore, k^2 != 1 (mod pq), and hence k^2 != 1 (mod n). This k is a counterexample.
This demonstrates that n cannot have two distinct odd prime factors.
