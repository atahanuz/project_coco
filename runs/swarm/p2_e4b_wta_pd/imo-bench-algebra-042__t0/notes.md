### [W4, round 1]
PROBLEM ANALYSIS: Find $L_{\min} = \sup_{f} \left( \frac{\sum f_i^2}{\sum i f_i^2} \right)$, where $f$ is concave.
1. Concavity condition: $\Delta^2 f_i = f_{i+2} - 2f_{i+1} + f_i \le 0$.
2. The general strategy involves using this constraint to bound the ratio $\sum f_i^2 / \sum i f_i^2$. This is likely related to minimizing the variance of the index $i$ when weighted by $f_i^2$.
3. Initial test case: If $f_i = c$ (constant, which is concave), the ratio is $\frac{1028}{1028 \cdot 1029 / 2} = \frac{2}{1029} \approx 0.00194$. This suggests $L$ might be very small.
4. Further investigation needed to use the second-difference constraint effectively.

### [W3, round 1]
Calculated the ratio R(f) = (Sum i*f_i^2) / (Sum f_i^2) for the linear sequence f_i = 1028 - i.
The derived general formula for R(f) in terms of N=1028 is R(f) = N(N+1) / (2(2N-1)).
Substituting N=1028, we found:
R(f) = (1028 * 1029) / (2 * 2055) = 1057812 / 4110.
This is a strong candidate for the minimum constant L. We must now test other piecewise linear/triangular sequences (e.g., concentrated near endpoints) to see if they yield a larger ratio.

### [W1, round 1]
Investigation of R(f) = (\sum f_i^2) / (\sum i f_i^2) for concave sequences (N=3, 4, 5).
A concave sequence satisfies $f_{i+1} \le 2f_i - f_{i-1}$, meaning the sequence of first differences must be non-increasing.
To maximize R(f), we seek sequences heavily weighted towards smaller indices i.

N=3: Max ratio found is 1, achieved by (1, 0, 0).
N=4: Max ratio found is 0.7, achieved by (3, 2, 1, 0).
N=5: We investigated arithmetic progressions that satisfy non-negativity constraints.
The sequence f = (4, 3, 2, 1, 0) is concave.
Sum of squares: 4^2 + 3^2 + 2^2 + 1^2 + 0^2 = 16 + 9 + 4 + 1 = 30.
Weighted sum: 1*16 + 2*9 + 3*4 + 4*1 + 5*0 = 16 + 18 + 12 + 4 = 50.
Ratio R(f) = 30/50 = 0.6.
This appears to be the optimal solution for N=5 among simple candidates.

### [W2, round 1]
Analyzing the concavity constraint: $f_{i+1} - 2f_i + f_{i-1} \le 0$. This means the sequence of first differences, $\Delta f_i = f_{i+1} - f_i$, must be non-increasing. This is the discrete analog of $f''(x) \le 0$.

We seek to maximize the ratio $R(f) = \frac{\sum f_i^2}{\sum i f_i^2}$.

Using the continuous analogy, we examine simple concave functions.

1. **Constant Sequence ($f_i = C$):** This sequence is concave since $C - 2C + C = 0 \le 0$.
   $R(f) = \frac{\sum C^2}{\sum i C^2} = \frac{C^2 \cdot 1028}{C^2 \sum_{i=1}^{1028} i} = \frac{1028}{1028 \cdot 1029 / 2} = \frac{2}{1029}$.

2. **Concentrated Sequences (Heuristic Check):** Sequences that concentrate mass at small $i$ (like plateaus or rapid initial decay) tend to maximize this ratio. However, constructing such sequences that maintain concavity for all $i$ while having $f_i \ge 0$ is challenging. We tested a plateau sequence ($f_1=1, f_i=M, f_{1028}=0$) and found that for large $M$, the ratio approaches $1026/528797 \approx 0.001937$. Since $2/1029 \approx 0.001942$, the constant sequence provides a slightly better upper bound based on simple candidates.

The heuristic suggests that $L$ must be at least $2/1029$. We propose $L=2/1029$ as a strong candidate for the minimum required constant, as the constant function is the simplest concave sequence and maximizes the ratio among simple linear/constant choices.
