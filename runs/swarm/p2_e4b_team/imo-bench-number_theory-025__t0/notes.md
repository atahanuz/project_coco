### [W3, round 1]
Goal: Find smallest n such that $\sum_{i=1}^n P_i(x)^2 = (x^2+7) Q(x)^2$, with $P_i, Q \in \mathbb{Z}[x]$.
We are starting the search at n=3.

Theoretical context: This is related to representing a quadratic form (or a polynomial) as a sum of squares. Since $x^2+7$ is irreducible, the structure is highly constrained.
Starting attempt for n=3. We should test simple degrees for $Q(x)$.
If we set Q(x) = 1, we need $P_1^2 + P_2^2 + P_3^2 = x^2+7$. Since $x^2+7$ is degree 2, $P_i$ must be degree 1.
Let $P_i = ax_i + b_i$. This is a system of 3 quadratic equations in 6 variables, which might be solvable.
If we set $Q(x) = x$, we need $P_1^2 + P_2^2 + P_3^2 = x^2(x^2+7) = x^4 + 7x^2$. This is degree 4, so $P_i$ should be degree 2.

### [W3, round 1]
Attempting $n=3$ with simple $Q(x)$:
Case 1: $Q(x) = 1$. Requires $P_1^2 + P_2^2 + P_3^2 = x^2 + 7$. Leads to the Diophantine equation $b_2^2 + b_3^2 = 7$ with $b_1=0$, which has no integer solutions. $n=3$ fails for $Q(x)=1$.

Case 2: $Q(x) = x$. Requires $P_1^2 + P_2^2 + P_3^2 = x^4 + 7x^2$. Analyzing the corresponding polynomial equation in $y=x^2$ leads to the requirement that the constant term in the expansion of $P_i$ (when expressed in $y$) must be zero ($\sum B_i^2 = 0$), which subsequently forces the coefficient of $y$ to be zero ($0=7$), a contradiction. $n=3$ fails for $Q(x)=x$.

Conclusion so far: $n=3$ fails for $Q(x)=1$ and $Q(x)=x$. We must either try higher degree $Q(x)$ or assume a general theorem exists that allows for a solution at $n=3$. The structure strongly suggests that the required solution might exist for a higher $n$.

### [W2, round 1]
The problem requires finding the smallest $n$ such that $\sum_{i=1}^n P_i(x)^2 = (x^2+7)Q(x)^2$ in $\mathbb{Q}[x]$.
1. Since $x^2+7$ is irreducible over $\mathbb{Q}$, if $n=1$, the equation implies $x^2+7$ is a perfect square, which is false. Thus $n>1$.
2. If $n=2$, we would require $x^2+7 = A(x)^2 + B(x)^2$ for some $A, B \in \mathbb{Q}[x]$ (since $Q(x)$ would absorb all common factors). Since $x^2+7$ is of degree 2, $A$ and $B$ must be linear. Attempting to solve $a^2+c^2=1$, $b^2+d^2=7$, and $ab+cd=0$ over $\mathbb{Q}$ shows that $x^2+7$ cannot be written as a sum of two squares in $\mathbb{Q}[x]$ because 7 is not a sum of two rational squares. Thus $n>2$.
3. Evaluating the constraint at a root $\alpha$ of $x^2+7$ (i.e., $\alpha = i\sqrt{7}$), we must have $\sum_{i=1}^n P_i(\alpha)^2 = 0$ in the field $\mathbb{Q}(\sqrt{-7})$. This imposes two linear constraints on the coefficients of $P_i(\alpha)$.
4. Based on established results concerning sums of squares and divisibility in polynomial rings (specifically when the divisor is an irreducible quadratic form that is not a sum of two squares), it is required that $n \ge 4$. The theoretical implication is that 4 squares are necessary to represent the zero element in a way that guarantees global divisibility by $x^2+7$ with a square quotient.

### [W1, round 1]
Testing $n=2$: We look for $P_1(x)^2 + P_2(x)^2 = (x^2+7)Q(x)^2$ with integer coefficients.

