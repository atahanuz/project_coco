### [W1, round 1]
Analysis of the case p=q:
If p=q, S simplifies to S = (12+n + 13-n) / p = 25/p.
The condition S < 1 implies 25/p < 1, so p > 25.
To maximize S = 25/p, we must minimize p. Since p is an integer, the minimum is p=26.
Thus, the maximum S when p=q occurs at p=q=26, yielding S = 25/26.

### [W3, round 1]
Focused on boundary conditions n=1 and n=12 with the constraint p, q <= 10.
For n=1, S = 13/p + 12/q. The minimum S achievable when p, q <= 10 is 2.5 (at p=10, q=10). Thus, S < 1 is impossible under this constraint.
For n=12, S = 24/p + 1/q. The minimum S achievable when p, q <= 10 is 2.5 (at p=10, q=10). Thus, S < 1 is impossible under this constraint.
Conclusion: The constraints p, q <= 10 are too restrictive to yield any solutions satisfying S < 1 for n=1 or n=12. We need to expand the search range for p and q.

### [W3, round 1]
Follow-up analysis for n=12 (S = 24/p + 1/q):
The initial constraint p, q <= 10 yielded no solutions for S < 1. By expanding the search to p, q <= 50, we found a strong candidate for the maximum S. The maximum S is achieved at p=25, q=26, yielding S = 24/25 + 1/26 = 649/650 (approx 0.99846).

Next step: Investigate maximizing S for n=1 (S = 13/p + 12/q) using larger p and q, aiming to exceed 649/650. Also consider how the maximum changes for intermediate values of n.

### [W4, round 1]
Investigated maximizing S = (12+n)/p + (13-n)/q < 1. For fixed p and q, S is linear in n.
1. If p < q, max S occurs at n=12. Best result found was (p, q) = (25, 26), yielding S = 649/650.
2. If p > q, max S occurs at n=1. Best result found was (p, q) = (170, 13), yielding S = 2209/2210.
The maximum value found is 2209/2210, achieved with p=170, q=13, and n=1. This demonstrates that the optimal p*q value is much larger than 25.

### [W2, round 2]
Systematic re-investigation of n=1 (S = 13/p + 12/q) focusing on p >> q.
We must satisfy 13/p + 12/q < 1. To maximize S, we want 12/q to be as close to 1 as possible, suggesting q should be slightly larger than 12.
The ideal choice for q is q=13, as it allows 12/q = 12/13, leaving 1/13 for the p term.
For q=13, we need 13/p < 1/13, so p > 169. Minimal integer p is 170.
This yields S = 13/170 + 12/13 = 2209/2210.

Testing nearby values for q:
1. q=14: Minimal p=92. S = 13/92 + 6/7 = 643/644. (Lower than 2209/2210).
2. q=15: Minimal p=66. S = 13/66 + 4/5 = 329/330. (Lower than 2209/2210).
3. q=16: Minimal p=53. S = 13/53 + 3/4 = 211/212. (Lower than 2209/2210).

The systematic search confirms that q=13 yields the maximum S for the constraint p >> q, achieving S = 2209/2210. No candidates exceeding this value were found.

### [W3, round 2]
### [W3, round 2]
Re-investigation of $n=12$: $S = 24/p + 1/q$.
The current maximum is $S = 649/650$ at $(p, q) = (25, 26)$.
We systematically searched for values exceeding this.

1.  **Lowering p**: If $p=24$, $S = 1 + 1/q > 1$. This violates the constraint $S < 1$. Thus, $p \ge 25$ is required.
2.  **Lowering q**: If $q=25$, we require $24/p < 1 - 1/25 = 24/25$, implying $p > 25$. The smallest integer $p$ is $p=26$. At $(p, q) = (26, 25)$, $S = 313/325 \approx 0.96307$, which is less than $649/650$.
3.  **Varying neighbors**:
    *   Increasing $q$ to 27 (while keeping $p=25$): $S = 24/25 + 1/27 < 649/650$.
    *   Increasing $p$ to 26 (while keeping $q=26$): $S = 24/26 + 1/26 = 25/26 \approx 0.9615$, which is less than $649/650$.

Conclusion: The combination $(p, q) = (25, 26)$ yields the maximum possible value of $S < 1$ for the case $n=12$.
The maximum value for $n=12$ is $649/650$.

### [W1, round 2]
### [W1, round 2]
Verification of W4's claim: For $(p, q, n) = (170, 13, 1)$, $S = \frac{13}{170} + \frac{12}{13} = \frac{13 \cdot 13 + 12 \cdot 170}{170 \cdot 13} = \frac{169 + 2040}{2210} = \frac{2209}{2210}$. This value is verified.

Search for better candidates (n=1, p>q, S > 2209/2210):
We require $S = 13/p + 12/q < 1$. This implies $q > 12$ and $p > 13$.
We tested minimizing $p$ for increasing $q$, starting from $q=13$.
1. $q=13$: $p_{min}=170$. $S = 2209/2210$.
2. $q=14$: $p_{min}=92$. $S = 643/644$. Since $644 < 2210$, $1/644 > 1/2210$, so $S < 2209/2210$.
3. $q=15$: $p_{min}=66$. $S = 329/330$. Since $330 < 2210$, $1/330 > 1/2210$, so $S < 2209/2210$.
The maximum value found under the constraints $p>q$ and $n=1$ remains $2209/2210$ at $(170, 13, 1)$.
