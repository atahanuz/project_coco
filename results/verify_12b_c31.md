# Pooled verification of the 12B answers, checker run `verify_12b_c31` (129 of 129 contested problems checked)

On the 207 problems available so far (all unanimous + checked ones); checker trials per problem: {1: 129}

| method | pass@1 | vs swarm [95% CI] |
|---|---|---|
| maj@8 | 0.719 | |
| swarm | 0.744 | |
| vote, no checker: maj@8 + swarm ×2 | 0.760 | +1.6 [-3.5, +6.7] |
| vote, no checker: maj@8 + swarm ×4 | 0.778 | +3.4 [-0.5, +7.5] |
| **checker, pre-registered rule (w = 2)** | 0.824 | +8.0 [+2.9, +13.0] |
| checker, same rule, w = 1 | 0.821 | +7.7 [+2.9, +12.6] |
| checker, same rule, w = 4 | 0.836 | +9.2 [+4.3, +14.0] |
| **checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5) | 0.821 | +7.7 [+3.9, +12.1] |
| checker over the 8 single answers only (no swarm) | 0.783 | +3.9 [-1.9, +9.7] |
| checker, trials combined (score = #CONFIRMED - #REFUTED, then votes, w = 2) | 0.824 | +8.0 [+3.1, +13.0] |

Checker's contribution beyond the same vote, pre-registered rule, on 129 contested problems: 0.725 vs 0.623, **+10.2 [+3.9, +16.7]**

Checker's contribution beyond the same vote, soft rule, on 129 contested problems: 0.721 vs 0.651, **+7.0 [+2.7, +11.6]**

right candidates (107): CONFIRMED 89%, REFUTED 9%, UNCLEAR 2%

wrong candidates (340): CONFIRMED 11%, REFUTED 86%, UNCLEAR 4%
precision of CONFIRMED: 72%

checker tokens per checked problem: mean 12k, median 12k
