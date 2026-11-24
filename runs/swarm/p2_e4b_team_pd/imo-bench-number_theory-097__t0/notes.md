### [W2, round 1]
Calculated $N_3(k) = |\{(c, d) : c^3 - d^3 \equiv k \pmod{61}\}|$ for $k \in \{0, 1, \dots, 60\}$.
$N_3 = [181, 60, 45, 60, 72, 45, 45, 45, 60, 60, 72, 60, 72, 45, 72, 45, 45, 72, 45, 72, 60, 45, 45, 60, 60, 72, 72, 60, 60, 72, 72, 72, 72, 60, 60, 72, 72, 60, 60, 45, 45, 60, 72, 45, 72, 45, 45, 72, 45, 72, 60, 72, 60, 60, 45, 45, 45, 72, 60, 45, 60]$.
The sum of $N_3(k)$ is $61^2 = 3721$, which confirms the counting was done correctly over all pairs $(c, d)$.

### [W1, round 1]
Calculated $N_2(r) = |\{(a, b) : a^2 + b^2 \equiv r \pmod{61}\}|$ for $r \in \{0, 1, \dots, 60\}$, where $a, b \in \{1, \dots, 61\}$.
The distribution is as follows:
$N_2(0) = 121$.
$N_2(r) = 60$ for all $r \in \{1, 2, \dots, 60\}$.
Total number of solutions: $121 + 60 \times 60 = 3721 = 61^2$.

### [W4, round 1]
Investigation into $x_1^2 + x_2^2 + x_3^3 \equiv x_4^3 \pmod{61}$.
This problem falls under the study of the number of solutions to diagonal equations in finite fields, often analyzed using character sums.
Let $N$ be the number of solutions. We are looking for solutions to $f(a, b, c, d) \equiv 0 \pmod{61}$, where $f(a,b,c,d) = a^2 + b^2 + c^3 - d^3$.
The general expected number of solutions for a non-degenerate diagonal equation of this form modulo a prime $p$ is close to $p^3$.
More precisely, using Weil bounds or similar techniques for exponential sums, the number of solutions $N$ is typically given by:
$N = p^{k-1} + O(p^{(k-1)/2})$
where $k$ is the number of variables (here $k=4$).
Therefore, we expect $N \approx 61^{4-1} = 61^3$.
Specific formulas depend heavily on whether the exponents lead to multiplicative characters that are non-trivial. For sums involving mixed exponents like $\{2, 3\}$, the calculation often involves summing generalized Gauss sums over the characters associated with the respective exponents.

A precise general formula applicable here is highly complex, but the standard theoretical approach is to use the orthogonality of additive characters $\psi$:
$N = \frac{1}{61} \sum_{\xi \in \mathbb{Z}_{61}} \sum_{a, b, c, d} \psi(\xi(a^2 + b^2 + c^3 - d^3))$.
When $\xi=0$, the sum is $61^3$. The remaining terms involve sums of the form $\sum_x \psi(\xi x^k)$, which are generalized Gauss sums whose magnitudes are bounded, leading to the asymptotic result $N = 61^3 + E$, where $|E| = O(61^{3/2})$.

### [W3, round 1]
Brute force solution for $a^2+b^2+c^3-d^3 \equiv 0 \pmod{5}$ for $1 \le a,b,c,d \le 5$ yields a total count of 125 quadruples.

Pattern analysis:
1. Let $s = a^2 + b^2 \pmod{5}$. The distribution of $s$ is not uniform. The count $C(s)$ of $(a, b)$ pairs resulting in $s$ is: $C(0)=9, C(1)=4, C(2)=4, C(3)=4, C(4)=4$.
2. The condition simplifies to $s \equiv d^3 - c^3 \pmod{5}$.
3. Since $x \mapsto x^3 \pmod{5}$ is a permutation of the residues $\{0, 1, 2, 3, 4\}$, the residues of $c^3$ and $d^3$ are uniformly distributed. For any fixed $s$, the number of pairs $(c, d)$ such that $d^3 - c^3 \equiv s \pmod{5}$ is exactly 5.
4. The total count is $\sum_{s=0}^4 C(s) \cdot 5 = 5 \cdot (9+4+4+4+4) = 5 \cdot 25 = 125$.
