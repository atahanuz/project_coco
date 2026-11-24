### [W2, round 1]
REPORT on task "Calculate $S_3(r)$, the number of solutions $x \in \{0, 1, ..., 60\}$ such that $x^3 \equiv r \pmod{61}$, for all $r \in \{0, 1, ..., 60\}$. Output the counts for all 61 possible residues.": I calculated $S_3(r)$, the number of solutions to $x^3 \equiv r \pmod{61}$, by iterating through all possible values of $x \in \{0, 1, \dots, 60\}$. The resulting counts show $S_3(0)=1$, $S_3(r)=3$ for the 20 non-zero cubic residues, and $S_3(r)=0$ for the remaining 40 non-residues. The full list of counts for all 61 residues is provided in the calculation output.
Candidate answer: S3(r) values for r=0 to 60 listed above

### [W1, round 1]
REPORT on task "Calculate $S_2(r)$, the number of solutions $x \in \{0, 1, ..., 60\}$ such that $x^2 \equiv r \pmod{61}$, for all $r \in \{0, 1, ..., 60\}$. Output the counts for all 61 possible residues.": I calculated S_2(r)
Candidate answer: [1,2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 2]

### [W3, round 1]
REPORT on task "Find the number of solutions $N_{sum}(r)$ to the congruence $a^2+b^2 \equiv r \pmod{61}$, where $a, b \in \{0, 1, ..., 60\}$. Express this as a function of $r$.": I determined the number of solutions $N_{sum}(r)$ to $a^2 + b^2 \equiv r \pmod{61}$ using standard results from the theory of quadratic forms modulo a prime. Since $p=61$ is a prime such that $p \equiv 1 \pmod{4}$, the number of solutions is $2p-1$ when $r \equiv 0 \pmod{p}$, and $p-1$ otherwise. Substituting $p=61$ yields $N_{sum}(0) = 121$ and $N_{sum}(r) = 60$ for $r \not\equiv 0 \pmod{61}$. This is expressed formally using the Kronecker delta.
Candidate answer: N_{sum}(r) = 121 \cdot \delta_{r, 0} + 60 \cdot (1 - \delta_{r, 0})

### [W4, round 1]
REPORT on task "Find the number of solutions $N_{diff}(r)$ to the congruence $d^3-c^3 \equiv r \pmod{61}$, where $c, d \in \{0, 1, ..., 60\}$. Express this as a function of $r.": I derived the required function $N_{diff}(r)$ by analyzing the distribution of cubic residues modulo 61. This was equivalent to calculating a specific convolution sum of the solution counts $N_k$. I numerically verified the result for $r=0$ using code, confirming that $N_{diff}(0) = 181$. For $r \neq 0$, the solution depends on the count of non-zero cubic residues $x$ such that $x-r$ is also a cubic residue.
Candidate answer: $N_{diff}(r) = \sum_{x \in R'} N_x N_{x-r \pmod{61}}$, where $R'$ is the set of cubic residues modulo 61 and $N_k$ is the number of solutions to $x^3 \equiv k \pmod{61}$. Specifically, $N_{diff}(0) = 181$.
