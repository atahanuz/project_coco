### [W3, round 1]
Investigated p=1 case. Found a solution for N=2. Let A_n, B_n be the additions. We need sum(A_n - B_n) = 0 with at least one difference. Setting N=2, we choose (A_1, B_1) = (1, 0) and (A_2, B_2) = (0, 1). Alice's total is 1+0=1, Bob's total is 0+1=1. Since A_1 != B_1, p=1 is a possible solution.

### [W3, round 1]
REPORT on task "Investigate the case p=1. If p=1, the equation becomes $\sum_{n=1}^{N} C_n = 0$. Show whether there exist choices of $A_n$ and $B_n$ (such that at least one difference exists) that satisfy this condit": I investigated the case p=1. The problem requires finding a sequence of choices such that the sums of Alice's and Bob's additions are equal, while at least one choice differs. I demonstrated that for N=2 minutes, choosing (A_1, B_1) = (1, 0) and (A_2, B_2) = (0, 1) results in both totals being 1, satisfying all conditions. Therefore, p=1 is a possible value.
Candidate answer: p=1

### [W4, round 1]
Analysis of p = 1/k (where k > 1):
The condition that Alice and Bob display the same number after $N$ minutes leads to the equation:
$$\sum_{n=1}^{N} (s_{A,n} - s_{B,n}) p^n = 0$$
Let $c_n = s_{A,n} - s_{B,n}$. Since $s_{A,n}, s_{B,n} \in \{-1, 0, 1\}$, the coefficients $c_n$ are integers such that $c_n \in \{-2, -1, 0, 1, 2\}$.
Substituting $p=1/k$ and multiplying by $k^N$, we get:
$$\sum_{n=1}^{N} c_n k^{N-n} = 0$$
Dividing by $k$, we get a polynomial equation in $p$:
$$P(p) = c_1 + c_2 p + c_3 p^2 + \dots + c_N p^{N-1} = 0$$
Since $p=1/k$ is a rational root, we apply the Rational Root Theorem (RRT). If we write $p=1/k$ in lowest terms (which it is, since $k>1$ and we assume $\gcd(1, k)=1$), then $k$ must divide the leading coefficient $c_N$.
Since $c_N \in \{-2, -1, 0, 1, 2\}$, and $k$ is an integer greater than 1, the only possibility for $k$ to divide $c_N$ is if $c_N$ is 2 or -2, which implies $k=2$.
If $c_N=0$, we look at the highest non-zero coefficient $c_M$ ($M < N$). $k$ must divide $c_M$, which again implies $k=2$.
Therefore, the only possible candidate value for $k > 1$ is $k=2$, meaning $p=1/2$. This value can be verified to work (e.g., for N=3, $4c_1 + 2c_2 + c_3 = 0$ has solutions with $c_i \in \{-2, \dots, 2\}$).

### [W4, round 1]
REPORT on task "Consider p = 1/k for integer k > 1. Substitute $p=1/k$ into the equation $C_1 + C_2 p + \dots + C_N p^{N-1} = 0$. Since $C_n$ are integers, analyze this structure to find candidate values for $k$ (and": I analyzed the case where $p = 1/k$ for integer $k > 1$. By setting up the equality of the blackboard totals, the problem reduces to finding a rational root $p=1/k$ for the polynomial $P(p) = c_1 + c_2 p + \dots + c_N p^{N-1} = 0$, where $c_i \in \{-2, -1, 0, 1, 2\}$. Applying the Rational Root Theorem, since $k$ must divide the highest non-zero coefficient $c_N$ (or $c_M$), and $|c_N| \le 2$, the only possible integer value for $k>1$ is $k=2$. This yields the candidate solution $p=1/2$.
Candidate answer: p = 1/2

### [W2, round 1]
General necessary constraint on p: If p > 1, we derived the inequality $|C_N| p^N \le 2 \sum_{n=1}^{N-1} p^n$. Since $|C_N| \ge 1$, this implies $p < 1 + 2/|C_N|$. The tightest general upper bound is established when $|C_N|=1$, giving $p < 3$.

### [W1, round 1]
ANALYSIS FOR N=2:
The condition $S_A = S_B$ for N=2 leads to $A_1 - B_1 + A_2 - B_2 = 0$.
Since $A_1, B_1$ are multiples of $p$ and $A_2, B_2$ are multiples of $p^2$, we group terms:
$p(c_{A1} - c_{B1}) + p^2(c_{A2} - c_{B2}) = 0$.
Dividing by $p$ (since $p>0$):
$(c_{A1} - c_{B1}) + p(c_{A2} - c_{B2}) = 0$.
Let $C_1 = c_{A1} - c_{B1}$ and $C_2 = c_{A2} - c_{B2}$. We require $C_1 + C_2 p = 0$.
The coefficients $C_1$ and $C_2$ are differences of values in $\{-1, 0, 1\}$, so $C_1, C_2 \in \{-2, -1, 0, 1, 2\}$.
The constraint that they made at least one different choice means $(C_1, C_2) \neq (0, 0)$.

We solve for $p$: $p = -C_1 / C_2$. Since $p$ must be positive, $C_1$ and $C_2$ must have opposite signs.

Systematic check yields the following positive rational values for p:
1. $p=1$: Found when $C_1=-1, C_2=1$ (and others, e.g., $C_1=-2, C_2=2$).
2. $p=2$: Found when $C_1=-2, C_2=1$.
3. $p=1/2$: Found when $C_1=-1, C_2=2$.

The possible values of p derived from N=2 are $\{1/2, 1, 2\}$.

### [W2, round 1]
REPORT on task "Determine general necessary constraints on p. Use the bounded nature of the coefficients $C_n \in \{-2, -1, 0, 1, 2\}$ to try and establish an upper bound for p. For example, if p is large, which term": I modeled the problem as a polynomial equation $\sum_{n=1}^{N} C_n p^n = 0$, where $|C_n| \le 2$. By assuming $p>1$, I analyzed the dominance of the highest degree term $C_N p^N$. This led to the necessary inequality $|C_N| < 2/(p-1)$. Since $|C_N|$ must be at least 1 for the constraint to apply, the tightest general upper bound derived is $p < 3$.
Candidate answer: $p < 3$

### [W1, round 1]
REPORT on task "Analyze the case N=2. Set up the equation $C_1 + C_2 p = 0$, where $C_1, C_2 \in \{-2, -1, 0, 1, 2\}$ and $C_2 \neq 0$. Determine all possible positive rational values of p derived from this case, and": I analyzed the case for N=2 minutes. The equality of the final totals leads to the equation $C_1 + C_2 p = 0$, where $C_1$ and $C_2$ are integers ranging from -2 to 2, and $(C_1, C_2) \neq (0, 0)$. By systematically checking combinations of $C_1$ and $C_2$ that yield a positive rational $p$, I found three possible values. These values are $p = 1/2$, $p = 1$, and $p = 2$.
Candidate answer: {1/2, 1, 2}
