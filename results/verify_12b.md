# Pooled verification of the 12B answers, checker run `verify_12b` (129 of 129 contested problems checked)

On the 207 problems available so far (all unanimous + checked ones); checker trials per problem: {1: 129}

| method | pass@1 | vs swarm [95% CI] |
|---|---|---|
| maj@8 | 0.719 | |
| swarm | 0.744 | |
| vote, no checker: maj@8 + swarm ×2 | 0.760 | +1.6 [-3.5, +6.7] |
| vote, no checker: maj@8 + swarm ×4 | 0.778 | +3.4 [-0.5, +7.5] |
| **checker, pre-registered rule (w = 2)** | 0.758 | +1.4 [-3.9, +6.8] |
| checker, same rule, w = 1 | 0.751 | +0.7 [-4.6, +6.0] |
| checker, same rule, w = 4 | 0.773 | +2.9 [-1.9, +7.7] |
| **checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5) | 0.800 | +5.6 [+1.4, +9.9] |
| checker over the 8 single answers only (no swarm) | 0.713 | -3.1 [-9.1, +2.9] |
| checker, trials combined (score = #CONFIRMED - #REFUTED, then votes, w = 2) | 0.758 | +1.4 [-3.6, +6.8] |

Checker's contribution beyond the same vote, pre-registered rule, on 94 contested problems (held out: not used to choose the soft rule): 0.601 vs 0.574, **+2.7 [-5.9, +11.2]**

Checker's contribution beyond the same vote, soft rule, on 94 contested problems (held out: not used to choose the soft rule): 0.665 vs 0.628, **+3.7 [-1.6, +9.6]**

right candidates (107): CONFIRMED 69%, REFUTED 22%, UNCLEAR 8%

wrong candidates (340): CONFIRMED 11%, REFUTED 75%, UNCLEAR 13%
precision of CONFIRMED: 65%

checker tokens per checked problem: mean 46k, median 44k
