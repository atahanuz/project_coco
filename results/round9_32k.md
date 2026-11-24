# Round 9: 12B swarm, 32k vs 16k per-call limit (64 of 64 hard problems finished)

Paired on the problems the 32k run has finished. The 16k numbers are the main 12B swarm (ng207_12b_swarm) on the same problems.

16k swarm on all 64 hard problems: 0.438, 9 with no answer.

| | single 12B pass@1 | 12B maj@8 | swarm 16k | swarm 32k |
|---|---|---|---|---|
| solved | 0.113 | 0.105 | 0.438 | 0.406 |
| solved, closed forms evaluated | | | 0.438 | 0.422 |
| no answer | | | 9 | 0 |
| worker calls cut at the limit | | | 65.4% (4306/6585) | 46.0% (2134/4636) |
| completion tokens per problem | | | 480k | 542k |

32k − 16k: -3.1 points [-12.5, +6.2] (paired bootstrap, n=64). Wins 4, losses 6, ties 54.
With closed forms evaluated: -1.6 points [-10.9, +7.8].
Minutes per problem (32k): median 127, max 235; 42 resumed from a checkpoint.

| problem | gold | 16k answer | 32k answer |
|---|---|---|---|
| algebra-010 | $-\frac{2}{3},0,\frac{2}{3}$ | 0, 2/3, -2/3 ✓ | 0 ✗ |
| algebra-012 | $\frac{1}{2}$ | 1/2 ✓ | 1 ✗ |
| algebra-026 | 1 | 1 ✓ | 0 ✗ |
| algebra-066 | 997008, 995026, 995018 | 995018 ✗ | 995018, 995026, 997008 ✓ |
| combinatorics-023 | 127009 | 125060 ✗ | 127009 ✓ |
| combinatorics-026 | 847288609444 | 847288609444 ✓ | 3^{25} + 1 ✗ |
| combinatorics-028 | 1198 | no answer ✗ | 1198 ✓ |
| combinatorics-033 | 498 | 498 ✓ | 500 ✗ |
| combinatorics-035 | 2027091 | no answer ✗ | 2027091 ✓ |
| combinatorics-079 | 81729648000 | 81729648000 ✓ | 12870 ✗ |
