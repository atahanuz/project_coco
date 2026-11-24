# Pooled verification of the MIX answers, checker run `verify_mix_c26` (132 of 134 contested problems checked)

On the 205 problems available so far (all unanimous + checked ones); checker trials per problem: {1: 98, 2: 34}

| method | pass@1 | vs swarm [95% CI] |
|---|---|---|
| maj@8 | 0.721 | |
| swarm | 0.751 | |
| vote, no checker: maj@8 + swarm ×2 | 0.785 | +3.4 [-2.2, +9.3] |
| vote, no checker: maj@8 + swarm ×4 | 0.793 | +4.1 [-1.2, +9.5] |
| **checker, pre-registered rule (w = 2)** | 0.817 | +6.6 [+1.7, +11.7] |
| checker, same rule, w = 1 | 0.817 | +6.6 [+1.5, +11.7] |
| checker, same rule, w = 4 | 0.817 | +6.6 [+1.5, +11.5] |
| **checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5) | 0.837 | +8.5 [+3.9, +13.2] |
| checker over the 8 single answers only (no swarm) | 0.800 | +4.9 [-0.5, +10.5] |
| checker, trials combined (score = #CONFIRMED - #REFUTED, then votes, w = 2) | 0.820 | +6.8 [+2.0, +11.7] |

Checker's contribution beyond the same vote, pre-registered rule, on 132 contested problems: 0.723 vs 0.674, **+4.9 [-2.3, +11.7]**

Checker's contribution beyond the same vote, soft rule, on 132 contested problems: 0.754 vs 0.686, **+6.8 [+1.9, +12.1]**

right candidates (149): CONFIRMED 80%, REFUTED 14%, UNCLEAR 6%

wrong candidates (493): CONFIRMED 8%, REFUTED 83%, UNCLEAR 9%
precision of CONFIRMED: 76%

checker tokens per checked problem: mean 29k, median 23k
