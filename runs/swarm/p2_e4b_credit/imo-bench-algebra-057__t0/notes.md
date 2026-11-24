### [W1, round 1]
Analysis for N=2:
We analyze the equation $k_1 p + k_2 p^2 = 0$, where $p$ is positive rational, $k_1, k_2 \in \{-2, -1, 0, 1, 2\}$, and $(k_1, k_2) \neq (0, 0)$.
Factoring gives $p(k_1 + k_2 p) = 0$. Since $p>0$, we must have $k_1 + k_2 p = 0$.
If $k_2 = 0$, then $k_1 = 0$, which is disallowed. Thus $k_2 \neq 0$.
We solve for $p$: $p = -k_1/k_2$.
Since $p > 0$, $k_1$ and $k_2$ must have opposite signs.
If $k_1 = 0$, then $p=0$, which is disallowed since $p$ must be positive. Thus $k_1 \neq 0$.
Possible values for $p$ derived from combinations where $k_1, k_2 \in \{-2, -1, 1, 2\}$ and $\text{sgn}(k_1) = -\text{sgn}(k_2)$:
1. $k_1 > 0, k_2 < 0$: $p \in \{1, 1/2, 2\}$.
2. $k_1 < 0, k_2 > 0$: $p \in \{1, 1/2, 2\}$.
The set of all possible values for $p$ when $N=2$ is $\{1/2, 1, 2\}$.

### [W3, round 1]
CASE p=1:
Let $a_n$ and $b_n$ be the values added by Alice and Bob at minute $n$. Since $p=1$, $a_n, b_n \in \{1, 0, -1\}$.
The condition $S_A(N) = S_B(N)$ requires $\sum_{n=1}^{N} (a_n - b_n) = 0$.
Let $d_n = a_n - b_n$. Possible values for $d_n$ are $\{-2, -1, 0, 1, 2\}$.
A solution exists if and only if there is a finite sequence $(d_1, d_2, \ldots, d_N)$ such that:
1. $\sum_{n=1}^{N} d_n = 0$.
2. At least one $d_n \neq 0$.
3. Each $d_n$ corresponds to a valid pair $(a_n, b_n) \in \{-1, 0, 1\}^2$. (This is always possible for $d_n \in \{-2, -1, 0, 1, 2\}$).

Therefore, a solution exists for any $N \geq 2$ (e.g., $N=2$ with $d_1=1, d_2=-1$).
The required sequence of coefficients/differences is any non-zero, zero-sum sequence $(d_n)$ whose elements are in $\{-2, -1, 0, 1, 2\}$.

### [W2, round 1]
Analysis for N=3:
The condition that the totals are equal after 3 minutes leads to the equation:
k_1 p + k_2 p^2 + k_3 p^3 = 0
where p is a positive rational number, and k_n = c_A,n - c_B,n must be an integer in {-2, -1, 0, 1, 2}.
The constraint requires that at least one k_n is non-zero.

Since p > 0, we divide by p to get:
k_3 p^2 + k_2 p + k_1 = 0

Case 1: k_3 = 0.
k_2 p + k_1 = 0 => p = -k_1 / k_2.
For p > 0, k_1 and k_2 must have opposite signs, and |k_1|, |k_2| in {1, 2}.
Possible positive rational values for p are {1/2, 1, 2}.

Case 2: k_3 != 0.
This is a quadratic equation. We check cases where the resulting positive rational roots are found.

1. Check p=1: k_3 + k_2 + k_1 = 0. E.g., (1, -2, 1) works. p=1 is a solution.
2. Check p=2: 4k_3 + 2k_2 + k_1 = 0. E.g., (1, -1, -2) works. p=2 is a solution.
3. Check p=1/2: k_3/4 + k_2/2 + k_1 = 0. Multiply by 4: k_3 + 2k_2 + 4k_1 = 0. E.g., (2, -2, 0) fails (k1=0). Try (0, -2, 1): 0 + 2(-2) + 4(1) = 0. p=1/2 is a solution.

The possible rational values for p found are {1/2, 1, 2}.

### [W4, round 1]
Analysis of $\sum_{n=1}^N k_n p^n = 0$ for integer $p \ge 2$.

The coefficients $k_n = a_n - b_n$ are bounded such that $k_n \in \{-2, -1, 0, 1, 2\}$. Since at least one $k_n \neq 0$, we seek non-trivial solutions.

