# Pooled verification of the MIX answers, checker run `verify_mix_c31` (134 of 134 contested problems checked)

On the 207 problems available so far (all unanimous + checked ones); checker trials per problem: {1: 2, 2: 132}

| method | pass@1 | vs swarm [95% CI] |
|---|---|---|
| maj@8 | 0.719 | |
| swarm | 0.744 | |
| vote, no checker: maj@8 + swarm ×2 | 0.783 | +3.9 [-1.9, +9.7] |
| vote, no checker: maj@8 + swarm ×4 | 0.790 | +4.6 [-0.7, +9.9] |
| **checker, pre-registered rule (w = 2)** | 0.831 | +8.7 [+3.9, +13.8] |
| checker, same rule, w = 1 | 0.831 | +8.7 [+3.9, +13.8] |
| checker, same rule, w = 4 | 0.831 | +8.7 [+3.9, +13.8] |
| **checker, frozen soft rule** (w = 4, CONFIRMED ×2, REFUTED ×0.5) | 0.838 | +9.4 [+4.8, +14.5] |
| checker over the 8 single answers only (no swarm) | 0.810 | +6.6 [+1.3, +12.1] |
| checker, trials combined (score = #CONFIRMED - #REFUTED, then votes, w = 2) | 0.841 | +9.7 [+4.3, +15.0] |

Checker's contribution beyond the same vote, pre-registered rule, on 134 contested problems: 0.746 vs 0.672, **+7.5 [+1.1, +14.2]**

Checker's contribution beyond the same vote, soft rule, on 134 contested problems: 0.757 vs 0.683, **+7.5 [+1.9, +13.1]**

right candidates (232): CONFIRMED 88%, REFUTED 11%, UNCLEAR 2%

wrong candidates (848): CONFIRMED 8%, REFUTED 87%, UNCLEAR 5%
precision of CONFIRMED: 74%

checker tokens per checked problem: mean 13k, median 12k
