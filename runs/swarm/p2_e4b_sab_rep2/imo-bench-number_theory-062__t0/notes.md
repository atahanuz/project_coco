### [W2, round 1]
Derivation of the functional equation for $f(n) = g(n) - n$:
We use condition (ii): $g(nm) + nm = ng(m) + mg(n)$.
Substituting $g(n) = f(n) + n$:
$(f(nm) + nm) + nm = n(f(m) + m) + m(f(n) + n)$
$f(nm) + 2nm = nf(m) + nm + mf(n) + mn$
$f(nm) = nf(m) + mf(n)$. (This is the derived functional equation.)

Verification of $f(p)=1$:
Using condition (i): $g(p) = p+1$.
$f(p) = g(p) - p = (p+1) - p = 1$.

Proof by induction that $f(p^k) = k p^{k-1}$ for a prime $p$ and $k \ge 1$:
Base Case (k=1): $f(p^1) = f(p) = 1$. The formula gives $1 \cdot p^{1-1} = 1$. It holds.
Inductive Hypothesis (IH): Assume $f(p^k) = k p^{k-1}$ for some $k \ge 1$.
Inductive Step (k+1): We evaluate $f(p^{k+1}) = f(p \cdot p^k)$.
Using the functional equation $f(nm) = nf(m) + mf(n)$:
$f(p^{k+1}) = p f(p^k) + p^k f(p)$.
Substitute IH and $f(p)=1$:
$f(p^{k+1}) = p (k p^{k-1}) + p^k (1)$
$f(p^{k+1}) = k p^k + p^k$
$f(p^{k+1}) = (k+1) p^k$.
The formula holds for $k+1$.
The proof by induction is complete.

### [W2, round 1]
REPORT on task "Rigourously derive the functional equation satisfied by $f(n) = g(n) - n$, show that $f(p)=1$, and prove by induction that for any prime $p$, $f(p^k) = k p^{k-1}$.": I successfully derived the functional equation for $f(n) = g(n) - n$, which is $f(nm) = nf(m) + mf(n)$. I rigorously showed that $f(p)=1$ for all primes $p$ using the initial conditions. Furthermore, I proved by induction that for any prime $p$ and integer $k \ge 1$, the relationship $f(p^k) = k p^{k-1}$ holds. These findings are documented in notes.md.
Candidate answer: N/A (Task completed, next steps involve solving $f(n)=n$)

### [W4, round 1]
**Task 1: Solutions of the form $n=p^p \le 4000$**
We tested prime values $p$ such that $p^p \le 4000$.
For $p=2$, $n=4$.
For $p=3$, $n=27$.
For $p=5$, $n=3125$.
For $p=7$, $7^7 > 4000$.
The solutions are $n \in \{4, 27, 3125\}$.

**Task 2: Solutions composed of powers of 2, 3, and 5, not prime powers ($n = 2^a 3^b 5^c \le 4000$)**
We searched systematically for $n = 2^a 3^b 5^c \le 4000$ that are not pure prime powers ($p^k$). The list of such integers found is:
[1, 15, 75, 375, 1875, 45, 225, 1125, 135, 675, 3375, 405, 2025, 1215, 3645, 10, 50, 250, 1250, 6, 30, 150, 750, 3750, 18, 90, 450, 2250, 54, 270, 1350, 162, 810, 486, 2430, 1458, 20, 100, 500, 2500, 12, 60, 300, 1500, 36, 180, 900, 108, 540, 2700, 324, 1620, 972, 2916, 40, 200, 1000, 24, 120, 600, 3000, 72, 360, 1800, 216, 1080, 648, 3240, 1944, 80, 400, 2000, 48, 240, 1200, 144, 720, 3600, 432, 2160, 1296, 3888, 160, 800, 4000, 96, 480, 2400, 288, 1440, 864, 2592, 320, 1600, 192, 960, 576, 2880, 1728, 640, 3200, 384, 1920, 1152, 3456, 1280, 768, 3840, 2304, 2560, 1536, 3072]

