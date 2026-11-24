# Adaptive swarm: call the swarm only when single answers disagree (offline, existing runs)

Rule (m, t): draw m single answers; if at least t agree, submit their answer, otherwise run the swarm. The rule uses only the single answers' agreement, never the gold answer. Expected values over every m-subset of the ≈8 stored single answers and over the swarm's trials. Paired 95% CIs by bootstrap over problems.

## 12B (207 problems)

| method | pass@1 | vs swarm | swarm called | tokens / problem |
|---|---|---|---|---|
| single answer | 0.626 | | | 26k |
| maj@8 | 0.719 | | | 206k |
| swarm | 0.744 | | 100% | 340k |
| adaptive m=2, t=2 | **0.748** | +0.4 [-2.3, +3.2] | 38% | 229k |
| adaptive m=3, t=2 | **0.737** | -0.7 [-4.8, +3.6] | 18% | 167k |
| adaptive m=3, t=3 | **0.754** | +1.0 [-1.2, +3.2] | 48% | 300k |
| adaptive m=4, t=3 | **0.755** | +1.1 [-2.3, +4.5] | 32% | 260k |
| adaptive m=4, t=4 | **0.753** | +0.9 [-0.8, +2.8] | 53% | 348k |
| adaptive m=5, t=4 | **0.755** | +1.1 [-1.9, +4.2] | 39% | 323k |
| adaptive m=6, t=5 | **0.753** | +0.9 [-1.8, +3.6] | 44% | 372k |
| maj@8 + swarm answer ×1 | 0.740 | -0.4 [-5.9, +5.2] | 100% | 546k |
| maj@8 + swarm answer ×2 | 0.760 | +1.6 [-3.5, +6.8] | 100% | 546k |
| maj@8 + swarm answer ×3 | 0.771 | +2.7 [-1.7, +7.2] | 100% | 546k |
| maj@8 + swarm answer ×4 | 0.778 | +3.4 [-0.5, +7.5] | 100% | 546k |

Upper bound, any of the single answers or the swarm right: 0.889.

By single-answer difficulty, adaptive m=5, t=4 (buckets from the same samples, so the hard buckets favour the swarm through regression to the mean):

| bucket | problems | single | maj@8 | swarm | adaptive |
|---|---|---|---|---|---|
| 0 right | 34 | 0.000 | 0.000 | 0.324 | 0.225 |
| ≤ 3/8 | 30 | 0.240 | 0.225 | 0.567 | 0.495 |
| 3/8 – 6/8 | 47 | 0.613 | 0.979 | 0.723 | 0.805 |
| > 6/8 | 96 | 0.975 | 1.000 | 0.958 | 1.000 |

## E4B (207 problems)

| method | pass@1 | vs swarm | swarm called | tokens / problem |
|---|---|---|---|---|
| single answer | 0.308 | | | 5k |
| maj@8 | 0.368 | | | 43k |
| swarm | 0.425 | | 100% | 33k |
| adaptive m=2, t=2 | **0.408** | -1.7 [-4.1, +0.5] | 55% | 30k |
| adaptive m=3, t=2 | **0.387** | -3.8 [-7.3, -0.4] | 28% | 26k |
| adaptive m=3, t=3 | **0.419** | -0.6 [-2.5, +1.1] | 69% | 40k |
| adaptive m=4, t=3 | **0.412** | -1.4 [-4.2, +1.4] | 48% | 39k |
| adaptive m=4, t=4 | **0.421** | -0.4 [-2.1, +1.1] | 75% | 47k |
| adaptive m=5, t=4 | **0.417** | -0.8 [-3.4, +1.7] | 58% | 47k |
| adaptive m=6, t=5 | **0.418** | -0.7 [-3.1, +1.4] | 64% | 55k |
| maj@8 + swarm answer ×1 | 0.384 | -4.1 [-8.8, +0.4] | 100% | 76k |
| maj@8 + swarm answer ×2 | 0.395 | -3.1 [-7.4, +1.3] | 100% | 76k |
| maj@8 + swarm answer ×3 | 0.407 | -1.8 [-5.7, +2.0] | 100% | 76k |
| maj@8 + swarm answer ×4 | 0.421 | -0.4 [-3.5, +2.8] | 100% | 76k |

Upper bound, any of the single answers or the swarm right: 0.614.

By single-answer difficulty, adaptive m=4, t=4 (buckets from the same samples, so the hard buckets favour the swarm through regression to the mean):

| bucket | problems | single | maj@8 | swarm | adaptive |
|---|---|---|---|---|---|
| 0 right | 100 | 0.000 | 0.000 | 0.130 | 0.099 |
| ≤ 3/8 | 41 | 0.238 | 0.272 | 0.476 | 0.455 |
| 3/8 – 6/8 | 28 | 0.638 | 0.964 | 0.732 | 0.763 |
| > 6/8 | 38 | 0.951 | 1.000 | 0.921 | 0.980 |

