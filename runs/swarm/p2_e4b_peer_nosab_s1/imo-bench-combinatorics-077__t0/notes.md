### [W1, round 1]
Investigation for N=3 (Start state: {1, 1, 1}).
A removes {1, 1}. Remaining elements before B's move: {1}.
B has two choices:
1. B chooses x+y = 2. New state S1 = {1, 2}.
   Termination check: Is 2 > 1? Yes. The game terminates. Number of elements = 2.
2. B chooses |x-y| = 0. New state S1 = {1, 0}.
   Termination check: Is 1 > 0? Yes. The game terminates. Number of elements = 2.

Conclusion for N=3: The game always terminates after the first round. The final number of elements remaining is 2, regardless of B's move. Thus, Max cookies = Min cookies = 2.

### [W1, round 1]
REPORT on task "Investigate the effect of a single move on a small blackboard (e.g., starting with 3 copies of 1). Map out the resulting possibilities for the next state and determine the maximum/minimum possible num": I investigated the game starting with N=3 copies of 1 ({1, 1, 1}). After player A removes two 1s, player B adds either 2 or 0. In both resulting states ({1, 2} or {1, 0}), the termination condition (one number being larger than the sum of all others) is immediately met. Therefore, the game always terminates after the first round, resulting in 2 numbers remaining on the blackboard. The maximum and minimum number of cookies A receives is 2.
Candidate answer: 2

### [W2, round 1]
### [W2, round 1] Analysis of Sum ($\Sigma$) and Invariants

**Analysis of Sum ($\Sigma$):**
Let $\Sigma_{old}$ be the sum before a round, and $x, y$ be the erased numbers. The new number $z$ is added.
The change in sum is $\Delta \Sigma = z - (x+y)$.

1. **If Player B chooses $z = x+y$**:
   $\Delta \Sigma = (x+y) - (x+y) = 0$. The sum remains constant.

2. **If Player B chooses $z = |x-y|$**:
   a. If $x \ge y$, $z = x-y$. $\Delta \Sigma = (x-y) - (x+y) = -2y$.
   b. If $y > x$, $z = y-x$. $\Delta \Sigma = (y-x) - (x+y) = -2x$.
   In both cases, $\Delta \Sigma \le 0$.

**Conclusion on $\Sigma$:** The sum $\Sigma$ is a non-increasing quantity. Thus, $\Sigma$ is a semi-invariant.

**Analysis of Invariants (GCD):**
Let $\mathcal{G}$ be the greatest common divisor (GCD) of all numbers on the blackboard.
If we replace $x, y$ with $z$, since $x$ and $y$ are multiples of $\mathcal{G}$, both $x+y$ and $|x-y|$ must also be multiples of $\mathcal{G}$. Therefore, $\mathcal{G}$ is an absolute invariant throughout the game.

**Initial State:** Since the board starts with 1997 copies of 1, the initial GCD is $\mathcal{G}_0 = 1$. This invariant must hold for all subsequent states.

### [W2, round 1]
REPORT on task "Analyze the sum of the numbers on the blackboard ($\Sigma$). Determine how $\Sigma$ changes after one move (replacing $x, y$ with $z$, where $z \in \{x+y, |x-y|\}$). Does any simple invariant or semi-": I analyzed how the sum ($\Sigma$) of the numbers on the blackboard changes after one move. I found that $\Sigma$ is a non-increasing semi-invariant, as replacing $x, y$ with $z$ results in $\Sigma_{new} \le \Sigma_{old}$. Furthermore, I proved that the greatest common divisor (GCD) of all numbers on the board is a strict invariant, which is fixed at 1 since the game starts with all 1s.
Candidate answer: N/A (Task was analysis, not final solution)

### [W3, round 1]
**Task: Minimum N for Termination Condition (1)**

We analyze the termination condition (1): one number $M$ is larger than the sum of all other numbers.

Let $N$ be the total number of items on the blackboard, and let $S$ be the total sum.
If $M$ is the largest number, the sum of the rest of the numbers is $S - M$.
The condition is $M > S - M$.
This simplifies to $2M > S$, or $M > S/2$.

We are looking for the minimum number of items, $N$, such that a set of $N$ numbers $\{x_1, x_2, \dots, x_N\}$ exists where $M > S/2$.

1.  **Case N=1:** If $N=1$, $S=M$. The condition $M > S/2$ holds if $M>0$. However, the game dynamics require at least two numbers to initiate a round, and the operations maintain a constant $N \ge 2$ (unless we reach zero state).
2.  **Case N=2:** The blackboard contains $\{M, Z\}$. The total sum is $S = M+Z$. The condition requires $M > Z$. This is possible (e.g., $\{2, 1\}$).
3.  **Case N=3:** The blackboard contains $\{M, Z_1, Z_2\}$. The total sum is $S = M+Z_1+Z_2$. The condition requires $M > Z_1+Z_2$. This is possible (e.g., $\{3, 1, 1\}$).

