# Result note — N-07

**ID:** N-07  
**Artifact:** `simulations/07_homogenization_fast_field.py`  
**Claim:** Pure high-frequency mechanical averaging of V = A(x) cos(ωt) recovers Kapitza / ∇I-type effective forces; occupation does **not** lock to I.  
**Status:** shown-numerically (**load-bearing negative result**; mechanical route closed)

## How to regenerate
```bash
python simulations/07_homogenization_fast_field.py
```
**Seed:** 7

## Printed output (regenerated 2026-07-30)
```
Numerical occupation correlation with I: 0.171
(Near zero or negative is expected — pure mechanical averaging
does *not* lock the density to the intensity pattern.)
```

## Analytic target
Kapitza: V_eff ∝ (A')²/(4ω²) ⇒ F_eff is ∇I-type, not ∇log I.  
See `derivations/kapitza_effective_potential.py`.

## Metric
Correlation of occupation histogram with normalized I.  
**Locking would require correlation near 1.** Observed corr ≈ 0.17 is **not** locking (supports the negative claim).

## Notes
1-D overdamped toy model; additive noise. Itô/Stratonovich check for this additive case does not invent a log structure.  
This is the single most important Phase-1 numerical finding for ontology: mechanics closed; records remain.
