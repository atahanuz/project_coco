### [W2, round 1]
Analysis assuming $0 \in K$ and $M=2021$. The condition is $p+q \equiv 2r \pmod{M}$ for some $r \in K$.

1. Setting $p=0$ and $q=0$: Since $0 \in K$, there must exist $r_0 \in K$ such that $0+0 \equiv 2r_0 \pmod{M}$. Thus, $2r_0 \equiv 0 \pmod{2021}$ for some $r_0 \in K$.

2. Setting $p=0$ and $q \in K$: For any $q \in K$, there must exist $r \in K$ such that $q+0 \equiv 2r \pmod{M}$. This implies that every element $q \in K$ must be congruent to $2r \pmod{M}$ for some $r \in K$.

3. Conclusion on $\{2r \mid r \in K\}$: Let $S = \{2r \pmod{M} \mid r \in K\}$. The analysis shows that $K \subseteq S$ (in terms of residues modulo $M$). Furthermore, there must be an element $r_0 \in K$ such that $2r_0 \equiv 0 \pmod{M}$.

### [W4, round 1]
Structural Implication of K+K \subseteq 2K in Z_M:
Let M = 2021. The condition K+K \subseteq 2K implies strong regularity on K.
Consider any two elements p, q in K. We have p+q = 2r for some r in K.
Subtracting 2q from both sides:
p - q = 2r - 2q = 2(r - q).
Since r, q are in K, this means that the difference between any two elements in K, p-q, must be twice an element (r-q) that is itself a difference of two elements in K.

If M is odd (which 2021 is), 2 is invertible mod M.
The property K+K \subseteq 2K is closely related to K being a coset of a subgroup H where 2H \subseteq H.
A known result (related to sum-free sets and density arguments) implies that K must be an arithmetic progression of a specific form, or highly structured. Specifically, for $M$ odd, this property strongly suggests K must be contained within a specific structure dictated by the prime factorization of M (2021 = 43 * 47). Further investigation is needed to pinpoint the exact structure, but the primary implication is that K must be highly arithmetic.

### [W3, round 1]
Analysis of $K$ as an arithmetic progression modulo $M$.
Let $K = \{a, a+d, \dots, a+(n-1)d\} \pmod{M}$.
The condition $\forall p, q \in K, \exists r \in K$ such that $p+q \equiv 2r \pmod{M}$ translates to:
For all $S \in \{0, 1, \dots, 2n-2\}$, the congruence $2k d \equiv S d \pmod{M}$ must have a solution $k \in \{0, 1, \dots, n-1\}$.

Let $g = \gcd(d, M)$ and $M' = M/g$. The congruence is equivalent to $2k \equiv S \pmod{M'}$.

1. If $M'$ is even, $2k \pmod{M'}$ only produces even residues. Since $S=1$ is in $\{0, 1, \dots, 2n-2\}$ (assuming $n \ge 2$), and $1$ is odd, the condition cannot be satisfied unless $n=1$. Since the original problem implies $|K| \ge 3$ (so $n \ge 3$), we must require $M'$ to be odd.

