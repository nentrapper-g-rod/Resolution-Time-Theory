# Result note — N-08

**ID:** N-08  
**Artifact:** `simulations/08_bayesian_score_forced_likelihood.py` (revised)  
**Claim:** (1) Event locations with rate ∝ I have empirical density ∝ I (counting). (2) Mean Poisson score (k−λ)∇log I is consistent with zero — no net score-driven climb.  
**Status:** shown-numerically; prior independent “score derivation” of ∇log I drift is **withdrawn**

## How to regenerate
```bash
python simulations/08_bayesian_score_forced_likelihood.py
```
**Seed:** 42

## Printed output (regenerated 2026-07-30)
```
1. Recorded event locations (rate ∝ I):
   L1 distance to normalized I: 0.0523

2. Sample mean of Poisson score (k−λ)∇log I:
   Estimated mean score ≈ -0.0651  (should be ~0)
```

## Analytic target
∂_x log p(k|x) = (k−λ) ∇log I; E[score] = 0.  
See `derivations/poisson_score.py`.

## Notes
My first version hard-coded ∇log I (circular). I withdrew that claim. The revised script demonstrates mean-score-zero and the counting result of 1.2.
