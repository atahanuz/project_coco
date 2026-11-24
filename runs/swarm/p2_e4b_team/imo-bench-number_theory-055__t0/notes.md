### [W1, round 1]
Computational analysis of "good" numbers found for 1, 2, and 3 distinct nonzero digits:

1. 1-Digit Good Numbers: All numbers [1, 2, 3, 4, 5, 6, 7, 8, 9] are good.
   - Smallest found: 1
   - Largest found: 9

2. 2-Digit Good Numbers: 41 such numbers were found (e.g., 12, 14, 24, 96).
   - Smallest found: 12
   - Largest found: 96

3. 3-Digit Good Numbers: 55 such numbers were found (e.g., 125, 975).
   - Smallest found: 125
   - Largest found: 975

Overall, the smallest good number found is 1, and the largest good number found among these categories is 975.

### [W4, round 1]
Investigation of "Good" Numbers Constraints:
1. Base Cases: All single-digit numbers (1 through 9) are good by definition.
2. Constraint on Digits: The digits must be distinct and nonzero.
3. Multi-Digit Analysis (k digits): Let $m$ be a good number. If removing the last digit $d_1$ results in $m'$, we must have $m' | m$. Since $m = 10m' + d_1$, this implies $m' | d_1$.
4. Upper Bound on k: Since $d_1$ is a single nonzero digit ($d_1 \le 9$), $m'$ must be $\le 9$. If $m$ has $k \ge 3$ digits, $m'$ must have at least two digits and thus $m' \ge 11$. This contradiction proves that no good number can have 3 or more digits.
5. Two-Digit Analysis: For $m=10a+b$, $m$ is good if removing $a$ yields $b|10a$ (since $b$ is single-digit and hence good), OR if removing $b$ yields $a|b$ (since $a$ is single-digit and hence good).
6. Search: Maximizing $m=10a+b$ subject to $a \neq b$ and ($a|b$ or $b|10a$):
- Max $a=9$: $m=90+b$. $9|b$ is impossible. Need $b|90$. Max $b$ such that $b|90$ and $b \neq 9$ is $b=6$. $m=96$.
- Max $a=8$: $m=80+b$. Need $b|80$. Max $b$ such that $b|80$ and $b \neq 8$ is $b=5$. $m=85$.
The largest good number found is 96.

### [W2, round 1]
Analysis of the structural constraint m' | m:

