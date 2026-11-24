### [W2, round 1]
Investigating necessary conditions for P(k) being a multiple of n for all k > 0.
Let P(x) = sum_{i=0}^D a_i x^i, where D <= n, and a_i in {-1, 0, 1}.

1. Constraint from P(1):
P(1) = sum a_i. Since P(1) must be a multiple of n, we require:
sum_{i=0}^D a_i \equiv 0 \pmod{n}

Let N be the number of non-zero coefficients. Let N+ be the count of +1 coefficients and N- be the count of -1 coefficients. Then N = N+ + N-, and sum a_i = N+ - N-.
Thus, N+ - N- must be a multiple of n.

2. Constraint from P(2):
P(2) = sum a_i 2^i. Since P(2) must be a multiple of n, we require:
sum_{i=0}^D a_i 2^i \equiv 0 \pmod{n}

These two conditions (P(1) and P(2)) provide the initial structural constraints on the coefficients modulo n. Further investigation must use the general condition P(k) = 0 mod n for all k.

### [W2, round 1]
REPORT on task "Use the condition P(k) is a multiple of n for all positive integers k to derive necessary conditions on the coefficients $a_i$ of P. Specifically, investigate how the structure of P modulo n constrain": I used the condition that P(k) is a multiple of n for all positive integers k to derive necessary conditions on the coefficients $a_i$. Specifically, checking P(1) yields the constraint that the sum of coefficients must be a multiple of n ($\sum a_i \equiv 0 \pmod{n}$). Checking P(2) provides a second constraint: $\sum a_i 2^i \equiv 0 \pmod{n}$. I have documented these structural requirements in notes.md.
Candidate answer: Not applicable for this task phase.

### [W1, round 1]
## Task Results: Testing small n (n=2, 3, 4)

**Case n=2:**
We require $P(k) \equiv 0 \pmod{2}$ for all $k \ge 1$.
The minimum number of non-zero coefficients found is $N_{nz}=2$.
A suitable polynomial is $P(x) = x^2 + x$.
Check: $P(k) = k(k+1)$, which is always even.

**Case n=3:**
We require $P(k) \equiv 0 \pmod{3}$ for all $k \ge 1$.
The minimum number of non-zero coefficients found is $N_{nz}=2$.
A suitable polynomial is $P(x) = x^3 - x$.
Check: $P(k) = k(k^2 - 1) = (k-1)k(k+1)$, which is the product of three consecutive integers, hence always divisible by 3.

**Case n=4:**
We require $P(k) \equiv 0 \pmod{4}$ for all $k \ge 1$.
The minimum number of non-zero coefficients found is $N_{nz}=2$.
A suitable polynomial is $P(x) = x^4 - x^2$.
Check: $P(k) = k^2(k^2 - 1)$. If $k$ is even, $k^2 \equiv 0 \pmod{4}$. If $k$ is odd, $k^2-1 = (k-1)(k+1)$, where both $k-1$ and $k+1$ are consecutive even numbers, so $(k-1)(k+1)$ is divisible by $4$. Thus $P(k) \equiv 0 \pmod{4}$.

**Conclusion for small n:** For $n=2, 3, 4$, the minimum number of non-zero coefficients found is 2.

### [W3, round 1]
### [W3, round 1] Investigation of P(k) mod n structure

**Relationship to Polynomial Rings over $\mathbb{Z}_n$:**
The condition $P(k) \equiv 0 \pmod n$ for all positive integers $k$ implies that $P(x)$ belongs to the set of polynomials that vanish for all integers when reduced modulo $n$. When viewed in $\mathbb{Z}_n[x]$, $P(x)$ must satisfy $P(k) = 0$ for all $k \in \mathbb{Z}_n$. This means that $P(x)$ must be a polynomial whose roots cover all elements of $\mathbb{Z}_n$ (or is zero when restricted to $\mathbb{Z}_n$).

**Case: $n=p$ (Prime)**
Since $\mathbb{Z}_p$ is a field, the set of polynomials vanishing on all of $\mathbb{Z}_p$ is exactly the set of multiples of $x^p - x$ modulo $p$.
Thus, we must have $P(x) \equiv c(x^p - x) \pmod p$ for some constant $c \in \mathbb{Z}_p$.
Since $\deg(P) = n = p$, this implies $P(x)$ must take the form:
$P(x) = a_p x^p + a_1 x + (\text{terms divisible by } p)$
Since the coefficients $a_i$ are restricted to $\{-1, 0, 1\}$, we find:
1. $a_0$ must be $0 \pmod p$, so $a_0 = 0$.
2. $a_i$ must be $0 \pmod p$ for $1 < i < p$, so $a_i = 0$.
3. $a_p$ and $a_1$ must satisfy $a_p \equiv c \pmod p$ and $a_1 \equiv -c \pmod p$.
Choosing $c = a_p \in \{-1, 1\}$, we must have $a_1 = -a_p$.
Therefore, for prime $p$, $P(x)$ must be of the form $P(x) = a_p x^p - a_p x$, where $a_p \in \{-1, 1\}$.
This structure requires exactly 2 non-zero coefficients ($a_p$ and $-a_p$). The minimum possible number of non-zero coefficients when $n$ is prime is 2 (for $n \ge 2$).

