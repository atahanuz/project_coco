### [W4, round 1]
The expression $E$ simplifies to $E = \sqrt{\frac{1001}{a}} + \sqrt{\frac{1001}{b}} + \sqrt{\frac{1001}{c}}$. For $E$ to be a positive integer $K$, we require:
$$\sqrt{\frac{1001}{a}} + \sqrt{\frac{1001}{b}} + \sqrt{\frac{1001}{c}} = K$$

This condition is equivalent to the required condition: $\frac{1}{\sqrt{a}} + \frac{1}{\sqrt{b}} + \frac{1}{\sqrt{c}} = \frac{K}{\sqrt{1001}}$, where $K$ is an integer.

Based on the properties of linear independence of square roots, for a sum of radicals like this to equal a rational number ($K$), the arguments $1001/a, 1001/b, 1001/c$ must be highly constrained relative to 1001. A strong necessary condition derived from this setup is that the resulting terms must either be perfect squares, or $a, b, c$ must be structured such that the cross-terms generated when squaring the sum vanish or combine into a rational number.

A simplest necessary condition is that $a, b, c$ are divisors of 1001 such that $1001/a, 1001/b, 1001/c$ are all perfect squares. Since 1001 is square-free ($7 \cdot 11 \cdot 13$), this implies $a=b=c=1001$.

### [W2, round 1]
ANALYSIS OF K:
The expression simplifies to $K = \sqrt{1001} \left( \frac{1}{\sqrt{a}} + \frac{1}{\sqrt{b}} + \frac{1}{\sqrt{c}} \right)$.
For $K$ to be an integer, the sum $S = 1/\sqrt{a} + 1/\sqrt{b} + 1/\sqrt{c}$ must be of the form $R\sqrt{1001}$, where $R$ is a rational number.

Let $a = a_0^2 m_a$, $b = b_0^2 m_b$, $c = c_0^2 m_c$, where $m_a, m_b, m_c$ are square-free.
We require the sum of the rationalized terms $\sum \frac{\sqrt{m_i}}{a_0 m_i}$ to be proportional to $\sqrt{1001}$.

The simplest case that guarantees this proportionality is when $m_a = m_b = m_c = 1001$.
In this case, $a = 1001 a_0^2$, $b = 1001 b_0^2$, and $c = 1001 c_0^2$.
Substituting this into $K$:
$K = \sqrt{1001} \left( \frac{\sqrt{1001}}{1001 a_0} + \frac{\sqrt{1001}}{1001 b_0} + \frac{\sqrt{1001}}{1001 c_0} \right)$
$K = \frac{1001}{1001} \left( \frac{1}{a_0} + \frac{1}{b_0} + \frac{1}{c_0} \right) = \frac{1}{a_0} + \frac{1}{b_0} + \frac{1}{c_0}$.

Necessary Condition: $a, b, c$ must be of the form $1001 k^2$ for some positive integers $k$. This leads to the requirement that $\frac{1}{a_0} + \frac{1}{b_0} + \frac{1}{c_0}$ must be a positive integer $N$.

### [W1, round 1]
Initial search for solutions (a, b, c) where $1 \le a, b, c \le 10$ yielded zero solutions.
The expression simplifies to $E = \sqrt{\frac{1001}{a}} + \sqrt{\frac{1001}{b}} + \sqrt{\frac{1001}{c}}$.
For $E$ to be an integer, given that $1001$ is square-free ($7 \times 11 \times 13$), all three terms must combine such that the irrational component $\sqrt{1001}$ (if present) cancels out, or all terms must be rational.
A simple solution exists if $a=b=c=1001$, resulting in $E = 1+1+1=3$. This suggests that solutions might involve $a, b, c$ being divisors of 1001, potentially 1001 itself.

### [W3, round 1]
The problem asks for the number of triples $(a, b, c)$ such that $K = \sqrt{\frac{1001}{a}} + \sqrt{\frac{1001}{b}} + \sqrt{\frac{1001}{c}}$ is a positive integer. Let $N=1001 = 7 \cdot 11 \cdot 13$. Since $N$ is square-free, we analyze the structure required for the sum to be an integer. For $K$ to be an integer, the terms must simplify. This generally requires $\frac{N}{a}, \frac{N}{b}, \frac{N}{c}$ to share the same square-free part, say $D$.
This leads to the form $\frac{N}{a} = D k_a^2$, where $D$ is a square-free divisor of $N$. Since $N/D$ is also square-free, $k_a$ must be 1 for $a$ to be an integer.
Thus, $a = N/D$. Similarly, $b=N/D$ and $c=N/D$.
The sum simplifies to $K = \sqrt{D} (1+1+1) = 3\sqrt{D}$.
For $K$ to be an integer, $D$ must be a perfect square. Since $D$ is square-free, we must have $D=1$.
If $D=1$, then $a=b=c=N/1 = 1001$.
This provides exactly one solution: $(1001, 1001, 1001)$.
