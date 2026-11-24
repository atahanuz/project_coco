### [W3, round 1]
Initial analysis of the state transitions (G, B):
1. If a Girl (G) is picked (Prob G/(G+B)): (G, B) -> (G-1, B-1). Delta B = -1.
2. If a Boy (B) is picked (Prob B/(G+B)): (G, B) -> (G+1, B+1). Delta B = +1.

Expected change in B: E[Delta B] = (B/(G+B)) * (+1) + (G/(G+B)) * (-1) = (B - G) / (G + B).

Condition for B to increase (positive drift): B > G.
When B is much larger than G (B >> G), E[Delta B] approaches 1, strongly favoring an increase in B and suggesting non-termination.

Necessary Condition for Non-Termination: For the process to have a high probability of never ending (B never reaching 2), the drift must be positive ($B > G$) or zero ($B=G$) for most relevant states. If G significantly dominates B, the drift becomes strongly negative, pushing B down toward the stopping condition (B=2).

The problem starts with $B_0=26, G_0=24$, so $B_0 > G_0$, and the process starts with a positive drift.

### [W1, round 1]
Simulations for (G, B) = (5, 5) were run for 10 trials. The process exhibits high variability. 
In 5 out of 10 trials, the process terminated successfully (B reached 2). 
In the other 5 trials, the process reached the maximum step limit (100 steps) without terminating, suggesting it might never end, though this is not a proof of non-termination. 
The dynamics suggest that if $B$ increases relative to $G$ (i.e., $B/(G+B)$ is large), $B$ tends to grow rapidly due to the Boy picked rule: $(G, B) \to (G+1, B+1)$. Conversely, when $G$ is picked, both decrease: $(G, B) \to (G-1, B-1)$. The termination heavily depends on the relative probabilities driving the process towards decreasing $B$.

### [W2, round 1]
--- Analysis of D = B - G ---
Initial state: G_0 = 24, B_0 = 26. Initial difference D_0 = 2.
Total participants in the pool: N = G + B.

Case 1: A Girl (G) is picked.
Probability P(G) = G / N.
Action: Girl invites a boy from the pool. Both leave.
Change: Delta G = -1, Delta B = -1.
Change in D: Delta D_G = (-1) - (-1) = 0.

Case 2: A Boy (B) is picked.
Probability P(B) = B / N.
Action: Boy invites a girl and a boy from the waiting line. All three stay.
Change: Delta G = +1, Delta B = +1.
Change in D: Delta D_B = (+1) - (+1) = 0.

Expected change of D given state (G, B):
E[Delta D | G, B] = P(G) * Delta D_G + P(B) * Delta D_B
E[Delta D | G, B] = (G/N) * 0 + (B/N) * 0 = 0.

Conclusion: D = B - G is a martingale, meaning its expected future value, given the current state, is the current value. Since D_0 = 2, D remains 2 throughout the process.
The stopping condition is B = 2. If D = 2, then B = G + 2. The stopping condition translates to G + 2 = 2, which means G = 0.
The process must end when G reaches 0. Since G is a non-negative integer and the state transitions allow G to decrease (only when G > 0), G must eventually reach 0.
Therefore, the probability that the party never ends is 0.

### [W4, round 1]
### Analysis of the stopping condition and setup of the recurrence

**1. State Definition and Transitions:**
Let the state be $(G, B)$, the number of girls and boys in the party pool. The initial state is $(G_0, B_0) = (24, 26)$. The stopping condition is $B=2$.

*   **Transition 1 (Girl picked):** Probability $p_G = \frac{G}{G+B}$. State changes from $(G, B)$ to $(G-1, B-1)$. (Both leave).
*   **Transition 2 (Boy picked):** Probability $p_B = \frac{B}{G+B}$. State changes from $(G, B)$ to $(G+1, B+1)$. (Existing boy stays, one girl and one boy enter from the waiting line).

**2. Framing the Problem (Absorption):**
We are interested in $P(\text{the party never ends})$. Let $P_{stop}(G, B)$ be the probability that the party *eventually ends* (i.e., reaches the state $B=2$) starting from state $(G, B)$. The probability that the party never ends is $1 - P_{stop}(24, 26)$.

The process is a random walk in the $(G, B)$ plane. The set of states where $B=2$ constitutes the absorbing barrier.

