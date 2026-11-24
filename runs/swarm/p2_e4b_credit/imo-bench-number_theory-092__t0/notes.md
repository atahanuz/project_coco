### [W3, round 1]
Assuming r+p=800, we searched for prime pairs (p, r) and corresponding prime q such that the four derived expressions (A, B, C, D) are all prime. The exhaustive search found no solutions for r under these constraints.

### [W2, round 1]
Analysis of the case q+r=800:
I found 21 candidate pairs of odd primes (q, r) summing to 800. For every single pair, I systematically checked all possible primes p < q. In no case did all four derived numbers (A=p+q-r, B=800-p, C=r+p-q, D=p+800) satisfy the primality condition simultaneously. Therefore, under the assumption q+r=800, there are no solutions for r.

### [W4, round 1]
Analysis of Constraints for $\{p, q, r\}$

1.  **Initial Parity Check (If all four expressions $p+q-r, q+r-p, r+p-q, p+q+r$ must be prime):**
    *   For $D = p+q+r$ to be prime, since $p, q, r$ are distinct primes, $D$ must be odd (as $D \ge 2+3+5=10$).
    *   For $D$ to be odd, exactly one of $p, q, r$ must be the only even prime, 2. Since $p<q<r$, we must have $p=2$.
    *   If $p=2$, then $q$ and $r$ are odd primes. Thus, $D = 2 + \text{odd} + \text{odd} = 2 + \text{even} = \text{even}$.
    *   Since $q \ge 3$ and $r \ge 5$, $D \ge 10$. Therefore, $D$ is an even number greater than 2, meaning $D$ is composite.
    *   **Conclusion:** The initial constraint set (where ALL four expressions are prime) is mathematically impossible to satisfy. The problem must rely on the condition "If one of $p+q, q+r, r+p$ is 800" overriding the primality constraint for that specific sum.

2.  **Structural Constraints from $A', B', C'$ Primality:**
    *   Let $A' = p+q-r$, $B' = q+r-p$, $C' = r+p-q$.
    *   We observe the following relations:
        *   $A' + C' = (p+q-r) + (r+p-q) = 2p$
        *   $A' + B' = (p+q-r) + (q+r-p) = 2q$
        *   $B' + C' = (q+r-p) + (r+p-q) = 2r$
    *   Since $p, q, r$ are primes, $A'+C'$, $A'+B'$, and $B'+C'$ must all be even integers.
    *   **Strong Constraint:** $A'$, $B'$, and $C'$ must all have the same parity. Since they are required to be primes, they must either all be 2 (impossible as $p, q, r$ would not be distinct), or they must all be odd primes.

3.  **Constraints Specific to the 800 Cases:**
    *   **Case 1: $p+q = 800$.** (We seek to maximize $r$).
        *   $A' = 800 - r$ must be prime.
        *   $D' = 800 + r$ must be prime.
        *   $p$ and $q$ must be primes summing to 800.
    *   **Case 2: $q+r = 800$.** (We seek to maximize $r$, implicitly limited by $q$).
        *   $B' = 800 - p$ must be prime.
        *   $D' = 800 + p$ must be prime.
        *   $q$ and $r$ must be primes summing to 800.
    *   **Case 3: $r+p = 800$.** (We seek to maximize $r$).
        *   $C' = 800 - q$ must be prime.
        *   $D' = 800 + q$ must be prime.
        *   $r$ and $p$ must be primes summing to 800.

These structural constraints dramatically limit the search space by requiring that specific linear combinations (like $800 \pm x$) must result in primes. This is the best starting point for W1/W2/W3.
