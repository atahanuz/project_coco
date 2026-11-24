### [W3, round 1]
Analysis for M=2, P(x) = c1 x^a + c2 x^b with a > b >= 0.
Constraint 1: We showed that for P(k) to be divisible by n for all k, we must have b >= 1, otherwise P(n) = c1 n^a + c2 would imply c2 is divisible by n, which is impossible since c2 = +/- 1 and n > 1. Thus, a > b >= 1.

Constraint 2: Testing k=1, P(1) = c1 + c2 must be divisible by n. Since c1, c2 = +/- 1, c1+c2 is in {-2, 0, 2}. For n=3 or n=5, the only possibility is c1 + c2 = 0, meaning c1 = -c2.
We examine P(x) = x^a - x^b. We require k^a - k^b = k^b (k^{a-b} - 1) \equiv 0 \pmod n$ for all k.

Case n=3:
We need k^(a-b) = 1 mod 3 for k not divisible by 3. This requires a-b to be even.
Example found: P(x) = x^3 - x (a=3, b=1, a-b=2). This satisfies the condition.

Case n=5:
We need k^(a-b) = 1 mod 5 for k not divisible by 5. This requires a-b to be a multiple of phi(5) = 4.
Example found: P(x) = x^5 - x (a=5, b=1, a-b=4). This satisfies the condition.

Conclusion for M=2: Solutions exist for n=3 and n=5.

### [W1, round 1]
Results for small n:

n=2: Minimum number of non-zero coefficients M = 2.
Polynomial example: P(x) = x^2 + x.
Verification: P(k) = k(k+1), which is always even, so P(k) is a multiple of 2 for all k. M=1 is impossible.

n=3: Minimum number of non-zero coefficients M = 2.
Polynomial example: P(x) = x^3 - x.
Verification: P(k) = k(k-1)(k+1), which is a product of three consecutive integers, so P(k) is always a multiple of 3 for all k. M=1 is impossible.

n=4: Minimum number of non-zero coefficients M = 2.
Polynomial example: P(x) = x^4 - x^2.
Verification: P(k) = k^2(k^2-1). If k is even, P(k) is divisible by 4. If k is odd, k-1 and k+1 are consecutive even numbers, so (k-1)(k+1) is divisible by 8, and thus by 4. M=1 is impossible.

### [W3, round 1]
REPORT on task "Focus on minimizing M. Start by assuming M=2, i.e., P(x) = ± x^a ± x^b. Find all pairs (a, b) and corresponding signs that satisfy P(k) = 0 (mod n) for a small prime n (e.g., n=3, 5).": I focused on the case M=2, where $P(x) = \pm x^a \pm x^b$. By testing small primes $n=3$ and $n=5$, I derived necessary conditions: the coefficients must be opposite signs ($c_1=-c_2$), and the exponent difference $a-b$ must be a multiple of $\phi(n)$ when $n$ is prime. For $n=3$, $a-b$ must be even, and for $n=5$, $a-b$ must be a multiple of 4. Examples like $P(x)=x^3-x$ and $P(x)=x^5-x$ satisfy the condition.
Candidate answer: M=2 is possible for $n=3$ (e.g., $P(x)=x^3-x$) and $n=5$ (e.g., $P(x)=x^5-x$).

### [W1, round 1]
REPORT on task "Test small values of n (n=2, 3, 4). For each n, find the minimum number of non-zero coefficients M such that P(k) is a multiple of n for all k. Record the polynomial and M.": I tested the problem for $n=2, 3,$ and $4$. For all three cases, the minimum possible number of non-zero coefficients found was $M=2$. I showed that $M=1$ is impossible in each case. For $n=2$, $P(x)=x^2+x$; for $n=3$, $P(x)=x^3-x$; and for $n=4$, $P(x)=x^4-x^2$ satisfy the conditions. These findings have been recorded in notes.md.
Candidate answer: n=2: M=2, P(x)=x^2+x; n=3: M=2, P(x)=x^3-x; n=4: M=2, P(x)=x^4-x^2

### [W2, round 1]
Analysis of $P(k) \equiv 0 \pmod{n}$ for all $k \in \mathbb{Z}^+$:
This condition implies that the polynomial $\bar{P}(x)$ over $\mathbb{Z}_n$ evaluates to zero for all $x \in \mathbb{Z}_n$.

