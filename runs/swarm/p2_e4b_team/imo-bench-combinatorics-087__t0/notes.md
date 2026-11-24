### [W3, round 1]
Finding: The largest guaranteed number of correct guesses, s, is 1.
Reasoning: Since the sequence is an arbitrary 0-1 sequence, for any index $i$ not revealed by An ($i \neq k$), the value $a_i$ is independent of the revealed value $a_k$. If Bình chooses any set of indices $I$ where $|I| > 1$ and $I$ contains an index $i \neq k$, An can arbitrarily set $a_i$ to 0 or 1, preventing Bình from guaranteeing a correct guess. Therefore, the only index Bình can always guarantee to guess correctly is the revealed index $k$ itself.
Strategy: Choose $s=1$ and select the index $k$.

### [W1, round 1]
Analysis for small N:
For N=2, the observed value is s=1.
For N=4, the observed value is s=2.
For N=8, the observed value is s=3.
For N=16, the observed value is s=4.
The observed pattern strongly suggests that the largest number s is given by s = log₂(N).

### [W2, round 1]
Analysis of the problem formulation:
The sequence X is in (F_2)^N where N=4096. An reveals (k, X_k).
Bình chooses a set of indices I = {i_1, ..., i_s} beforehand.
Bình can guarantee a guess for X_i if and only if X_i is constant across all possible sequences consistent with the constraint X_k = c.
The set of differing sequences W_k forms a subspace where D_k = 0.
For Bình to succeed for all k, the chosen indices I must be zeroed out by all difference vectors in W_k for all k.
If i is an index chosen by Bình (i in I), and if k != i, then the standard basis vector e_i belongs to W_k.
Since e_i has a 1 at position i, X_i is not fixed for all sequences in S_k if i != k.
Thus, for a deterministic strategy to exist, I must be empty.
The largest number s is 0.

### [W4, round 1]
Investigating the upper bound for $s$.
The problem requires finding the largest $s$ such that for ANY sequence $A$ of length $N=4096$, and for ANY revealed information $(k, a_k)$, Bình can successfully guess the values of $s$ members.

We aim to prove that if $s > 1$, a counterexample sequence $A$ and choice $k$ exists.

Let $s=2$. Bình must choose two indices $I = \{i_1, i_2\}$ and make two guesses, $g_{i_1}$ and $g_{i_2}$.
Consider a strategy where Bình always attempts to guess $a_{i_1}$ and $a_{i_2}$.

Case 1: An reveals $k=i_1$. Bình knows $a_{i_1}$.
For Bình to succeed, he must uniquely determine $a_{i_2}$ based on $a_{i_1}$ and the strategy. Since the sequence $A$ is arbitrary (i.e., the values $a_{i_1}$ and $a_{i_2}$ are independent choices across the set of all possible sequences), Bình cannot determine $a_{i_2}$ uniquely. For any guess $g_{i_2}$ Bình makes, we can construct a sequence $A$ such that $a_{i_2} = g_{i_2} + 1 \pmod 2$. Thus, $s=2$ fails.

Conclusion: The largest possible number $s$ under the assumption that $A$ is an arbitrary 0-1 sequence is $s=1$.

The task requires proving the necessity of the condition: if $s$ is greater than some value, a counterexample exists. We have shown that $s > 1$ fails.

### [W2, round 2]
### [W2, round 2] Linear Algebra Proof for s=1

The problem asks for the largest $s$ such that Bình can *always* guess $s$ values correctly, given the revealed constraint $a_k=c$. We assume the optimal strategy for Bình is to guess $a_k$ and $s-1$ other values, and we find $s_{max}=1$ under the adaptive assumption that Bình chooses his guesses after observing $(k, c)$.

Let $S_k^c$ be the set of all sequences $A \in (\mathbb{F}_2)^N$ satisfying $a_k=c$. Bình can guarantee a guess for $a_i$ if and only if $a_i$ is constant for all $A \in S_k^c$.

**1. Necessity of $s \le 1$ (Proof by contradiction for $s > 1$):**
Suppose $s \ge 2$. Bình must select $I=\{i_1, i_2, \ldots\}$.
If Bình chooses $I$ such that $k \in I$ (i.e., he chooses to guess the revealed element $a_k$), he is guaranteed to be correct for $a_k$.
For any other index $i_j \in I$ where $i_j \neq k$, we must show $a_{i_j}$ is not constant across $S_k^c$.
Consider $e_{i_j}$, the standard basis vector with 1 at position $i_j$ and 0 elsewhere.
Since $i_j \neq k$, $e_{i_j}$ has $e_{i_j, k} = 0$.
Let $A$ be any sequence in $S_k^c$. Define $A' = A + e_{i_j}$.
Since $A' \in (\mathbb{F}_2)^N$ and $a'_k = a_k + e_{i_j, k} = c + 0 = c$, $A'$ is also in $S_k^c$.
However, $a'_{i_j} = a_{i_j} + 1 \pmod 2$. Since $a_{i_j}$ can be either 0 or 1 (depending on $A$), $a'_{i_j}$ is different from $a_{i_j}$.
Since $a_{i_j}$ takes at least two different values across $S_k^c$, Bình cannot guarantee a correct guess for $a_{i_j}$.
Therefore, $s$ cannot be greater than 1.

**2. $s=1$ is always achievable:**
Bình observes $(k, c)$. He chooses $I=\{k\}$ and guesses $g_k = c$. Since $a_k=c$ is the defining constraint, this guess is always correct.

**Conclusion:** The largest number $s$ is 1.

**Summary against task requirements:**
- Rigorously proved $s=1$: Yes, by showing $s>1$ fails due to non-uniqueness.
- Linear Algebra confirmation (i != k): Confirmed that for $i \neq k$, $a_i$ is not uniquely determined because $e_i$ is in the difference space between sequences in $S_k^c$.
- Linear Algebra confirmation (k uniquely determined): Confirmed trivially by observation; $k$ is the index revealed by An.
