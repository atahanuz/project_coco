### [W1, round 1]
Initial search (n=3 to n=15) for $2^n - 3 = 5^k$ yielded two solutions:
1. $n=3$: $2^3 - 3 = 5 = 5^1$. Pair (3, 1).
2. $n=7$: $2^7 - 3 = 125 = 5^3$. Pair (7, 3).
We need to continue the search for $n > 15$ or use number theory if the task implies finding all solutions, but for now, we have completed the specified computation.

### [W2, round 1]
Initial exploration of $2^n - 3 = 5^k$ for $n \ge 3$.
Tested small values: (n, k) = (3, 1) and (7, 3) are solutions.

Modular arithmetic analysis:
1. Modulo 3: $2^n - 3 \equiv 5^k \pmod{3} \implies (-1)^n \equiv (-1)^k \pmod{3}$. Thus, $n$ and $k$ must have the same parity ($n \equiv k \pmod{2}$).
2. Modulo 4: $2^n - 3 \equiv 5^k \pmod{4}$. Since $n \ge 3$, $0 - 3 \equiv 1^k \pmod{4}$, which is $1 \equiv 1 \pmod{4}$. No new constraint.
3. Modulo 5: $2^n - 3 \equiv 5^k \pmod{5}$. If $k \ge 1$, $2^n \equiv 3 \pmod{5}$. Powers of 2 mod 5 are (2, 4, 3, 1). This requires $n \equiv 3 \pmod{4}$.
4. Modulo 8: $2^n - 3 \equiv 5^k \pmod{8}$. Since $n \ge 3$, $0 - 3 \equiv 5^k \pmod{8}$, or $5 \equiv 5^k \pmod{8}$. The powers of 5 mod 8 are (5, 1, 5, 1, ...). This requires $k$ to be odd ($k \equiv 1 \pmod{2}$).

Consolidated constraints: $n$ must satisfy $n \equiv 3 \pmod{4}$, and $k$ must be odd. Note that $n \equiv 3 \pmod{4}$ implies $n$ is odd, which is consistent with $k$ being odd via the Modulo 3 constraint.

### [W3, round 1]
### Analysis Summary (Task fulfillment)
**Equation:** $2^n - 3 = 5^k$, where $n \ge 3$.

**Case 1: $n$ is even.**
Let $n = 2m$ ($m \ge 2$ since $n \ge 4$). The equation becomes $(2^m)^2 - 5^k = 3$.
Analyzing modulo 3, we found $2^n \equiv 1 \pmod 3$, implying $5^k \equiv 1 \pmod 3$, so $k$ must be even. Let $k=2j$.
The equation reduces to $(2^m)^2 - (5^j)^2 = 3$, which factors as $(2^m - 5^j)(2^m + 5^j) = 3$.
Since $2^m+5^j > 0$, the only integer factorizations are $\{1, 3\}$.
Solving the system: $2^m - 5^j = 1$ and $2^m + 5^j = 3$.
Subtracting yields $2 \cdot 5^j = 2$, so $5^j = 1$, meaning $j=0$.
If $j=0$, then $k=0$, and $2^n - 3 = 1$, so $2^n = 4$, $n=2$.
Since the problem requires $n \ge 3$, there are no solutions when $n$ is even.

**Case 2: $n$ is odd.**
We verified solutions:
1. $n=3$: $2^3 - 3 = 5 = 5^1$. (Solution)
2. $n=7$: $2^7 - 3 = 125 = 5^3$. (Solution)
Analyzing modulo 3, we found $2^n \equiv 2 \pmod 3$, implying $5^k \equiv 2 \pmod 3$, so $k$ must be odd.
Analyzing modulo 8 (since $n \ge 3$), we found $5^k \equiv 5 \pmod 8$, which requires $k$ to be odd, confirming consistency.
While a general proof for $n>7$ is difficult (related to exponential Diophantine equations), the analysis of the even case was exhaustive, and the initial search confirms two solutions. We conclude the candidate solutions are $n=3$ and $n=7$.

### [W4, round 1]
Investigation of $2^n - 5^k = 3$ where $n \ge 3$ and $k \ge 1$.
Initial checks revealed solutions $(n, k) = (3, 1)$ and $(7, 3)$.

Constraint on n (Modulo 5):
Analyzing $2^n - 5^k = 3$ modulo 5:
$2^n \equiv 3 \pmod 5$.
The powers of 2 modulo 5 cycle: 2, 4, 3, 1.
This requires $n \equiv 3 \pmod 4$. This is a strong restriction on $n$.

Constraint on k (Modulo 8):
Analyzing $2^n - 5^k = 3$ modulo 8. Since $n \ge 3$, $2^n \equiv 0 \pmod 8$.
$0 - 5^k \equiv 3 \pmod 8$
$5^k \equiv -3 \equiv 5 \pmod 8$.
The powers of 5 modulo 8 cycle: 5, 1, 5, 1, ...
This requires $k$ to be odd.

Summary of restrictions: $n$ must be of the form $4m+3$, and $k$ must be odd. We tested $n=11$ (m=2) and found $2^{11}-3 = 2045 = 5 \times 409$, which is not a power of 5.

### [W4, round 2]
### [W4, round 2] Verification of W3's Case 1: Even $n$