2. If $M'$ is odd, the mapping $k \mapsto 2k \pmod{M'}$ is a bijection on $\mathbb{Z}_{M'}$. We need the set of possible sums $S \in \{0, 1, \dots, 2n-2\}$ to be covered by the values $2k \pmod{M'}$ for $k \in \{0, 1, \dots, n-1\}$.
For $2k \pmod{M'}$ to cover all residues modulo $M'$, we need $n-1 \ge (M'-1)/2$, which implies $n \ge (M'+1)/2$. Since $M'$ is odd, this condition is necessary and sufficient for the set of $2k$'s to cover all of $\mathbb{Z}_{M'}$. Given that $S$ takes on all residues modulo $M'$ up to $\min(M'-1, 2n-2)$, if $n \ge (M'+1)/2$, then $2n-2 \ge M'-1$, so $S$ covers all residues modulo $M'$.

Necessary Conditions:
Let $g = \gcd(d, M)$. The necessary conditions on $n$ and $d$ are:
1. $M/g$ must be odd.
2. $n \ge (M/g + 1)/2$.

### [W1, round 1]
--- Analysis of the problem constraints for small moduli M ---

The condition is: For any $p, q \in K$, there exists $r \in K$ such that $p+q \equiv 2r \pmod{M}$.

Case M=5 (Prime, odd):
Since 2 is invertible modulo 5 (2^-1 = 3), the condition is equivalent to: For any $p, q \in K$, the average $a = 3(p+q) \pmod{5}$ must be in $K$.
If $K$ is closed under averaging in $\mathbb{Z}_5$, $K$ must be a subgroup, as 5 is prime. Since $|K| \ge 3$, we must have $K = \mathbb{Z}_5$, giving $|K|=5$.
We verified that $K=\{0, 1, 2, 3, 4\}$ works.
It is conjectured that no other size $|K| \ge 3$ is possible for M=5.

Case M=7 (Prime, odd):
Since 2 is invertible modulo 7 (2^-1 = 4), the condition is equivalent to: For any $p, q \in K$, the average $a = 4(p+q) \pmod{7}$ must be in $K$.
By similar reasoning as M=5, $K$ must be a subgroup of $\mathbb{Z}_7$. Since $|K| \ge 3$, we must have $K = \mathbb{Z}_7$, giving $|K|=7$.
We verified that $K=\{0, 1, 2, 3, 4, 5, 6\}$ works.
It is conjectured that no other size $|K| \ge 3$ is possible for M=7.

Observed Pattern (for prime M):
If M is a prime number, the only possible value for $|K| \ge 3$ appears to be $|K|=M$.

### [W4, round 2]
Synthesis of Structural Implications (W4):
The problem requires that $K \subseteq \{0, 1, \dots, 2020\}$, $|K| \ge 3$, and for any $p, q \in K$, there exists $r \in K$ such that $p+q \equiv 2r \pmod{2021}$.
Let $M=2021$. Since $M$ is odd, $2$ is invertible modulo $M$. The condition $K+K \subseteq 2K$ is equivalent to stating that $K$ is closed under averaging: for any $p, q \in K$, the element $\frac{p+q}{2} \pmod{M}$ must be in $K$.
A well-known result in additive combinatorics states that any subset $K \subseteq \mathbb{Z}_M$ that is closed under averaging (when $M$ is odd) must be a coset of a subgroup of $\mathbb{Z}_M$. That is, $K = a + H$ for some $a \in \mathbb{Z}_M$ and a subgroup $H \le \mathbb{Z}_M$.
The possible sizes of $K$ are therefore equal to the possible sizes of subgroups of $\mathbb{Z}_{2021}$.
Since $2021 = 43 \times 47$, the order of any subgroup must divide $2021$.
The divisors of 2021 are $\{1, 43, 47, 2021\}$.
Since $|K| \ge 3$, the possible values for $|K|$ are $43, 47, 2021$.
(Note: The case $K$ being an arithmetic progression is covered by $K$ being a coset of a subgroup, as subgroups are specific APs starting at 0).

### [W3, round 2]
### [W3, round 2] Investigation of proper sub-AP solutions

We investigate the necessary condition $n \ge (M'+1)/2$ derived for $K$ being an arithmetic progression (AP), where $M' = M/g$ and $M'$ is odd. The task is to determine if solutions exist where $n < M'$.

Let $K = \{a + kd \pmod{M} \mid k=0, \dots, n-1\}$. The core condition translates to ensuring that for every pair of indices $(k_1, k_2) \in \{0, \dots, n-1\}^2$, the sum $k_1+k_2$ must be congruent to $2k_3 \pmod{M'}$ for some $k_3 \in \{0, \dots, n-1\}$.

This requires the set of sums $\{0, 1, \dots, 2n-2\} \pmod{M'}$ to be contained within the set $\{2k_3 \pmod{M'} \mid k_3=0, \dots, n-1\}$.

If $n < M'$, then $2n-2 < 2M'-2$. Since $M'$ is odd, let $M'=2j+1$. The full set of residues is $\mathbb{Z}_{M'}$.
The set $\{2k_3 \pmod{M'}\}$ contains $n$ distinct residues.

For the condition to hold, we require $n$ to be large enough so that $n$ distinct values cover all residues $0, 1, \dots, 2n-2 \pmod{M'}$. This implies that the structure of the AP is too sparse to satisfy the closure property unless it spans the entire coset.

For a generic odd $M'$, the condition $n \ge (M'+1)/2$ is necessary but not sufficient for $n < M'$. Specifically, for $M' \ge 9$, if $n < M'$, there will exist a residue $S < 2n-1$ such that $S$ is odd, and $2k_3 \equiv S \pmod{M'}$ implies $k_3 \equiv 2^{-1}S \pmod{M'}$. If $S$ is chosen such that $2^{-1}S \pmod{M'}$ falls outside the range $\{0, 1, \dots, n-1\}$, the condition fails.

Conclusion for AP structure: The necessary condition $n \ge (M'+1)/2$ only leads to a valid solution when $n = M'$, i.e., the progression spans the full coset determined by $d$ (since $n$ cannot exceed $M'$).

Applying this to $M=2021$:
1. If $g=1$, $M'=2021$. Solution requires $n=2021$.
2. If $g=43$, $M'=47$. Solution requires $n=47$.
3. If $g=47$, $M'=43$. Solution requires $n=43$.

This strongly suggests that if $K$ is an AP, the only solutions are the ones that span the entire coset. This addresses the prompt's investigation.
