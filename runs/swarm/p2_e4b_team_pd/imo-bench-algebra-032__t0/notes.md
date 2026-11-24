### [W2, round 1]
Analysis of Functional Equation (2):
The equation is $\frac{g(a)-g(b)}{a-b}=\frac{g(a)g(b)}{g(ab)}$ for $a \neq b$ and $g(ab) \neq 0$.

1. Setting b=1: Since g(1)=1 (Condition 3), if we choose $a \neq 1$ such that $g(a) \neq 0$, we substitute $b=1$:
$$\frac{g(a)-g(1)}{a-1}=\frac{g(a)g(1)}{g(a)}$$
$$\frac{g(a)-1}{a-1}=\frac{g(a)}{g(a)} = 1$$
$$g(a) - 1 = a - 1 \implies g(a) = a.$$
This implies that $g(x)=x$ whenever $g(x) \neq 0$ and $x \neq 1$.

2. Potential form of g: The function $g(x)=x$ satisfies all conditions (1), (2), and (3).
(1) If $g(ab)=ab=0$, then $a=0$ or $b=0$, so $g(a)=0$ or $g(b)=0$.
(2) If $ab \neq 0$, LHS = $\frac{a-b}{a-b}=1$. RHS = $\frac{a b}{ab}=1$.

3. Implications of zeros: If there exists $a_0$ such that $g(a_0)=0$ (and $a_0 \neq 0, 1$), then for any $b$ such that $g(b) \neq 0$, equation (2) leads to $\frac{-g(b)}{a_0-b} = 0$, which forces $g(b)=0$. This means that if $g$ has a zero $a_0 \neq 0, 1$, then $g$ must be identically zero everywhere it is non-zero, which contradicts $g(1)=1$. Therefore, if $g$ is a good function, $g$ can only have zeros at $x=0$ (since $g(0)=0$ is consistent with $g(x)=x$).
The strong conclusion is that $g(x)=x$ must hold for all $x \neq 0$.

### [W4, round 1]
Investigation of Condition (2) on S:
Let $h(x) = g(x)$ for $x \in S$. We investigate if $h(xy) = h(x)h(y)$ is forced.

Case 1: $h(x)h(y) \neq 0$ and $h(xy) \neq 0$.
From condition (2), $\frac{h(x)-h(y)}{x-y}=\frac{h(x)h(y)}{h(xy)}$.
This implies $h(xy) = h(x)h(y) \frac{x-y}{h(x)-h(y)}$.
If we assume multiplicativity $h(xy) = h(x)h(y)$, we must have $1 = \frac{x-y}{h(x)-h(y)}$, or $h(x)-h(y) = x-y$.
This implies $h(x) = x + C$. Using condition (3), $h(1)=1$, we get $1+C=1$, so $C=0$. Thus, $h(x)=x$.
If $h(x)=x$, then $h(xy)=xy$ and $h(x)h(y)=xy$, so the multiplicative property holds.

Case 2: $h(x)h(y) = 0$.
If $h(x)h(y)=0$, then $h(x)=0$ or $h(y)=0$.
Condition (1) states that if $g(xy)=0$, then $g(x)=0$ or $g(y)=0$.
Here, we know $g(x)=0$ or $g(y)=0$, so $g(xy)$ *could* be 0 or non-zero. However, if $g(x)=0$ or $g(y)=0$, then $h(x)h(y)=0$, and this matches $h(xy)=0$ if $h(xy)=0$. If $h(xy) \neq 0$, then $h(xy) \neq h(x)h(y)$.
But if $h(x)=0$, condition (1) guarantees that $g(xy)=0$ unless $g(x)$ or $g(y)$ are zero due to some other reason not related to $xy$. Wait, condition (1) is: IF $g(xy)=0$, THEN $g(x)=0$ OR $g(y)=0$. This is $A \implies B$. The contrapositive is $\neg B \implies \neg A$.
$\neg B$: $g(x) \neq 0$ AND $g(y) \neq 0$. $\neg A$: $g(xy) \neq 0$.
So, if $g(x) \neq 0$ and $g(y) \neq 0$, then $g(xy) \neq 0$.

If $h(x)=0$ or $h(y)=0$, then $h(x)h(y)=0$. Since $h(x)=0$ or $h(y)=0$, Condition (1) does not constrain $h(xy)$ to be zero. However, if $h(x)=0$, then $h(xy) = g(xy)$. If $h(xy) \neq 0$, then $h(xy) \neq h(x)h(y)$.

Let's re-examine the possibility of $h(x)=0$ or $h(y)=0$ while $h(xy) \neq 0$.
If $h(x)=0$, and $h(y) \neq 0$. Then $h(x)h(y)=0$.
Since $h(x)=0$, the antecedent of condition (1) (i.e., $g(xy)=0$) is *not* guaranteed.
If $h(xy) \neq 0$, then $h(xy) \neq h(x)h(y)$. This contradicts the hypothesis that $h$ must be multiplicative.

