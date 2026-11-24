## ng207_e4b_swarm vs ng207_e4b_solo vs gemma-4-E4B-it_think

207 problems with all three results (baseline 207, solo 207, swarm 207).

Mean completion tokens per attempt: single 5,413 (maj@8: 43,308), solo 5,664, swarm 32,533.
Swarm: the right answer appeared among the worker candidates in 0.449 of attempts.

### Overall

|  | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| all | 207 | 0.308 | 0.372 | 0.258 | **0.454** | +0.146 |

### By single-model difficulty (correct out of 8 baseline samples)

| difficulty | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| 0/8 (unsolved) | 100 | 0.000 | 0.000 | 0.045 | **0.140** | +0.140 |
| 1-2/8 (hard) | 29 | 0.181 | 0.103 | 0.241 | **0.483** | +0.302 |
| 3-5/8 (medium) | 29 | 0.487 | 0.862 | 0.379 | **0.759** | +0.272 |
| 6-8/8 (easy) | 49 | 0.906 | 1.000 | 0.633 | **0.898** | -0.008 |

### By category

| category | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| Algebra | 54 | 0.336 | 0.407 | 0.287 | **0.519** | +0.183 |
| Combinatorics | 91 | 0.174 | 0.231 | 0.104 | **0.286** | +0.111 |
| Number theory | 62 | 0.480 | 0.548 | 0.460 | **0.645** | +0.165 |

### By cooperation tag

| tag | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| C compute | 28 | 0.353 | 0.429 | 0.375 | **0.571** | +0.219 |
| E explore | 58 | 0.487 | 0.569 | 0.422 | **0.638** | +0.151 |
| N numeric | 18 | 0.361 | 0.500 | 0.306 | **0.778** | +0.417 |
| R reasoning | 103 | 0.186 | 0.223 | 0.126 | **0.262** | +0.076 |

### Held-out difficulty: buckets from baseline samples 0-3, single pass@1 from samples 4-7 (maj@8 column still uses all 8, so ignore it here)

| ho_bucket | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| 0/4 of samples 0-3 | 111 | 0.038 | 0.018 | 0.063 | **0.189** | +0.151 |
| 1/4 of samples 0-3 | 29 | 0.328 | 0.414 | 0.224 | **0.517** | +0.190 |
| 2-3/4 of samples 0-3 | 32 | 0.633 | 0.875 | 0.531 | **0.781** | +0.148 |
| 4/4 of samples 0-3 | 35 | 0.879 | 1.000 | 0.657 | **0.943** | +0.064 |

### Headroom subset: problems the single model solves in at most 5 of 8 samples (158)

|  | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| all | 158 | 0.123 | 0.177 | 0.142 | **0.316** | +0.194 |
