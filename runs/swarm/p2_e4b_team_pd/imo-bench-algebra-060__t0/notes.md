### [W3, round 1]
Structural Analysis for maximizing S = (12+n)/p + (13-n)/q < 1.
Let A = 12+n and B = 13-n. We seek to maximize S such that S approaches 1 from below.
To maximize the sum while adhering to the inequality constraint, the contributions of the two terms, A/p and B/q, should be balanced.
Setting A/p = B/q leads to the optimal continuous ratio p/q = A/B = (12+n)/(13-n).
We expect the optimal integer solutions for p and q to maintain a ratio close to (12+n)/(13-n) for a fixed n. This ratio defines the required structure for maximization.

### [W4, round 1]
Analysis for n=6: We seek to maximize S = 18/p + 7/q < 1. By iterating p > 18, we found the maximum candidate S is achieved with p=19 and q=134. S = 18/19 + 7/134 = 2545/2546.

Analysis for n=10: We seek to maximize S = 22/p + 3/q < 1. By iterating p > 22, we found the maximum candidate S is achieved with p=23 and q=70. S = 22/23 + 3/70 = 1609/1610.

### [W2, round 1]
For the case $n=12$, the expression is $S = \frac{24}{p} + \frac{1}{q}$, subject to $S < 1$. We sought to maximize $S$.
We tested configurations near $p=24$ and $q=1$.
1. If $q=1$, $S = 24/p + 1 \ge 1$, so $q>1$.
2. By setting $p = 24+k$, we found the smallest integer $q$ satisfying the constraint $S<1$ is $q = \lfloor 1 + 24/k \rfloor + 1$.
3. For $k=1$ ($p=25$), $q=26$, yielding $S = 24/25 + 1/26 = 649/650$.
4. For $k=2$ ($p=26$), $q=14$, yielding $S = 181/182 < 649/650$.
5. For $k=3$ ($p=27$), $q=10$, yielding $S = 89/90 < 649/650$.
The maximum value found for $n=12$ is $649/650$, achieved at $(p, q) = (25, 26)$.

### [W1, round 1]
Maximum S found for $n=1$ (p=14, q=169): $2365/2366$
Maximum S found for $n=2$ (p=15, q=166): $2489/2490$
Maximum S found for $n=3$ (p=16, q=161): $2575/2576$
Maximum S found for $n=4$ (p=17, q=154): $2617/2618$
Maximum S found for $n=5$ (p=18, q=145): $2609/2610$

### [W4, round 2]
### [W4, round 2] Verification of Candidate Maxima (n=4, 5, 6)

We verify the candidate maxima found for $n=4, 5, 6$ by checking immediate neighbors $(p', q')$ of the recorded optimal pairs $(p, q)$ to ensure the strict inequality $S < 1$ is maintained and $S$ cannot be improved by slight integer adjustments.

**Case n=4:** Candidate $(p, q) = (17, 154)$, $S = 2617/2618$. ($A=16, B=9$)
1. Check $p'=16$: $S = 16/16 + 9/q = 1 + 9/q \ge 1$. Constraint violated. Thus $p \ge 17$.
2. Check $q'=153$: $S = 16/17 + 9/153 = 16/17 + 1/17 = 1$. Constraint violated (not strictly less than 1). Thus $q \ge 154$.
The solution $(17, 154)$ is confirmed to be a local maximum.

**Case n=5:** Candidate $(p, q) = (18, 145)$, $S = 2609/2610$. ($A=17, B=8$)
1. Check $p'=17$: $S = 17/17 + 8/q = 1 + 8/q \ge 1$. Constraint violated. Thus $p \ge 18$.
2. Check $q'=144$: $S = 17/18 + 8/144 = 17/18 + 1/18 = 1$. Constraint violated. Thus $q \ge 145$.
The solution $(18, 145)$ is confirmed to be a local maximum.

**Case n=6:** Candidate $(p, q) = (19, 134)$, $S = 2545/2546$. ($A=18, B=7$)
1. Check $p'=18$: $S = 18/18 + 7/q = 1 + 7/q \ge 1$. Constraint violated. Thus $p \ge 19$.
2. Check $q'=133$: $S = 18/19 + 7/133 = 18/19 + 1/19 = 1$. Constraint violated. Thus $q \ge 134$.
The solution $(19, 134)$ is confirmed to be a local maximum.

### [W2, round 2]
For n=11, we seek to maximize S = 23/p + 2/q < 1. Systematically testing minimal p starting from p=24:
1. p=24: q must satisfy 2/q < 1/24, so q > 48. Minimal q=49. S = 23/24 + 2/49 = 1175/1176.
2. p=25: q must satisfy 2/q < 2/25, so q > 25. Minimal q=26. S = 23/25 + 2/26 = 324/325.
3. p=26: q must satisfy 2/q < 3/26, so q > 52/3 approx 17.33. Minimal q=18. S = 23/26 + 2/18 = 233/234.
The maximum value found is S = 1175/1176, achieved at (p, q) = (24, 49).

### [W1, round 2]
### [W1, round 2]
Results for specified values of n:
For n=7, $S = 19/p + 6/q < 1$. By testing small $p$ starting from $p=20$, the maximum value found is $S = 2419/2420$, achieved with $(p, q) = (20, 121)$.
For n=8, $S = 20/p + 5/q < 1$. By testing small $p$ starting from $p=21$, the maximum value found is $S = 2225/2226$, achieved with $(p, q) = (21, 106)$.
For n=9, $S = 21/p + 4/q < 1$. By testing small $p$ starting from $p=22$, the maximum value found is $S = 1957/1958$, achieved with $(p, q) = (22, 89)$.
