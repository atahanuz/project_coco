# Spot-check audits: how much ground truth does reputation need? (offline replay)

Fidelity check: peer-agreement signal replayed on the colluding no-defense runs (live peer runs expelled W1 and W2 after 28–29 and 30–31):

- two colluding, seed 0: replay expels W1 (19), W2 (20)
- two colluding, seed 1: replay expels W1 (25), W2 (75)

Pooled over both problem orders (2 runs per row; 9 runs without a saboteur for false expulsions):

| audited | two colluders: all expelled | median problem | one saboteur: expelled | median problem | honest worker expelled (saboteur runs) | honest worker expelled (no-saboteur runs) |
|---|---|---|---|---|---|---|
| 10% | 0% | 186 | 7% | 175 | 0% | 0.0% |
| 20% | 6% | 174 | 45% | 150 | 0% | 0.2% |
| 30% | 25% | 168 | 76% | 107 | 1% | 0.7% |
| 40% | 38% | 157 | 93% | 90 | 3% | 0.8% |
| 50% | 54% | 122 | 99% | 78 | 5% | 0.8% |
| 60% | 66% | 116 | 100% | 46 | 5% | 0.6% |
| 75% | 78% | 95 | 100% | 39 | 7% | 0.5% |
| 90% | 93% | 85 | 100% | 35 | 4% | 0.1% |
| 100% | 100% | 80 | 100% | 55 | 0% | 0.0% |
