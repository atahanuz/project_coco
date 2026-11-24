### [W4, round 1]
Strategy for counting numbers of length L:
Let C_L(r) be the count of sequences of length L using digits {0, 1, 2, 8} whose sum is congruent to r mod 3.
The total count of sequences of length L whose sum is 0 mod 3 is C_L(0).
The required count N_L for natural numbers (no leading zero) is:
N_L = C_L(0) - C_{L-1}(0)

Base Case (L=0): C_0(0) = 1, C_0(1) = 0, C_0(2) = 0.

Recurrence Relations (L >= 1):
a_L = 1 * a_{L-1} + 2 * b_{L-1} + 1 * c_{L-1}  (where a=C(0), b=C(1), c=C(2))
b_L = 1 * a_{L-1} + 1 * b_{L-1} + 2 * c_{L-1}
c_L = 2 * a_{L-1} + 1 * b_{L-1} + 1 * c_{L-1}
(Coefficients correspond to the counts of {d mod 3} for d in {0, 1, 2, 8}: {0, 1, 2, 2})

### [W2, round 1]
**Dynamic Programming Approach for Sequence Counting**

Goal: Count the number of sequences of length $L$ using digits from $S=\{0, 1, 2, 8\}$ whose digits sum to $0 \pmod 3$.

1.  **State Definition**:
    Let $dp[i][j]$ be the number of sequences of length $i$ such that the sum of the digits is congruent to $j$ modulo 3, where $i \ge 1$ and $j \in \{0, 1, 2\}$.

2.  **Digit Analysis (Modulo 3)**:
    We categorize the allowed digits $S$ based on their residue modulo 3:
    *   $r=0$: Digits $\{0\}$. Count $C_0 = 1$.
    *   $r=1$: Digits $\{1\}$. Count $C_1 = 1$.
    *   $r=2$: Digits $\{2, 8\}$. Count $C_2 = 2$.

3.  **Base Case ($L=1$)**:
    $dp[1][0] = C_0 = 1$
    $dp[1][1] = C_1 = 1$
    $dp[1][2] = C_2 = 2$

4.  **Recurrence Relation (For $i > 1$)**:
    To transition from length $i-1$ to $i$, if the current sum is $j \pmod 3$, and the previous sum was $k \pmod 3$, we must append a digit $d$ such that $d \equiv j - k \pmod 3$.

    $dp[i][j] = \sum_{k=0}^{2} dp[i-1][k] \cdot C_{(j - k) \pmod 3}$

    Expanding the relations for $j=0, 1, 2$:

    *   $dp[i][0] = dp[i-1][0] \cdot C_0 + dp[i-1][1] \cdot C_2 + dp[i-1][2] \cdot C_1$
        $dp[i][0] = dp[i-1][0] + 2 dp[i-1][1] + dp[i-1][2]$

    *   $dp[i][1] = dp[i-1][0] \cdot C_1 + dp[i-1][1] \cdot C_0 + dp[i-1][2] \cdot C_2$
        $dp[i][1] = dp[i-1][0] + dp[i-1][1] + 2 dp[i-1][2]$

    *   $dp[i][2] = dp[i-1][0] \cdot C_2 + dp[i-1][1] \cdot C_1 + dp[i-1][2] \cdot C_0$
        $dp[i][2] = 2 dp[i-1][0] + dp[i-1][1] + dp[i-1][2]$

The final answer to the sequence counting problem for length $L$ is $dp[L][0]$.

### [W3, round 1]
Analysis for counting sequences of length L with digit sum $\equiv 0 \pmod 3$.
Allowed digits S = {2, 0, 1, 8}. Residues modulo 3: c_0=1 ({0}), c_1=1 ({1}), c_2=2 ({2, 8}).

Using generating functions $G(x) = 1 + x + 2x^2$, the number of sequences $a_0(L)$ is given by:
$a_0(L) = \frac{1}{3} \left( (G(1))^L + (G(\omega))^L + (G(\omega^2))^L \right)$, where $\omega = e^{i 2\pi/3}$.

We found $G(1) = 4$, $G(\omega) = \omega^2$, and $G(\omega^2) = \omega$.
Thus, the closed-form expression is:
$a_0(L) = \frac{1}{3} \left( 4^L + \omega^{2L} + \omega^{L} \right)$.

This simplifies based on $L \pmod 3$:
1. If $L \equiv 0 \pmod 3$: $a_0(L) = (4^L + 2)/3$.
2. If $L \equiv 1 \pmod 3$: $a_0(L) = (4^L - 1)/3$.
3. If $L \equiv 2 \pmod 3$: $a_0(L) = (4^L - 1)/3$.

A simplified recurrence relation can also be found using the transition matrix M = [[1, 2, 1], [1, 1, 2], [2, 1, 1]] for the counts $(a_0, a_1, a_2)$.

### [W1, round 1]
Manual count for length L=1:
Allowed digits (natural numbers): {1, 2, 8}.
None of these sum to $0 \pmod 3$.
N(1) = 0.

Manual count for length L=2:
Numbers $d_1 d_2$ where $d_1 \in \{1, 2, 8\}$ and $d_2 \in \{0, 1, 2, 8\}$.
We need $d_1 + d_2 \equiv 0 \pmod 3$.
1. $d_1 \equiv 1 \pmod 3$ (i.e., $d_1=1$) and $d_2 \equiv 2 \pmod 3$ (i.e., $d_2 \in \{2, 8\}$). Count: 2.
2. $d_1 \equiv 2 \pmod 3$ (i.e., $d_1 \in \{2, 8\}$) and $d_2 \equiv 1 \pmod 3$ (i.e., $d_2=1$). Count: 2.
Total N(2) = 4. (Numbers: 12, 18, 21, 81)

Manual count for length L=3:
Numbers $d_1 d_2 d_3$ where $d_1 \in \{1, 2, 8\}$ and $d_2, d_3 \in \{0, 1, 2, 8\}$.
We need $d_1 + d_2 + d_3 \equiv 0 \pmod 3$.
We use the counts of 2-digit sequences $d_2 d_3$ that sum to $r \pmod 3$. Let $S_2(r)$ be this count.
Digits set $D=\{0, 1, 2, 8\}$. Remainders mod 3: $R_0=\{0\}, R_1=\{1\}, R_2=\{2, 8\}$.
Using DP setup (allowing leading zeros for $d_2, d_3$):
A_1(0)=1, A_1(1)=1, A_1(2)=2.
A_2(0)=5, A_2(1)=6, A_2(2)=5. Thus S_2(0)=5, S_2(1)=6, S_2(2)=5.
1. $d_1=1$ ($1 \pmod 3$): Need $d_2+d_3 \equiv -1 \equiv 2 \pmod 3$. Count: S_2(2) = 5.
2. $d_1=2$ ($2 \pmod 3$): Need $d_2+d_3 \equiv -2 \equiv 1 \pmod 3$. Count: S_2(1) = 6.
3. $d_1=8$ ($2 \pmod 3$): Need $d_2+d_3 \equiv 1 \pmod 3$. Count: S_2(1) = 6.
Total N(3) = 5 + 6 + 6 = 17.

Verification of DP setup:
The setup for $A_L(r)$ (sequences of length L with digits from D, sum $\equiv r \pmod 3$) is:
$A_L(r) = 1 \cdot A_{L-1}(r) + 1 \cdot A_{L-1}((r-1) \bmod 3) + 2 \cdot A_{L-1}((r-2) \bmod 3)$.
This was verified by calculating $A_2(r)$ and using it to find $N(3)$.