We rewrite the equation as:
$$\sum_{n: k_n > 0} k_n p^n = -\sum_{n: k_n < 0} k_n p^n = \sum_{n: k_n < 0} (-k_n) p^n$$
Let $K^+$ be the left side and $K^-$ be the right side. $K^+ = K^-$.

Assume $N$ is the largest index such that $k_N \neq 0$. We examine the magnitude of $K^+$ and $K^-$ relative to $p^N$.

1.  **Case $k_N > 0$ (i.e., $k_N=1$ or $k_N=2$):**
    $K^+ \ge k_N p^N$.
    $K^- = \sum_{n=1}^{N-1} (-k_n) p^n$. The maximum possible value for $K^-$ occurs when all $k_n$ for $n<N$ are $-2$ (meaning $-k_n=2$).
    $$K^- \le \sum_{n=1}^{N-1} 2 p^n = 2p \frac{p^{N-1} - 1}{p-1}$$
    For a solution to exist, we must have $k_N p^N \le K^-$.

    *   **If $k_N = 2$:**
        $2p^N \le 2p \frac{p^{N-1} - 1}{p-1}$
        $p^N (p-1) \le p \cdot p^{N-1} - p$
        $p^{N+1} - p^N \le p^N - p$
        $p^{N+1} - 2p^N \le -p$
        $p^N(p - 2) \le -p$.
        If $p=2$, this implies $0 \le -2$, which is false.
        If $p \ge 3$, then $p-2 \ge 1$, so $p^N(p-2) > 0$, which contradicts $p^N(p-2) \le -p < 0$.
        Thus, if $k_N=2$, no solution exists for any $p \ge 2$.

    *   **If $k_N = 1$:**
        $p^N \le 2p \frac{p^{N-1} - 1}{p-1}$
        $p^N (p-1) \le 2p(p^{N-1} - 1)$
        $p^{N+1} - p^N \le 2p^N - 2p$
        $p^{N+1} - 3p^N \le -2p$
        $p^N(p - 3) \le -2p$.

        *   If $p=2$: $2^N(2 - 3) \le -4$, which means $-2^N \le -4$, or $2^N \ge 4$. This requires $N \ge 2$.
        *   If $p=3$: $3^N(3 - 3) \le -6$, which means $0 \le -6$. This is false.
        *   If $p \ge 4$: $p-3 \ge 1$, so $p^N(p-3) > 0$, which contradicts $p^N(p - 3) \le -2p < 0$.

2.  **Case $k_N < 0$ (i.e., $k_N=-1$ or $k_N=-2$):**
    By symmetry, if $k_N=-2$, no solution exists.
    If $k_N=-1$, we must have $(-1) p^N + \sum_{n=1}^{N-1} k_n p^n = 0$.
    $\sum_{n=1}^{N-1} k_n p^n = p^N$.
    The maximum possible value for the sum on the left is $2 \sum_{n=1}^{N-1} p^n$.
    We require $p^N \le 2 \sum_{n=1}^{N-1} p^n$.
    $p^N \le 2p \frac{p^{N-1} - 1}{p-1}$. This leads to the exact same constraint: $p^N(p-3) \le -2p$.

**Conclusion:**
For $\sum k_n p^n = 0$ to have a non-trivial solution ($k_n$ not all zero), $p$ must be $p=2$. For $p \ge 3$, the only possible solution is $k_n=0$ for all $n$, which violates the problem constraints.

The required constraints are:
1. $p$ must be $p=2$.
2. If $N$ is the largest index such that $k_N \neq 0$, then $k_N$ must be $\pm 1$.
3. Furthermore, $N$ must satisfy $N \ge 2$ (from the $p=2$ case constraint $2^N \ge 4$).

### [W1, round 2]
Reviewing W3's conclusion for p=1:
The condition for the blackboards to display the same number is $\sum_{n=1}^{N} d_n = 0$, where $d_n = a_n - b_n$, and $a_n, b_n \in \{-1, 0, 1\}$.
The problem requires that at least one different choice was made during the process. A "different choice" means $(a_n, b_n) \neq (0, 0)$ for at least one $n$.
W3 correctly identifies that a solution exists if and only if there is a non-zero, zero-sum sequence $(d_n)$.
We confirm that if $(d_n)$ is non-zero, then at least one $d_k \neq 0$. Since $d_k = a_k - b_k \neq 0$, it implies $a_k \neq b_k$. If $a_k \neq b_k$, it is impossible that $a_k=0$ AND $b_k=0$. Therefore, $d_k \neq 0$ implies $(a_k, b_k) \neq (0, 0)$, satisfying the constraint that at least one different choice was made. W3's conclusion is verified.

