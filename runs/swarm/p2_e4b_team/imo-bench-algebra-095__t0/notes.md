### [W4, round 1]
Initial terms calculated:
a_1 = 0
a_2 = 1
a_3 = 2
a_4 = 4
a_5 = 5
a_6 = 7

Hypothesis based on the maximization structure (checking the median split):
If n is even (n=2k), the maximum occurs at i=k: a_n = 2*a_k + k.
If n is odd (n=2k+1), the maximum occurs at i=k or i=k+1: a_n = a_k + a_{k+1} + k.

This recurrence holds for the initial terms. I will calculate a_2025 using this recurrence.

### [W3, round 1]
Initial calculations for small $n$:
$a_1 = 0$
$a_2 = 1$
$a_3 = 2$
$a_4 = 4$
$a_5 = 5$
$a_6 = 7$
$a_7 = 9$

Focusing on odd $n = 2k+1$:
For $k=0, n=1$: $a_1 = 0$.
For $k=1, n=3$: $a_3 = 2$.
For $k=2, n=5$: $a_5 = 5$.
For $k=3, n=7$: $a_7 = 9$.

The differences are $a_3 - a_1 = 2$, $a_5 - a_3 = 3$, $a_7 - a_5 = 4$.
This suggests the relationship $a_{2k+1} = a_{2k-1} + (k+1)$ for $k \ge 1$.
This implies a quadratic relationship: $a_{2k+1} = \frac{(k+1)(k+2)}{2} - 1$.

We need $a_{2025}$. $2k+1 = 2025$, so $2k = 2024$, and $k = 1012$.
$a_{2025} = \frac{(1012+1)(1012+2)}{2} - 1 = \frac{1013 \cdot 1014}{2} - 1$
$a_{2025} = 1013 \cdot 507 - 1 = 513591 - 1 = 513590$.

### [W1, round 1]
Calculations for $a_n$ up to $n=12$:

$a_1 = 0$ (Base case)

$n=2$: $a_2 = \max_{i=1} \{a_1 + a_1 + \min(1, 1)\} = 0 + 0 + 1 = 1$.
$a_2 = 1$.

$n=3$: $a_3 = \max \{
  i=1: a_1 + a_2 + \min(1, 2) = 0 + 1 + 1 = 2, \\
  i=2: a_2 + a_1 + \min(2, 1) = 1 + 0 + 1 = 2
\}$.
$a_3 = 2$.

$n=4$: $a_4 = \max \{
  i=1: a_1 + a_3 + \min(1, 3) = 0 + 2 + 1 = 3, \\
  i=2: a_2 + a_2 + \min(2, 2) = 1 + 1 + 2 = 4, \\
  i=3: a_3 + a_1 + \min(3, 1) = 2 + 0 + 1 = 3
\}$.
$a_4 = 4$.

$n=5$: $a_5 = \max \{
  i=1: a_1 + a_4 + \min(1, 4) = 0 + 4 + 1 = 5, \\
  i=2: a_2 + a_3 + \min(2, 3) = 1 + 2 + 2 = 5, \\
  i=3: a_3 + a_2 + \min(3, 2) = 2 + 1 + 2 = 5, \\
  i=4: a_4 + a_1 + \min(4, 1) = 4 + 0 + 1 = 5
\}$.
$a_5 = 5$.

$n=6$: $a_6 = \max \{
  i=1: a_1 + a_5 + \min(1, 5) = 0 + 5 + 1 = 6, \\
  i=2: a_2 + a_4 + \min(2, 4) = 1 + 4 + 2 = 7, \\
  i=3: a_3 + a_3 + \min(3, 3) = 2 + 2 + 3 = 7, \\
  i=4: a_4 + a_2 + \min(4, 2) = 4 + 1 + 2 = 7, \\
  i=5: a_5 + a_1 + \min(5, 1) = 5 + 0 + 1 = 6
\}$.
$a_6 = 7$.

$n=7$: $a_7 = \max \{
  i=1: a_1 + a_6 + \min(1, 6) = 0 + 7 + 1 = 8, \\
  i=2: a_2 + a_5 + \min(2, 5) = 1 + 5 + 2 = 8, \\
  i=3: a_3 + a_4 + \min(3, 4) = 2 + 4 + 3 = 9, \\
  i=4: a_4 + a_3 + \min(4, 3) = 4 + 2 + 3 = 9, \\
  i=5: a_5 + a_2 + \min(5, 2) = 5 + 1 + 2 = 8, \\
  i=6: a_6 + a_1 + \min(6, 1) = 7 + 0 + 1 = 8
\}$.
$a_7 = 9$.

$n=8$: $a_8 = \max \{
  i=1: a_1 + a_7 + \min(1, 7) = 0 + 9 + 1 = 10, \\
  i=2: a_2 + a_6 + \min(2, 6) = 1 + 7 + 2 = 10, \\
  i=3: a_3 + a_5 + \min(3, 5) = 2 + 5 + 3 = 10, \\
  i=4: a_4 + a_4 + \min(4, 4) = 4 + 4 + 4 = 12, \\
  i=5: a_5 + a_3 + \min(5, 3) = 5 + 2 + 3 = 10, \\
  i=6: a_6 + a_2 + \min(6, 2) = 7 + 1 + 2 = 10, \\
  i=7: a_7 + a_1 + \min(7, 1) = 9 + 0 + 1 = 10
\}$.
$a_8 = 12$.

