### [W2, round 1]
Invariant Derivation:
Let G and B be the current number of girls and boys. The total number of participants is N = G + B.

Case 1: Girl picked (Prob = G/N).
Action: Girl invites a boy from the pool. Both leave.
Change: $\Delta G = -1$, $\Delta B = -1$.
Change in difference: $\Delta(G-B) = (-1) - (-1) = 0$.

Case 2: Boy picked (Prob = B/N).
Action: Boy invites a girl and a boy from the waiting line. All three stay.
Interpretation: The boy picked (B) is replaced by three participants (B, G_new, B_new). Net change is $\Delta G = +1$ and $\Delta B = +1$.
Change: $\Delta G = +1$, $\Delta B = +1$.
Change in difference: $\Delta(G-B) = (+1) - (+1) = 0$.

Since $\Delta(G-B) = 0$ in both cases, $G-B$ is an invariant.
Initial state: $G_0 = 24, B_0 = 26$.
Invariant relationship: $G - B = G_0 - B_0 = 24 - 26 = -2$.
Thus, $G = B - 2$.

Transition Probabilities (as functions of B):
Total participants $N = G + B = (B-2) + B = 2B - 2$.

P(B -> B-1) occurs when a girl is picked (Case 1):
$P(B \to B-1) = \frac{G}{N} = \frac{B-2}{2B-2}$.

P(B -> B+1) occurs when a boy is picked (Case 2):
$P(B \to B+1) = \frac{B}{N} = \frac{B}{2B-2}$.

### [W4, round 1]
--- Analysis of Expected Drift $E[\Delta B]$ ---

1. Define State Variables: Let $G$ be the number of girls and $B$ be the number of boys in the pool. Initial state: $G_0 = 24, B_0 = 26$.

2. Analyze State Transitions: The state changes depending on who is picked:
    a) Girl picked (Probability $P(G) = G/(G+B)$): $\Delta G = -1$, $\Delta B = -1$.
    b) Boy picked (Probability $P(B) = B/(G+B)$): $\Delta G = +1$, $\Delta B = +1$.

3. Find Invariant Quantity: Check the difference $D = G - B$.
    a) If Girl picked: $\Delta D = (-1) - (-1) = 0$.
    b) If Boy picked: $\Delta D = (+1) - (+1) = 0$.
    Since $D$ is constant, $G - B = G_0 - B_0 = 24 - 26 = -2$.
    Thus, $G = B - 2$ always holds.

4. Calculate Expected Drift $E[\Delta B]$:
$$E[\Delta B] = P(G) \cdot (\Delta B | G) + P(B) \cdot (\Delta B | B)$$
$$E[\Delta B] = \left(\frac{G}{G+B}\right) (-1) + \left(\frac{B}{G+B}\right) (1)$$
$$E[\Delta B] = \frac{B - G}{G+B}$$

5. Express Drift as a function of B: Substitute $G = B - 2$:
$$E[\Delta B](B) = \frac{B - (B - 2)}{(B - 2) + B} = \frac{2}{2B - 2} = \frac{1}{B - 1}$$

--- Long-Term Behavior (Recurrence vs. Transience) ---

6. Analyze $E[\Delta B](B)$:
For the process to end, $B$ must reach 2. The process starts at $B_0 = 26$.
For any state $B > 2$, the drift $E[\Delta B](B) = 1/(B-1)$ is strictly positive.

7. Conclusion: Since the expected drift is positive for all states $B > 2$, the process is strongly biased toward increasing $B$ and thus moving away from the termination barrier at $B=2$. This indicates that the random walk is transient. The probability that the process never reaches $B=2$ (i.e., the party never ends) is positive. Given the positive drift, this probability is 1.

### [W1, round 1]
### Boundary Condition Analysis: Probability of Reaching B=2

The problem describes a stochastic process which, under the assumption of an underlying "invariant relationship," simplifies to a one-dimensional random walk on the number of boys, $B$. The target state is the absorbing barrier $B=2$. We must identify the failure state, $B_{fail}$, which is likely $B=0$ (the party ends in an undefined state, or cannot proceed further).

Let $P_B$ be the probability of reaching $B=2$ before reaching $B_{fail}$. This probability follows the standard Gambler's Ruin recurrence relation:
$$P_B = p P_{B+1} + q P_{B-1}$$
where $p$ is the probability of moving $B \to B+1$ and $q$ is the probability of moving $B \to B-1$, and $p+q=1$.