### [W1, round 1]
REPORT on task "Test small values of n (n=2, 3, 4). For each n, find the minimum number of non-zero coefficients (N_nz) required for a polynomial P satisfying the conditions, and provide the polynomial(s) found. Reco": I tested the required small values of n (n=2, 3, and 4). For all three cases, the minimum number of non-zero coefficients found was $N_{nz}=2$. I found specific polynomials satisfying the condition for each n: $P(x) = x^2+x$ for $n=2$, $P(x) = x^3-x$ for $n=3$, and $P(x) = x^4-x^2$ for $n=4$. These results have been recorded in notes.md.
Candidate answer: N/A (Task completion only)

### [W3, round 1]
REPORT on task "Investigate how the property $P(k) \equiv 0 \pmod n$ for all $k$ relates to properties of polynomial rings over $\mathbb{Z}_n$. If $n$ is prime, how does this simplify the necessary structure of P?": I investigated the condition $P(k) \equiv 0 \pmod n$ for all integers $k$. This requires $P(x)$ to vanish on all elements of $\mathbb{Z}_n$. For prime $n=p$, the structure is constrained by $P(x) \equiv c(x^p - x) \pmod p$. Given the coefficient constraints ($a_i \in \{-1, 0, 1\}$), this forces $P(x)$ to be of the form $P(x) = a_p x^p - a_p x$, which has exactly 2 non-zero coefficients. This sets the minimum number of non-zero coefficients to 2 when $n$ is prime.
Candidate answer: ""

### [W3, round 2]
### [W3, round 2] Proofs and Narrowing Down

**1. Proof that $N_{nz} \ge 2$ for $n>1$:**
Let $P(x) = \sum_{i=0}^n a_i x^i$ be the polynomial with $a_i \in \{-1, 0, 1\}$. Let $N_{nz}$ be the number of non-zero coefficients. We are given that $P(k) \equiv 0 \pmod n$ for all $k \ge 1$.
If $N_{nz}=1$, then $P(x) = a_j x^j$ for some $0 \le j \le n$, where $a_j \in \{-1, 1\}$.
We evaluate $P(1)$:
$P(1) = a_j (1)^j = a_j$.
Since $P(1)$ must be a multiple of $n$, we require $a_j \equiv 0 \pmod n$.
However, since $a_j$ is either $1$ or $-1$, and $n>1$, $a_j$ cannot be a multiple of $n$.
This is a contradiction. Therefore, the minimum number of non-zero coefficients must be $N_{nz} \ge 2$.

**2. Narrowing Down the General Case:**
*   **Prime $n=p$:** The findings (documented in [W3, round 1]) show that $P(x)$ must be of the form $a_p x^p - a_p x$, which requires exactly $N_{nz}=2$. This establishes that $N_{nz}=2$ is achievable when $n$ is prime.
*   **General $n$:** Since $N_{nz} \ge 2$, and we know $N_{nz}=2$ is possible for prime $n$ and for small composite $n$ (e.g., $n=4$, where $P(x) = x^4 - x^2$ yields $N_{nz}=2$), the minimum possible value is at least 2.
The combined result suggests that the challenge lies in determining if $N_{nz}=2$ is possible for *all* composite $n$, or if certain composite $n$ force a higher minimum $N_{nz} > 2$. The necessary constraint is that $P(x) = a_j x^j + a_i x^i$ must vanish modulo $n$ for all integers $k$.

### [W3, round 2]
REPORT on task "Prove that the minimum number of non-zero coefficients $N_{nz}$ must be greater than or equal to 2 for any $n>1$. Use this result, combined with the findings for prime $n$, to narrow down the possibil": I proved that the minimum number of non-zero coefficients, $N_{nz}$, must be greater than or equal to 2 by examining the constraint $P(1) \equiv 0 \pmod n$. If $N_{nz}=1$, the single coefficient must be divisible by $n$, which is impossible for $n>1$. Combining this with the finding for prime $n$, where $N_{nz}=2$ is achieved by $P(x) = a_n x^n - a_n x$, we narrow down the minimum possibility to 2. The focus for the general case is now determining if $N_{nz}=2$ holds for all composite $n$.
Candidate answer: 2

