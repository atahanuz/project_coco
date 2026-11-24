## ng207_12b_swarm vs ng207_12b_solo vs gemma-4-12B-it_think

154 problems with all three results (baseline 207, solo 154, swarm 207).

Mean completion tokens per attempt: single 26,827 (maj@8: 214,614), solo 47,932, swarm 360,328.
Swarm: the right answer appeared among the worker candidates in 0.760 of attempts.

### Overall

|  | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| all | 154 | 0.589 | 0.682 | 0.545 | **0.727** | +0.138 |

### By single-model difficulty (correct out of 8 baseline samples)

| difficulty | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| 0/8 (unsolved) | 28 | 0.000 | 0.000 | 0.250 | **0.357** | +0.357 |
| 1-2/8 (hard) | 16 | 0.169 | 0.125 | 0.188 | **0.375** | +0.206 |
| 3-5/8 (medium) | 32 | 0.487 | 0.781 | 0.469 | **0.750** | +0.263 |
| 6-8/8 (easy) | 78 | 0.929 | 1.000 | 0.756 | **0.923** | -0.006 |

### By category

| category | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| Algebra | 54 | 0.709 | 0.815 | 0.574 | **0.833** | +0.124 |
| Combinatorics | 87 | 0.491 | 0.586 | 0.471 | **0.632** | +0.141 |
| Number theory | 13 | 0.750 | 0.769 | 0.923 | **0.923** | +0.173 |

### By cooperation tag

| tag | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| C compute | 14 | 0.742 | 0.857 | 0.857 | **1.000** | +0.258 |
| E explore | 33 | 0.698 | 0.727 | 0.697 | **0.939** | +0.241 |
| N numeric | 18 | 0.833 | 0.944 | 0.722 | **1.000** | +0.167 |
| R reasoning | 89 | 0.476 | 0.584 | 0.404 | **0.551** | +0.075 |

### Held-out difficulty: buckets from baseline samples 0-3, single pass@1 from samples 4-7 (maj@8 column still uses all 8, so ignore it here)

| ho_bucket | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| 0/4 of samples 0-3 | 29 | 0.086 | 0.034 | 0.310 | **0.483** | +0.397 |
| 1/4 of samples 0-3 | 14 | 0.446 | 0.429 | 0.214 | **0.571** | +0.125 |
| 2-3/4 of samples 0-3 | 38 | 0.664 | 0.974 | 0.553 | **0.684** | +0.020 |
| 4/4 of samples 0-3 | 43 | 0.977 | 1.000 | 0.791 | **0.977** | +0.000 |

### Headroom subset: problems the single model solves in at most 5 of 8 samples (76)

|  | problems | single pass@1 | single maj@8 | solo+python pass@1 | swarm pass@1 | swarm − single |
|---|---|---|---|---|---|---|
| all | 76 | 0.241 | 0.355 | 0.329 | **0.526** | +0.286 |
