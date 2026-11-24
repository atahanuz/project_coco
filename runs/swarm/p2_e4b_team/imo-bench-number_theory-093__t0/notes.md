### [W1, round 1]
The multiplicative order of 3 modulo 625, denoted L, was determined to be 500. This was found by checking the order modulo smaller powers of 5 and verifying that 3^100 mod 625 is 126, not 1.

### [W4, round 1]
Fundamental result found: The order of 3 modulo 10000 is 500. For $3^a \equiv 3^b \equiv 3^c \pmod{10000}$ with $a<b<c$, we must have $b-a = 500k$ and $c-b = 500m$ for integers $k, m \ge 1$. The constraint $c \le a+b$ requires $a \ge 500m$. To minimize $a+b+c$, we chose the smallest possible values: $m=1$, leading to $a_{min}=500$. Then we chose $k=1$ to minimize $b$, resulting in the smallest case: $(a, b, c) = (500, 1000, 1500)$. The minimum sum is $a+b+c = 3000$. This must be compared against any lower sums found by W2.

### [W3, round 1]
Derived L = ord_{10000}(3) = 500.
The constraints are b = a + k1*500 and c = a + k2*500, with 1 <= k1 < k2.
Applying c <= a + b:
a + k2*500 <= a + (a + k1*500)
k2*500 - k1*500 <= a
500(k2 - k1) <= a.
For a solution for a to exist (a non-negative integer), we require k2 > k1.
The minimal integers satisfying 1 <= k1 < k2 are k1 = 1 and k2 = 2.

### [W2, round 1]
Finding the smallest pair (a, b) with a < b such that 3^a = 3^b (mod 10000) requires finding the order of 3 modulo 10000. The order k is 500. The smallest pair found is (a, b) = (0, 500). This implies that b-a must be a multiple of 500.
