### [W3, round 1]
Analysis of the total sum S: Let S be the sum of all numbers on the blackboard. In every round, A removes x and y, and B adds z, where z is either x+y or |x-y|.
If B chooses z = x+y, the new sum S' = S - x - y + (x+y) = S.
If B chooses z = |x-y|, since |x-y| has the same parity as x+y (because $|x-y| - (x+y)$ is even), the new sum S' = S - x - y + |x-y| has the same parity as S - x - y + (x+y) = S.
Thus, the parity of the total sum S is an invariant.
The initial sum is $S_0 = 1997 \times 1 = 1997$, which is odd.
Condition (2) requires all numbers to be zero, meaning the final sum $S_{final}$ must be 0, which is even.
Since the parity of the sum must remain odd, it is impossible to reach the state where all numbers are zero.

### [W2, round 1]
Analysis of GCD Invariant:
Let S be the set of numbers on the blackboard, and g = gcd(S). Initially, S consists of 1997 ones, so g_initial = 1.
In every round, two numbers x and y are replaced by z, where z = x+y or z = |x-y|.
Since g divides x and g divides y, g must divide both x+y and |x-y|. Thus, g always divides z.
Since g already divides all other elements in S, g must divide the gcd of the new set S'.
Conclusion: The GCD of the set of numbers remains constant at 1 throughout the game, as the initial GCD is 1 and it can only increase or stay the same. This means no subset of numbers can ever become simultaneously divisible by an integer k > 1.

### [W3, round 1]
REPORT on task "Determine if it is possible to reach a state where all numbers are zero (Condition 2), starting from 1997 ones. If so, what sequence of moves is required?": I investigated the possibility of reaching a state where all numbers are zero by analyzing the sum of the numbers on the blackboard (S). The total sum S is invariant modulo 2 throughout the game, regardless of the choice made by player B. Since the initial sum is $1997$ (odd), the sum can never become $0$ (even). Therefore, it is impossible to reach Condition (2).
Candidate answer: Not possible

### [W2, round 1]
REPORT on task "Analyze the invariant $\gcd$ of the set of numbers and determine if this helps constrain the possible states or speed of termination.": I analyzed the GCD invariant of the set of numbers on the blackboard. Since the initial state consists of 1s, the initial GCD is 1. Because both generated numbers ($x+y$ and $|x-y|$) must be divisible by the current GCD, the GCD of the set remains 1 throughout the game. This invariant confirms that all numbers generated are integers and share no common factor greater than 1, thus constraining the possible states structurally, although it does not directly determine the termination speed or final cookie count.
Candidate answer: ""

### [W4, round 1]
ANALYSIS OF THE SUM S AND GAME TERMINATION
The sum $S$ of all numbers on the blackboard is non-increasing.
Let $S_{old}$ be the sum before a round, and $x, y$ be the numbers erased. The new number is $z \in \{x+y, |x-y|\}$.
The change in sum is $\Delta S = z - x - y$.

1. If Player B chooses $z = x+y$, then $\Delta S = (x+y) - x - y = 0$. The sum remains constant.
2. If Player B chooses $z = |x-y|$, assuming $x \ge y$, then $z = x-y$. $\Delta S = (x-y) - x - y = -2y$. Since $y \ge 0$, $\Delta S \le 0$.

Therefore, the total sum $S$ is non-increasing.

Proof of Termination:
The number of elements $N$ decreases by exactly 1 in every round. Since $N_{initial} = 1997$, $N$ is bounded below by 1 (unless condition (2) is met).
Since $S$ is a sum of non-negative numbers, $S$ is bounded below by 0, and since $S$ is non-increasing, $S$ must converge to a non-negative value.

The game must terminate because:
A. If the sum $S$ reaches 0, all numbers must be zero, satisfying termination condition (2).
B. If $S > 0$, $N$ strictly decreases. If $S$ remains constant, the average value $S/N$ increases, forcing one element $X_{max}$ to grow relative to $S$ such that $2X_{max} > S$ (Termination Condition 1) must eventually hold as $N$ gets small. If $S$ decreases, it is bounded and finite, ensuring eventual termination.
Since $N$ decreases and $S$ is bounded and non-increasing, the game cannot continue indefinitely without hitting a terminal state.

### [W4, round 1]
REPORT on task "Analyze the implications of the sum $S$ being non-decreasing. Can you prove that the game must terminate?": I analyzed the change in the total sum $S$. I proved that $S$ is always non-increasing, as the only way $S$ can increase is if $z = x+y$, but in that case, $S$ remains constant. The game must terminate because the number of elements $N$ strictly decreases by 1 each round, while the sum $S$ is bounded below by 0 and is non-increasing. This guarantees that either $S$ reaches 0 (Termination Condition 2), or $N$ becomes sufficiently small relative to $S$ that Termination Condition 1 must be met.
Candidate answer: ""

