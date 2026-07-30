# Result Provenance — N-05

**ID:** N-05  
**Artifact:** `simulations/05_state_dependent_diffusion_equilibrium.py`  
**Claim:** Zero-drift Itô diffusion with D(x) ∝ 1/I(x) yields a Monte-Carlo density that tracks normalized I (consistency with the exact FP stationary solution ρ∞ ∝ 1/D).  
**Status:** shown-numerically (consistency / reachability only; not a derivation of D ∝ 1/I from mechanics)

## How to regenerate
```bash
python simulations/05_state_dependent_diffusion_equilibrium.py
```
**Environment:** see requirements.txt (numpy; matplotlib optional)  
**Seed:** 42  
**Note:** On NumPy ≥2, replace deprecated `np.trapz` with `np.trapezoid` if the script errors.

**Printed output (regenerated 2026-07-30, after trapz fix):**
```
RTT 05 — D ∝ 1/I equilibrium demonstration
==================================================
Correlation (histogram vs normalized I): 0.8512
Particles: 800, steps: 30000
Done. Exact stationary result follows from Fokker–Planck;
numerics are a consistency check only.
```

## Analytic target
Fokker–Planck for zero-drift Itô diffusion: ρ∞ ∝ 1/D. With D ∝ 1/I, ρ∞ ∝ I exactly.  
See `derivations/fp_stationary_diffusion.py`.

## Metric used and why
Script currently reports **correlation**. Prefer **L¹** to normalized I (lesson of the 1.4 audit: correlation can hide power-law bias). Future runs should print L¹.

## Pass / Fail criterion
Illustrative consistency: histogram visibly tracks I; correlation ≳ 0.8 under default parameters.  
Exact result is analytic (FP), not numerical.

## Convergence / negative controls
See N-10 for L¹ vs N and constant-D negative control.

## Notes / limitations
By construction once D ∝ 1/I is granted. Does **not** derive that D from high-frequency particle-field mechanics (see N-07).
