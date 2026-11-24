### [W1, round 1]
Tested condition n | (k^2 - 1) for 2 <= n <= 20. The passing candidates are n = 2, 3, 4, 6, 8, and 12.

### [W2, round 1]
Analysis for prime numbers $p$: The condition requires that for all $k$ coprime to $p$, $k^2 \equiv 1 \pmod{p}$. This means every element $k$ in the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^*$ must satisfy $k^2 \equiv 1 \pmod{p}$, i.e., the order of every element must divide 2. Since $(\mathbb{Z}/p\mathbb{Z})^*$ is a cyclic group of order $p-1$, for all elements to have order dividing 2, the group order must be 1 or 2. This requires $p-1 \le 2$.
If $p-1=1$, $p=2$. Check: $(\mathbb{Z}/2\mathbb{Z})^* = \{1\}$. $1^2 \equiv 1 \pmod{2}$. Satisfied.
If $p-1=2$, $p=3$. Check: $(\mathbb{Z}/3\mathbb{Z})^* = \{1, 2\}$. $1^2 \equiv 1$, $2^2=4 \equiv 1 \pmod{3}$. Satisfied.
If $p-1>2$, the cyclic group $(\mathbb{Z}/p\mathbb{Z})^*$ contains an element of order greater than 2, violating the condition.
Therefore, the only prime numbers $p$ satisfying the condition are $p=2$ and $p=3$.

### [W3, round 1]
Investigation of $n=2^e$:
The problem requires that for all $k$ such that $\gcd(k, 2^e)=1$ (i.e., all odd $k$), we must have $k^2 \equiv 1 \pmod{2^e}$.

1.  $e=1$ ($n=2$): $k$ is odd, $k^2 \equiv 1 \pmod{2}$. Works.
2.  $e=2$ ($n=4$): $k$ is odd, $k^2 \equiv 1 \pmod{4}$. Works.
3.  $e=3$ ($n=8$): $k$ is odd, $k^2 \equiv 1 \pmod{8}$. Works.
4.  $e=4$ ($n=16$): We test $k=3$. $\gcd(3, 16)=1$. $3^2 - 1 = 8$. Since $16 \nmid 8$, $n=16$ fails.
5.  $e \ge 4$: For any $e \ge 4$, we choose $k=3$. $k^2 - 1 = 8$. Since $2^e \ge 16$, $2^e$ cannot divide 8. Thus, $n=2^e$ fails for $e \ge 4$.

Conclusion: $n=2^e$ is a solution if and only if $e \in \{1, 2, 3\}$.

### [W1, round 2]
### [W1, round 2]
Task completion check:
1. Verification for n=24: For all k coprime to 24, k^2 === 1 (mod 24). This is confirmed (e.g., 5^2=25=1 mod 24).
2. Verification for n=18: There exists at least one k coprime to 18 such that k^2 !== 1 (mod 18). Specifically, for k=5, 5^2 = 25 === 7 (mod 18).
These two results are recorded.

### [W4, round 2]
### [W4, round 1] Formal Proof for $3^f, f \ge 2$
Let $n$ be a positive integer such that $3^f$ divides $n$ for some $f \ge 2$.
The condition requires that for all $k$ coprime to $n$, $k^2 \equiv 1 \pmod{n}$. If this holds, it must also hold modulo $3^f$: for all $k$ coprime to $3^f$, we must have $k^2 \equiv 1 \pmod{3^f}$.
The multiplicative group $(\mathbb{Z}/3^f\mathbb{Z})^*$ has order $\phi(3^f) = 3^f - 3^{f-1} = 2 \cdot 3^{f-1}$.
Since $f \ge 2$, $3^{f-1} \ge 3$, so $\phi(3^f) \ge 6$.
For the condition $k^2 \equiv 1 \pmod{3^f}$ to hold for all $k$, every element in the group $(\mathbb{Z}/3^f\mathbb{Z})^*$ must have an order that divides 2. This implies that the group must be an elementary abelian 2-group.
However, for $f \ge 2$, $(\mathbb{Z}/3^f\mathbb{Z})^*$ is a cyclic group of order $2 \cdot 3^{f-1}$. Since $2 \cdot 3^{f-1} > 2$ for $f \ge 2$, the group contains elements whose order is strictly greater than 2.
Therefore, there must exist at least one $k$ coprime to $3^f$ such that $k^2 \not\equiv 1 \pmod{3^f}$. This contradicts the required condition for $n$, proving that no such $n$ can be a solution if $3^2 | n$.

### [W3, round 2]
Final check: The condition implies that the exponent of $(\mathbb{Z}/n\mathbb{Z})^*$ must be 2. This limits $n$ to be of the form $2^e 3^f$. We found $e \in \{0, 1, 2, 3\}$ and $f \in \{0, 1\}$. This yields the solutions $n \in \{2, 4, 8, 3, 6, 12, 24\}$. $n=24$ was confirmed by CRT as $k^2 \equiv 1 \pmod{8}$ and $k^2 \equiv 1 \pmod{3}$.

### [W2, round 2]
### [W2, round 2] - Finalizing Solution
The problem requires that every element $k$ in the multiplicative group $(\mathbb{Z}/n\mathbb{Z})^*$ must have order dividing 2. This is equivalent to requiring that the Carmichael function $\lambda(n)$ divides 2, i.e., $\lambda(n) \in \{1, 2\}$.

1.  **Prime Factors:** If $p|n$, then $\lambda(p) | \lambda(n) \le 2$. This restricts prime factors to $p=2$ or $p=3$. Thus, $n$ must be of the form $2^a 3^b$.
2.  **Power of 3:** For $n=3^b$, $\lambda(3^b) = \phi(3^b) = 2 \cdot 3^{b-1}$. We require $2 \cdot 3^{b-1} \le 2$. This forces $b-1 \le 0$, so $b=1$. (Solutions: $n=3$).
3.  **Power of 2:** For $n=2^a$, we require $\lambda(2^a) \le 2$. This holds only for $a \in \{1, 2, 3\}$. (Solutions: $n=2, 4, 8$).
4.  **Mixed Case $n=2^a 3^b$:** We must have $b=1$. We require $\lambda(2^a 3) = \operatorname{lcm}(\lambda(2^a), \lambda(3)) = \operatorname{lcm}(\lambda(2^a), 2) \le 2$. This requires $\lambda(2^a)$ to divide 2. This yields $a \in \{1, 2, 3\}$.
    Candidates: $n = 2^1\cdot 3 = 6$, $n = 2^2\cdot 3 = 12$, $n = 2^3\cdot 3 = 24$.

The complete set of solutions is $\{2, 3, 4, 8, 6, 12, 24\}$.