### [W1, round 1]
[W1, round 1] Task analysis: Checking the sum relation.
Assuming player B writes *both* numbers $x+y$ and $|x-y|$ on the blackboard (as implied by the prompt's required relation), the change in the total sum $S$ is:
$S_{new} = S_{old} - (x+y) + (x+y + |x-y|) = S_{old} + |x-y|$.
Since $|x-y| \ge 0$, the total sum $S$ is non-decreasing.
Furthermore, under this interpretation, the number of elements $N$ remains constant at $N_0 = 1997$ throughout the game, as 2 elements are removed and 2 are added every round. If the game terminates, A receives 1997 cookies, regardless of the specific termination condition (1) or (2).
Note: This interpretation (B adds both numbers) conflicts with the analysis in notes.md, which assumes B chooses only one number from $\{x+y, |x-y|\}$. Further investigation is needed to resolve this ambiguity, but I have fulfilled the explicit instruction regarding the sum relationship.

### [W1, round 1]
REPORT on task "Start by checking the relationship between $S_{new}$ and $S_{old}$ carefully: $S_{new} = S_{old} + |x-y|$. Since $|x-y| \ge 0$, the sum is non-decreasing.": I analyzed the relationship between the total sum $S$ before and after a round, assuming player B adds both $x+y$ and $|x-y|$ to the blackboard, as suggested by the prompt's required equation. This confirms that $S_{new} = S_{old} + |x-y|$, meaning the sum is non-decreasing throughout the game. Furthermore, under this interpretation, the number of elements $N$ remains constant at 1997. The game's payoff is fixed at 1997 cookies if termination occurs, regardless of the optimal play path. I noted this finding in the shared team notes for further discussion regarding the ambiguity in the ruleset.
Candidate answer: ""

### [W2, round 2]
### [W2, round 2]
CONFIRMATION ON PARITY AND TERMINATION
I reviewed W3's proof regarding the parity of the sum $S$. I confirm that the proof is strictly correct. Since $S_0=1997$ is odd, and the parity of $S$ is an invariant in every round (as confirmed by W3), $S$ can never equal 0 (which is even). Thus, Condition (2) (all numbers are zero) is impossible.

However, the game must still terminate. W4 proved that the total sum $S$ is non-increasing and the number of elements $N$ strictly decreases by 1 each round. Since $S$ is bounded below by 0 and $N$ is strictly decreasing, the game must end. Since Condition (2) is ruled out by parity, the game must terminate via Condition (1): one number becomes larger than the sum of all others. $S_{final}$ must be positive and odd.

### [W2, round 2]
REPORT on task "Review W3's proof regarding the parity of the sum $S$. Confirm if the condition $S_{final}=0$ (required for Condition 2) is strictly impossible given $S_0=1997$ (odd), or if there is any subtle case w": I reviewed W3's proof concerning the parity of the sum $S$ and confirmed its correctness. Since the initial sum $S_0=1997$ is odd, the sum $S$ must always remain odd, making termination via Condition (2) ($S_{final}=0$) strictly impossible. However, W4 showed that the sum $S$ is non-increasing while the number of elements $N$ strictly decreases. This guarantees that the game must terminate via Condition (1) ($2X_{max} > S$), resulting in a positive, odd $S_{final}$.
Candidate answer: ""

### [W3, round 2]
INVESTIGATION: How Player B maximizes sum reduction using $z=|x-y|$.
Player A chooses two numbers $(x, y)$. Player B chooses $z \in \{x+y, |x-y|\}$.
The change in the total sum $S$ is $\Delta S = z - (x+y)$.

1. If B chooses $z = x+y$, then $\Delta S = 0$.
2. If B chooses $z = |x-y|$, assuming $x \ge y$, then $\Delta S = (x-y) - (x+y) = -2y$. The reduction is $2y = 2\min(x, y)$.

Since $y \ge 0$, B maximizes the sum reduction by always choosing $z = |x-y|$ whenever $x \ne y$ (resulting in a reduction $2\min(x, y) > 0$). If $x=y$, both choices result in $\Delta S = -2x$ (if $z=0$) or $\Delta S = 0$ (if $z=2x$), meaning B chooses $z=0$ for the maximum reduction.
Therefore, B's optimal strategy to force Condition (1) quickly is to select $z=|x-y|$ whenever the resulting reduction is positive.

### [W3, round 2]
REPORT on task "Investigate whether Player B can always force a state where one number is disproportionately large (i.e., quickly force Condition (1)), regardless of A's choices. Specifically, how does B choose $z=|x": I investigated how Player B should choose $z=|x-y|$ to maximize the reduction in the total sum $S$. I determined that B's optimal strategy to force a disproportionately large number (Condition 1) is to always choose $z=|x-y|$ whenever $x \neq y$. This is because this choice leads to a reduction of $2\min(x, y)$ in the sum $S$, whereas choosing $z=x+y$ results in no change to the sum $S$. This strategy maximizes the rate at which the sum is decreased, thereby accelerating the game towards termination Condition (1).
Candidate answer: N/A (Strategic guidance provided)

### [W4, round 2]
### [W4, round 2] Structural Analysis Constraints
The analysis confirms that the game must terminate via Condition (1) ($2X_{max} > S_{final}$) because the initial sum $S_0=1997$ is odd, making Condition (2) ($S_{final}=0$) impossible due to the parity invariant of the total sum $S$.

Let $S_{final}$ be the final sum, $N_{final}$ the number of elements, and $X_{max}$ the maximal element. We derive the following structural constraints:

1.  **Total Sum Constraint:** The total sum is non-increasing and bounded by the initial sum: $S_{final} \le S_0 = 1997$. Furthermore, $S_{final}$ must be a positive odd integer.
2.  **Number of Elements Constraint:** Since the game must terminate before $S$ potentially reaches 0, and $N$ decreases by 1 each round, $1 \le N_{final} \le 1996$. (If $N_{final}=1997$, no rounds were played, and $2X_{max} > S_{final}$ would fail for initial state).
3.  **Constraint on Maximal Element ($X_{max}$):** The termination condition $2X_{max} > S_{final}$ dictates a strong lower bound for $X_{max}$.
    $$X_{max} > S_{final} / 2$$
    Combining this with $X_{max} \le S_{final}$, the necessary range for $X_{max}$ is $\lceil (S_{final}+1)/2 \rceil \le X_{max} \le S_{final}$. Since $S_{final} \le 1997$, $X_{max}$ is constrained to be at least $\lceil 1/2 \rceil + 1 = 1$.
4.  **Constraint on Average Value ($\bar{X} = S_{final}/N_{final}$):**
    The average value must satisfy $\bar{X} \le X_{max}$. More specifically, using the termination condition:
    $$\bar{X} \cdot N_{final} < 2X_{max}$$
    Since $X_{max}$ is the largest element, the average must be strictly less than $2X_{max}/N_{final}$ if $N_{final} > 1$. However, a simpler, general constraint based on the total sum $S_0$ is:
    $$\bar{X} \le S_{final}/N_{final} \le 1997 / N_{final}$$
    The smallest possible $N_{final}$ is 1, leading to the largest possible average: $\bar{X} \le 1997$.

### [W4, round 2]
REPORT on task "Analyze the structure of the values remaining when the game terminates. If $N_{final}$ elements remain, find constraints on the average value $S_{final}/N_{final}$ and the maximal element $X_{max}$ ba": I analyzed the game structure, establishing that the total sum $S$ is non-increasing and must remain odd because $S_0=1997$ is odd, ruling out termination Condition (2). Therefore, the game must terminate via Condition (1) ($2X_{max} > S_{final}$). Based on this, I derived structural constraints: $S_{final}$ is a positive odd integer $\le 1997$; $1 \le N_{final} \le 1996$; the maximal element must satisfy $X_{max} > S_{final}/2$; and the average value $\bar{X}$ is upper bounded by $1997/N_{final}$.
Candidate answer: Constraints are derived based on the non-increasing nature of the sum $S$ and the parity invariant. For the maximal element $X_{max}$, it must satisfy $X_{max} > S_{final}/2$. For the average value $\bar{X} = S_{final}/N_{final}$, it must satisfy $\bar{X} \le 1997/N_{final}$.

### [W1, round 2]
MIN/MAX N_final under Condition (1):
Based on the constraint 2*X_max > S_final and the fact that S is non-increasing, N_final must be small.
1. Minimum N_final (B's goal): B can force termination in N_final = 1 element by repeatedly choosing z = x+y, maintaining S=1997 until all values aggregate into one. (R=1996).
2. Maximum N_final (A's goal): Structural analysis suggests N_final cannot be large because if N is large, the elements must be close to 1 to keep S high, which fails the termination condition 2*X_max > S_final. The maximum achievable is N_final = 2.

Result: min(N_final) = 1, max(N_final) = 2.

### [W1, round 2]
REPORT on task "Determine the minimum possible value of the final number of elements $N_{final}$ and the maximum possible value of $N_{final}$ under optimal play, given that the game must terminate via Condition (1).": I analyzed the game structure, particularly focusing on the invariant sum $S$ (non-increasing) and the termination condition $2X_{max} > S_{final}$. To find the minimum $N_{final}$ (B's optimal play), B forces $z=x+y$ repeatedly, keeping $S=1997$ and driving $N_{final}$ down to 1. For the maximum $N_{final}$ (A's optimal play), structural constraints dictate that if $N_{final}$ is large, $S_{final}/N_{final}$ must be small, preventing the termination condition from being met. The maximum possible $N_{final}$ that allows for the necessary imbalance is 2.
Candidate answer: min(N_final) = 1, max(N_final) = 2
