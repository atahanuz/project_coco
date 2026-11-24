### [W1, round 1]
From the identity $\sin^2 \theta_i + \cos^2 \theta_i = 1$, we have $\cos^2 \theta_i = 1 - \sin^2 \theta_i$.
Substituting into the second equation:
$\sum_{i=1}^n (1 - \sin^2 \theta_i) = n - 2025$
$n - \sum_{i=1}^n \sin^2 \theta_i = n - 2025$
This simplifies to the constraint: $\sum_{i=1}^n \sin^2 \theta_i = 2025$.

Since $\sin^2 \theta_i \le 1$ for all $i$, we must have $\sum_{i=1}^n \sin^2 \theta_i \le n$.
Therefore, $2025 \le n$. The necessary lower bound for $n$ is 2025.

### [W2, round 1]
Investigation for n=2025:
The second equation becomes: $\sum_{i=1}^{2025} \cos^2 \theta_i = 2025 - 2025 = 0$.
This implies $\cos^2 \theta_i = 0$ for all $i$, so $\sin^2 \theta_i = 1$ and $\sin \theta_i \in \{-1, 1\}$.
For the first equation, $\sum_{i=1}^{2025} \sin\theta_i = 0$, we need $k$ terms equal to 1 and $2025-k$ terms equal to -1, such that $k - (2025-k) = 0$, or $2k = 2025$. Since 2025 is odd, $k=1012.5$ is not an integer. Thus, no solution exists for $n=2025$.

### [W3, round 1]
Target: Construct $x_i = \sin\theta_i$ for $n=2026$ such that $\sum x_i = 0$ and $\sum x_i^2 = 2025$.
Construction found by setting $q=2$ (two variables not $\pm 1$):
Let $x_1, \ldots, x_{1012} = 1$.
Let $x_{1013}, \ldots, x_{2024} = -1$. (1012 terms)
Let $x_{2025} = 1/\sqrt{2}$.
Let $x_{2026} = -1/\sqrt{2}$.
Total terms: $1012 + 1012 + 2 = 2026$.
Verification:
Sum: $1012(1) + 1012(-1) + 1/\sqrt{2} - 1/\sqrt{2} = 0$.
Sum of Squares: $1012(1)^2 + 1012(-1)^2 + (1/\sqrt{2})^2 + (-1/\sqrt{2})^2 = 1012 + 1012 + 1/2 + 1/2 = 2025$.
This construction is valid.

### [W4, round 1]
The problem requires finding the smallest positive integer $n$ such that $\sum_{i=1}^n \sin\theta_i = 0$ and $\sum_{i=1}^n \cos^2 \theta_i = n - 2025$.

By substituting $\cos^2 \theta_i = 1 - \sin^2 \theta_i$, the second condition simplifies to $\sum_{i=1}^n \sin^2 \theta_i = 2025$.

1. Necessary Condition on $n$: Since $0 \le \sin^2 \theta_i \le 1$, we must have $0 \le \sum \sin^2 \theta_i \le n$. Thus, $2025 \le n$.
2. Test $n=2025$: If $n=2025$, then we must have $\sin^2 \theta_i = 1$ for all $i$. This means $\sin \theta_i = \pm 1$. For the sum $\sum \sin \theta_i = 0$ to hold, the number of $+1$'s must equal the number of $-1$'s, which requires an even number (2025) to be divisible by 2. This is impossible. Thus, $n \neq 2025$.
3. Test $n=2026$: Since $n \ge 2026$, $n=2026$ is the candidate for the smallest value. We seek real numbers $s_i = \sin \theta_i$ such that $\sum s_i = 0$ and $\sum s_i^2 = 2025$.
A construction exists:
Let 1012 values be $s_i = 1$.
Let 1012 values be $s_i = -1$.
Let 1 value be $s_{2025} = 1/\sqrt{2}$.
Let 1 value be $s_{2026} = -1/\sqrt{2}$.
Check sums:
$\sum s_i = 1012(1) + 1012(-1) + 1/\sqrt{2} + (-1/\sqrt{2}) = 0$. (Satisfied)
$\sum s_i^2 = 1012(1) + 1012(1) + (1/\sqrt{2})^2 + (-1/\sqrt{2})^2 = 2024 + 1/2 + 1/2 = 2025$. (Satisfied)
Since a solution exists for $n=2026$, and we proved $n \ge 2026$, $n=2026$ is the smallest possible value.
