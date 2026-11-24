### [W2, round 1]
Case 1: p+q=800. We require $r$ to be prime, $r>q$, $A=800-r$ prime, and $D=800+r$ prime. For $A$ to be positive, we must have $r < 800$. The maximum prime $r < 800$ is $r=797$.
Testing $r=797$:
1. (p, q) = (13, 787). $q=787 < 797$.
   $A = 3$ (prime). $D = 1597$ (prime).
   $B = q+r-p = 787+797-13 = 1571$ (prime).
   $C = r+p-q = 797+13-787 = 23$ (prime).
   This is a valid solution.
2. (p, q) = (43, 757). $q=757 < 797$.
   $A = 3$ (prime). $D = 1597$ (prime).
   $B = q+r-p = 757+797-43 = 1511$ (prime).
   $C = r+p-q = 797+43-757 = 83$ (prime).
   This is also a valid solution.

Since $r$ must be less than 800, the maximum possible value for $r$ in Case 1 is 797.

### [W4, round 1]
Case 3 Investigation (r+p=800):
We investigated the case where r+p=800. Constraints required finding primes p (< 400), r=800-p, and q such that:
1. p < q < r
2. A = 2p + q - 800 is prime
3. B = q + 800 - 2p is prime
4. C = 800 - q is prime
5. D = 800 + q is prime

By systematically checking all valid (p, r) pairs, we found that for every pair, no prime q satisfied all constraints. The script execution confirmed that no solution exists for Case 3.

### [W3, round 1]
# Investigation of Case 2: q + r = 800

**1. Bounds and Candidates for r:**
Since $p < q < r$ and $q+r=800$, we must have $400 < r < 800$. We identified 20 candidate pairs $(q, r)$ where both are prime, starting with the largest $r=787$ (when $q=13$) and ending with the smallest $r=421$ (when $q=379$).

**2. Constraints on p (General Analysis):**
For $p, q, r$ to satisfy all primality conditions, $p$ must adhere to several tight constraints derived from $q+r=800$:
*   $p$ must be prime.
*   $p < q$.
*   $p+800$ must be prime. (This rules out $p=2, 3, p \equiv 1 \pmod 3$ for $p>3$).
*   $800-p$ must be prime.

**3. Analysis of Maximum r:**
To maximize $r$, we test the pair $(q, r) = (13, 787)$. Here, $p$ must be a prime such that $p < 13$. The possible values for $p$ satisfying the initial constraints (i.e., $p+800$ and $800-p$ prime) do not exist for $p < 13$. Since the maximum possible $r$ corresponds to the minimum possible $q$, and the minimum $q$ yields no solution, the maximum $r$ must be smaller than 787.

Further investigation on the remaining 19 pairs is required to find the actual maximum $r$.

### [W1, round 1]
Initial analysis concluded that p, q, r must all be odd primes because otherwise D=p+q+r would be even and greater than 2, hence composite.
The condition that one of p+q, q+r, r+p equals 800 leads to three cases. Cases 1 and 2 were ruled out because they require q=r or p=r, contradicting p < q < r.
We must be in Case 3: r + p = 800. To maximize r, we must minimize p.
The primality of A = p+q-r = 2p+q-800 requires q > 800 - 2p. Combined with q < r = 800-p, this imposes a strong lower bound on p.
p=3 (r=797) failed because it required q > 794, contradicting q < 797.
p=13 (r=787) failed because it required q > 774, contradicting q < 787.
The smallest prime p found that allows a valid range for q is p=31, giving r = 769.
Testing p=31, r=769 showed that while a suitable q must be found in [739, 767], the specific constraints on C=800-q and D=800+q being prime, alongside A and B being prime, are extremely restrictive and suggest that 769 is the maximum possible value based on systematic bounds established.
