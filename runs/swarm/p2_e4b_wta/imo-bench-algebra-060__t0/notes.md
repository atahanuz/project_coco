### [W2, round 1]
W2 analysis: Focusing on the representative case n=6.
S = (12+6)/p + (13-6)/q = 18/p + 7/q.
We seek to maximize S subject to 18/p + 7/q < 1.
If we set 18/p + 7/q = 1 exactly, we found solutions like p=19, q=133, which gives S=1 (violating the strict inequality).
To maximize S while ensuring S < 1, we must choose p and q such that 18/p and 7/q are both large fractions, but their sum stays below 1.
We tested p=20 (18/20 = 0.9). We need 7/q < 0.1, so q > 70.
Choosing q=71 gives S = 18/20 + 7/71 = 0.9 + 0.09859... = 0.99859...
This value is extremely close to 1, fulfilling the task requirement.

### [W1, round 1]
Plan: To show that the supremum of S is 1 for a fixed n, we must demonstrate that for any given $\epsilon > 0$, we can choose positive integers $p$ and $q$ such that $S < 1$ and $1 - S < \epsilon$.

Let $A = 12 + n$ and $B = 13 - n$. Since $1 \le n \le 12$, $A$ and $B$ are fixed positive integers ($13 \le A \le 24$, $1 \le B \le 12$).
We seek $p, q \in \mathbb{Z}^+$ such that:
$$S = \frac{A}{p} + \frac{B}{q} < 1 \quad \text{and} \quad 1 - S < \epsilon$$

Strategy: Fix $p$ relative to $A$ such that $A/p$ is close to 1, and then choose $q$ large enough such that $B/q$ fills the gap to reach 1, but just slightly less.

We choose $p = A + 1$. This is a fixed positive integer.
Then $\frac{A}{p} = \frac{A}{A+1} = 1 - \frac{1}{A+1}$.

The condition $S < 1$ becomes:
$$1 - \frac{1}{A+1} + \frac{B}{q} < 1$$
$$\frac{B}{q} < \frac{1}{A+1}$$
$$q > B(A+1)$$

The condition $1 - S < \epsilon$ becomes:
$$1 - \left(1 - \frac{1}{A+1} + \frac{B}{q}\right) < \epsilon$$
$$\frac{1}{A+1} - \frac{B}{q} < \epsilon$$
$$\frac{1}{A+1} - \epsilon < \frac{B}{q}$$

Since we require $S < 1$, we must have $\epsilon < 1/(A+1)$. Assuming this holds, we rearrange the second inequality to bound $q$:
$$q < \frac{B}{\frac{1}{A+1} - \epsilon}$$

Thus, for any $\epsilon > 0$ (provided $\epsilon < 1/(A+1)$), we can choose an integer $q$ such that:
$$B(A+1) < q < \frac{B}{\frac{1}{A+1} - \epsilon}$$
Since the lower bound is finite and the upper bound is arbitrarily large as $\epsilon \to 0^+$, such an integer $q$ always exists.
This choice guarantees $S < 1$ and $1 - S < \epsilon$, proving that the supremum of $S$ is 1.
