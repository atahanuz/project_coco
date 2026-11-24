### [W2, round 1]
Analysis for $C(r)$ where $r \in \{0, 1, \ldots, 60\}$ and $p=61$.
The problem is to find the number of solutions to $c^3 \equiv r \pmod{61}$ for $1 \le c \le 61$.

Case 1: $r=0$.
$c^3 \equiv 0 \pmod{61}$. Since 61 is prime, $c \equiv 0 \pmod{61}$.
Given the range $1 \le c \le 61$, the only solution is $c=61$.
Thus, $C(0) = 1$.

Case 2: $r \in \{1, 2, \ldots, 60\}$.
We consider the congruence $c^3 \equiv r \pmod{61}$ in the multiplicative group $\mathbb{Z}_{61}^*$, which has order $p-1=60$.
Let $d = \gcd(3, 60) = 3$.
For $r \in \mathbb{Z}_{61}^*$, the number of solutions $C(r)$ is either $d=3$ or $0$.
$C(r) = 3$ if $r$ is a cubic residue modulo 61, and $C(r) = 0$ otherwise.
The number of non-zero cubic residues is $\frac{p-1}{d} = \frac{60}{3} = 20$.
Therefore, $C(r)=3$ for 20 values of $r \in \{1, \ldots, 60\}$.
And $C(r)=0$ for the remaining $60 - 20 = 40$ values of $r \in \{1, \ldots, 60\}$.

Summary:
$C(0) = 1$.
$C(r) = 3$ for 20 specific values of $r \in \{1, \ldots, 60\}$.
$C(r) = 0$ for 40 specific values of $r \in \{1, \ldots, 60\}$.

### [W3, round 1]
Calculated D(r), the number of solutions d^3 = r (mod 61) for d in {1, ..., 61}.
The results are:
1. D(0) = 1 (the solution is d=61).
2. For r in {1, ..., 60}, D(r) is either 0 or 3.
3. There are exactly 20 values of r such that D(r) = 3 (the cubic residues modulo 61).
4. There are exactly 40 values of r such that D(r) = 0.

### [W1, round 1]
Calculated N(r) = #{(a, b) : 1<=a,b<=61, a^2 + b^2 \equiv r \pmod{61}}.
For p=61 (a prime such that p \equiv 1 \pmod 4), we found:
N(0) = 121
N(r) = 60 for r \in \{1, 2, ..., 60\}.

### [W4, round 1]
Calculated $M(s)$, the number of pairs $(c, d)$ such that $d^3 - c^3 \equiv s \pmod{61}$. Since the constraints $1\le c,d\le 61$ map bijectively to residues in $\{0, \ldots, 60\}$, we analyzed $d^3 - c^3 \equiv s \pmod{61}$.
The counts $n(z)$, the number of solutions to $x^3 \equiv z \pmod{61}$, were found to be $n(0)=1$ and $n(z)=3$ for the 20 non-zero cubic residues, and $n(z)=0$ otherwise.
$M(s)$ was calculated as $M(s) = \sum_{z_x=0}^{60} n(z_x) n(z_x + s)$.
The distribution of $M(s)$ is:
$M(0) = 181$.
$M(s) = 60$ for $s=1$ and $s=60$.
$M(s) = 59$ for $s \in \{2, 3, \ldots, 59\}$.
The sum $\sum M(s) = 181 + 2 \times 60 + 58 \times 59 = 181 + 120 + 3422 = 3721 = 61^2$, which confirms the calculations.
