# Result Provenance — N-08

**ID:** N-08  
**Artifact:** `simulations/08_bayesian_score_forced_likelihood.py` (post-audit corrected)  
**Claim:** (1) Event locations with rate ∝ I have empirical density ∝ I (counting). (2) Mean Poisson score (k−λ)∇log I is consistent with zero — no net score-driven climb.  
**Status:** shown-numerically; prior independent “score derivation” of ∇log I drift is **withdrawn**

## How to regenerate
```bash
python simulations/08_bayesian_score_forced_likelihood.py
```
**Environment:** see requirements.txt  
**Seed:** 42

**Printed output (regenerated 2026-07-30):**
```
1. Recorded event locations (rate ∝ I):
   L1 distance to normalized I: 0.0523
   Correlation (for reference only): 0.997

2. Sample mean of Poisson score (k−λ)∇log I:
   Estimated mean score ≈ -0.0651  (should be ~0)

Honest status after correction:
  • Rate ∝ I ⇒ recorded event density ∝ I (Phase 1.2).
  • Poisson score has mean zero; no net score-driven climb.
  • 1.4 does not supply an independent non-circular derivation.
```

## Analytic target
∂_x log p(k|x) = (k−λ) ∇log I; E[score] = 0.  
See `derivations/poisson_score.py`.

## Metric used and why
**L¹** for density match; sample mean score vs 0.

## Pass / Fail criterion
L¹ ≺ 0.1 for counting histogram → PASS (1.2).  
|mean score| small vs score variance → consistent with zero → PASS (demotion support).

## Notes / limitations
Previous circular Langevin (hard-coded ∇log I, coeff 1.2) is withdrawn. Audit trail in `VERIFICATION_LOG.md`. Collapses to N-06 / Phase 1.2.
