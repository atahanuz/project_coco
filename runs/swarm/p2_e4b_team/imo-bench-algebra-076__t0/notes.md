### [W1, round 1]
Analysis of constraints:
We are given:
1. $\sum_{i=1}^n \sin\theta_i = 0$
2. $\sum_{i=1}^n \cos^2 \theta_i = n - 2025$

Using $\cos^2 \theta_i = 1 - \sin^2 \theta_i$, the second equation transforms to:
$\sum_{i=1}^n (1 - \sin^2 \theta_i) = n - 2025$
$n - \sum_{i=1}^n \sin^2 \theta_i = n - 2025$
This simplifies to the necessary condition: $\sum_{i=1}^n \sin^2 \theta_i = 2025$.

Necessary condition on n:
Since $|\sin \theta_i| \le 1$, we have $\sin^2 \theta_i \le 1$. Therefore, $\sum_{i=1}^n \sin^2 \theta_i \le n$.
$2025 \le n$.

Impossibility of n=2025:
If $n=2025$, then $\sum_{i=1}^{2025} \sin^2 \theta_i = 2025$. This requires $\sin^2 \theta_i = 1$ for all $i$, meaning $\sin \theta_i \in \{1, -1\}$.
Let $p$ be the count of $\sin \theta_i = 1$ and $m$ be the count of $\sin \theta_i = -1$.
We must have $p+m = 2025$ and $p - m = \sum \sin \theta_i = 0$.
$p=m \implies 2p = 2025$. Since 2025 is odd, $p$ is not an integer, so $n=2025$ is impossible.

Conclusion:
Since $n \ge 2025$ and $n=2025$ is impossible, the strict lower bound is $n \ge 2026$.

### [W4, round 1]
Constraint derivation: The problem is equivalent to finding the smallest $n$ such that there exist $s_1, \ldots, s_n$ with $|s_i| \le 1$ satisfying $\sum s_i = 0$ and $\sum s_i^2 = 2025$. Since $\sum s_i^2 \le n$, we must have $n \ge 2025$.
If $n=2025$, then $s_i^2=1$ for all $i$, meaning $s_i = \pm 1$. The condition $\sum s_i = 0$ requires an equal number of $+1$s and $-1$s, which is impossible as 2025 is odd.
The smallest possible $n$ is $n=2026$. A construction exists for $n=2026$: let $n=2m=2026$, so $m=1013$. Set $s_i = a$ for $m$ indices and $s_i = -a$ for $m$ indices. $\sum s_i = 0$ is satisfied. $\sum s_i^2 = 2m a^2 = n a^2$. We require $n a^2 = 2025$. This gives $a^2 = 2025/2026$, so $a = \sqrt{2025/2026}$. Since $2025/2026 < 1$, $|a| < 1$, satisfying the required constraint. The sign choices are robust due to the perfect symmetry of the construction.

### [W3, round 1]
Analysis of the problem:
The conditions are:
1. $\sum_{i=1}^n \sin\theta_i = 0$
2. $\sum_{i=1}^n \cos^2 \theta_i = n - 2025$

Using the identity $\sin^2 \theta_i + \cos^2 \theta_i = 1$, summing over $i$:
$\sum \sin^2 \theta_i + \sum \cos^2 \theta_i = n$.
Substituting condition (2):
$\sum_{i=1}^n \sin^2 \theta_i + (n - 2025) = n$
$\sum_{i=1}^n \sin^2 \theta_i = 2025$.

Since $\sin^2 \theta_i \le 1$, we must have $n = \sum 1 \ge \sum \sin^2 \theta_i = 2025$. Thus, $n \ge 2025$.

Case $n=2025$:
If $n=2025$, then $\sum \sin^2 \theta_i = 2025$ implies $\sin^2 \theta_i = 1$ for all $i$.
This means $\sin \theta_i = \pm 1$. Condition (1) requires $\sum_{i=1}^{2025} \sin \theta_i = 0$. This requires an equal number of $+1$s and $-1$s among the 2025 terms, which is impossible since 2025 is odd. So $n \ne 2025$.

Case $n=2026$:
We need $\sum_{i=1}^{2026} \sin^2 \theta_i = 2025$. This requires that the sum of $\sin^2 \theta_i$ is short by 1 from the maximum possible sum of 2026.
A solution exists if we set 2024 terms to have $\sin^2 \theta_i = 1$, and the remaining two terms, $x_{2025}$ and $x_{2026}$, must sum to 1 (e.g., $x_{2025} = 0.5$ and $x_{2026} = 0.5$).

For $\sin^2 \theta_i = 1$ (2024 terms), we have $\sin \theta_i = \pm 1$. Let $k_+$ and $k_-$ be the counts of $+1$ and $-1$ respectively, so $k_+ + k_- = 2024$.
For $\sin^2 \theta_i = 0.5$ (2 terms), we have $\sin \theta_i = \pm 1/\sqrt{2}$.

We need the total sum to be zero: $\sum \sin \theta_i = (k_+ - k_-) + s_{2025} + s_{2026} = 0$.
If we choose $s_{2025} = 1/\sqrt{2}$ and $s_{2026} = -1/\sqrt{2}$, the last two terms sum to zero.
Then we require $k_+ - k_- = 0$. Since $k_+ + k_- = 2024$, we set $k_+ = k_- = 1012$.

This construction works: 1012 terms are 1, 1012 terms are -1, one term is $1/\sqrt{2}$, and one term is $-1/\sqrt{2}$.
$\sum \sin \theta_i = 0$.
$\sum \sin^2 \theta_i = 2024(1) + 0.5 + 0.5 = 2025$.
Since $n=2026$ works and $n=2025$ does not, $n=2026$ is the smallest positive integer solution.

### [W2, round 1]
Construction for n=2026:
To satisfy $\sum \sin \theta_i = 0$ and $\sum \cos^2 \theta_i = 1$.
We define the angles as follows:
1. For $i \in \{1, 3, 5, \ldots, 2023\}$ (1012 angles): $\theta_i = \pi/2$.
2. For $i \in \{2, 4, 6, \ldots, 2022\}$ (1012 angles): $\theta_i = 3\pi/2$.
3. $\theta_{2025} = \pi/4$.
4. $\theta_{2026} = 5\pi/4$.

Verification:
Sum of Sines: $1012 \times (1) + 1012 \times (-1) + 1/\sqrt{2} + (-1/\sqrt{2}) = 0$.
Sum of Cosines Squared: $1012 \times (0) + 1012 \times (0) + (1 - 1/2) + (1 - 1/2) = 0 + 1 = 1$.
The construction is verified.
