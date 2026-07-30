# Result Provenance — N-06

**ID:** N-06  
**Artifact:** `simulations/06_rate_and_counting_models.py`  
**Claim:** If detection rate (or CTMC rates into a cell) scales with I, the recorded / stationary density tracks I by construction (LLN / detailed balance).  
**Status:** shown-numerically / by construction (**solid Phase-1.2 content**)

## How to regenerate
```bash
python simulations/06_rate_and_counting_models.py
```
**Environment:** see requirements.txt  
**Seed:** 42 (Poisson demo)

**Printed output (regenerated 2026-07-30):**
```
=== Poisson counting process (detection rate ∝ I) ===
Correlation: 0.9988
L1 distance: 0.0368

=== Lattice CTMC with target-proportional rates ===
Correlation: 1.000000
L1 distance: 3.85e-13

Both constructions produce ρ ∝ I by design once intensity enters the rates/detection measure.
```

## Analytic target
Inhomogeneous Poisson with intensity measure ∝ I ⇒ empirical event density ∝ I (LLN).  
CTMC with rates into j ∝ I[j] ⇒ stationary mass ∝ I (null-space / detailed balance).

## Metric used and why
**L¹** primary; correlation secondary.

## Pass / Fail criterion
Poisson L¹ ≺ 0.05 at 5×10⁴ events → PASS.  
Lattice L¹ ~ machine epsilon → PASS (exact structure).

## Notes / limitations
**By construction** once rate ∝ I is granted. Does not derive intensity→rate from high-frequency particle mechanics. This is the load-bearing record-side statement of Phase 1.