1. Minimum number of coefficients: Since $n>1$ and all non-zero coefficients $a_i$ satisfy $|a_i|=1$, if $P(x)$ had only one non-zero coefficient, say $a_n$, then $P(1) = a_n$. For $P(1) \equiv 0 \pmod{n}$, we must have $n$ dividing $a_n$. Since $|a_n|=1$ and $n>1$, this is impossible. Therefore, $P(x)$ must have at least two non-zero coefficients.

2. Investigation for prime $n=p$:
If $n=p$ is prime, we rely on Fermat's Little Theorem, $x^p \equiv x \pmod{p}$ for all $x \in \mathbb{Z}_p$.
Consider $P(x) = x^p - x$. This polynomial has degree $p=n$. Its coefficients are $a_p=1$, $a_1=-1$, and all others are 0. The number of non-zero coefficients is 2.
Since $P(x) \equiv 0 \pmod{p}$ for all $x \in \mathbb{Z}_p$, this satisfies the condition. Thus, for prime $n$, the minimum is 2.

3. Investigation for composite $n=4$:
For $n=4$, we analyzed the constraints on $P(x) = a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0$. We found that $a_0=0, a_1=0, a_3=0$, and $a_2 = -a_4$ with $a_4 \ne 0$. Choosing $a_4=1, a_2=-1$, we get $P(x) = x^4 - x^2$. This polynomial has degree 4 and 2 non-zero coefficients, and it satisfies $P(k) \equiv 0 \pmod{4}$ for all $k$. Thus, for $n=4$, the minimum is 2.

Conclusion: Since 2 is the lowest possible number of non-zero coefficients (as shown by $P(1)$), and we found constructions achieving 2 for both prime and composite $n>1$, the minimum possible number is 2.

### [W2, round 1]
REPORT on task "Analyze the condition P(k) = 0 (mod n) for all k in Z+. Investigate what this implies about P(x) when considered as a polynomial over Z_n. Are there known constraints on polynomials with coefficients ": I analyzed the condition $P(k) \equiv 0 \pmod{n}$ for all positive integers $k$. This implies that $P(x)$ must evaluate to zero for all $x$ in the ring $\mathbb{Z}_n$. I first established that $P(x)$ must have at least two non-zero coefficients because $P(1)$ must be divisible by $n$, and this is impossible if only one coefficient is non-zero. For prime $n=p$, the polynomial $P(x) = x^p - x$ satisfies the condition and has exactly two non-zero coefficients. For composite $n$, testing $n=4$ showed that $P(x) = x^4 - x^2$ is a solution with only two non-zero coefficients. Since 2 is the minimum possible count and we found constructive examples for multiple $n>1$, the minimum possible number of non-zero coefficients is 2.
Candidate answer: 2

### [W4, round 1]
REPORT on task "Investigate the consequences of P(k) being divisible by n, specifically looking at the structure of n. If P(x) is related to a cyclotomic polynomial, what restrictions does that place on the coefficie": I investigated the constraints imposed by $P(k) \equiv 0 \pmod n$ for all positive integers $k$. First, I showed that the minimum number of non-zero coefficients must be at least 2, as a single monomial polynomial $P(x)=a_n x^n$ would require $n$ to divide $a_n$, which is impossible for $n>1$ and $|a_n|=1$. For small values of $n$ (2, 3, 4), I found polynomials achieving this minimum of 2 coefficients. Specifically, for prime $n$, $P(x)=x^n-x$ satisfies the condition, while for $n=4$, $P(x)=x^4-x^2$ works. These results strongly suggest that the minimum possible number is 2.
Candidate answer: 2

### [CHECKER, round 1]
Independent check of the new candidate answers (the checker saw only the problem and the answers, not who proposed them and not these notes):
- `2`: CONFIRMED: The minimum number of non-zero coefficients must be at least 2 since $n>1$. Numerical tests confirm that $M=2$ is achievable for $n=2, 3, 4, 5$ using polynomials like $x^2+x$ and $x^3-x$, supporting the claim that $M=2$ is the overall minimum.
- `n=2: M=2, P(x)=x^2+x; n=3: M=2, P(x)=x^3-x; n=4: M=2, P(x)=x^4-x^2`: CONFIRMED: The specific examples provided in Candidate B ($n=2, 3, 4$) were numerically verified using Python, confirming that $M=2$ is achievable in these cases.
- `M=2 is possible for $n=3$ (e.g., $P(x)=x^3-x$) and $n=5$ (e.g., $P(x)=x^5-x$).`: CONFIRMED: The specific examples provided in Candidate C ($n=3$ and $n=5$) were numerically verified using Python, confirming that $M=2$ is achievable in these cases.
