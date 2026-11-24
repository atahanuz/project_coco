### [W1, round 1]
Side lengths are defined as (n-1, n, n+1).
For these to form a valid triangle:
1. Positive side lengths: n-1 > 0 => n > 1.
2. Triangle Inequality:
   (n-1) + n > n+1 => 2n-1 > n+1 => n > 2.
   (n-1) + (n+1) > n => 2n > n => n > 0.
   n + (n+1) > n-1 => 2n+1 > n-1 => n > -2.
The strictest constraint requires n to be an integer such that n > 2, so n >= 3.

### [W2, round 1]
The side lengths are $n-1, n, n+1$. The semi-perimeter is $s = 3n/2$.
Using Heron's formula, the area $K$ of the triangle is derived as:
$K = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{\frac{3n}{2} \cdot \frac{n+2}{2} \cdot \frac{n}{2} \cdot \frac{n-2}{2}}$
$K = \frac{n}{4} \sqrt{3(n^2 - 4)}$

### [W3, round 1]
Triangle sides: n-1, n, n+1 (where n >= 3 is an integer).
Semi-perimeter (s): s = ((n-1) + n + (n+1)) / 2 = 3n/2.

Area (K) using Heron's formula:
s-a = (n+2)/2
s-b = n/2
s-c = (n-2)/2
K = sqrt( (3n/2) * ((n+2)/2) * (n/2) * ((n-2)/2) )
K = sqrt( 3n^2(n^2 - 4) / 16 )
K = (n/4) * sqrt(3(n^2 - 4)).

Condition: r = 1. Since r = K/s, we must have K = s.
Primary algebraic equation in n: (n/4) * sqrt(3(n^2 - 4)) = 3n/2.

### [W4, round 1]
### [W4, round 1]
Solving the equation derived from r=1 (using $r=K/s$):
$1 = \frac{\frac{n}{4} \sqrt{3(n^2 - 4)}}{3n/2}$
This simplifies to $\frac{\sqrt{3(n^2 - 4)}}{6} = 1$, leading to $n^2 - 4 = 36/3 = 12$.
The algebraic equation is $n^2 = 16$, giving solutions $n = 4$ and $n = -4$.
Checking the constraints from W1 ($n \ge 3$):
1. $n=4$: Satisfies $n \ge 3$. Valid.
2. $n=-4$: Does not satisfy $n \ge 3$. Invalid.
The only possible integer value for $n$ is 4.
The perimeter $P$ is $3n$. For $n=4$, $P = 12$.
