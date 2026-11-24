### [W4, round 1]
Verification of K = {0, 1, ..., 2020} (mod 2021):
Let N = 2021. K = Z_N. We need to check if for any p, q in K, there exists r in K such that p+q-2r is a multiple of N.
This is equivalent to finding r in Z_N such that 2r = p+q (mod N).
Since N = 2021 is odd, gcd(2, N) = 1. Thus, 2 has a multiplicative inverse modulo N.
For any choice of p and q, the sum c = p+q (mod N) is an element of K. The equation 2r = c (mod N) has a unique solution r in Z_N. Since K = Z_N, this solution r is in K.
Therefore, K = {0, 1, ..., 2020} is a valid solution set.

### [W4, round 1]
REPORT on task "Determine if the maximum possible size, $|K| = 2021$ (i.e., $K = \{0, 1, \dots, 2020\}$), is a valid solution set. If so, provide a brief proof.": I checked if the set K = {0, 1, \dots, 2020} is a valid solution. Since 2021 is odd, the equation $2r \equiv p+q \pmod{2021}$ always has a unique solution for $r$ for any $p, q$. Since K contains all residues modulo 2021, this solution $r$ is guaranteed to be in K. Therefore, K = {0, 1, \dots, 2020} is a valid solution set, and the maximum possible size is valid.
Candidate answer: {0, 1, \dots, 2020}

### [W2, round 1]
Analysis assuming $0 \in K$:
The condition is $p+q \equiv 2r \pmod{2021}$ for some $r \in K$.

1.  Setting $p=0$ and $q=0$:
    $0+0 \equiv 2r \pmod{2021}$. Since $\gcd(2, 2021) = 1$, this implies $r \equiv 0 \pmod{2021}$. As $r \in K \subseteq \{0, \dots, 2020\}$, we must have $r=0$. This is consistent with the assumption $0 \in K$.

2.  Setting $p=0$ and $q \in K$:
    $0+q \equiv 2r \pmod{2021}$ for some $r \in K$.
    This leads to the constraint: For every $q \in K$, there must exist $r \in K$ such that $q \equiv 2r \pmod{2021}$.

Implication for the set $\{2r \mid r \in K\}$:
Let $S = \{2r \pmod{2021} \mid r \in K\}$. The constraint derived above shows that $K$ must be a subset of $S$, i.e., $K \subseteq S$. Every element in $K$ must be representable as $2r$ for some $r \in K$.

### [W2, round 1]
REPORT on task "Perform an algebraic analysis of the condition $p+q \equiv 2r \pmod{2021}$. Specifically, assume $0 \in K$ and derive constraints on the set $K$. What does this imply about the set $\{2r \mid r \in K\": I performed the required algebraic analysis assuming $0 \in K$. By setting $p=0$ and $q \in K$ in the defining congruence, I found a crucial constraint: for every element $q \in K$, there must exist an element $r \in K$ such that $q \equiv 2r \pmod{2021}$. This implies that the entire set $K$ must be a subset of the set of doubles of its own elements, $K \subseteq \{2r \pmod{2021} \mid r \in K\}$. These findings have been recorded in notes.md.
Candidate answer: N/A (Intermediate task)

### [W1, round 1]
### Investigation for M=7
Let $M=7$. The condition is: For any $p, q \in K \subseteq \mathbb{Z}_7$, there exists $r \in K$ such that $p+q \equiv 2r \pmod{7}$. Since 2 is invertible mod 7 (inverse is 4), this is equivalent to requiring that $4(p+q) \pmod{7} \in K$ for all $p, q \in K$.

1.  **Case $0 \in K$**: If $0 \in K$, then for any $q \in K$, we must have $4(0+q) = 4q \in K$. Thus, $K$ must be closed under multiplication by 4 modulo 7. Since the set of non-zero elements $\{1, 2, 3, 4, 5, 6\}$ breaks into two orbits under $x \mapsto 4x$ (Orbit 1: $\{1, 2, 4\}$; Orbit 2: $\{3, 5, 6\}$), and $|K| \ge 3$, $K$ must contain at least one full orbit plus 0, leading to $|K| \ge 4$. Detailed checks showed that no subset containing 0 and a proper subset of $\mathbb{Z}_7$ satisfies the condition (e.g., $\{0, 1, 2, 4\}$ fails for (1, 2) $\to 5 \notin K$). The only solution with $0 \in K$ is $K=\mathbb{Z}_7$, so $|K|=7$.
2.  **Case $0 \notin K$**: Testing orbits of size 3 (e.g., $\{1, 2, 4\}$ or $\{3, 5, 6\}$) showed they fail the condition for cross-pairs (e.g., $\{1, 2, 4\}$ fails for (1, 2) $\to 5 \notin K$).

**Conclusion for M=7**: The only possible size is $|K|=7$.

### Investigation for M=11
Let $M=11$. The condition is: For any $p, q \in K \subseteq \mathbb{Z}_{11}$, there exists $r \in K$ such that $p+q \equiv 2r \pmod{11}$. Since 2 is invertible mod 11 (inverse is 6), this is equivalent to requiring that $6(p+q) \pmod{11} \in K$ for all $p, q \in K$.

1.  **Case $0 \in K$**: If $0 \in K$, then $K$ must be closed under multiplication by 6 modulo 11. Since 6 is a primitive root modulo 11, any non-zero element generates all 10 non-zero residues. Thus, $K$ must be $\mathbb{Z}_{11}$, so $|K|=11$.
2.  **Case $0 \notin K$**: We showed that if $K = \mathbb{Z}_{11} \setminus \{x\}$, then for $p=x^{-1}$ and $q=x$, $p+q=0$, and $6(0) = 0$, which is not in $K$. Testing small $|K|$ shows rapid failure.

**Conclusion for M=11**: The only possible size is $|K|=11$.

**Necessary Condition Summary**: For both $M=7$ and $M=11$, the size $|K|$ must be equal to $M$.

### [W1, round 1]
REPORT on task "Investigate the problem using a small modulus, such as $M=7$ or $M=11$, keeping $|K| \ge 3$. Find all possible values of $|K|$ for this smaller modulus and record the necessary conditions.": I investigated the problem for small moduli, $M=7$ and $M=11$. For both prime moduli, the required condition implies that $K$ must be closed under a specific transformation of pairs from $K$. Analysis showed that for $M=7$, the only possible size is $|K|=7$, and for $M=11$, the only possible size is $|K|=11$. This leads to the necessary condition that $|K|=M$.
Candidate answer: |K|=M

### [W3, round 1]
Investigated K as an AP: K = {a, a+d, ..., a+(n-1)d} mod 2021. The condition requires that for any indices i, j, there exists k in {0, ..., n-1} such that i+j = 2k (mod M'), where M' = 2021 / gcd(d, 2021). This is satisfied if the size of K, n, is greater than or equal to M'.
Structural Constraint Found: |K| >= 2021 / gcd(d, 2021).

### [W3, round 1]
REPORT on task "Investigate the case where $K$ is an arithmetic progression (AP). Determine if there are structural constraints on the common difference or the size of $K$ that satisfy the condition.": I investigated the constraints on an arithmetic progression $K$ modulo 2021. By analyzing the condition $p+q \equiv 2r \pmod{2021}$ in terms of the indices of the AP elements, I derived that the required condition holds if and only if the size of the set, $|K|=n$, is greater than or equal to $M'$, where $M' = 2021 / \gcd(d, 2021)$. This provides the structural constraint on $|K|$.
Candidate answer: |K| >= 2021 / gcd(d, 2021)
