### [W4, round 1]
Analysis of $ab=2cd$ with $c=gx', d=gy'$ and $\gcd(x', y')=1$.
The condition that $a$ and $b$ are integers requires the discriminant $D$ of $t^2 - g(x'+y')t + 2g^2 x'y' = 0$ to be a perfect square.
$D = g^2 [(x'+y')^2 - 8x'y']$.
We require $M = x'^2 - 6x'y' + y'^2$ to be a perfect square, $K'^2$.
For $a$ and $b$ to be positive integers, we must have $M \ge 0$, which implies $y'/x' \ge 3 + 2\sqrt{2} \approx 5.828$ (assuming $y' \ge x'$).

The simplest solution found is $(x', y') = (1, 6)$, which gives $M = 1^2 - 6(1)(6) + 6^2 = 1$. So $K'=1$.
For this pair, $a$ and $b$ are found to be $3g$ and $4g$ (up to permutation).
The resulting value for $R = \frac{c^2 +d^2}{cd} = \frac{c}{d} + \frac{d}{c}$ is $\frac{1}{6} + 6 = \frac{37}{6}$.
This value is constant for all $g \ge 1$ in this family.
Further investigation into other pairs $(x', y')$ is needed to ensure $\frac{37}{6}$ is the minimum possible ratio.

### [W1, round 1]
---
### Analysis of Quadruples (S=3 to S=10)

The goal is to find quadruples $(a, b, c, d)$ such that $a+b=c+d=S$ and $ab=2cd$. For $a, b$ to be positive integers, the discriminant of $x^2 - Sx + 2cd = 0$, which is $\Delta = S^2 - 8cd$, must be a perfect square ($m^2$). We calculate $f(c, d) = \frac{c}{d} + \frac{d}{c}$.

**S=3:** No solutions for (a, b).
**S=4:** No solutions for (a, b).
**S=5:** No solutions for (a, b).
**S=6:** No solutions for (a, b).
**S=7:**
*   (c, d) = (1, 6): $cd=6$. $2cd=12$. $x^2 - 7x + 12 = 0$. Roots are $a=3, b=4$. **VALID QUADRUPLE.** $f(1, 6) = 1/6 + 6/1 = 37/6$.
*   (c, d) = (2, 5): No solutions for (a, b).
*   (c, d) = (3, 4): No solutions for (a, b).
**S=8:** No solutions for (a, b).
**S=9:** No solutions for (a, b).
**S=10:** No solutions for (a, b).

**Summary:**
The only valid quadruple found in the range $S=3$ to $S=10$ is based on $(c, d) = (1, 6)$ (or $(6, 1)$), which yields $f(c, d) = 37/6$.
The maximum value of $f(c, d)$ found in this range is $37/6$.
---

### [W2, round 1]
Goal: Find the minimum value of $f(r) = r + 1/r$, where $r = c/d$ is a positive rational number satisfying $r^2 - 6r + 1 = Q^2$ for some rational $Q$, derived from the discriminant condition $D = S^2 - 8cd$ being a perfect square.

Derivation:
1. Let $S = c+d$. From (1), $a+b = S$. From (2), $ab = 2cd$.
2. $a$ and $b$ are roots of $x^2 - Sx + 2cd = 0$.
3. The discriminant is $D = S^2 - 8cd$.
4. Substitute $c = rd$: $S = d(r+1)$ and $cd = rd^2$.
5. $D = (d(r+1))^2 - 8rd^2 = d^2 [(r+1)^2 - 8r] = d^2 [r^2 + 2r + 1 - 8r] = d^2 (r^2 - 6r + 1)$.
6. For $a$ and $b$ to be integers, $D$ must be a perfect square. Since $d^2$ is a perfect square, $r^2 - 6r + 1$ must be the square of a rational number, $Q^2$.
7. This leads to the relationship: $r^2 - 6r + 1 = Q^2$.

Optimization:
We minimize $f(r) = r + 1/r$. This function is minimized when $r$ is closest to 1.
We solve $r^2 - 6r + 1 = Q^2$ by rewriting it as $(r-3)^2 - 8 = Q^2$, or $(r-3)^2 - Q^2 = 8$.
Setting $X = r-3$ and $Y = Q$, we solve $X^2 - Y^2 = 8$ for rational solutions $(X, Y)$.

We found solutions by setting $X$ and $Y$ values derived from integer factorizations of 8:
1. $X = 3, Y = 1 \implies r = 6$. $f(6) = 6 + 1/6 = 37/6$. (Verified solution $(3, 4, 6, 1)$).
2. $X = 9/2, Y = 7/2 \implies r = 15/2$. $f(15/2) = 15/2 + 2/15 = 229/30$. (Verified solution $(5, 12, 15, 2)$).

Since $37/6 = 5.166...$ and $229/30 = 7.633...$, the current minimum is $37/6$. Given that no solutions exist arbitrarily close to $r=1$, $k = 37/6$ is the maximum value satisfying the constraint.
