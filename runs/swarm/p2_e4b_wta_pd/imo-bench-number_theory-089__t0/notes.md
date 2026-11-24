### [W1, round 1]
Verification of inradius formula for consecutive integer sides (n-1, n, n+1):
The derived formula for the inradius is r = sqrt(3(n^2 - 4)) / 6.

Case n=3 (Sides 2, 3, 4):
Perimeter P = 9.
Calculated inradius r = sqrt(3(3^2 - 4)) / 6 = sqrt(15) / 6.

Case n=4 (Sides 3, 4, 5):
Perimeter P = 12.
Calculated inradius r = sqrt(3(4^2 - 4)) / 6 = 6 / 6 = 1.
This confirms the formula for the Pythagorean triple case.

### [W3, round 1]
Derivation for the inradius (r) of a triangle with sides n, n+1, n+2:
Semi-perimeter s = (3n+3)/2.
Area A = (n+1)/4 * sqrt(3(n+3)(n-1)).
Inradius r = A/s = 1/6 * sqrt(3(n^2 + 2n - 3)).

Solving r=1:
1 = 1/6 * sqrt(3(n^2 + 2n - 3))
36 = 3(n^2 + 2n - 3)
12 = n^2 + 2n - 3
n^2 + 2n - 15 = 0
(n+5)(n-3) = 0

Valid integer solutions for n:
We require n >= 2 for a valid triangle. Thus, n=3 is the only valid solution.
The perimeter P = 3n + 3.
For n=3, P = 3(3) + 3 = 12.
The only possible value for the perimeter is 12.

### [W2, round 1]
**Derivation: Inradius (r) in terms of central integer (n) for triangle sides (n-1, n, n+1)**

1.  **Sides and Semi-perimeter (s):**
    The side lengths are $a = n-1$, $b = n$, and $c = n+1$.
    The semi-perimeter $s$ is calculated as:
    $s = \frac{(n-1) + n + (n+1)}{2} = \frac{3n}{2}$.

2.  **Area ($\mathcal{A}$) using Heron's Formula:**
    We calculate the terms needed for Heron's formula:
    $s-a = \frac{3n}{2} - (n-1) = \frac{n+2}{2}$
    $s-b = \frac{3n}{2} - n = \frac{n}{2}$
    $s-c = \frac{3n}{2} - (n+1) = \frac{n-2}{2}$

    The area $\mathcal{A}$ is:
    $\mathcal{A} = \sqrt{s(s-a)(s-b)(s-c)}$
    $\mathcal{A} = \sqrt{\frac{3n}{2} \cdot \frac{n+2}{2} \cdot \frac{n}{2} \cdot \frac{n-2}{2}}$
    $\mathcal{A} = \sqrt{\frac{3n^2(n+2)(n-2)}{16}} = \frac{n}{4}\sqrt{3(n^2 - 4)}$.

3.  **Inradius (r):**
    Using the formula $\mathcal{A} = rs$, we have $r = \mathcal{A}/s$:
    $r = \frac{\frac{n}{4}\sqrt{3(n^2 - 4)}}{\frac{3n}{2}}$
    $r = \frac{n\sqrt{3(n^2 - 4)}}{4} \cdot \frac{2}{3n}$
    $r = \frac{2\sqrt{3(n^2 - 4)}}{12}$
    $r = \frac{\sqrt{3(n^2 - 4)}}{6}$.

This establishes the relationship $r = f(n)$. (Note: A triangle exists only if $n>2$).

### [W4, round 1]
Investigating the relationship between inradius (r=1) and consecutive side lengths $n, n+1, n+2$ using half-angle formulas.
Let the sides be $a=n, b=n+1, c=n+2$. The semi-perimeter is $s = (3n+3)/2$.
The tangent half-angle formulas give:
tan(A/2) = 1/(s-a) = 2/(n+3)
tan(B/2) = 1/(s-b) = 2/(n+1)
tan(C/2) = 1/(s-c) = 2/(n-1)

Using the identity tan(C/2) = (1 - tan(A/2)tan(B/2)) / (tan(A/2) + tan(B/2)), we derived:
tan(C/2) = (n^2 + 4n - 1) / (4(n+2)).

Equating this to the definition, we arrive at the cubic equation for $n$:
n^3 + 3n^2 - 13n - 15 = 0.
Since side lengths must be positive integers, we require $n > 1$. The integer solutions are $n=3$, $n=-1$, and $n=-5$. Only $n=3$ yields a valid physical triangle.