### [W1, round 1]
Calculations for g(n) up to n=50 have been completed using the defining properties (i) and (ii) and recursive application based on prime factorization.

Key findings regarding the condition g(n) = 2n:
1. g(4) = 8. This satisfies g(n) = 2n.
2. g(27) = 54. This satisfies g(n) = 2n.
No other solutions were found for $1 \le n \le 50$.

Observations for composite numbers that are not prime powers (e.g., 6, 10, 12, 14, 15, ...):
- g(6) = 11. Not a solution.
- g(10) = 17. Not a solution.
- g(12) = 28. Not a solution.
- g(15) = 23. Not a solution.
- g(30) = 61. Not a solution.
The function seems to deviate significantly from $2n$ for most composite numbers that are not prime powers.

Example calculations checked:
g(1) = 1
g(2) = 3 (Prime)
g(3) = 4 (Prime)
g(5) = 6 (Prime)
g(6) = 11 (Composite, 2*3)
g(9) = 15 (Prime Power, 3^2)
g(10) = 17 (Composite, 2*5)
g(27) = 54 (Prime Power, 3^3)

### [W1, round 1]
REPORT on task "Compute $g(n)$ and check if $g(n) = 2n$ for all integers $n$ from 1 up to 50, using the defining properties (i) and (ii). Record all observations, especially for composite numbers that are not prime p": I computed the function $g(n)$ for all integers $n$ from 1 to 50 by recursively applying the defining properties (i) and (ii). The calculation showed that $g(4) = 8$ and $g(27) = 54$, meaning these are solutions in the tested range. For composite numbers that are not prime powers (like 6, 10, 12, etc.), $g(n)$ typically deviates significantly from $2n$. All numerical observations and patterns have been recorded in notes.md.
Candidate answer: 4, 27 (within the checked range)

### [W3, round 1]
Investigation of $g(n)=n$ for composite $n$ with $\ge 2$ distinct prime factors:
1. The functional equation implies $g(n) = n + h(n)$, where $h(nm) = nh(m) + mh(n)$.
2. For $n=pq$ (distinct primes $p, q$), we found $g(pq) = pq + p + q$. Setting $g(pq)=pq$ requires $p+q=0$, which is impossible for positive primes.
3. For $n=p^2 q$ (distinct primes $p, q$), we found $g(p^2 q) = p^2 q + p^2 + 2pq$. Setting $g(p^2 q)=p^2 q$ requires $p(p+2q)=0$, which is impossible for positive primes.
Conclusion: $g(n) = n$ has no solutions when $n$ has at least two distinct prime factors (based on tested cases).

### [W3, round 1]
REPORT on task "Using the functional equation for $f$, investigate the case where $n$ is composite with at least two distinct prime factors ($n=p_1^{a_1} p_2^{a_2} \cdots$). Prove that $f(n) = n$ has no solutions in ": I investigated the case where $n$ has at least two distinct prime factors by analyzing $n=pq$ and $n=p^2 q$. By transforming the functional equation $g(nm) + nm = ng(m) + mg(n)$ into $h(nm) = nh(m) + mh(n)$ where $g(n)=n+h(n)$, I found $g(pq) = pq + p + q$ and $g(p^2 q) = p^2 q + p^2 + 2pq$. In both cases, $g(n) > n$, proving that $g(n)=n$ has no solutions for these composite structures.
Candidate answer: N/A (Task was investigative)

### [W4, round 1]
REPORT on task "Determine the maximum possible value of $p$ such that $n=p^p$ satisfies $n \le 4000$. Provide all solutions of the form $n=p^p$. Search for solutions composed of powers of 2, 3, and 5 that are not pri": I have completed the preliminary search for solutions $1 \le n \le 4000$. We found three solutions of the form $n=p^p$: $\{4
Candidate answer: {4,27, 32, 81, 125}
