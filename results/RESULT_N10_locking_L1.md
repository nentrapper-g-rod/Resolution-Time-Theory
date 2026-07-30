# Result note — N-10

**ID:** N-10  
**Artifact:** `simulations/10_locking_L1_convergence.py`  
**Claim:** Under Itô pure diffusion with D(x) ∝ 1/I(x), empirical density approaches ρ ∝ I in L¹; residual floor remains from finite binning/sampling.  
**Status:** shown-numerically (consistency / reachability only)

## How to regenerate
```bash
python simulations/10_locking_L1_convergence.py
```
**Seed:** 7

## Printed output (regenerated 2026-07-30)
```
(A) L¹ vs N (dt=0.002, T=16):
  N=200 → 0.288; N=800 → 0.265; N=2000 → 0.172; N=4000 → 0.192

(B) Timestep convergence (N=4000, T=16):
  dt=0.008 → L1=0.211
  dt=0.004 → L1=0.165
  dt=0.002 → L1=0.163
  dt=0.001 → L1=0.162

Negative control (constant D): L1=0.734 (does not lock)
```

## Analytic target
Fokker–Planck stationary solution for zero-drift Itô diffusion: ρ∞ ∝ 1/D.  
With D ∝ 1/I, ρ∞ ∝ I exactly. See `derivations/fp_stationary_diffusion.py`.

## Metric
L¹ distance to normalized intensity. Correlation is not used as a primary metric because it can hide power-law bias (lesson from revising 1.4).

## Interpretation
Refining dt reduces integrator bias; L¹ plateaus near ~0.16 under these bins and sample sizes. That residual is consistent with finite histogram resolution, not a claim of exact numerical lock.  
Negative control (constant D) stays far from I (L¹ ≈ 0.73).

## Notes
Confirms reachability once D ∝ 1/I is granted. Does **not** derive that D from particle-field mechanics (mechanical route closed by 1.3).