### [W1, round 2]
### [W1, round 2]
## Task Results: Testing n=6 with P(x) = x^6 ± x^m

The task required testing polynomials of the form $P(x) = x^6 \pm x^m$ ($m < 6$, two non-zero coefficients) to see if $P(k) \equiv 0 \pmod 6$ for all positive integers $k$.

1. **Case $P(x) = x^6 + x^m$:** Theoretical analysis showed that for $k=1$, $P(1) = 1+1 = 2$. Since $2 \not\equiv 0 \pmod 3$, no polynomial of this form satisfies the condition for $n=6$.

2. **Case $P(x) = x^6 - x^m$:**
    *   **$m=1$:** Numerical checks (and theoretical analysis) confirmed $P(2) = 2^6 - 2^1 = 62$. Since $62 \equiv 2 \pmod 6$, this case fails.
    *   **$m=2$:** $P(x) = x^6 - x^2$. Numerical testing confirms $P(k) \equiv 0 \pmod 6$ for $k=1$ to $k=10$. This form is a solution.
    *   **$m=4$:** $P(x) = x^6 - x^4$. Numerical testing confirms $P(k) \equiv 0 \pmod 6$ for $k=1$ to $k=10$. This form is also a solution.

**Conclusion:** Polynomials of the form $P(x) = x^6 - x^m$ where $m=2$ or $m=4$ satisfy the required condition $P(k) \equiv 0 \pmod 6$ for all positive integers $k$.

### [W1, round 2]
REPORT on task "Test the case n=6. Check if a polynomial of degree 6 with exactly two non-zero coefficients, specifically of the form P(x) = x^6 $\pm$ x^m (for m < 6), satisfies P(k) $\equiv 0 \pmod 6$ for all positi": I tested the specified case $n=6$ for polynomials of the form $P(x) = x^6 \pm x^m$. Theoretical analysis showed that the positive form $x^6 + x^m$ fails modulo 3. For the negative form $x^6 - x^m$, I found that $m$ must be even. Numerical checks confirmed that $P(x) = x^6 - x^2$ and $P(x) = x^6 - x^4$ both satisfy $P(k) \equiv 0 \pmod 6$ for tested values of $k$, indicating they are valid solutions for this test case.
Candidate answer: Yes, polynomials of the form $P(x) = x^6 - x^m$ where $m=2$ or $m=4$ satisfy the condition $P(k) \equiv 0 \pmod 6$ for all positive integers $k$. For example, $P(x) = x^6 - x^2$.

### [W2, round 2]
## Task Completion: Conditions for P(x) = x^n +/- x^m

We investigated the conditions on $n$ and $m$ such that $P(k) \equiv 0 \pmod n$ for all integers $k$, for polynomials of the form $P(x) = x^n \pm x^m$.

**1. Case $P(x) = x^n + x^m$:**
The condition $P(1) \equiv 0 \pmod n$ forces $n=2$. The necessary and sufficient condition is $n=2$ and $m=1$.
$P(x) = x^2 + x$.

**2. Case $P(x) = x^n - x^m$:**
The condition $k^n \equiv k^m \pmod n$ for all $k$ is equivalent to two number-theoretic constraints:
a. $m \ge \max \{e \mid p^e \text{ exactly divides } n \}$.
b. $n \equiv m \pmod{\lambda(n)}$, where $\lambda(n)$ is the Carmichael function.
These conditions are necessary and sufficient. This structure allows $N_{nz}=2$ to be achieved for many $n$, including all primes and certain composite numbers (e.g., $n=4, 6$).

### [W2, round 2]
REPORT on task "Investigate the structure of polynomials with $N_{nz}=2$ coefficients of the form $P(x) = x^n - x^m$ (or $P(x) = x^n + x^m$). Determine the necessary and sufficient conditions on $n$ and $m$ such that": I investigated the structural requirements for $P(x) = x^n \pm x^m$ to satisfy $P(k) \equiv 0 \pmod n$ for all integers $k$. For $P(x) = x^n + x^m$, the constraints imply $n=2$ and $m=1$. For $P(x) = x^n - x^m$, the necessary and sufficient conditions are that $m$ must be greater than or equal to the largest prime exponent dividing $n$, and $n$ and $m$ must be congruent modulo the Carmichael function $\lambda(n)$.
Candidate answer: See derived conditions for $P(x) = x^n \pm x^m$.
