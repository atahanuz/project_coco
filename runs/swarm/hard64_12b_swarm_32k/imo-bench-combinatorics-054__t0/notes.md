### [W1, round 1]
REPORT on task "Use Python to compute small cases / brute-force search, record data and patterns in notes.md, and propose a candidate answer.": (no report: step or token limit reached)

### [W3, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": (no report: step or token limit reached)

### [W2, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": We analyzed the invariants of the system during collisions. The differences $D_x = n_x^+ - n_x^-$ and $D_y = n_y^+ - n_y^-$ remain invariant because a collision between two ants moving in opposite directions results in a $90^\circ$ clockwise turn for both, changing $n_x^+ \to n_x^+ - 1$, $n_x^- \to n_x^- - 1$, $n_y^+ \to n_y^+ + 1$, and $n_y^- \to n_y^- + 1$ (or similar for vertical collisions). By choosing a starting configuration such that $D_x = 0$ and $D_y = 0$, the center of mass of the ants remains stationary. Furthermore, by choosing initial positions such that $\sum (x_i \dot{x}_i + y_i \dot{y}_i) = 0$, the quantity $Q = \sum (x_i^2 + y_i^2)$ remains constant, implying the ants are confined to a bounded region. Thus, there are configurations where no ant ever falls off the checkerboard.
Candidate answer: does not necessarily exist

### [W4, round 1]
REPORT on task "Solve the problem with your own approach (different from the others), using notes.md data.": (no report: step or token limit reached)