Since the condition $M > S/2$ can be satisfied by a configuration of only two positive numbers, the minimum total number of items ($N$) required for this condition to be met is $N=2$.

### [W3, round 1]
REPORT on task "Examine the termination condition (1): $M > \sum(\text{rest})$. Derive the minimum number of total items ($N$) required for this condition to be met. Specifically, if the sum is $S$, what is the minim": I examined the termination condition $M > \sum(\text{rest})$, which is mathematically equivalent to $M > S/2$. By testing small values for the total number of items $N$, I determined that the minimum $N$ required for this condition to be met is $N=2$. A configuration $\{M, Z\}$ where $M>Z$ satisfies this requirement.
Candidate answer: 2

### [W4, round 1]
### [W4, round 1]
**Analysis of Termination Condition (2): All numbers are zeros.**

The initial sum of numbers is $S_0 = 1997$, which is an odd number. The game terminates under condition (2) if the sum $S$ becomes 0, which is an even number.

We analyze how the sum $S$ changes in a single round, replacing $x$ and $y$ with $z \in \{x+y, |x-y|\}$.

1. **If B chooses $z = x+y$:** The change in sum is $\Delta S = z - (x+y) = 0$. The sum $S$ is invariant.
2. **If B chooses $z = |x-y|$:** The change in sum is $\Delta S = |x-y| - (x+y)$.
   - If $x \ge y$, $\Delta S = (x-y) - (x+y) = -2y$.
   - If $y > x$, $\Delta S = (y-x) - (x+y) = -2x$.
   In both cases, $\Delta S$ is a negative even number or zero (if $x=y$).

Since both possible moves result in a change in the sum $\Delta S$ that is either 0 or an even number, the parity of the sum $S$ is invariant. Starting with $S_0 = 1997$ (Odd), $S$ will always remain odd. Consequently, $S$ can never equal 0.

**Conclusion:** Termination condition (2) (All numbers are zeros) is mathematically impossible to reach given the starting state $S_0=1997$.

### [W4, round 1]
REPORT on task "Analyze the termination condition (2): All numbers are zeros. What sequence of moves leads quickest to this state? Consider the parities of the numbers generated.": I analyzed termination condition (2) (All numbers are zeros) by examining the parity of the sum of all numbers, $S$. Since the initial sum $S_0=1997$ is odd, and both possible moves (replacing $\{x, y\}$ with $x+y$ or $|x-y|$) result in a change in sum $\Delta S$ that is either zero or an even number, the parity of the sum $S$ must always remain odd. Therefore, $S$ can never reach 0, and termination condition (2) is mathematically impossible to achieve starting from $N_0=1997$. The game must therefore terminate under condition (1).
Candidate answer: ""

### [W1, round 2]
### [W1, round 2] Synthesis and Conclusion

Based on the analysis of termination conditions:
1. **Termination under Condition (2) is impossible:** Since the initial sum $S_0 = 1997$ is odd, and the parity of the sum is invariant, the sum $S$ can never reach 0. Therefore, the game must terminate under Condition (1).
2. **Minimum Termination State:** Condition (1) requires one number $M$ to be strictly greater than the sum of all others ($M > S/2$). We established that the minimum number of elements $N$ required to satisfy this condition is $N=2$.
3. **Optimal Play Implication:** The number of elements $N$ decreases by exactly 1 in every round. Player A seeks to maximize $N_{final}$ (maximize cookies), while Player B seeks to minimize $N_{final}$ (minimize cookies). Since $N$ is strictly decreasing, B's optimal strategy is to force termination as quickly as possible, i.e., reaching the minimum possible $N$ that satisfies Condition (1).
4. **Conclusion:** Given that $N=2$ is the smallest possible terminal state, and B actively seeks to minimize the cookie count, optimal play dictates that the game proceeds until $N=2$. Any attempt by A to delay termination must be countered by B forcing a configuration satisfying $M > S/2$ when $N=2$ is reached, as this represents the lowest possible cookie count B can achieve. Therefore, the final number of cookies A receives is 2.

### [W1, round 2]
REPORT on task "Synthesize the findings from all rounds. Specifically, use the invariant that the number of blackboard elements $N$ decreases by exactly 1 in every round. Combine this with the established constraints": I synthesized the findings regarding the game's termination conditions. Since the initial sum (1997) is odd, termination condition (2) is impossible. The game must terminate under condition (1), which requires a single number $M$ to be larger than the sum of the rest ($M > S/2$). I established that the minimum number of elements $N$ required to satisfy this condition is $N=2$. Since the number of elements $N$ strictly decreases every round, and player B seeks to minimize the final count, optimal play ensures the game progresses until this minimum terminal state, $N=2$, is reached.
Candidate answer: 2
