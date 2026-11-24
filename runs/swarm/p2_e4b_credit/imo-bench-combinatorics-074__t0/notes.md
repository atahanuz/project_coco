### [W1, round 1]
Necessary condition for Alice to prevent Bob from winning in Round 1 (for any cut k): For every k in {1, ..., 99}, it must hold that min(x_1, ..., x_k) >= 2 OR min(x_{k+1}, ..., x_{100}) >= 2. This ensures that for any cut, Alice can choose a group such that the other group survives the $\pm 1$ operation.

### [W3, round 2]
### [W3, analysis of sufficiency]
The condition derived by W1: For every cut k in {1, ..., 99}, it must hold that min(x_1, ..., x_k) >= 2 OR min(x_{k+1}, ..., x_{100}) >= 2, is necessary AND sufficient for Alice to prevent Bob from winning indefinitely. This is because for any cut k, if this condition holds, Alice can always choose a group (G_A) such that the minimum pebble count in the *other* group (G_O) is at least 2, ensuring that after losing one pebble, all boxes in G_O still contain at least 1 pebble. Since this structural requirement must hold for *any* future cut k, if the initial state satisfies it, all subsequent safe states must also satisfy it.

### [W4, round 2]
Investigating non-uniform distributions satisfying the Round 1 necessary condition: For any cut k, $\min(x_1, \ldots, x_k) \ge 2$ OR $\min(x_{k+1}, \ldots, x_{100}) \ge 2$.

If there are two or more boxes with $x_i=1$, say $x_{i_1}=1$ and $x_{i_2}=1$ with $i_1 < i_2$, choosing the cut $k=i_1$ results in $\min(x_1, \ldots, x_{i_1}) = 1$ and $\min(x_{i_1+1}, \ldots, x_{100}) = 1$, violating the condition. Thus, at most one box can have $x_i=1$.

Case 1: All $x_i \ge 2$. Minimum sum $n = 100 \times 2 = 200$.
Case 2: Exactly one box, say $x_{i^*}=1$. To satisfy the condition for all $k$, all other boxes must have $x_j \ge 2$. If $x_j=2$ for all $j \ne i^*$, the total sum is $n = 1 + 99 \times 2 = 199$. This distribution satisfies the condition for all $k$.

The minimum possible sum $n$ is 199.

### [W2, round 3]
Verification of distribution {1, 2, ..., 2}:
The proposed distribution has exactly one box $B_{i^*}$ with 1 pebble, and all other 99 boxes have 2 pebbles.
The necessary condition for Alice to prevent Bob from winning is that for any cut $k \in \{1, \ldots, 99\}$, either $\min(x_1, \ldots, x_k) \ge 2$ OR $\min(x_{k+1}, \ldots, x_{100}) \ge 2$.

If the box $B_{i^*}$ is in the left group ($i^* \le k$), then $\min(x_1, \ldots, x_k) = 1$. Since all boxes in the right group ($B_{k+1}, \ldots, B_{100}$) have 2 pebbles (as $i^* \le k$), $\min(x_{k+1}, \ldots, x_{100}) = 2$. The condition holds (since $2 \ge 2$).
If the box $B_{i^*}$ is in the right group ($i^* > k$), then $\min(x_{k+1}, \ldots, x_{100}) = 1$. Since all boxes in the left group ($B_1, \ldots, B_k$) have 2 pebbles (as $i^* > k$), $\min(x_1, \ldots, x_k) = 2$. The condition holds (since $2 \ge 2$).

Thus, the distribution {1, 2, ..., 2} satisfies the necessary condition for all $k$.

### [W1, round 3]
### [W1, proof for n=198]
We aim to prove that any distribution $\{x_i\}$ summing to $n=198$ (assuming $x_i \ge 1$) violates the necessary condition: For every cut $k$, $\min(x_1, \ldots, x_k) \ge 2$ OR $\min(x_{k+1}, \ldots, x_{100}) \ge 2$.

1.  **Condition Implies Structure:** The condition can only be satisfied if there is at most one box $x_i$ such that $x_i=1$. If there are two such boxes, $x_{i_1}=1$ and $x_{i_2}=1$ ($i_1 < i_2$), the cut $k=i_1$ shows $\min(x_1, \ldots, x_{i_1})=1$ and $\min(x_{i_1+1}, \ldots, x_{100})=1$, violating the condition. The minimum sum $n$ for the condition to hold is 199 (achieved by one box being 1 and the rest being 2).

2.  **Constraint on Sum:** Since $n=198 < 199$, any distribution summing to 198 must have at least two boxes $x_i=1$. (More formally, if $N_1$ is the count of $x_i=1$, the sum is $\ge 200 - N_1$, so $198 \ge 200 - N_1 \implies N_1 \ge 2$).

3.  **Conclusion:** Since $n=198$ forces $N_1 \ge 2$, there exist $i_1 < i_2$ such that $x_{i_1}=1$ and $x_{i_2}=1$. Choosing the cut $k=i_1$ results in both groups having a minimum of 1, violating the necessary condition.