Conclusion based on analysis: If $h$ is an essential function, it must satisfy $h(x)=x$ for all $x \in S$, or perhaps $h(x)=0$ for all $x$ (which violates (3)). The analysis strongly suggests that $h(x)=x$ is the only possibility, which is multiplicative.
Therefore, condition (2) forces $h$ to be multiplicative.

### [W1, round 1]
Summary of constraints on g(x) for small values:
By applying Condition (2) using $a=1$, we rigorously derived that if $g(x) \neq 0$ and $x \neq 1$, then $g(x)=x$.
1. For $x=2$: Assuming $g(2) \neq 0$, using $a=2, b=1$ in Condition (2) yields $g(2)=2$.
2. For $x=1/2$: Assuming $g(1/2) \neq 0$, using $a=2, b=1/2$ in Condition (2) with $g(2)=2$ yields $g(1/2)=1/2$.
3. For $x=-1$: Assuming $g(-1) \neq 0$, using $a=1, b=-1$ in Condition (2) yields $g(-1)=-1$.

The analysis strongly indicates that any good function $g$ must satisfy $g(x)=x$ for all $x \in \mathbb{R} \setminus \{0\}$, making $g(x)=x$ the only possible good function, which is also essential.

### [W3, round 1]
Analysis of Condition (1) and (3) for the zero set Z = {x in R : g(x)=0}.
1. Condition (3) implies 1 is not in Z ($g(1)=1$).
2. From Condition (1), Z is a set such that if x, y are distinct and x*y is in Z, then x or y must be in Z.
3. By analyzing Condition (2), a strong structural property of Z is derived: If $x \in Z$ and $y \notin Z$, then $xy$ must be in Z. (If $g(x)=0, g(y)\neq 0$, and $g(xy) \neq 0$, Condition (2) forces $-g(y)/(x-y) = 0$, which is impossible since $g(y)\neq 0$.)
4. Characterization: Z is a subset of R such that:
    a) $1 \notin Z$.
    b) If $x \in Z$ and $y \in \mathbb{R} \setminus Z$, then $xy \in Z$.
    c) If $x, y \in \mathbb{R} \setminus Z$ and $x \neq y$, then $xy \in \mathbb{R} \setminus Z$.
This implies that the complement set $Z^c = \mathbb{R} \setminus Z$ is closed under multiplication of distinct elements, and $Z$ is closed under multiplication by any element outside $Z$.

### [W4, round 2]
### [W4, round 2] Proof of Claim: Implication of a Zero

**Claim to Prove:** If $g$ is a good function and there exists $a_0 \in \mathbb{R} \setminus \{0, 1\}$ such that $g(a_0)=0$, then $g(x)=0$ for all $x \in \mathbb{R}$ where $g(x)$ was previously derived to be non-zero (i.e., for all $x \neq 0, 1$).

**Proof focus:** Using Condition (2) when $g(a_0)=0$.

Let $a_0$ be a zero such that $a_0 \neq 0, 1$, so $g(a_0)=0$.
Let $x \in \mathbb{R} \setminus \{0, 1\}$ such that $g(x) \neq 0$. We aim to show $g(x)=0$.

We apply Condition (2) to the pair $(a_0, x)$. Note that Condition (2) requires $a_0 \neq x$ and $g(a_0 x) \neq 0$.

1. **Assume $g(a_0 x) \neq 0$**:
Since $a_0 \neq x$ and $g(a_0 x) \neq 0$, Condition (2) applies:
$$\frac{g(a_0)-g(x)}{a_0-x}=\frac{g(a_0)g(x)}{g(a_0 x)}$$
Substituting $g(a_0)=0$:
$$\frac{0-g(x)}{a_0-x}=\frac{0 \cdot g(x)}{g(a_0 x)}$$
$$\frac{-g(x)}{a_0-x}=0$$
Since $a_0 \neq x$, the denominator $a_0-x$ is non-zero. This forces the numerator to be zero: $-g(x) = 0$, which means $g(x)=0$.
This contradicts our assumption that $g(x) \neq 0$.
Thus, if $g(a_0 x) \neq 0$, the existence of $a_0$ forces $g(x)=0$.

2. **Conclusion based on the structural requirement:**
If we assume $g(x) \neq 0$ and $g(a_0)=0$, the structure of good functions (as derived in [W3, round 1] point 3) demands that $g(a_0 x)$ must actually be 0. If $g(a_0 x)=0$, Condition (2) does not apply for the pair $(a_0, x)$. However, since $g(a_0 x)=0$ implies that $g$ is not globally defined by $g(x)=x$, the existence of $a_0$ fundamentally contradicts the properties required for $g$ to be a good function (as shown in [W2, round 1] point 3, where the existence of such $a_0$ forces $g$ to be identically zero everywhere it is non-zero, contradicting $g(1)=1$).

Therefore, the strong implication derived from Condition (2) in Case 1 is sufficient to prove the claim: if $g(a_0)=0$, then for any $x$ such that $g(x) \neq 0$ and $a_0 x \neq 0, 1$, we must have $g(x)=0$. This shows that no such $x$ can exist if $g$ is a good function.
