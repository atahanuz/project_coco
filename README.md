# COCO: a swarm of small models on olympiad math

A team of small gemma-4 models (a master and four workers sharing a notes file and a Python tool) solves IMO-AnswerBench problems (207 auto-gradable, non-geometry). The project compares the swarm with single models and majority voting, then studies rewards and defection, planted saboteurs, reputation and expulsion, checker agents, and pooled verification.

- **[FINDINGS.md](FINDINGS.md)**: the lab notebook, with every experiment, its design, results and caveats.
- **[coco_atahanuz_proposal.md](coco_atahanuz_proposal.md)**: the original project proposal.

## Layout

| Path | Contents |
|---|---|
| `swarm/` | the swarm (`swarm.py`) and the blind answer checker (`verify.py`) |
| `calib/` | single-model baselines |
| `coco/` | answer grading |
| `analysis/` | analysis and figure scripts |
| `data/` | problem sets, pools and verification inputs |
| `results/` | summary tables, figures and the problem explorer |
| `runs/` | raw outputs: per-problem notes, traces and `results.jsonl` per run |

The models ran under vLLM on the MareNostrum 5 GPU cluster. The Slurm job scripts and job logs are not part of this repository.
