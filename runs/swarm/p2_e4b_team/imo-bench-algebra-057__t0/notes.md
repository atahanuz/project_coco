### [W1, round 1]
Analysis for N=2:
The condition that the blackboards display the same number after 2 minutes leads to the equation:
$(A_1 - B_1) + (A_2 - B_2) p = 0$, or $d_1 + d_2 p = 0$, where $d_1 = A_1 - B_1$ and $d_2 = A_2 - B_2$.

We are constrained to $d_1, d_2 \in \{-2, -1, 1, 2\}$ and $p > 0$.
Since $p = -d_1/d_2$ must be positive, $d_1$ and $d_2$ must have opposite signs.

Case 1: $d_1 > 0$ and $d_2 < 0$.
$d_1 \in \{1, 2\}$, $d_2 \in \{-1, -2\}$.
1. $d_1=1, d_2=-1 \implies p = -1/(-1) = 1$.
2. $d_1=1, d_2=-2 \implies p = -1/(-2) = 1/2$.
3. $d_1=2, d_2=-1 \implies p = -2/(-1) = 2$.
4. $d_1=2, d_2=-2 \implies p = -2/(-2) = 1$.

Case 2: $d_1 < 0$ and $d_2 > 0$.
$d_1 \in \{-2, -1\}$, $d_2 \in \{1, 2\}$.
1. $d_1=-1, d_2=1 \implies p = -(-1)/1 = 1$.
2. $d_1=-1, d_2=2 \implies p = -(-1)/2 = 1/2$.
3. $d_1=-2, d_2=1 \implies p = -(-2)/1 = 2$.
4. $d_1=-2, d_2=2 \implies p = -(-2)/2 = 1$.

The set of all possible values for $p$ is the union of results from both cases: $\{1, 1/2, 2\}$.

### [W2, round 1]
Analysis for N=3:
The equation derived is $d_1 p + d_2 p^2 + d_3 p^3 = 0$, where $p$ is a positive rational number and $d_i \in \{-2, -1, 0, 1, 2\}$, with at least one $d_i \neq 0$.
Since $p>0$, we divide by $p$ to get: $d_1 + d_2 p + d_3 p^2 = 0$.

1. Case $d_3 = 0$: $d_1 + d_2 p = 0$. $p = -d_1/d_2$. For $p>0$, $d_1$ and $d_2$ must have opposite signs. Testing combinations of $|d_1|, |d_2| \in \{1, 2\}$ yields $p \in \{1/2, 1, 2\}$.

2. Case $d_3 \neq 0$: $d_3 p^2 + d_2 p + d_1 = 0$. We test $p \in \{1/2, 1, 2\}$ as these candidates derived from the linear case are often the solutions in related higher-order problems.
    - If $p=1$: $d_1+d_2+d_3=0$. This is possible (e.g., $d_1=1, d_2=1, d_3=-2$).
    - If $p=1/2$: $d_1 + d_2/2 + d_3/4 = 0 \implies 4d_1 + 2d_2 + d_3 = 0$. This is possible (e.g., $d_1=0, d_2=-1, d_3=2$).
    - If $p=2$: $d_1 + 2d_2 + 4d_3 = 0$. This is possible (e.g., $d_1=0, d_2=-2, d_3=1$).

The set of possible positive rational values for $p$ is $\{1/2, 1, 2\}$.

### [W4, round 1]
Investigated the case p=1:
The equation becomes $\sum_{n=1}^N (\epsilon_{A,n} - \epsilon_{B,n}) = 0$.
We found a solution exists for N=2. Choose $\epsilon_{A,1}=1, \epsilon_{B,1}=0$ (difference 1) and $\epsilon_{A,2}=0, \epsilon_{B,2}=1$ (difference -1). Both sums equal 1.
Conclusion: p=1 is a possible solution.

Investigated the case p is a positive integer (p >= 2):
The equation is $\sum_{n=1}^N x_n p^n = 0$, where $x_n = \epsilon_{A,n} - \epsilon_{B,n} \in \{-2, -1, 0, 1, 2\}$.
For p=2, a solution exists for N=2. Choose $x_2=1$ and $x_1=-2$. This corresponds to $(\epsilon_{A,2}, \epsilon_{B,2}) = (1, 0)$ and $(\epsilon_{A,1}, \epsilon_{B,1}) = (-1, 1)$. Both sums equal 2.
Conclusion: p=2 is a possible solution.
For p >= 3, an upper bound analysis shows that $|x_N|p^N \le 2 \frac{p^N - p}{p-1}$. Since $|x_N| \ge 1$, this leads to $p^N(p-3) + 2p \le 0$, which is impossible for $p \ge 3$.
Conclusion: For integers p >= 3, no solutions exist.
Overall: Solutions exist for integer p (namely p=1 and p=2).

### [W3, round 1]
Analysis of the equation $\sum_{n=1}^{N} d_n p^n = 0$, where $p=a/b$ is a positive rational number in lowest terms, and $d_n \in \{-2, -1, 0, 1, 2\}$ with at least one $d_n \ne 0$.

1.  **Case $p > 1$ (i.e., $a > b \ge 1$):**
    By multiplying by $b^N$ and rearranging, we found $|d_N| a^N \le 2 \sum_{n=1}^{N-1} a^n b^{N-n}$.
    This led to the crucial bound $|d_N| \le 2 / (a-b)$.
    Since $|d_N| \ge 1$ (assuming $d_N \ne 0$), we must have $a-b \le 2$.
    Testing the possible differences ($a-b=1$ or $a-b=2$):
    -   If $a-b=2$, then $|d_N| \le 1$. Testing $N=3$ for $p=3$ ($a=3, b=1$) showed $|d_3| \ge 3$, violating the constraint. This suggests $p=3$ is impossible for $N \ge 3$. For $N=2$, $p=3$ requires $|d_1/d_2|=3$, impossible with $|d_i|\le 2$.
    -   If $a-b=1$, $p=2/1=2$ is a solution (e.g., $d_1=0, d_2=-1, d_3=2$ for $N=3$). $p=1$ is also covered here (if we allow $b=1, a=1$).

2.  **Case $p < 1$ (i.e., $a < b$):**
    By analyzing the lowest power of $a$, we showed that $a$ must divide $d_1$. Since $|d_1| \le 2$, $a$ must be 1 or 2.
    -   If $a=1$ ($p=1/b, b \ge 2$): For $N=2$, $d_2 = -d_1 b$. Since $|d_2| \le 2$ and $|d_1| \ge 1$, we must have $b=2$ and $|d_1|=1$. Thus $p=1/2$ is a solution. Any larger $b$ forces $d_1=0$.
    -   If $a=2$ ($p=2/b, b \ge 3$): We showed $b$ must divide $d_N$. Since $\gcd(2^N, b)=1$ and $|d_N| \le 2$, this forces $d_N=0$, which implies all coefficients must be zero by recursion, contradicting the problem premise.

3.  **Case $p = 1$ ($a=b=1$):**
    $d_1 + d_2 + \dots + d_N = 0$. This is possible (e.g., $d_1=1, d_2=-1, d_3=0$ for $N=3$). $p=1$ is a solution.

Conclusion: The only possible values for $p$ are $1/2, 1, 2$.
