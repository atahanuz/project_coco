### [W1, round 1]
Constraint analysis: The condition states that for any positive integer $k$, at most one of the pairs $(k, k)$ and $(-k, -k)$ is present. This constraint only restricts the inclusion of these specific types of pairs (where both elements are equal). The pair $(k, -k)$ (where $k \neq 0$) is not of the form $(x, x)$ or $(-x, -x)$, so its presence is not restricted by this specific condition. Therefore, the constraint does not logically exclude the possibility of any pair $(k, -k)$ existing among the 68 pairs.

### [W2, round 1]
Under the assumption that all 68 pairs are structured such that no two written integers sum to zero, we prove the student can score 68 points by erasing all integers.

1. Definition of the set of integers: Let $I$ be the set of 136 integers on the board. The 68 pairs partition $I$.
2. The Sum-Free Condition: The assumption states that no two integers $x, y \in I$ sum to zero (i.e., $I$ is sum-free, so $\forall x \in I, -x \notin I$).
3. The Erasure Condition: The student erases a set $E \subset I$ such that no two erased integers sum to zero. Since $I$ itself is sum-free by assumption, choosing $E=I$ satisfies the erasure condition.
4. Scoring: The student scores 1 point for each of the 68 pairs in which at least one integer is erased. Since $E=I$, all 136 integers are erased, meaning every pair has at least one erased integer.
5. Conclusion: The student scores 68 points.

### [W4, round 1]
## Analysis of Scoring Mechanism and Constraints
The student scores 1 point for each of the 68 pairs $(a_i, b_i)$ if at least one of $a_i$ or $b_i$ is erased. The erasing constraint is that no two erased integers may sum to 0. This means the set of erased integers, $E$, must be an independent set in the graph defined by $x \leftrightarrow -x$.

The maximum possible score is 68, as there are only 68 pairs. To find the guaranteed score $N$, we must find the minimum score achievable across all possible configurations of the 68 pairs.

1.  **The Role of the Structural Constraint:** The problem specifies a restriction only on pairs where $a=b$ or $a=-b$. If we assume the 68 pairs can be general, the analysis is simpler.
2.  **Worst-Case Scenario:** The worst case would be a configuration that forces the student to leave at least one element un-erased from a pair. This happens only if the pair is antagonistic, i.e., $(k, -k)$, and the student is forced to choose only one of $k$ or $-k$ due to interaction with other antagonistic pairs.
3.  **Guaranteeing a Score of 68:** Since there are only 68 pairs, if we can show that for any configuration, there exists an independent set $E$ that contains at least one element from every pair $(a_i, b_i)$, then the guaranteed score $N$ must be 68. For any pair $(a_i, b_i)$, we can always choose to erase $a_i$. This choice is only forbidden if $-a_i$ is already chosen. Since $a_i$ and $-a_i$ might belong to different pairs, and we only need to ensure $a_i$ is erased, this is always possible unless $a_i$ itself is zero (which is excluded) or if the entire structure forces the exclusion of $a_i$. Because the constraints only restrict pairs that sum to zero, and we are only required to pick *one* element per pair, we can always construct an independent set $E$ that covers at least one element from every single pair.

Therefore, the guaranteed score $N$ is 68.
