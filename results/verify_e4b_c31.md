# Pooled verification of the E4B answers, checker run `verify_e4b_c31` (188 of 188 contested problems checked)

On the 207 problems available so far (all unanimous + checked ones):

| method | pass@1 | vs swarm [95% CI] |
|---|---|---|
| maj@8 | 0.368 | |
| swarm | 0.425 | |
| vote, no checker: maj@8 + swarm ×2 | 0.425 | +0.0 [-4.1, +3.9] |
| vote, no checker: maj@8 + swarm ×4 | 0.453 | +2.8 [-0.2, +5.8] |
| **checker, pre-registered rule (w = 2)** | 0.594 | +16.9 [+12.8, +21.0] |
| checker, same rule, w = 1 | 0.594 | +16.9 [+12.8, +21.0] |
| checker, same rule, w = 4 | 0.592 | +16.7 [+12.8, +20.8] |
| **checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5) | 0.570 | +14.5 [+11.1, +18.4] |
| checker over the 8 single answers only (no swarm) | 0.498 | +7.2 [+2.2, +12.3] |

Checker's contribution beyond the same vote, pre-registered rule, on 188 contested problems: 0.564 vs 0.378, **+18.6 [+13.3, +24.2]**

Checker's contribution beyond the same vote, soft rule, on 188 contested problems: 0.537 vs 0.409, **+12.9 [+8.5, +17.6]**

right candidates (116): CONFIRMED 95%, REFUTED 4%, UNCLEAR 1%

wrong candidates (696): CONFIRMED 8%, REFUTED 89%, UNCLEAR 4%
precision of CONFIRMED: 67%

checker tokens per checked problem: mean 13k, median 12k
