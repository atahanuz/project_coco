## Reward systems (proposal §6-7)

Reports are private to the master in all three runs; notes.md is voluntary.

| reward rule | problems | pass@1 | Δ vs public-report swarm [95% CI] | tokens / attempt | tasks shared | candidates withheld | accusations / 100 tasks | false alarms / 100 tasks | notes chars / task |
|---|---|---|---|---|---|---|---|---|---|
| team | 207 | **0.430** | +0.005 [-0.046, +0.056] | 30,370 | 85.7% | 65.8% | 1.2 | 0.2 | 988 |
| credit | 207 | **0.411** | -0.014 [-0.068, +0.036] | 31,031 | 89.2% | 64.4% | 2.5 | 0.3 | 992 |
| wta | 207 | **0.391** | -0.034 [-0.082, +0.012] | 29,316 | 87.1% | 63.7% | 2.0 | 0.3 | 980 |

**Credit named by the master:** team: W1 50, W2 46, W3 52, W4 59. credit: W1 40, W2 60, W3 54, W4 52, none 1. wta: W1 47, W2 50, W3 53, W4 57. 

## Planted saboteur W4 (proposal §8): does the reputation loop protect the team?

| condition | problems | pass@1 | Δ vs no saboteur [95% CI] | final = saboteur's answer | W4 track record at the end | W4 expelled after problem # |
|---|---|---|---|---|---|---|
| no saboteur (`ng207_e4b_swarm`) | 207 | **0.425** | — | — | — | — |
| no defense | 207 | **0.343** | -0.082 [-0.135, -0.029] | 30.9% | — | — |
| track record shown | 207 | **0.401** | -0.024 [-0.077, +0.029] | 30.0% | 24 of 192 correct | — |
| track record + expulsion | 207 | **0.411** | -0.014 [-0.070, +0.041] | 11.6% | 8 of 65 correct | 58 |