### [W4, round 2]
### [W4, round 2] Rigorous Proof for p=2 and p=1/2

We analyze the equation $\sum_{n=1}^N k_n p^n = 0$, where $p$ is a positive rational number and $k_n = a_n - b_n$, with $a_n, b_n \in \{p^n, 0, -p^n\}$. We must show that for $p=2$ and $p=1/2$, the only solution is $k_n=0$ for all $n$.

**Case 1: p = 2**
Let $P_n = 2^n$. The possible values for $k_n = a_n - b_n$ are $k_n \in \{-2^n, 0, 2^n, 2 \cdot 2^n\}$.
We can write $k_n = d_n 2^n$, where $d_n \in \{-1, 0, 1, 2\}$.
Substituting this into the equation:
$$\sum_{n=1}^N d_n 2^n \cdot 2^n = 0 \implies \sum_{n=1}^N d_n 4^n = 0$$
We rearrange the equation to isolate the highest power term:
$$d_N 4^N = - \sum_{n=1}^{N-1} d_n 4^n$$
Dividing by $4^N$:
$$d_N = - \sum_{n=1}^{N-1} d_n 4^{n-N} = - \left( d_{N-1} 4^{-1} + d_{N-2} 4^{-2} + \cdots + d_1 4^{-(N-1)} 4^{-1} \right)$$
We bound the absolute value of the right-hand side (RHS):
$$|d_N| \le \sum_{n=1}^{N-1} \frac{|d_n|}{4^{N-n}}$$
Since $|d_n| \le 2$, we have:
$$|d_N| \le 2 \sum_{n=1}^{N-1} (1/4)^{N-n} = 2 \left( (1/4)^{N-1} + (1/4)^{N-2} + \cdots + 1/4 \right)$$
This is a finite geometric series $\sum_{j=1}^{N-1} (1/4)^j$.
$$\sum_{j=1}^{N-1} (1/4)^j = \frac{1/4 (1 - (1/4)^{N-1})}{1 - 1/4} = \frac{1/3}{4} (1 - 4^{-(N-1)}) < \frac{1/3}{4} \cdot 1 / (1 - 1/4) = 1/3$$
Wait, this summation formula is wrong. The sum is $\frac{a(1-r^m)}{1-r}$. Here $a=1/4$, $r=1/4$, $m=N-1$.
$$\sum_{j=1}^{N-1} (1/4)^j = \frac{1/4 (1 - (1/4)^{N-1})}{3/4} = \frac{1}{3} (1 - 4^{-(N-1)})$$
Thus,
$$|d_N| \le 2 \cdot \frac{1}{3} (1 - 4^{-(N-1)}) < 2/3$$
Since $d_N$ must be an integer, we conclude $d_N = 0$.
By working backward (i.e., setting $N' = N-1$ and repeating the argument), we show $d_{N-1}=0$, and inductively, $d_n=0$ for all $n$. Therefore, $k_n=0$ for all $n$.

**Case 2: p = 1/2**
Let $P_n = (1/2)^n$. The possible values for $k_n = a_n - b_n$ are $k_n \in \{-1/2^n, 0, 1/2^n, 2/2^n\}$.
We can write $k_n = d_n / 2^n$, where $d_n \in \{-1, 0, 1, 2\}$.
Substituting this into the equation:
$$\sum_{n=1}^N \frac{d_n}{2^n} \left(\frac{1}{2}\right)^n = 0 \implies \sum_{n=1}^N d_n \frac{1}{4^n} = 0$$
Multiplying by $4^N$:
$$\sum_{n=1}^N d_n 4^{N-n} = 0$$
Isolating the highest power term, $d_N$:
$$d_N = - \sum_{n=1}^{N-1} d_n 4^{n-N} = - \sum_{n=1}^{N-1} \frac{d_n}{4^{N-n}}$$
Since $|d_n| \le 2$, we bound the RHS:
$$|d_N| \le 2 \sum_{n=1}^{N-1} (1/4)^{N-n}$$
This is exactly the same bound as in Case 1, leading to $|d_N| < 2/3$.
Therefore, $d_N = 0$. By induction, $d_n=0$ for all $n$. Thus, $k_n=0$ for all $n$.

This completes the proof that for $p=2$ and $p=1/2$, the equation admits no non-trivial solution for $N \ge 2$.
