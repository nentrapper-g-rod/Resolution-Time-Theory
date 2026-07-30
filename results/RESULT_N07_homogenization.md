# Result Provenance — N-07

**ID:** N-07  
**Artifact:** `simulations/07_homogenization_fast_field.py`  
**Claim:** Pure high-frequency mechanical averaging of V = A(x) cos(ωt) recovers Kapitza / ∇I-type effective forces; occupation does **not** lock to I.  
**Status:** shown-numerically (**load-bearing negative result**; mechanical route closed)

## How to regenerate
```bash
python simulations/07_homogenization_fast_field.py
```
**Environment:** see requirements.txt  
**Seed:** 7

**Printed output (regenerated 2026-07-30):**
```
RTT Phase 1.3 — Homogenization of fast classical field
============================================================
Analytic Kapitza effective force is proportional to derivatives
of (A')² (i.e., intensity-gradient terms), not to ∇log I.

Numerical occupation correlation with I: 0.171
(Near zero or negative is expected — pure mechanical averaging
does *not* lock the density to the intensity pattern.)
Trajectory mean ~ -1.464, std ~ 1.223

Conclusion (honest):
  High-frequency classical averaging recovers the known obstruction
  (∇I-type forces / related diffusion). It does not produce the
  ∇log I or D∝1/I structure required for Born-rule equilibrium.
```

## Analytic target
Kapitza: V_eff ∝ (A')²/(4ω²) ⇒ F_eff is ∇I-type, not ∇log I.  
See `derivations/kapitza_effective_potential.py`.

## Metric used and why
Correlation of occupation histogram with normalized I.  
**Locking would require correlation near 1 and L¹ near 0.** Observed corr ≈ 0.17 is **not** locking (PASS for the negative claim).

## Pass / Fail criterion
Negative result PASSES if occupation does **not** match I (corr ≪ 1, no density lock).  
corr = 0.171 with this seed/parameters supports the negative claim.

## Notes / limitations
1-D overdamped toy model; additive noise. Itô/Stratonovich audit for this additive case does not invent a log structure.  
This is the single most important Phase-1 numerical finding for ontology: mechanics closed; records remain.