**3. Setting up the Recurrence Equation:**
For any state $(G, B)$ where $B > 2$, the probability of eventual absorption $P_{stop}(G, B)$ is given by the weighted average of the probabilities of absorption from the subsequent states:

$$P_{stop}(G, B) = p_G \cdot P_{stop}(G-1, B-1) + p_B \cdot P_{stop}(G+1, B+1)$$

Substituting the probabilities:
$$P_{stop}(G, B) = \frac{G}{G+B} P_{stop}(G-1, B-1) + \frac{B}{G+B} P_{stop}(G+1, B+1) \quad \text{for } B > 2$$

**4. Boundary Conditions:**
*   If $B=2$, the party has stopped: $P_{stop}(G, 2) = 1$ for all $G \ge 0$.
*   Since $G$ can be arbitrarily large, we also need constraints for $G$. If $G$ approaches $-\infty$ (which shouldn't happen given $G_0=24$), the probability would depend on that limit. For $G \ge 0$, the process is well-defined.

The goal is now to solve this system of linear equations starting from $(24, 26)$ towards the boundary $B=2$.

### [W3, round 2]
### [W3, round 2] - Verification of W2's Martingale Proof

**1. Martingale Verification (D = B - G):**
The verification confirms that $D=B-G$ is a martingale.
*   If G is picked: $\Delta D = (-1) - (-1) = 0$.
*   If B is picked: $\Delta D = (+1) - (+1) = 0$.
Thus, $E[\Delta D | G, B] = 0$ for all valid states.

**2. Boundary Alignment:**
Since $D_0 = 26 - 24 = 2$, the process must satisfy $B_t - G_t = 2$. The stopping condition $B_{final}=2$ rigorously implies $G_{final}=0$. The required termination state is $(0, 2)$.

**3. Critique of W2's Conclusion:**
W2 correctly derived the necessary termination state $(0, 2)$, but incorrectly concluded that $G$ *must* reach 0. Since $D$ is fixed at 2, the process is restricted to states $(G, G+2)$. This constitutes a random walk on $G \ge 0$ with an absorbing barrier at $G=0$.
The expected drift of $G$ is $\mu(G) = E[G_{t+1} - G_t] = \frac{1}{G+1}$. Since $\mu(G) > 0$ for all $G \ge 1$, the random walk is transient towards $G \to \infty$.
Therefore, the probability that the walk reaches $G=0$ (the party ends) is strictly less than 1. There is a positive probability that $G$ runs away to infinity, meaning the party never ends. W2's conclusion that the probability is 0 is incorrect due to this oversight.

### [W3, round 3]
### [W3, round 3] - Solution Derivation for Absorption Probability h(G)

**1. State Reduction and Random Walk Definition:**
The difference $D = B-G$ is a martingale, fixed at $D=2$. The problem is equivalent to a 1D random walk on $G$ starting at $G_0=24$, with an absorbing barrier at $G=0$.
Transitions: $\Delta G = -1$ with probability $p_G(G) = \frac{G}{2G+2}$, and $\Delta G = +1$ with probability $p_B(G) = \frac{G+2}{2G+2}$.

**2. Recurrence and Difference Equation:**
The probability of absorption $h(G)$ satisfies $h(G) = p_G(G) h(G-1) + p_B(G) h(G+1)$.
This leads to the difference equation for $\Delta h(G) = h(G) - h(G-1)$:
$$\Delta h(G+1) = \frac{G}{G+2} \Delta h(G)$$

**3. General Solution:**
By solving the telescoping product, we find $\Delta h(G) = \Delta h(1) \frac{2}{G(G+1)}$.
Integrating yields the general solution:
$$h(G) = 1 + \Delta h(1) \frac{2G}{G+1}$$

**4. Boundary Condition Analysis:**
Since $E[\Delta G] = 1/(G+1) > 0$, the walk is transient and drifts towards $G=\infty$. We enforce the necessary condition for absorption probability in a positively drifting transient walk: $h(\infty)=0$.
$$0 = \lim_{G \to \infty} h(G) = 1 + 2 \Delta h(1) \implies \Delta h(1) = -1/2$$

**5. Closed-Form Solution and Final Answer:**
Substituting $\Delta h(1) = -1/2$:
$$h(G) = 1 - \frac{G}{G+1} = \frac{1}{G+1}$$
The probability that the party ends (reaches $G=0$) is $h(24) = 1/25$.
The probability that the party never ends is $1 - h(24) = 24/25$.
