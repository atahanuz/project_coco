# Pooled verification of the 12B answers, checker run `verify_12b_c26` (129 of 129 contested problems checked)

On the 207 problems available so far (all unanimous + checked ones):

| method | pass@1 | vs swarm [95% CI] |
|---|---|---|
| maj@8 | 0.719 | |
| swarm | 0.744 | |
| vote, no checker: maj@8 + swarm ×2 | 0.760 | +1.6 [-3.5, +6.7] |
| vote, no checker: maj@8 + swarm ×4 | 0.778 | +3.4 [-0.5, +7.5] |
| **checker, pre-registered rule (w = 2)** | 0.812 | +6.8 [+1.9, +11.8] |
| checker, same rule, w = 1 | 0.812 | +6.8 [+1.9, +11.6] |
| checker, same rule, w = 4 | 0.814 | +7.0 [+2.7, +11.4] |
| **checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5) | 0.816 | +7.2 [+3.6, +11.1] |
| checker over the 8 single answers only (no swarm) | 0.766 | +2.2 [-3.6, +8.0] |

Checker's contribution beyond the same vote, pre-registered rule, on 129 contested problems: 0.705 vs 0.623, **+8.3 [+1.3, +15.5]**

Checker's contribution beyond the same vote, soft rule, on 129 contested problems: 0.713 vs 0.651, **+6.2 [+1.6, +11.2]**

right candidates (107): CONFIRMED 78%, REFUTED 12%, UNCLEAR 10%

wrong candidates (340): CONFIRMED 9%, REFUTED 77%, UNCLEAR 14%
precision of CONFIRMED: 73%

checker tokens per checked problem: mean 29k, median 22k
