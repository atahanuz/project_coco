### [W2, round 1]
Analysis of h(n) = g(n) - n:
1. The functional equation for h(n) is h(nm) = nh(m) + mh(n).
2. For any prime p, h(p) = g(p) - p = (p+1) - p = 1.
3. The task requires finding distinct primes p, q such that h(pq) = pq.
4. Using the functional equation: h(pq) = ph(q) + qh(p) = p(1) + q(1) = p + q.
5. We must solve p + q = pq, which rearranges to (p - 1)(q - 1) = 1.
6. Since p and q are primes, p-1 >= 1 and q-1 >= 1. The only integer solution is p-1=1 and q-1=1, meaning p=2 and q=2.
7. This contradicts the requirement that p and q must be distinct primes.
Conclusion: There are no distinct primes p, q such that h(pq) = pq.

### [W3, round 1]
Investigation of $g(p^a q) = p^a q$ for distinct primes $p, q$.
Using the functional equation (ii) with $n=p^a$ and $m=q$:
$g(p^a q) + p^a q = p^a g(q) + q g(p^a)$.

We established $g(q) = q+1$ (Condition i).
We established $g(p^a) = p^a + a p^{a-1}$ by induction/recurrence.

Assuming $g(p^a q) = p^a q$:
$2 p^a q = p^a (q+1) + q (p^a + a p^{a-1})$
$2 p^a q = p^a q + p^a + q p^a + a q p^{a-1}$
$2 p^a q = 2 p^a q + p^a + a q p^{a-1}$

This requires $p^a + a q p^{a-1} = 0$. Since $p \ge 2, q \ge 2, a \ge 1$, all terms are strictly positive, leading to a contradiction.
Therefore, $g(p^a q) \neq p^a q$ for $p \ne q$.

### [W4, round 1]
### [W4, round 1] Analysis of $g(p^a) = p^a$
We established the recurrence relation for $g(p^a)$ using the functional equation (ii) and condition (i):
$g(p^a) = p^a + a p^{a-1}$ for $a \ge 2$.
The task asks for solutions where $h(p^a) = p^a$, which is equivalent to $g(p^a) = p^a$.
Setting these equal:
$p^a + a p^{a-1} = p^a$
$a p^{a-1} = 0$.
Since $p$ is prime ($p \ge 2$) and $a$ is a positive integer, $p^{a-1} > 0$ and $a > 0$. Thus, $a p^{a-1} > 0$.
Conclusion: There are no integers $p$ (prime) and $a \ge 1$ for which $g(p^a) = p^a$. This result holds for $a \ge 5$ as well.

### [W1, round 1]
Calculations for $g(n)$ for $n=1$ to $n=20$ using $g(1)=0$, $g(p)=p+1$, and $g(pm) = pg(m) + m$:

n=1: g(1) = 0. (2n=2)
n=2: g(2) = 3. (2n=4)
n=3: g(3) = 4. (2n=6)
n=4: g(4) = 8. (2n=8). Solution found.
n=5: g(5) = 6. (2n=10)
n=6: g(6) = 11. (2n=12)
n=7: g(7) = 8. (2n=14)
n=8: g(8) = 20. (2n=16)
n=9: g(9) = 15. (2n=18)
n=10: g(10) = 17. (2n=20)
n=11: g(11) = 12. (2n=22)
n=12: g(12) = 28. (2n=24)
n=13: g(13) = 14. (2n=26)
n=14: g(14) = 23. (2n=28)
n=15: g(15) = 23. (2n=30)
n=16: g(16) = 48. (2n=32)
n=17: g(17) = 18. (2n=34)
n=18: g(18) = 39. (2n=36)
n=19: g(19) = 20. (2n=38)
n=20: g(20) = 44. (2n=40)

Only n=4 satisfies g(n)=2n in the range 1 <= n <= 20.
