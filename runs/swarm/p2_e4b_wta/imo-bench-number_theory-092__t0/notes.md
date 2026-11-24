### [W2, round 1]
Structural Analysis of the Problem: Primes p, q, r

1. Parity Constraint (Modulo 2):
Let the four expressions be $A=p+q-r$, $B=q+r-p$, $C=r+p-q$, and $D=p+q+r$.
Since $p<q<r$, we must have $p+q > r$ for $A$ to be positive, which is required for $A$ to be prime.
If $p=2$, then $A = 2+q-r$. Since $q<r$, $2+q-r \le 1$. For $A$ to be prime, $A$ must be $\ge 2$. This implies $q-r \ge 0$, contradicting $q<r$.
Therefore, $p, q, r$ must all be odd primes.
If $p, q, r$ are all odd:
    D = Odd + Odd + Odd = Odd.
    A, B, C are all differences/sums of three odd numbers, resulting in Odd numbers.
Since $A, B, C, D$ are all odd primes, they must all be $\ge 3$.

2. Modulo 3 Constraint:
If none of $p, q, r$ is 3, then $p, q, r \equiv 1$ or $2 \pmod 3$.
If all three are $1 \pmod 3$, then $D = p+q+r \equiv 1+1+1 \equiv 3 \equiv 0 \pmod 3$. Since $p, q, r$ are primes $> 3$, $D > 3$, so $D$ is composite. Contradiction.
If all three are $2 \pmod 3$, then $D = p+q+r \equiv 2+2+2 \equiv 6 \equiv 0 \pmod 3$. $D$ is composite. Contradiction.
Therefore, at least one of $p, q, r$ must be 3. Since $p < q < r$, we must have $p=3$.

3. Consequences of p=3:
If $p=3$, then $q, r$ are primes greater than 3, so $q, r \equiv 1$ or $2 \pmod 3$.
$D = 3+q+r$. For $D$ to be prime, $q+r$ cannot be $0 \pmod 3$.
    a) If $q \equiv 1, r \equiv 2 \pmod 3$ (or vice versa): $q+r \equiv 0 \pmod 3$. Then $D = 3 + (0) \equiv 0 \pmod 3$. Since $D > 3$, $D$ is composite. Contradiction.
    b) If $q \equiv 1, r \equiv 1 \pmod 3$: $q+r \equiv 2 \pmod 3$. $D \equiv 3+2 \equiv 2 \pmod 3$. (Possible)
    c) If $q \equiv 2, r \equiv 2 \pmod 3$: $q+r \equiv 4 \equiv 1 \pmod 3$. $D \equiv 3+1 \equiv 1 \pmod 3$. (Possible)

Necessary Conditions Summary:
1. $p=3$.
2. $q$ and $r$ are primes $> 3$.
3. $q$ and $r$ must have the same residue modulo 3 (both 1 or both 2).
4. Constraint $p+q > r$ must hold (i.e., $3+q > r$).

### [W4, round 1]
Case 3 investigation (r+p=800): We analyzed the constraints using the requirement that $p, r$ must be odd primes. We iterated over possible values of the smallest prime $p$ (minimizing $p$ maximizes $r$) and checked all valid intervening primes $q$ such that $p<q<r$. For every valid triplet $(p, q, r)$, we verified that $800-q$, $800+q$, $p+q-r$, and $q+r-p$ must all be prime. The search concluded that no prime triplet $(p, q, r)$ satisfies all the necessary conditions when $r+p=800$. Therefore, there are no solutions for $r$ in Case 3.

### [W3, round 1]
Case 2: q+r=800. We investigated the requirement that 800-p and 800+p must be prime while p < 400. Modulo 3 analysis showed that for any prime p > 3, either p+800 or 800-p is composite. The only possible solution for 800-p to be prime is p=797, but this violates the constraint p < 400. Therefore, Case 2 yields no solutions.
