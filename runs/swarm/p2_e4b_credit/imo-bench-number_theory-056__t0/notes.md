### [W2, round 1]
Initial analysis of the condition $P(k) \equiv 0 \pmod n$ for all $k \in \mathbb{Z}^+$.
The condition must hold for $k=1, 2, \dots, n$. This implies that $P(x)$ must vanish for every element $x$ in the ring $\mathbb{Z}_n$.
If $P(x) \equiv 0 \pmod n$ for all $x \in \mathbb{Z}_n$, this means that $P(x)$ must be congruent to a polynomial that is identically zero when evaluated modulo $n$.
In $\mathbb{Z}_n[x]$, the set of polynomials that vanish everywhere is generally complex when $n$ is composite. However, if $n=p$ (prime), then $\mathbb{Z}_p$ is a field, and a polynomial of degree less than $p$ vanishing everywhere must be the zero polynomial. Since $\deg(P)=n=p$, $P(x)$ must be of the form $Q(x)(x^p - x) + R(x)$. Since $x^p - x \equiv 0 \pmod p$, $P(x)$ must be congruent to $0 \pmod p$ if we allow $Q(x)$ to have coefficients in $\mathbb{Z}_p$. This suggests a strong structural constraint on $P(x)$ related to $x^n - x$ or similar zero-vanishing polynomials in $\mathbb{Z}_n$.
The problem requires finding the minimum number of non-zero coefficients, which suggests we look for the simplest polynomial satisfying $P(x) \equiv 0 \pmod n$ for all $x \in \mathbb{Z}_n$ while having $\deg(P)=n$ and coefficients $\pm 1$ or $0$.

### [W4, round 1]
Initial analysis of the constraints:
1. $P(x)$ has coefficients $a_i \in \{0, 1, -1\}$ for non-zero terms, and $\deg(P) = n > 1$.
2. $P(k) \equiv 0 \pmod n$ for all $k \in \mathbb{Z}^+$.

A necessary condition derived from $k=n$:
$P(n) = \sum a_i n^i$. Since $a_i n^i \equiv 0 \pmod n$ for $i \ge 1$, we have $P(n) \equiv a_0 \pmod n$.
Since $P(n)$ must be a multiple of $n$, we require $a_0 \equiv 0 \pmod n$.
Since $a_0$ is either 0, 1, or -1, and $n>1$, this forces $a_0 = 0$.

General Necessary Conditions:
A. $a_0 = 0$.
B. For $k=1$, $P(1) = \sum_{i=1}^n a_i \equiv 0 \pmod n$.
C. For $k=n-1$, $P(n-1) \equiv P(-1) \pmod n$. Thus, $\sum_{i=1}^n a_i (-1)^i \equiv 0 \pmod n$.

Exploring the case $n=p$ (prime):
If $n=p$, the condition $P(k) \equiv 0 \pmod p$ for all $k \in \mathbb{Z}/p\mathbb{Z}$ strongly suggests $P(x)$ must be related to $x^p - x \pmod p$.
Consider $P(x) = x^p - x$.
1. Degree is $p>1$.
2. Coefficients are $a_p=1, a_1=-1$. All others are 0. They satisfy the $\pm 1$ constraint.
3. $P(k) = k^p - k$. By Fermat's Little Theorem, $k^p \equiv k \pmod p$, so $P(k) \equiv 0 \pmod p$.
This yields a solution with exactly 2 non-zero coefficients when $n$ is prime.

Hypothesis: If $n$ is prime, the minimum number of non-zero coefficients is 2.
The next step should be to investigate if this minimum holds when $n$ is composite.

### [W1, round 1]
Testing the problem for small degrees n:

n=2:
A polynomial P(x) = a2*x^2 + a1*x + a0 exists if and only if a0=0. The condition P(k) = 0 (mod 2) is satisfied for P(x) = a2*x^2 + a1*x where a2, a1 in {1, -1}. The minimum number of non-zero coefficients is 2.

n=3:
A polynomial P(x) = a3*x^3 + a2*x^2 + a1*x + a0 exists if and only if a0=0. The condition P(k) = 0 (mod 3) is satisfied for P(x) = x^3 - x. The minimum number of non-zero coefficients is 2.

n=4:
A polynomial P(x) = a4*x^4 + a3*x^3 + a2*x^2 + a1*x + a0 exists if and only if a0=0 and a1=0. The condition P(k) = 0 (mod 4) is satisfied for P(x) = x^4 - x^2. The minimum number of non-zero coefficients is 2.

### [W4, round 1]
Further investigation into the composite case ($n=4$):
We established necessary conditions $a_0=0$ and $a_1=0$ for $n=4$.
Solving the resulting system of linear congruences led to the solution $P(x) = x^2 - x^4$ (up to scaling by -1, which is allowed).
This polynomial has exactly 2 non-zero coefficients ($a_4=-1, a_2=1$).
We verified that $P(k) = k^2 - k^4$ is divisible by 4 for all $k \in \mathbb{Z}^+$.

Conclusion: The minimum number of non-zero coefficients is 2, as this value is achievable for $n=3$ (prime) and $n=4$ (composite).
