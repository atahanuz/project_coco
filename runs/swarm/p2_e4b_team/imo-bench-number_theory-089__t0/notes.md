### [W1, round 1]
Setting up the problem:
Sides are $n, n+1, n+2$.
Semi-perimeter $s = \frac{3n+3}{2}$.
Inradius $r=1$, so Area $A = s$.
Heron's formula yields $A = \sqrt{s(s-n)(s-(n+1))(s-(n+2))}$.
Substituting the side lengths and $s$:
$A = \sqrt{\frac{3n+3}{2} \cdot \frac{n+3}{2} \cdot \frac{n+1}{2} \cdot \frac{n-1}{2}}$
Equating $A=s$ and squaring both sides:
$s^2 = s \cdot \frac{(n+3)(n+1)(n-1)}{8}$
Dividing by $s$ (assuming $s>0$):
$s = \frac{(n+3)(n+1)(n-1)}{8}$
Substituting $s = \frac{3n+3}{2} = \frac{3(n+1)}{2}$:
$\frac{3(n+1)}{2} = \frac{(n+3)(n+1)(n-1)}{8}$
Since $n>1$ (to form a triangle), we divide by $(n+1)$:
$\frac{3}{2} = \frac{(n+3)(n-1)}{8}$
$12 = n^2 + 2n - 3$
$n^2 + 2n - 15 = 0$
$(n+5)(n-3) = 0$
The positive integer solution is $n=3$.
The side lengths are 3, 4, and 5. The perimeter is $3+4+5=12$.

### [W3, round 1]
Triangle side lengths are $n-1, n, n+1$.
1. Triangle Inequality Check: Requires $2n-1 > n+1$, leading to $n > 2$.
2. Semi-perimeter $s = \frac{3n}{2}$.
3. Inradius relationship: Given $r=1$, the area $A = rs = s = \frac{3n}{2}$.
4. Heron's Formula for Area Squared:
$A^2 = s(s-a)(s-b)(s-c)$
$A^2 = \left(\frac{3n}{2}\right) \left(\frac{n+2}{2}\right) \left(\frac{n}{2}\right) \left(\frac{n-2}{2}\right) = \frac{3n^2(n^2 - 4)}{16}$.
5. Setting $A^2 = s^2$:
$\left(\frac{3n}{2}\right)^2 = \frac{9n^2}{4}$.
6. Equating $A^2$:
$\frac{3n^2(n^2 - 4)}{16} = \frac{9n^2}{4}$.
7. Solving for $n$ (assuming $n \ne 0$):
$\frac{3(n^2 - 4)}{16} = \frac{9}{4}$
$3(n^2 - 4) = 36$
$n^2 - 4 = 12$
$n^2 = 16$
$n = 4$ (since $n$ must be positive and satisfy $n>2$).
8. The only valid integer value is $n=4$. The sides are 3, 4, 5. The perimeter is $3n = 12$.

### [W2, round 1]
Derivation for the problem: Side lengths are $n, n+1, n+2$. Semi-perimeter $s = (3n+3)/2$. Using $r^2 = \frac{(s-a)(s-b)(s-c)}{s}$, we found $r^2 = \frac{(n+3)(n-1)}{12}$. Setting $r^2=1$ leads to $n^2 + 2n - 15 = 0$, which factors to $(n+5)(n-3)=0$. Since $n$ must be a positive integer greater than 1 for a valid triangle, we must have $n=3$. The sides are 3, 4, 5, and the perimeter is $P = 3n+3 = 3(3)+3 = 12$.