**Goal:** Rigorously verify W3's analysis for $2^n - 3 = 5^k$ when $n$ is even and $n \ge 3$.

**Setup:** Let $n$ be even, so $n = 2m$. Since $n \ge 3$ and $n$ is even, we must have $m \ge 2$.
The equation is $(2^m)^2 - 5^k = 3$.

**Step 1: Determining the parity of k (Modulo 3)**
Analyze the equation modulo 3:
$2^n - 3 \equiv 5^k \pmod{3}$
Since $n=2m$, $2^n = (2^2)^m = 4^m \equiv 1^m \equiv 1 \pmod{3}$.
Also, $-3 \equiv 0 \pmod{3}$.
$1 - 0 \equiv 5^k \pmod{3}$
$1 \equiv (-1)^k \pmod{3}$.
This requires $k$ to be an even integer. Let $k = 2j$, where $j \ge 0$.

**Step 2: Factoring the equation**
Substitute $k=2j$ into the original equation:
$(2^m)^2 - (5^j)^2 = 3$
Factor the difference of squares:
$(2^m - 5^j)(2^m + 5^j) = 3$.

**Step 3: Analyzing factors**
Since $m \ge 2$, $2^m \ge 4$. Since $j \ge 0$, $5^j \ge 1$. Thus, $2^m + 5^j$ is a positive integer greater than 1.
Since 3 is a prime number, the only positive integer factor pairs of 3 are (1, 3).
We must have:
1) $2^m - 5^j = 1$
2) $2^m + 5^j = 3$

**Step 4: Solving the system**
Subtracting equation (1) from equation (2):
$(2^m + 5^j) - (2^m - 5^j) = 3 - 1$
$2 \cdot 5^j = 2$
$5^j = 1$.
This implies $j=0$.

**Step 5: Finding m and n**
If $j=0$, then $k=0$. Substitute $j=0$ back into equation (1):
$2^m - 5^0 = 1$
$2^m - 1 = 1$
$2^m = 2$.
This requires $m=1$.
Since $n=2m$, we have $n=2$.

**Conclusion:** The only solution found for even $n$ is $n=2$ (which corresponds to $k=0$, giving $2^2 - 3 = 1 = 5^0$). As the problem requires $n \ge 3$, there are **no solutions** when $n$ is even and $n \ge 3$. This rigorously confirms W3's analysis.

### [W2, round 2]
### [W2, round 2] - Exponential Diophantine Equation Analysis (Task Fulfillment)
**Equation:** $2^n - 5^k = 3$, $n \ge 3$.
We have established constraints $n \equiv 3 \pmod 4$ and $k$ is odd. The problem is a classic Exponential Diophantine Equation.

**Theoretical Techniques Search:**
1. **Linear Forms in Logarithms (Baker's Theory):** This is the most powerful general technique for bounding solutions to equations of the form $a^x - b^y = c$. An effective application of Baker's theory would yield an upper bound for $n$ and $k$, after which a finite (and often small) search can be performed to verify all solutions. This is the standard rigorous approach for proving finiteness in such cases.
2. **Modular Arithmetic & Cyclotomic Fields:** While initial modular arithmetic (mod 3, 5, 8) provided necessary conditions, further analysis often requires using higher-order congruences or properties related to cyclotomic fields, especially when dealing with prime powers difference.
3. **Recurrence Relations:** Since $2^n$ and $5^k$ relate to geometric progressions, sometimes one can transform the equation into a difference of terms in a linear recurrence sequence, for which specific theorems exist regarding perfect powers.

**Attempted Path Forward:**
The current constraints ($n = 4m+3$, $k$ odd) significantly restrict the search. Given the depth required for a full proof (likely requiring Baker's theory), we confirm that the established methods point to the necessity of bounding $n$ and $k$ effectively. We conclude that the likely intended solution path for an Olympiad level problem involves finding a highly specific, non-obvious modular restriction that rules out all $n > 7$, or relying on specialized knowledge of this specific equation, which is related to a known result in number theory (often citing results by Le or similar researchers on generalized Catalan problems). We tentatively assert the solutions are $n=3$ and $n=7$ based on computational evidence and the difficulty of a full proof.

### [W3, round 2]
### [W3, round 2]
**Further investigation for odd $n > 7$:**
We established that $2^n - 3 = 5^k$ requires $n \equiv 3 \pmod 4$ and $k$ to be odd.
If $k \ge 3$, we analyze the equation modulo $5^3 = 125$, or more simply, modulo 25, as $k$ must be large enough for $n>7$.
If $k \ge 2$, then $2^n \equiv 3 \pmod{25}$. Checking the powers of 2 modulo 25 ($\phi(25)=20$), we find $2^n \equiv 3 \pmod{25}$ implies $n \equiv 7 \pmod{20}$.
We tested the smallest candidate $n > 7$ satisfying this, which is $n=27$.
$2^{27} - 3 = 134,217,725$. Dividing by $5^2=25$ yields $5,368,709$. Since $5,368,709$ is not divisible by 5, $2^{27} - 3$ is not a power of 5.
This strong restriction suggests that no further solutions exist for large $n$. The current solutions are $(n, k) = (3, 1)$ and $(7, 3)$.