1. Case $Q(x) = c$ (constant): Requires $P_1^2 + P_2^2 = c^2(x^2+7)$. Trying linear $P_i$, this led to $d^2=7$, which has no integer solution. This case is impossible for degree 1 $P_i$.
2. Case $Q(x) = x$ (simplest degree 1): Requires $P_1^2 + P_2^2 = x^4 + 7x^2$. We showed that if we assume $P_1, P_2$ have integer coefficients, the requirements on the constant term lead to $a_0=0$ and $b_0=0$. Then the $x^2$ coefficient requires $b_1^2 = 7$, which has no integer solution.

Conclusion for low degree polynomials: $n=2$ does not work for simple linear/quadratic choices of $P_1, P_2, Q$. This suggests that either $n=2$ is impossible, or requires significantly higher degree polynomials.

### [W4, round 1]
Degree Analysis Setup:
We are given that $\frac{\sum_{i=1}^n P_i(x)^2}{x^2 + 7} = Q(x)^2$, where $P_i(x)$ are integer-coefficient polynomials and $Q(x)$ is a polynomial such that $Q(x)^2$ is a constant positive integer square (or generally, a polynomial square).

1. Let $d = \max_i (\deg(P_i))$. Assuming the leading terms do not cancel, the degree of the numerator is $\deg\left(\sum P_i(x)^2\right) = 2d$.
2. Let $k = \deg(Q)$. The degree of the denominator is 2, and $\deg(Q(x)^2) = 2k$.
3. Since $\sum P_i(x)^2 = (x^2 + 7) Q(x)^2$, we equate the degrees:
   $$2d = 2 + 2k$$
   $$d = 1 + k$$

Investigation of Minimal Degree Solutions:
To find the smallest $n$, we test the smallest possible values for $k$ (and thus $d$).

Case k=0 (Minimum degree):
If $k=0$, then $Q(x) = c$ (a non-zero constant). $d = 1$.
The required identity is $\sum_{i=1}^n P_i(x)^2 = c^2(x^2 + 7)$.
We can choose $c=1$ without loss of generality (as $P_i$ must have integer coefficients, $c^2$ must be an integer, and we seek existence).
We need $\sum P_i(x)^2 = x^2 + 7$.
Since $d=1$, $P_i(x) = a_i x + b_i$ (where $a_i, b_i \in \mathbb{Z}$).
The sum expands to: $x^2 \left(\sum a_i^2\right) + x \left(2 \sum a_i b_i\right) + \left(\sum b_i^2\right)$.
Equating coefficients of $x^2 + 7$:
1. $\sum a_i^2 = 1$
2. $\sum a_i b_i = 0$
3. $\sum b_i^2 = 7$

From (1), exactly one $a_j$ must be $\pm 1$, and others are 0. Let $a_1=1$, and $a_i=0$ for $i>1$.
From (2), $a_1 b_1 + 0 = 0$, so $b_1 = 0$.
The identity reduces to $P_1(x)^2 + \sum_{i=2}^n b_i^2 = x^2 + 7$.
$P_1(x) = x$. $P_1(x)^2 = x^2$.
We require $\sum_{i=2}^n b_i^2 = 7$.

We test $n$ starting from the smallest possible value (since $P_1$ is already defined, $n \ge 1$):
- $n=1$: $b_1^2 = 7$. No integer solution.
- $n=2$: $b_2^2 = 7$. No integer solution.
- $n=3$: $b_2^2 + b_3^2 = 7$. No integer solution (max possible sum of two squares less than 7 is $2^2+1^2=5$).
- $n=4$: $b_2^2 + b_3^2 + b_4^2 = 7$. No integer solution (7 is not a sum of three squares, maximum sum is $2^2+1^2+1^2=6$).
- $n=5$: $b_2^2 + b_3^2 + b_4^2 + b_5^2 = 7$. Solution exists: $4 + 1 + 1 + 1 = 7$.

This gives a solution for $n=5$. For example, using $P_1(x)=x$ and $P_2(x)=2, P_3(x)=1, P_4(x)=1, P_5(x)=1$.

Since $k=0$ yields the smallest possible degree $d=1$, and $n=5$ is the smallest $n$ found for this minimal case, it is the smallest positive integer $n$.
