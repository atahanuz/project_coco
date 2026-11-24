### [W4, round 1]
Calculations for triangle with consecutive integer sides ($n-1, n, n+1$) and inradius $r=1$.
1. Semi-perimeter: $s = 3n/2$.
2. Area $K$ via Heron's formula: $K = \frac{n}{4} \sqrt{3(n^2 - 4)}$.
3. Inradius relationship: $K = rs$. Since $r=1$, $K = s = 3n/2$.
4. Equating areas:
   $\frac{n}{4} \sqrt{3(n^2 - 4)} = \frac{3n}{2}$
5. Solving for $n$ (assuming $n>0$):
   $\sqrt{3(n^2 - 4)} = 6$
   $3(n^2 - 4) = 36$
   $n^2 - 4 = 12$
   $n^2 = 16$
   $n = 4$ (since sides must be positive).
6. The side lengths are $3, 4, 5$.
7. The perimeter $P = 3n = 3(4) = 12$.
It appears there is only one solution.

### [W2, round 1]
The problem asks for the perimeter $P$ of a triangle whose sides are three consecutive integers ($n-1, n, n+1$) and whose inradius $r=1$.
1. Semi-perimeter: $s = (n-1 + n + n+1)/2 = 3n/2$.
2. Area using $r$: $A = rs = 1 \cdot (3n/2) = 3n/2$.
3. Area using Heron's formula:
   $s-a = 3n/2 - (n-1) = (n+2)/2$
   $s-b = 3n/2 - n = n/2$
   $s-c = 3n/2 - (n+1) = (n-2)/2$
   $A^2 = s(s-a)(s-b)(s-c) = (3n/2) \cdot \frac{n+2}{2} \cdot \frac{n}{2} \cdot \frac{n-2}{2} = \frac{3n(n^2-4)}{16}$.
4. Equating $A^2$:
   $(3n/2)^2 = \frac{9n^2}{4} = \frac{3n(n^2-4)}{16}$
5. Solving for $n$ (assuming $n>0$):
   $\frac{9n^2}{4} = \frac{3n(n^2-4)}{16}$
   Multiply by 16: $36n^2 = 3n(n^2-4)$.
   Since $n$ must be positive, we can divide by $3n$: $12n = n^2 - 4$.
   Rearranging gives the quadratic equation: $n^2 - 12n - 4 = 0$.

Wait, I made an error in the algebra in step 4. Let's recheck:

$A^2 = (3n/2)^2 = 9n^2/4$.
Heron's result: $A^2 = \frac{3n}{2} \cdot \frac{n+2}{2} \cdot \frac{n}{2} \cdot \frac{n-2}{2} = \frac{3n^2(n^2-4)}{16}$.

Equating:
$\frac{9n^2}{4} = \frac{3n^2(n^2-4)}{16}$

Divide both sides by $n^2$ (since $n>0$):
$\frac{9}{4} = \frac{3(n^2-4)}{16}$

Multiply by 16:
$16 \cdot \frac{9}{4} = 3(n^2-4)$
$36 = 3(n^2-4)$
$12 = n^2 - 4$
$n^2 = 16$
$n = 4$ (Since $n$ must be positive).

The perimeter $P = 3n = 3(4) = 12$. This confirms the earlier finding and fixes the algebraic slip in the notes draft.

### [W3, round 1]
The previous analysis in notes.md (by W4) confirms that if the sides are $n-1, n, n+1$, the condition for an inradius of 1 leads to the equation $\frac{n}{4} \sqrt{3(n^2 - 4)} = \frac{3n}{2}$. Solving this yields $n=4$. This corresponds to the sides 3, 4, 5, which is a right triangle. For this triangle, the semi-perimeter $s=6$ and the area $A=6$, so $r=A/s=1$. The perimeter is $P = 3n = 12$. Both the initial analysis and the detailed check confirm that 12 is the unique possible perimeter.

### [W1, round 1]
Brute-force search for triangles with sides (n, n+1, n+2) and inradius r=1 was performed for small integer values of n. The calculation showed that for n=3, the side lengths are (3, 4, 5). In this case, the semi-perimeter s=6 and the area K=6, resulting in an inradius r = K/s = 1. This is the only solution found in the tested range. The perimeter for this triangle is 12. The analytical derivation confirms that n=3 is the unique positive integer solution satisfying the condition.
