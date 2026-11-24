### [W1, round 1]
The side lengths are $a=n-1$, $b=n$, $c=n+1$. The semi-perimeter is $s = (3n)/2$.
The area $A$ is related to the inradius $r$ by $A = rs$. Since $r=1$, we have $A = 3n/2$.
Using Heron's formula:
$A = \sqrt{s(s-a)(s-b)(s-c)}$
$s-a = 3n/2 - (n-1) = (n+2)/2$
$s-b = 3n/2 - n = n/2$
$s-c = 3n/2 - (n+1) = (n-2)/2$
$A = \sqrt{\frac{3n}{2} \cdot \frac{n+2}{2} \cdot \frac{n}{2} \cdot \frac{n-2}{2}} = \frac{n}{4}\sqrt{3(n^2-4)}$
Equating the two expressions for A:
$3n/2 = \frac{n}{4}\sqrt{3(n^2-4)}$
Since $n>2$, we divide by $n/2$:
$3 = \frac{1}{2}\sqrt{3(n^2-4)}$
$6 = \sqrt{3(n^2-4)}$
$36 = 3(n^2-4)$
$12 = n^2-4$
$n^2 = 16$
$n = 4$ (since $n>0$).
The perimeter is $P = 3n = 3(4) = 12$.

### [W4, round 1]
Found a direct solution using Heron's formula and the inradius condition $r=K/s=1$.
Let the side lengths be $n-1, n, n+1$. The semi-perimeter $s = 3n/2$.
Setting $K^2 = s^2$ leads to $n^2 = 16$, so $n=4$.
The sides are 3, 4, 5, and the perimeter is 12.

Explored the angle formulation $r = (s-a)\tan(A/2)$. Equating this with $\tan(A/2) = \sqrt{\frac{(s-b)(s-c)}{s(s-a)}}$ also leads to $n=4$ and $P=12$.
No other values for $n$ are possible.

### [W3, round 1]
For triangles with consecutive integer side lengths $n, n+1, n+2$, the inradius $r$ was calculated for $n=3$ through $n=8$. The simulation showed that for $n=3$ (sides 3, 4, 5), the inradius $r=1$. Analytical confirmation showed that $r=1$ only occurs when $n=3$. The perimeter is $P = 3n+3$. For $n=3$, the perimeter is $3(3)+3 = 12$.

### [W2, round 1]
ANALYSIS COMPLETE:
Let the sides be $n, n+1, n+2$. The semi-perimeter is $s = (3n+3)/2$.
The inradius $r=1$ leads to the condition $A=s$. Using Heron's formula, this simplifies to the quadratic equation $n^2 + 2n - 15 = 0$.
The solutions are $n=3$ and $n=-5$.
Constraints require $n$ to be an integer and $n > 1$ (triangle inequality). Thus, $n=3$ is the unique valid value.
For $n=3$, the sides are $(3, 4, 5)$, and the perimeter $P = 12$.
(Note: The prompt mentioned verifying $n=4$ resulting in $P=12$. This appears contradictory; $P=12$ corresponds to $n=3$. For $n=4$, the inradius is $\sqrt{7}/2 \ne 1$.)
The only possible perimeter is 12.
