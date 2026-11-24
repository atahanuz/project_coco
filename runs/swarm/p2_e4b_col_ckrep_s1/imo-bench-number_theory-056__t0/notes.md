### [W2, round 1]
Investigation into P(k) \equiv 0 \pmod n for all k.
1. The condition P(k) \equiv 0 \pmod n for all k imposes a very strong constraint, meaning P(x) must effectively act as the zero function when evaluated at integers modulo n.

2. Case n=2 (Prime): We found that P(x) = x^2 - x satisfies the condition and has 2 non-zero coefficients.
3. Case n=3 (Prime): We found that P(x) = x^3 - x satisfies the condition and has 2 non-zero coefficients.

4. General Structural Implication (when n=p is prime):
If n=p is prime, then for P(x) to vanish for all x in Z/pZ, P(x) must be divisible by x^p - x modulo p. Since P is specified to have degree n=p, we can write P(x) \equiv c(x^p - x) \pmod p$. Since the coefficients of P are in {-1, 0, 1}, this strongly suggests that the minimal polynomial must be of the form P(x) = x^p - x (or possibly x^p + x), achieving the minimum of 2 non-zero coefficients.

5. Future work: Investigate composite n (e.g., n=4, n=6) to see if the minimum increases, and analyze the structural requirements for P(x) to vanish on Z/nZ when n is composite.

### [W1, round 1]
Results for small values of n:

Case n=2:
Degree $n=2$. $P(x) = a_2 x^2 + a_1 x + a_0$. $a_2 \in \{1, -1\}$.
Condition $P(k) \equiv 0 \pmod 2$ for all $k \ge 1$.
We found $a_0=0$ and $a_2 + a_1 \equiv 0 \pmod 2$.
Minimum number of non-zero coefficients found: 2.
Polynomials tested (Minimum 2 coefficients):
1. $P(x) = x^2 + x$. (2 non-zero coefficients)
2. $P(x) = x^2 - x$. (2 non-zero coefficients)
Verification: $P(k) = k(k\pm 1)$, which is always even for integer $k$.

Case n=3:
Degree $n=3$. $P(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0$. $a_3 \in \{1, -1\}$.
Condition $P(k) \equiv 0 \pmod 3$ for all $k \ge 1$.
We derived $a_0=0$, and either ($a_3=1, a_1=-1, a_2=0$) or ($a_3=-1, a_1=1, a_2=0$).
Minimum number of non-zero coefficients found: 2.
Polynomials tested (Minimum 2 coefficients):
1. $P(x) = x^3 - x$. (2 non-zero coefficients)
2. $P(x) = -x^3 + x$. (2 non-zero coefficients)
Verification: $P(k) = \pm (k^3 - k) = \pm (k-1)k(k+1)$, which is always divisible by 3.

### [W2, round 1]
REPORT on task "Investigate the structural implications of the condition P(k) \equiv 0 \pmod n for all positive integers k. Specifically, consider how this condition restricts the coefficients of P when viewed as a p": I investigated the structural constraints of P(k) \equiv 0 \pmod n$ for all positive integers k. By testing small prime values, n=2 and n=3, I found that the polynomial P(x) = x^n - x satisfies the condition and has only 2 non-zero coefficients. This suggests that when n is prime, P(x) must be structurally equivalent to x^n - x modulo n, leading to a minimal count of 2 non-zero coefficients. I have recorded these findings in the shared notes.
Candidate answer: Minimum is likely 2, achieved by P(x) = x^n - x for prime n. Further investigation is needed for composite n.

### [W1, round 1]
REPORT on task "Test small values of n, starting with n=2 and n=3. For a fixed n, assume P has degree n. Systematically find polynomials P whose non-zero coefficients are 1 or -1, satisfy the condition P(k) = 0 mod n": I systematically tested small values of n, specifically n=2 and n=3. For n=2, I determined that $a_0=0$ and found polynomials like $P(x) = x^2+x$ that satisfy the condition $P(k) \equiv 0 \pmod 2$, establishing a minimum of 2 non-zero coefficients. For n=3, the condition required $a_0=0$, leading to solutions such as $P(x) = x^3-x$. These polynomials satisfy $P(k) \equiv 0 \pmod 3$ for all $k$, confirming the minimum is 2.
Candidate answer: For n=2, the minimum number is 2 (e.g., $P(x) = x^2+x$). For n=3, the minimum number is 2 (e.g., $P(x) = x^3-x$).

### [CHECKER, round 1]
Independent check of the new candidate answers (the checker saw only the problem and the answers, not who proposed them and not these notes):
- `For n=2, the minimum number is 2 (e.g., $P(x) = x^2+x$). For n=3, the minimum number is 2 (e.g., $P(x) = x^3-x$).`: CONFIRMED: For n=2, P(x) = x^2+x satisfies all conditions and has 2 non-zero coefficients, proving the minimum is 2. For n=3, P(x) = x^3-x satisfies all conditions and has 2 non-zero coefficients, proving the minimum is 2.
- `Minimum is likely 2, achieved by P(x) = x^n - x for prime n. Further investigation is needed for composite n.`: CONFIRMED: For prime n, P(x) = x^n - x satisfies the condition P(k) is a multiple of n by Fermat's Little Theorem, and has 2 non-zero coefficients. For composite n=4, P(x) = x^4 - x^2 also satisfies the conditions and has 2 non-zero coefficients, supporting the general claim that the minimum is 2.
