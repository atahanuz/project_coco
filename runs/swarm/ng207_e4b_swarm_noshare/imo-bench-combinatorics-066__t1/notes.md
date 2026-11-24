### [W2, round 1]
REPORT on task "Determine the maximum size of a subset of diagonals that are pairwise non-intersecting (i.e., a set forming a fan or triangulation structure). This provides an upper bound based on one part of the 'go": The maximum size of a set of pairwise non-intersecting diagonals in an $n$-gon is given by $n-3$, as this corresponds to the number of diagonals required to fully triangulate the polygon. For a regular 109-gon, the maximum size is $109 - 3 = 106$.
Candidate answer: 106

### [W3, round 1]
REPORT on task "Attempt to establish a general upper bound for the size of a 'good' set by considering the density of perpendicular vs. intersecting diagonals. Look for a relationship between the maximum size and the": The task required establishing a general upper bound for the size of a 'good' set of diagonals. A good set requires that any intersecting pair of diagonals must be perpendicular. By analyzing the density constraint, if the set size $k$ grows faster than linearly with $N$, the number of required intersections vastly outweighs the constrained nature of perpendicularity. Therefore, the maximum size of the good set must be bounded linearly in the number of vertices $N$. This establishes the general upper bound as $O(N)$.
Candidate answer: O(N)

### [W4, round 1]
REPORT on task "Apply coordinate geometry or complex numbers to characterize the possible slopes (and thus perpendicularity) of diagonals in a regular 109-gon, specifically mapping the perpendicularity condition to v": I used complex numbers to model the vertices of the regular 109-gon. By analyzing the argument of the difference vector $Z_{i, j} = V_j - V_i$, I derived the angular orientation of the diagonal. The condition for two diagonals, $D_{i, j}$ and $D_{k, l}$, to be perpendicular is that their arguments differ by $\pi/2$ modulo $\pi$. This geometric condition translates directly to the index congruence: $2(k+l) - 2(i+j) \equiv N \pmod{2N}$. For $N=109$, this is $2(k+l) - 2(i+j) \equiv 109 \pmod{218}$.
Candidate answer: 2(k+l) - 2(i+j) \equiv 109 \pmod{218}

### [W1, round 1]
REPORT on task "Investigate the condition for perpendicularity of two diagonals in a general regular n-gon. Focus on understanding how the structure of the diagonals (defined by the length of the arcs they subtend) r": I investigated the condition for perpendicularity of two diagonals in a general regular $n$-gon. By relating the diagonals to the angular positions of their endpoints, I derived the condition that $j+i - (k+l) = n(m + 1/2)$. For $n=109$, which is odd, the right-hand side is never an integer, meaning no two diagonals in a regular 109-gon can be perpendicular. Therefore, a "good set" must consist of pairwise non-intersecting diagonals. The maximum size of such a set in an $n$-gon is $n-3$, yielding $109 - 3 = 106$.
Candidate answer: 106
