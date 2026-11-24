## Swarm ablations on 207 problems completed by every run (reference: `ng207_e4b_swarm`)

| run | pass@1 | Δ vs reference [95% CI] | tokens / attempt | trials per problem |
|---|---|---|---|---|
| ng207_e4b_swarm | **0.425** | — | 33,039 | 2.0 |
| ng207_e4b_swarm_noshare | **0.384** | -0.041 [-0.082, +0.000] | 39,322 | 2.0 |
| ng207_e4b_swarm_r1 | **0.350** | -0.075 [-0.116, -0.036] | 18,829 | 2.0 |
| ng207_e4b_swarm_w2 | **0.411** | -0.014 [-0.060, +0.031] | 22,047 | 1.0 |
| ng207_e4b_swarm_w8 | **0.444** | +0.019 [-0.031, +0.070] | 42,916 | 1.0 |
| ng207_e4b_solo | **0.258** | -0.167 [-0.220, -0.116] | 5,664 | 2.0 |
| single model (no tools) | **0.308** | -0.117 [-0.159, -0.075] | 5,413 | 8.0 |
| single model maj@8 | **0.372** | -0.053 [-0.106, -0.002] | 43,308 | 8.0 |

### pass@1 by cooperation tag

| run | C compute (n=28) | E explore (n=58) | N numeric (n=18) | R reasoning (n=103) |
|---|---|---|---|---|
| ng207_e4b_swarm | 0.536 | 0.629 | 0.667 | 0.238 |
| ng207_e4b_swarm_noshare | 0.571 | 0.526 | 0.556 | 0.223 |
| ng207_e4b_swarm_r1 | 0.429 | 0.517 | 0.389 | 0.228 |
| ng207_e4b_swarm_w2 | 0.536 | 0.603 | 0.778 | 0.204 |
| ng207_e4b_swarm_w8 | 0.643 | 0.621 | 0.556 | 0.272 |
| ng207_e4b_solo | 0.375 | 0.422 | 0.306 | 0.126 |
| single model (no tools) | 0.353 | 0.487 | 0.361 | 0.186 |
| single model maj@8 | 0.429 | 0.569 | 0.500 | 0.223 |