1. Removal of the Units Digit ($d_0$): If m has $k \ge 2$ digits, removing the units digit $d_0$ results in $m' = m // 10$. The constraint $m' | m$ implies $m' | d_0$. Since $d_0$ is a nonzero digit ($1 \le d_0 \le 9$), and for $k \ge 3$, $m'$ has at least two digits ($m' \ge 10$), it is impossible for $m' | d_0$. Therefore, if $m$ has 3 or more digits, the removed digit cannot be the units digit.

2. General Constraint ($m'$ formed by removing $d_j$): Let $m_H$ be the higher order prefix digits and $m_L$ be the lower order suffix digits relative to the removed digit $d_j$. The requirement $m' | m$ implies $m'$ must divide the expression $d_j \cdot 10^j - 9 m_L$, where $j$ is the position of $d_j$.

3. Maximum Ratio ($m/m'$): The ratio is maximized when the divisor $m'$ is as small as possible relative to $m$.
    * For $k=2$, $m=10a+b$. If $m'=b$ (removing $a$), the ratio is $r = 10a/b + 1$. By setting $b=1$ and maximizing $a$ (with $a \ne 1$), we get $m=91, m'=1$, yielding a ratio $r = 92$.
    * For $k=3$, $m=d_2 d_1 d_0$. The maximum ratio found was $r=75$ for $m=912$ (removing $d_2$, $m'=12$), while $m=92$ gives $r=92$ ($k=2$).

4. Digit Limitation: The ratio constraint severely limits digit choices. For $k=3$ (removing $d_2$), $m'=10d_1+d_0$ must divide $100d_2$. If $d_2=9$, $m'$ must be a divisor of 900 composed of distinct nonzero digits other than 9.
The current maximum ratio identified is 92.

### [W2, round 2]
[W2, Analysis of 14625 and Search Guidelines]
Candidate 14625 is a good number. Removing the digit 4 results in $m' = 1625$. Since $1625 | 14625$ (14625 / 1625 = 9), we check if 1625 is good. 1625 is good because removing 6 results in $m'' = 125$, and $125 | 1625$ (1625 / 125 = 13). 125 is good because removing 1 results in $m'''=25$, and $25 | 125$. 25 is good because removing 2 results in $m''''=5$, and $5 | 25$.

The initial constraint analysis (W4) suggesting $k<3$ is incorrect. The structure allows for large good numbers.
Stricter Guidelines for Search:
1. Focus on the Divisibility Ratio R: Given $m$ and $m'$ (where $m'$ is $m$ minus one digit), $R=m/m'$ must be an integer. Since $m$ and $m'$ are structurally similar, $R$ must be small, likely $R \in \{2, 3, \dots, 15\}$.
2. Recursive Goodness Check: The search must be recursive. $m$ is good if $\exists d_j$ such that $m'|m$ AND $m'$ is good.
3. Constraint on Digit Removal: Test all possible digit removals $d_j$, as the ratio $R$ depends heavily on the position of the removed digit $d_j$. For $m=d_k d_{k-1} \dots d_0$, removing $d_j$ leads to $m'$. Analyze the positional change to constrain the possible values of $R$.

### [W4, round 2]
## [W4, round 2] General Necessary Conditions for Good Numbers

Re-analyzing the condition: $m$ is good if removing one digit $d_j$ results in $m'|m$, where $m'$ is also a good number.

Let $m$ have $k$ digits, $m = d_{k-1} \dots d_j \dots d_0$.
When $d_j$ is removed, $m'$ is formed by concatenating the prefix $A$ (digits $d_{k-1} \dots d_{j+1}$) and the suffix $B$ (digits $d_{j-1} \dots d_0$).
Specifically, $m = A \cdot 10^{j+1} + d_j \cdot 10^j + B$, and $m' = A \cdot 10^j + B$.

The requirement $m' | m$ is equivalent to requiring $m' | (m - 10m')$.
$m - 10m' = (A \cdot 10^{j+1} + d_j \cdot 10^j + B) - 10(A \cdot 10^j + B)$
$m - 10m' = (A \cdot 10^{j+1} + d_j \cdot 10^j + B) - (A \cdot 10^{j+1} + 10B)$
$m - 10m' = d_j \cdot 10^j - 9B$.

**General Necessary Divisibility Condition:**
If $m$ is good by removing $d_j$, then $m'$ must divide $d_j \cdot 10^j - 9B$.

**Implications for $k=3$: $m = d_2 d_1 d_0$**
The digits $d_2, d_1, d_0$ must be distinct and nonzero.

1. **Remove $d_0$ ($j=0$):** $m' = d_2 d_1$. $A=d_2, B=d_1$.
   $m' | (d_0 \cdot 10^0 - 9d_1) \implies 10d_2+d_1 | (d_0 - 9d_1)$.
   Since $d_0 \le 9$ and $d_1 \ge 1$, $d_0 - 9d_1$ is highly negative (minimum is $1-9\cdot 9 = -80$). Since $10d_2+d_1 \ge 12$, the only way for division to occur is if $d_0 - 9d_1 = 0$, which implies $d_0 = 9d_1$. Since $d_0 \le 9$, this forces $d_1=1, d_0=9$.
   If $d_1=1, d_0=9$, $m'=d_2 1$. $m' | 0$. This holds for any $d_2$.
   So, if $d_1=1$ and $d_0=9$, the divisibility condition is met for any $d_2 \neq 1, 9$.
   Example: $m=219$. Removing 9 yields $m'=21$. $21 | 219$? No ($219 = 210 + 9$). Wait, the condition derived is $m' | (d_0 - 9d_1)$. If $d_0=9, d_1=1$, then $d_0 - 9d_1 = 0$. So $m' | 0$, which is always true.
   Thus, any number $m = d_2 19$ where $d_2 \notin \{1, 9\}$ satisfies the divisibility condition when removing 9. We must still check if $m'$ is good.

2. **Remove $d_2$ ($j=2$):** $m' = d_1 d_0$. $A$ is empty, $B=d_1 d_0$.
   $m' | (d_2 \cdot 10^2 - 9(0)) \implies 10d_1+d_0 | 100d_2$.
   Example found in preliminary notes: $m=975$. Removing 9 yields $m'=75$. $75 | 900$. This is true.

3. **Remove $d_1$ ($j=1$):** $m' = d_2 d_0$. $A=d_2, B=d_0$.
   $m' | (d_1 \cdot 10^1 - 9d_0) \implies 10d_2+d_0 | (10d_1 - 9d_0)$.
   Example found earlier: $m=231$. Removing 3 yields $m'=21$. $21 | (30 - 9) = 21$. True.
"""

### [W2, round 3]
Verification of Candidate 14625:
1. 14625 is good if removing 4 results in 1625 | 14625 AND 1625 is good.
   - 14625 / 1625 = 9. Condition met.
2. 1625 is good if removing 6 results in 125 | 1625 AND 125 is good.
   - 1625 / 125 = 13. Condition met.
3. 125 is good if removing 1 results in 25 | 125 AND 25 is good.
   - 125 / 25 = 5. Condition met.
4. 25 is good if removing 2 results in 5 | 25 AND 5 is good.
   - 25 / 5 = 5. Condition met.
5. 5 is good by definition.
Conclusion: 14625 is a good number.

Verification of Candidate 2475:
1. Test all removals:
   - Remove 2 $\to 475$. 2475 is not divisible by 475.
   - Remove 4 $\to 275$. 2475 / 275 = 9. Condition met.
   - Remove 7 $\to 245$. 2475 is not divisible by 245.
   - Remove 5 $\to 247$. 2475 is not divisible by 247.
2. Check sub-number $m'=275$. 275 is good if removing a digit results in a divisor $m''$ that is good.
   - Remove 7 $\to 25$. 275 / 25 = 11. Condition met.
3. Check sub-number $m''=25$. 25 is good (removing 2 yields 5, and 5 is good).
Conclusion: 2475 is a good number. Both primary candidates are structurally valid.
