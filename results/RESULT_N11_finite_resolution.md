# Result Provenance — N-11

**ID:** N-11  
**Artifact:** `simulations/11_finite_resolution_averaging.py`  
**Claim:** Finite-resolution (gate / averaging) sampling of a high-frequency intensity produces a recorded density that tracks the slow envelope more closely than instantaneous sampling.  
**Status:** shown-numerically (illustrative of under-sampling / measurement-record picture)

## How to regenerate
```bash
python simulations/11_finite_resolution_averaging.py
```
**Environment:** see requirements.txt  
**Seed:** 21

## Analytic / conceptual target
Under-sampling of a rapidly oscillating intensity by a finite gate (or equivalent spatial averaging proxy) yields a recorded event density that follows the slow envelope rather than the instantaneous field.

## Metric used and why
L¹ distance of the histogram to the normalized slow envelope.  
Comparison of instantaneous vs averaged sampling.

## Pass / Fail criterion
L¹(averaged → envelope) < L¹(instantaneous → envelope) and L¹(averaged → envelope) < 0.25 → PASS (illustrative).

## Notes / limitations
- The spatial convolution is a simple proxy for temporal gating of a moving interference pattern (δx ~ v · τ_c).
- This is an illustration of the under-sampling idea, not a derivation of the equilibrium postulate from a full microscopic model.
- Ontology: measurement-record side (consistent with Phase-1 conclusion).
