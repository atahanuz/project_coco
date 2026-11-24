### [W3, round 1]
Case 3 Analysis (r+p=800):
We analyzed the case where $r+p=800$, requiring $p$ and $r$ to be odd primes such that $p<400$ and $r=800-p$ is prime. For each such pair $(p, r)$, we iterated over primes $q$ such that $p < q < r$. The four required primes are $P_1 = 2p+q-800$, $P_2 = q+800-2p$, $P_3 = 800-q$, and $P_4 = q+800$. The computational check found no triplets $(p, q, r)$ that satisfy all primality conditions. Thus, no solution exists for Case 3.

### [W2, round 1]
Analysis of Case 2 (q+r=800): Exhaustive search across all prime pairs (q, r) such that q+r=800 and all primes p < q yielded no solutions (p, q, r) satisfying the conditions: p+q-r, q+r-p, r+p-q, and p+q+r are all prime.

### [W1, round 1]
Analysis of Case 1: p+q=800.
We are looking for distinct primes p < q < r such that p+q=800 and P1=800-r, P2=q+r-p, P3=r+p-q, P4=800+r are all prime.
The constraints require r < 800 and r > q.
A thorough iteration over all 21 possible pairs (p, q) resulted in finding one solution: (p, q, r) = (13, 787, 797).
For this solution, P1=3, P4=1597, P2=1571, P3=23, all of which are prime.
The maximum value of r found in Case 1 is 797.
