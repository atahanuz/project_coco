### [W4, round 1]
REPORT on task "Investigate the general property of polynomials P(x) such that P(k) \equiv 0 \pmod{n}. Use the property that P(x) must be a linear combination of \binom{x}{i}. Compare the coefficients of \sum c_i \bi": I investigated the conditions for $P(k) \equiv 0 \pmod{n}$ and showed that for any $n > 1$, there exists a polynomial of the form $P(x) = x^n - x^m$ for some $1 \le m < n$ that satisfies the required properties. Such a polynomial has exactly two non-zero coefficients (1 and -1). Since a polynomial with only one non-zero coefficient $a_n x^n$ would require $a_n \equiv 0 \pmod{n}$, which is impossible for $a_n \in \{1, -1\}$ and $n > 1$, the minimum number of non-zero coefficients is 2.
Candidate answer: 2

### [W2, round 1]
REPORT on task "Analyze the condition k^n \equiv k^m \pmod{n} for all k. Specifically, check if such m exists for all n. If not, find the smallest n where it fails and explore if 3 coefficients can satisfy the condit": I analyzed the condition $P(k) \equiv 0 \pmod{n}$ for all $k$. For $P(x)$ to have only 2 non-zero coefficients, it must be of the form $P(x) = a_n x^n + a_m x^m$ with $a_n, a_m \in \{1, -1\}$. This implies $a_n + a_m \equiv 0 \pmod{n}$, which for $n > 1$ forces $a_m = -a_n$, so $P(x) = a_n(x^n - x^m)$. The condition $k^n \equiv k^m \pmod{n}$ holds if $m \ge E$ and $L \mid (n-m)$, where $E$ is the maximum exponent in the prime factorization of $n$ and $L$ is the least common multiple of the $\phi(p^e)$ for all $p^e || n$. I verified that $L \le n-E$ for all $n > 1$, which ensures the existence of such an $m \in \{E, \dots, n-1\}$. Therefore, for every $n > 1$, there exists a polynomial with exactly 2 non-zero coefficients, and since 1 is impossible, the minimum number is 2.
Candidate answer: 2

### [W3, round 1]
For n=p^k, we found that P(x) = x^n - x^b works where b satisfies b >= k and b \equiv n (mod \lambda(p^k)).
For n=4 (2^2), \lambda(4)=2, b >= 2, b \equiv 0 (mod 2) => b=2, P(x) = x^4 - x^2.
For n=8 (2^3), \lambda(8)=2, b >= 3, b \equiv 0 (mod 2) => b=4, P(x) = x^8 - x^4.
For n=9 (3^2), \lambda(9)=6, b >= 2, b \equiv 0 (mod 6) => b=3 (since 9 \equiv 3 (mod 6)), P(x) = x^9 - x^3.
For n=16 (2^4), \lambda(16)=4, b >= 4, b \equiv 0 (mod 4) => b=4, P(x) = x^16 - x^4.
In all cases, a polynomial with 2 coefficients exists.
Since a polynomial with 1 coefficient \pm x^n gives P(1) = \pm 1, which is not a multiple of n for n > 1, the minimum number of non-zero coefficients is 2.
The construction P(x) = x^n - x^b works for any n > 1 if there exists b \in \{1, \dots, n-1\} such that b \ge \max(a_i) and b \equiv n (mod \lambda(n)).
Such a b always exists because \lambda(n) < n for n > 2, and for n=2, b=1 works.

### [W3, round 1]
REPORT on task "Explore the case where n is a prime power. For n=p^k, does a polynomial with only two non-zero coefficients always exist? Test specifically for n=4, 8, 9, 16.": I explored the condition $P(k) \equiv 0 \pmod n$ for all $k$ where $P$ is a polynomial of degree $n > 1$ with non-zero coefficients in $\{1, -1\}$. I tested small prime powers $n = 4, 8, 9, 16$ and found that polynomials with exactly 2 non-zero coefficients (of the form $P(x) = x^n - x^b$) satisfy the condition. Specifically, $b$ must satisfy $b \ge \max(a_i)$ and $b \equiv n \pmod{\lambda(n)}$, where $n = \prod p_i^{a_i}$ and $\lambda$ is the Carmichael function. For any $n > 1$, such a $b$ in the range $1 \le b < n$ exists. Since a polynomial with only 1 non-zero coefficient $\pm x^n$ cannot satisfy $P(1) \equiv 0 \pmod n$ for $n > 1$, the minimum number of non-zero coefficients is 2.
Candidate answer: 2

### [W1, round 1]
REPORT on task "For each n from 2 to 100, find if there exists a polynomial P(x) = a_n x^n + a_m x^m with a_n, a_m \in {1, -1} and 0 \le m < n such that P(k) \equiv 0 \pmod{n} for all k \in {1, \dots, n}. Record the ": I have analyzed the problem and checked the existence of a polynomial P(x) with 2 non-zero coefficients for n from 2 to 100. My script confirmed that for every n in this range, there exists a polynomial P(x) = x^n - x^m with m = n - lcm(phi(p_i^e_i)) such that P(k) is a multiple of n for all k. Since a polynomial with only 1 non-zero coefficient would require a_n = \pm 1 to be a multiple of n, which is impossible for n > 1, the minimum number of non-zero coefficients is 2 for all n > 1. Thus, the answer is 2.
Candidate answer: 2
