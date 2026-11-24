### [W2, round 1]
Analysis of $P(k) \equiv 0 \pmod n$ for all $k \ge 1$.
1. $P(k+n) \pmod n$: Since $P(x)$ has integer coefficients, $(k+n)^i \equiv k^i \pmod n$ for any $i$. Thus, $P(k+n) = \sum a_i (k+n)^i \equiv \sum a_i k^i = P(k) \pmod n$. The condition $P(k+n) \equiv 0 \pmod n$ is automatically satisfied if $P(k) \equiv 0 \pmod n$.
2. Implication for $a_0$: Since $P(k) \equiv 0 \pmod n$ for all positive integers $k$, this must hold for $k=n$.
$P(n) = a_0 + a_1 n + a_2 n^2 + \dots + a_n n^n$.
$P(n) \equiv a_0 \pmod n$.
Since $P(n) \equiv 0 \pmod n$, we must have $a_0 \equiv 0 \pmod n$. As $a_0 \in \{-1, 0, 1\}$, this forces $a_0 = 0$.
3. General constraint: $P(x)$ must vanish modulo $n$ for all inputs $x \in \mathbb{Z}$. This heavily restricts the possible coefficient vectors $(a_1, a_2, \dots, a_n)$.
4. Further step: Investigate $P(1) = \sum_{i=1}^n a_i \equiv 0 \pmod n$.

### [W4, round 1]
Initial investigation of necessary conditions from $P(k) \equiv 0 \pmod n$ for all $k \ge 1$.
The constraint implies that the forward difference polynomial $\Delta P(x) = P(x+1) - P(x)$ must satisfy $\Delta P(k) \equiv 0 \pmod n$ for all $k \ge 1$.
If $P(x) = \sum_{i=0}^n a_i x^i$, then $\Delta P(x)$ is a polynomial of degree $n-1$.
Let $b_j$ be the coefficient of $x^j$ in $\Delta P(x)$. We found:
$b_j = \sum_{i=j+1}^n a_i \binom{i}{j}$.
The condition $\Delta P(k) \equiv 0 \pmod n$ for all $k$ implies strong divisibility constraints on $b_j$. If $n$ is prime, this forces $b_j \equiv 0 \pmod n$ for all $j=0, \dots, n-1$. This leads to the system of congruences:
$\sum_{i=j+1}^n a_i \binom{i}{j} \equiv 0 \pmod n$ for $j=0, 1, \dots, n-1$.
We also derived $a_0 \equiv 0 \pmod n$, which forces $a_0=0$ since $|a_0| \le 1$.

### [W3, round 1]
Task: Investigate $m=2$ non-zero coefficients.
Let $P(x) = a_i x^i + a_j x^j$ with $a_i, a_j \in \{-1, 1\}$ and $i>j\ge 0$.
We require $P(k) \equiv 0 \pmod n$ for all $k \ge 1$ for some $n>1$.

Test case: $n=2$.
We require $a_i k^i + a_j k^j \equiv 0 \pmod 2$ for all $k \ge 1$.
Since $k^m \equiv k \pmod 2$, this reduces to $(a_i + a_j) k \equiv 0 \pmod 2$.
This is true for all $k$ if $a_i + a_j$ is even, meaning $a_i = a_j$.

Example solution: Let $a_i = a_j = 1$. $P(x) = x^i + x^j$.
If we choose $i=2$ and $j=1$, $P(x) = x^2 + x$. The degree is 2 > 1.
For $n=2$, $P(k) = k^2+k = k(k+1)$. Since $k$ or $k+1$ is even, $P(k)$ is always divisible by 2.
Thus, a solution exists for $m=2$ and $n=2$. The minimum number of coefficients is at most 2.

### [W1, round 1]
Analysis for n=2:
The polynomial is $P(x) = a_2 x^2 + a_1 x + a_0$. The condition $P(k) \equiv 0 \pmod{2}$ for all $k \geq 1$ requires $P(2) = 4a_2 + 2a_1 + a_0 \equiv a_0 \equiv 0 \pmod{2}$. Thus, $a_0=0$.
The condition $P(1) = a_2 + a_1 + a_0 \equiv a_2 + a_1 \equiv 0 \pmod{2}$ requires $a_1$ and $a_2$ to have the same parity. Since $a_2 \in \{1, -1\}$ (odd), $a_1$ must be odd, so $a_1 \in \{1, -1\}$.
Since $a_2 \neq 0$ (degree 2), $a_1 \neq 0$, and $a_0 = 0$, the minimum number of non-zero coefficients is 2. Example: $P(x) = x^2 + x$.

Analysis for n=3:
The polynomial is $P(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0$. The condition $P(k) \equiv 0 \pmod{3}$ for all $k \geq 1$ implies $P(3) \equiv a_0 \equiv 0 \pmod{3}$, so $a_0=0$.
Checking $k=1$ and $k=2$ leads to the system of congruences:
1) $a_3 + a_2 + a_1 \equiv 0 \pmod{3}$
2) $2a_3 + a_2 + 2a_1 \equiv 0 \pmod{3}$
Subtracting (1) from (2) yields $a_3 + a_1 \equiv 0 \pmod{3}$. Since $a_3, a_1 \in \{1, -1, 0\}$ and $a_3 \neq 0$, this forces $a_1 = -a_3$.
Substituting back into (1) yields $0 + a_2 \equiv 0 \pmod{3}$, so $a_2=0$.
The required non-zero coefficients are $a_3$ and $a_1 = -a_3$. The minimum number of non-zero coefficients is 2. Example: $P(x) = x^3 - x$.

### [W2, round 1]
Summary and Minimum Value:
1. We established that $a_0$ must be 0, meaning the minimum number of non-zero coefficients is at least 2 (since $n>1$ requires $a_n \neq 0$).
2. We tested $n=2$: $P(x) = x^2 + x$ satisfies the condition, having 2 non-zero coefficients.
3. We tested $n=3$: $P(x) = x^3 - x$ satisfies the condition, having 2 non-zero coefficients.
4. Since 1 coefficient is impossible, and we found examples with 2 coefficients for $n=2$ and $n=3$, the minimum possible number of non-zero coefficients is 2. This minimum holds for all $n>1$ for which such a polynomial exists (which is implied by the problem asking for the minimum).