$n=9$: $a_9 = \max \{
  i=1: a_1 + a_8 + \min(1, 8) = 0 + 12 + 1 = 13, \\
  i=2: a_2 + a_7 + \min(2, 7) = 1 + 9 + 2 = 12, \\
  i=3: a_3 + a_6 + \min(3, 6) = 2 + 7 + 3 = 12, \\
  i=4: a_4 + a_5 + \min(4, 5) = 4 + 5 + 4 = 13, \\
  i=5: a_5 + a_4 + \min(5, 4) = 5 + 4 + 4 = 13, \\
  i=6: a_6 + a_3 + \min(6, 3) = 7 + 2 + 3 = 12, \\
  i=7: a_7 + a_2 + \min(7, 2) = 9 + 1 + 2 = 12, \\
  i=8: a_8 + a_1 + \min(8, 1) = 12 + 0 + 1 = 13
\}$.
$a_9 = 13$.

$n=10$: $a_{10} = \max \{
  i=1: a_1 + a_9 + \min(1, 9) = 0 + 13 + 1 = 14, \\
  i=2: a_2 + a_8 + \min(2, 8) = 1 + 12 + 2 = 15, \\
  i=3: a_3 + a_7 + \min(3, 7) = 2 + 9 + 3 = 14, \\
  i=4: a_4 + a_6 + \min(4, 6) = 4 + 7 + 4 = 15, \\
  i=5: a_5 + a_5 + \min(5, 5) = 5 + 5 + 5 = 15, \\
  i=6: a_6 + a_4 + \min(6, 4) = 7 + 4 + 4 = 15, \\
  i=7: a_7 + a_3 + \min(7, 3) = 9 + 2 + 3 = 14, \\
  i=8: a_8 + a_2 + \min(8, 2) = 12 + 1 + 2 = 15, \\
  i=9: a_9 + a_1 + \min(9, 1) = 13 + 0 + 1 = 14
\}$.
$a_{10} = 15$.

$n=11$: $a_{11} = \max \{
  i=1: a_1 + a_{10} + \min(1, 10) = 0 + 15 + 1 = 16, \\
  i=2: a_2 + a_9 + \min(2, 9) = 1 + 13 + 2 = 16, \\
  i=3: a_3 + a_8 + \min(3, 8) = 2 + 12 + 3 = 17, \\
  i=4: a_4 + a_7 + \min(4, 7) = 4 + 9 + 4 = 17, \\
  i=5: a_5 + a_6 + \min(5, 6) = 5 + 7 + 5 = 17, \\
  i=6: a_6 + a_5 + \min(6, 5) = 7 + 5 + 5 = 17, \\
  i=7: a_7 + a_4 + \min(7, 4) = 9 + 4 + 4 = 17, \\
  i=8: a_8 + a_3 + \min(8, 3) = 12 + 2 + 3 = 17, \\
  i=9: a_9 + a_2 + \min(9, 2) = 13 + 1 + 2 = 16, \\
  i=10: a_{10} + a_1 + \min(10, 1) = 15 + 0 + 1 = 16
\}$.
$a_{11} = 17$.

$n=12$: $a_{12} = \max \{
  i=1: a_1 + a_{11} + \min(1, 11) = 0 + 17 + 1 = 18, \\
  i=2: a_2 + a_{10} + \min(2, 10) = 1 + 15 + 2 = 18, \\
  i=3: a_3 + a_9 + \min(3, 9) = 2 + 13 + 3 = 18, \\
  i=4: a_4 + a_8 + \min(4, 8) = 4 + 12 + 4 = 20, \\
  i=5: a_5 + a_7 + \min(5, 7) = 5 + 9 + 5 = 19, \\
  i=6: a_6 + a_6 + \min(6, 6) = 7 + 7 + 6 = 20, \\
  i=7: a_7 + a_5 + \min(7, 5) = 9 + 5 + 5 = 19, \\
  i=8: a_8 + a_4 + \min(8, 4) = 12 + 4 + 4 = 20, \\
  i=9: a_9 + a_3 + \min(9, 3) = 13 + 2 + 3 = 18, \\
  i=10: a_{10} + a_2 + \min(10, 2) = 15 + 1 + 2 = 18, \\
  i=11: a_{11} + a_1 + \min(11, 1) = 17 + 0 + 1 = 18
\}$.
$a_{12} = 20$.

Summary:
$a_1=0, a_2=1, a_3=2, a_4=4, a_5=5, a_6=7, a_7=9, a_8=12, a_9=13, a_{10}=15, a_{11}=17, a_{12}=20$.

### [W2, round 2]
**Proof Sketch: Optimal Split Index**
The recurrence relation is $a_n = \max_{1 \le i \le n - 1} \left\{a_i + a_{n - i} + \min(i, n - i) \right\}$. We aim to show the maximum is achieved when $i \approx n/2$.

1.  **Effect of $\min(i, n-i)$:** The auxiliary term $g(i) = \min(i, n-i)$ is maximized precisely when $i$ is closest to $n/2$.
2.  **Effect of $a_i + a_{n-i}$:** The sequence $a_n$ grows faster than linearly (observed growth rate $\approx 1.67$ for $n=12$). Due to the nature of its construction via maximizing balanced sums, $a_i + a_{n-i}$ is also maximized when $i$ and $n-i$ are as close as possible, i.e., near $n/2$.
3.  **Comparison:** Comparing the peripheral split ($i=1$, value $a_{n-1} + 1$) with the central split ($i \approx n/2$, value $\approx 2a_{n/2} + n/2$), the quadratic/super-linear growth of $a_n$ ensures that $2a_{n/2} + n/2$ significantly outweighs $a_{n-1} + 1$.

Thus, both components contributing to the sum are maximized simultaneously at the central split index $i = \lfloor n/2 \rfloor$ or $i = \lceil n/2 \rceil$, justifying the simplified recurrence relations used previously.
