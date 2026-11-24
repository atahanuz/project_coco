### [W4, round 1]
# Analysis of Numbers N with digits in {0, 1, 2, 8} divisible by 3

The number $N$ must be divisible by 3, meaning the sum of its digits must be divisible by 3. The allowed digits are $D = \{2, 0, 1, 8\}$.
Residues modulo 3 for $D$:
0: $R(0)=0$ (1 digit)
1: $R(1)=1$ (1 digit)
2: $R(2)=2$ (2 digits: 2, 8)

Let $S_L(r)$ be the count of numbers of length $L$ whose digits sum to $r \pmod 3$.
The first digit $d_1$ must be non-zero, so $d_1 \in \{1, 2, 8\}$.

---
**L=1 Calculation:**
Possible non-zero digits: {1, 2, 8}.
S_1(0) = 0
S_1(1) = 1 (for digit 1)
S_1(2) = 2 (for digits 2, 8)
Count for L=1: 0.

**L=2 Calculation:**
We require $d_1 + d_2 \equiv 0 \pmod 3$.
S_2(0) = 4 (12, 18, 21, 81)
S_2(1) = 5
S_2(2) = 3
Count for L=2: 4.

**L >= 3 Recurrence:**
For $L \ge 3$, the recurrence relations hold using $C_0=1, C_1=1, C_2=2$:
S_L(0) = S_{L-1}(0) * 1 + S_{L-1}(1) * 2 + S_{L-1}(2) * 1
S_L(1) = S_{L-1}(0) * 1 + S_{L-1}(1) * 1 + S_{L-1}(2) * 2
S_L(2) = S_{L-1}(0) * 2 + S_{L-1}(1) * 1 + S_{L-1}(2) * 1

**L=3 Calculation:**
S_3(0) = S_2(0)*1 + S_2(1)*2 + S_2(2)*1 = 4 + 5*2 + 3*1 = 17.
S_3(1) = S_2(0)*1 + S_2(1)*1 + S_2(2)*2 = 4 + 5 + 3*2 = 15.
S_3(2) = S_2(0)*2 + S_2(1)*1 + S_2(2)*1 = 4*2 + 5 + 3 = 16.
Count for L=3: 17.

**L=4 Calculation:**
S_4(0) = S_3(0)*1 + S_3(1)*2 + S_3(2)*1 = 17 + 15*2 + 16 = 17 + 30 + 16 = 63.
S_4(1) = S_3(0)*1 + S_3(1)*1 + S_3(2)*2 = 17 + 15 + 16*2 = 32 + 32 = 64.
S_4(2) = S_3(0)*2 + S_3(1)*1 + S_3(2)*1 = 17*2 + 15 + 16 = 34 + 31 = 65.
Count for L=4: 63.

**L=5 Calculation:**
S_5(0) = S_4(0)*1 + S_4(1)*2 + S_4(2)*1 = 63 + 64*2 + 65 = 63 + 128 + 65 = 256.
S_5(1) = S_4(0)*1 + S_4(1)*1 + S_4(2)*2 = 63 + 64 + 65*2 = 127 + 130 = 257.
S_5(2) = S_4(0)*2 + S_4(1)*1 + S_4(2)*1 = 63*2 + 64 + 65 = 126 + 129 = 255.
Count for L=5: 256.

**Summary:**
L=1: 0
L=2: 4
L=3: 17
L=4: 63
L=5: 256

### [W2, round 3]
**[W2] Algebraic Verification of Total Sum S**

The problem requires calculating $S = \sum_{L=1}^{16} A_L$, where $A_L$ is the count of $L$-digit numbers formed by $\{0, 1, 2, 8\}$ divisible by 3. We verified the algebraic derivation $S = (4^{16} - 4)/3$.

1. **Full Count ($A_L^{full}$):** Considering all $4^L$ sequences of length $L$ (including leading zeros), the number whose digit sum is $0 \pmod 3$ is found using generating functions. This yields:
$$A_L^{full} = \frac{1}{3} (4^L + \omega^{2L} + \omega^L)$$
where $\omega = e^{2\pi i/3}$.

2. **Constrained Count ($A_L$):** For natural numbers, we must exclude sequences starting with 0. If a sequence starts with 0 (a digit with residue 0 mod 3), the remaining $L-1$ digits must sum to $0 \pmod 3$. Thus, $A_L = A_L^{full} - A_{L-1}^{full}$. (We define $A_0^{full} = 1$).

3. **Telescoping Sum:** The total sum $S$ is a telescoping series:
$$S = \sum_{L=1}^{16} A_L = \sum_{L=1}^{16} (A_L^{full} - A_{L-1}^{full}) = A_{16}^{full} - A_0^{full}$$

4. **Final Calculation:** Since $16 \equiv 1 \pmod 3$, $A_{16}^{full}$ takes the form $\frac{4^{16} - 1}{3}$.
$$S = \frac{4^{16} - 1}{3} - 1 = \frac{4^{16} - 1 - 3}{3} = \frac{4^{16} - 4}{3}$$
This rigorously confirms the closed form provided. The numerical value is $1,431,655,764$.

### [W1, round 3]
## Independent DP Verification (L=16)

I independently re-implemented the DP calculation using the established recurrence relations derived in Round 1, starting from the verified base cases $L=1$ and $L=2$.

**Recurrence Check:**
The recurrence relations derived from considering transitions based on the last digit (which can be any digit in {0, 1, 2, 8}) appear correct and hold for $L \ge 3$. The initialization using $S_2 = [4, 5, 3]$ (from the notes) correctly incorporates the constraint that the first digit must be non-zero.

**Computational Results (L=1 to L=16):**
The calculation was carried out up to $L=16$.
$A_1 = 0$
$A_2 = 4$
$A_3 = 17$
$A_4 = 63$
$A_5 = 256$
...
$A_{16} = 1,073,741,823$.

**Total Sum Verification:**
The total sum of counts for $L=1$ through $L=16$ is:
$\sum_{L=1}^{16} A_L = 1,431,655,764$.
