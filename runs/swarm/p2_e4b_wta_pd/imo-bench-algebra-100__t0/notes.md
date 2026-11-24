### [W1, round 1]
Tested symmetric case x=y=z. Solutions found: (1, 1, 1) and (-1, -1, -1).
Checked permutations of (1, 1, -1) and (1, -1, -1) for integer solutions. None satisfied E2=3.
Specifically, for permutations of (1, 1, -1), E1=3 but E2=-1.

### [W2, round 1]
### W2 Analysis of E2 Structure
The equation $E_2 = xy^3 + yz^3 + zx^3$ is a cyclic polynomial of degree 4. The constraint $E_1 = x^2 + y^2 + z^2 = 3$ defines a sphere.
A direct algebraic rewriting of $E_2$ using $E_1$ (e.g., substituting $x^2 = 3 - y^2 - z^2$) leads to highly complex expressions, suggesting that simple cancellations or obvious linear factors are unlikely unless $x, y, z$ satisfy specific relations (like $x=y=z$).
The structure strongly suggests looking for solutions with high symmetry, which we have confirmed include $(1, 1, 1)$ and $(-1, -1, -1)$. Further investigation should focus on reducing the system using cyclic symmetry or parameterizing the intersection of the surface defined by $E_2=3$ and the sphere $E_1=3$.

### [W4, round 1]
Case x=y: Investigated the reduced system $2x^2 + z^2 = 3$ and $x^4 + xz^3 + zx^3 = 3$. Found the integer solution $(1, 1, 1)$ by testing $x=1$. This solution satisfies the original system: $1^2+1^2+1^2 = 3$ and $1(1^3) + 1(1^3) + 1(1^3) = 3$. Due to symmetry, other permutations are also solutions.

### [W3, round 1]
Goal: Use inequalities to constrain $(x, y, z)$ given $E_1 = x^2 + y^2 + z^2 = 3$ and $E_2 = xy^3 + yz^3 + zx^3 = 3$.

1. Apply Cauchy-Schwarz (CS) to $E_2 = x(y^3) + y(z^3) + z(x^3)$.
$E_2^2 = (x \cdot y^3 + y \cdot z^3 + z \cdot x^3)^2 \le (x^2 + y^2 + z^2) ((y^3)^2 + (z^3)^2 + (x^3)^2)$
Since $E_1 = 3$, we have:
$E_2^2 \le 3 (x^6 + y^6 + z^6)$.
Since $E_2 = 3$, $9 \le 3 (x^6 + y^6 + z^6)$, which implies $x^6 + y^6 + z^6 \ge 3$.

2. Use Power Mean Inequality (or Jensen's) on $u=x^2, v=y^2, w=z^2$.
We have $u+v+w = 3$. We need to constrain $u^3+v^3+w^3 = x^6+y^6+z^6$.
Since $f(t) = t^3$ is convex for $t \ge 0$:
$\frac{u^3 + v^3 + w^3}{3} \ge \left( \frac{u+v+w}{3} \right)^3$
$x^6 + y^6 + z^6 \ge 3 \left( \frac{3}{3} \right)^3 = 3$.

3. Conclusion on necessary condition:
Both constraints require $x^6 + y^6 + z^6 \ge 3$. Equality holds if and only if $u=v=w$, which means $x^2 = y^2 = z^2$.
Since $x^2+y^2+z^2 = 3$, we must have $3x^2 = 3$, so $x^2 = 1$.
Therefore, any solution $(x, y, z)$ must satisfy $x, y, z \in \{-1, 1\}$.

4. Further checks (assuming $x, y, z \in \{-1, 1\}$):
If $x^2=y^2=z^2=1$, then $x^3=x, y^3=y, z^3=z$.
$E_2 = xy + yz + zx$. We require $xy + yz + zx = 3$.
Since $x^2+y^2+z^2 = 3$, we have $(x+y+z)^2 = 3 + 2(3) = 9$, so $x+y+z = \pm 3$.
If $x+y+z=3$, then $x=y=z=1$. (Solution found)
If $x+y+z=-3$, then $x=y=z=-1$. (Solution found)

The inequality analysis strongly constrains the solutions to be exactly those two found above.