We define the boundary conditions:
1. $P_2 = 1$ (Success state)
2. $P_{B_{fail}} = 0$ (Failure state, assumed to be $B=0$).

The solution to this recurrence relation depends on the ratio $r = q/p$.

**Case 1: Unbiased Walk ($p=q=1/2$, so $r=1$)**
The solution is linear: $P_B = A + CB$.
Using $P_0=0 \implies A=0$.
Using $P_2=1 \implies C=1/2$.
Therefore, $P_B = B/2$.
*Note: This solution only works if $B$ is restricted such that $P_B \le 1$. If we start at $B=3$, $P_3 = 1.5$, which is impossible. This suggests the actual random walk governed by the invariant relationship is biased, or $B_{fail} \ne 0$.*

**Case 2: Biased Walk ($p \ne q$, so $r \ne 1$)**
The solution is:
$$P_B = \frac{r^B - r^{B_{fail}}}{r^2 - r^{B_{fail}}}$$
Setting $B_{fail}=0$:
$$P_B = \frac{r^B - r^0}{r^2 - r^0} = \frac{r^B - 1}{r^2 - 1}$$
Wait, the standard form for $P_B$ where $P_0=0$ and $P_M=1$ is $\frac{r^B - 1}{r^M - 1}$.
Let $M=2$ be the target. If we want $P_0=0$ and $P_2=1$:
$$P_B = \frac{r^B - 1}{r^2 - 1}$$
This confirms the result $P_B = B/2$ if $r=1$.

Since the derived $P_B = B/2$ fails for $B=3$, we must conclude that either the failure boundary $B_{fail}$ is higher than 0, or the walk is heavily biased towards $B=2$.

**Task Calculation (Assuming a suitable unknown bias $r$ allows $P_B \le 1$):**

If we proceed using the derived formula for $P_B$ relative to $B_{fail}=0$ and $B_{target}=2$, we must solve for the required bias $r$ such that the general solution holds. Given the prompt requires *calculation* for $B=3$ and $B=4$, we will write down the required expression in terms of $r$, noting that $r$ is derived from the ratio of probabilities $q/p$.

For $B=3$: $P_3 = \frac{r^3 - 1}{r^2 - 1} = \frac{(r-1)(r^2+r+1)}{(r-1)(r+1)} = \frac{r^2+r+1}{r+1}$.
For $B=4$: $P_4 = \frac{r^4 - 1}{r^2 - 1} = \frac{(r^2-1)(r^2+1)}{(r^2-1)} = r^2+1$.

These expressions represent the probability $P_B$ conditional on the parameters $p$ and $q$ (which define $r$), and assuming $B_{fail}=0$.
The required calculation steps involve finding the specific value of $r$ dictated by the invariant relationship, which is currently missing from the problem statement.

### [W3, round 1]
### Analysis Conclusion: Random Walk Drift
The process simplifies to a 1D random walk on the number of boys, $B$, starting at $B_0=26$, with the absorbing barrier at $B=2$.

1.  **Transition Probabilities:** Based on the invariant $G = B-2$, the probabilities of moving $\Delta B = -1$ or $\Delta B = +1$ at state $B$ are:
    $$q_B = P(B \to B-1) = \frac{B-2}{2B-2}$$
    $$r_B = P(B \to B+1) = \frac{B}{2B-2}$$

2.  **Expected Drift:** The expected change in $B$ at state $B$ is:
    $$E[\Delta B](B) = q_B (-1) + r_B (1) = \frac{B - (B-2)}{2B-2} = \frac{2}{2B-2} = \frac{1}{B-1}$$

3.  **Absorption Probability $p(26)$:** The party ends if $B$ reaches 2. We seek $p(26) = P(B \to 2 | B_0=26)$.
    Since $B_0=26 > 2$, the drift $E[\Delta B](B) = 1/(B-1)$ is strictly positive for all $B > 2$. A random walk with a consistently positive drift away from a finite target state is transient.
    Therefore, the probability of being absorbed at $B=2$ is $p(26) = 0$.

4.  **Probability of Never Ending:** The party never ends if $B \to \infty$. Since the walk is transient with positive drift, the probability of reaching infinity is $P(B \to \infty) = 1 - P(B \to 2) = 1 - 0 = 1$.
