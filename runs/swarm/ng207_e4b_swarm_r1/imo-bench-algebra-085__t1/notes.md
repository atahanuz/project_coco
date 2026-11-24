### [W4, round 1]
Testing $n=1$. We need to find $t_1, s_1 \in \{1, \ldots, 1000\}$ such that $x_{t_1}x_{s_1} \le 2014 \cdot 1000 = 2,014,000$ for all non-negative $x_i$ with $\sum x_i = 2014$.

Case 1: $t_1 = s_1$. The maximum value of $x_{t_1}^2$ occurs when $x_{t_1}=2014$, giving $2014^2 = 4,056,196$. Since $4,056,196 > 2,014,000$, this case fails.

Case 2: $t_1 \neq s_1$. The maximum value of $x_{t_1}x_{s_1}$ occurs when $x_{t_1} + x_{s_1} = 2014$ and $x_i=0$ for $i \notin \{t_1, s_1\}$. This maximum is $(2014/2)^2 = 1007^2 = 1,014,049$. Since $1,014,049 \le 2,014,000$, this case satisfies the condition.

Conclusion: $n=1$ satisfies the condition by choosing any indices $t_1 \neq s_1$.

### [W4, round 1]
REPORT on task "Test small values of $n$ (e.g., $n=1, 2, 3, 4$) by choosing diverse index patterns for $(t_i, s_i)$. Specifically, prove rigorously whether $n=1$ can satisfy the condition, given $N=1000$ and $S=2014$": I rigorously tested the case $n=1$ for $N=1000$ and $S=2014$. The inequality requires $x_{t_1}x_{s_1} \le 2,014,000$. If $t_1 = s_1$, the maximum possible value is $2014^2 \approx 4.05$ million, which exceeds the limit. However, if we choose $t_1 \neq s_1$, the maximum value is achieved when $x_{t_1} = x_{s_1} = 1007$, yielding $1,014,049$. Since $1,014,049 \le 2,014,000$, $n=1$ satisfies the condition.
Candidate answer: Yes, $n=1$ can satisfy the condition.

### [W3, round 1]
REPORT on task "Assume the optimal configuration of indices leads to a scenario where the quadratic form behaves similarly to its uniform distribution limit, $Q(x) \approx n (S/N)^2$. Use this approximation to derive": Based on the approximation $Q(x) \approx n (S/N)^2$, where $N=1000$ and $S=2014$, the upper bound for $n$ is derived as $n \le N^3/S = 1000^3/2014$. This calculation yields $n \le 496524.329...$, meaning the largest possible integer $n$ is $496524$. This bound is considered achievable because $n$ is much smaller than the total number of available index pairs ($N^2$), allowing for a sufficiently spread-out selection of pairs to satisfy the approximation in the worst-case scenario.
Candidate answer: 496524

### [W1, round 1]
REPORT on task "Analyze the necessary condition for the quadratic form $Q(x) = \sum x_{t_i}x_{s_i}$ to satisfy $Q(x) \le 2014 \cdot 1000$ for all $x$. Define the matrix $M$ corresponding to the sum, and determine the": I analyzed the problem by scaling the quadratic form $Q(\mathbf{x})$ using $x_i = S y_i$, reducing the required inequality to $Q(\mathbf{y}) \le N/S$. The matrix $M$ is defined as the sum of contributions from the pairs $(t_i, s_i)$. Based on the task requirement, I demonstrated that the necessary condition for the inequality to hold universally is that the maximum eigenvalue of $M$ must be bounded by the ratio of the dimensions: $\lambda_{\max}(M) \le N/S$. For the given values, this means $\lambda_{\max}(M) \le 1000/2014$.
Candidate answer: The largest positive integer $n$ must satisfy $\lambda_{\max}(M) \le 1000/2014$.

### [W2, round 1]
REPORT on task "Investigate structured choices of index pairs $(t_i, s_i)$, such as cyclic shifts ($t_i=i, s_i=i+k \pmod{1000}$) or specific sparse patterns, and calculate the maximum eigenvalue $\lambda_{\max}(M)$ f": I investigated the structured choice of cyclic shifts for the index pairs $(t_i, s_i)$. By setting $n=1000$ and defining $t_i=i$ and $s_i=i+1 \pmod{1000}$, the resulting matrix $M$ is a cyclic permutation matrix. For this specific structured choice, the maximum eigenvalue $\lambda_{\max}(M)$ is 1. This configuration satisfies the required inequality as $\mathbf{y}^T M \mathbf{y} \le 1/1000 \le 1000/2014$.
Candidate answer: $n=1000$, $\lambda_{\max}(M)=1$
