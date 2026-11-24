### [W2, round 1]
Found the maximum score N when the set S is known: N=68. Justification: Due to the constraint that for any magnitude k, S contains only positive k or only negative -k (but not both), the zero-sum erasure constraint is never binding. The student can erase all 136 integers, guaranteeing 1 point for all 68 pairs.

### [W1, round 1]
**Proof Attempt for Task:** Prove that the set S (formed by 68 pairs $P_i$) contains no additive inverse pairs, given that for $k>0$, at most one of the pairs $\{k, k\}$ and $\{-k, -k\}$ is present.

**Observation:** Under the standard interpretation where the 68 pairs can be arbitrary pairs of nonzero integers, the statement is false (e.g., a pair $\{1, -1\}$ satisfies the constraint but violates the conclusion).

**Assumption:** To make the statement provable using the given constraint, we must assume that all 68 pairs $P_i$ are restricted to be of the form $\{k, k\}$ or $\{-k, -k\}$ for some positive integer $k$.

**Proof based on assumption:**
Let $S$ be the set of integers contained in the 68 pairs $P_1, \ldots, P_{68}$.
Assume for contradiction that there exists an integer $x \in S$ such that $-x \in S$ and $x \neq 0$.

Case 1: $x > 0$.
Since $x \in S$ and we assume $P_i$ must be of the form $\{k, k\}$ or $\{-k, -k\}$, $x$ must belong to a pair $P_i$. If $P_i = \{-k, -k\}$, then $x=-k < 0$, a contradiction. Thus, $P_i$ must be $\{x, x\}$.
Since $-x < 0$ and $-x \in S$, $-x$ must belong to a pair $P_j$. Since $-x < 0$, $P_j$ must be of the form $\{-k', -k'\}$. Since $-x = -k'$, $P_j = \{-x, -x\}$.
The constraint states that for $k=x>0$, at most one of $\{x, x\}$ and $\{-x, -x\}$ is written. Since both $P_i=\{x, x\}$ and $P_j=\{-x, -x\}$ are present, this violates the constraint. This is a contradiction.

Case 2: $x < 0$.
Let $k = -x > 0$. Then $x = -k$.
Since $x \in S$, $x$ belongs to a pair $P_i$. Since $x < 0$, $P_i$ must be $\{-k, -k\}$.
Since $-x = k > 0$ and $-x \in S$, $-x$ belongs to a pair $P_j$. Since $-x > 0$, $P_j$ must be $\{k, k\}$.
The constraint states that for $k>0$, at most one of $\{k, k\}$ and $\{-k, -k\}$ is written. Since both $P_j=\{k, k\}$ and $P_i=\{-k, -k\}$ are present, this violates the constraint. This is a contradiction.

In both cases, the assumption that $S$ contains an additive inverse pair leads to a violation of the given constraint (under the necessary assumption that all pairs are of the form $\{k, k\}$ or $\{-k, -k\}$).
Therefore, if all 68 pairs are of the form $\{k, k\}$ or $\{-k, -k\}$, the set $S$ contains no additive inverse pairs.

### [W2, round 1]
REPORT on task "Assuming W1's proof is correct, determine the maximum score N achievable by the student when the complete set S is known, justifying the value based on the scoring rule and the constraint on erased in": I analyzed the constraints of the problem and determined the maximum possible score N when the full set S is known. Due to the restriction that for any magnitude k, S contains only positive or only negative integers, the constraint against erasing integers that sum to zero is never binding. The student can therefore erase all 136 integers in S, guaranteeing at least one erased integer for all 68 pairs. The maximum score is thus 68.
Candidate answer: 68

### [W1, round 1]
REPORT on task "Rigorously prove that the given constraint (for each positive integer k, at most one of (k, k) and (-k, -k) is written) guarantees that the set of 136 integers S contains no additive inverse pairs (i.": I rigorously proved the claim that the set S contains no additive inverse pairs. I noted that the claim is only provable if we assume all 68 pairs are restricted to be of the form $\{k, k\}$ or $\{-k, -k\}$, as the stated constraint alone is insufficient otherwise. Under this necessary assumption, the existence of $x$ and $-x$ in S directly contradicts the rule that at most one pair of the form $\{k, k\}$ and $\{-k, -k\}$ can exist for any $k>0$.
Candidate answer: The property holds, provided that all 68 pairs are restricted to being of the form $\{k, k\}$ or $\{-k, -k\}$.
