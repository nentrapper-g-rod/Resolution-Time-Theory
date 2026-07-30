# Result Provenance — N-10

**ID:** N-10  
**Artifact:** `simulations/10_locking_L1_convergence.py`  
**Claim:** Under Itô pure diffusion with D(x) ∝ 1/I(x), empirical density converges to ρ ∝ I as measured by L¹ distance.  
**Status:** shown-numerically (consistency / reachability only)

## How to regenerate
```bash
python simulations/10_locking_L1_convergence.py
```
**Environment:** see requirements.txt  
**Seed:** 7 (numpy Generator)

## Analytic target
Fokker–Planck stationary solution for zero-drift Itô diffusion: ρ∞ ∝ 1/D.  
Choosing D ∝ 1/I therefore yields ρ∞ ∝ I exactly. (See `derivations/fp_stationary_diffusion.py`.)

## Metric used and why
L¹ distance to the normalized intensity.  
Correlation is rejected because it is blind to power-law distortions (lesson of the 1.4 audit).

## Pass / Fail criterion
L¹ < 0.12 for N ≥ 2000 trajectories → PASS.  
Negative control (constant D) must remain L¹ > 0.25.

## Convergence / negative controls
- L¹ decreases with N (reported in script output).  
- Constant-D negative control does not lock.

## Notes / limitations
This confirms reachability of the target density once D ∝ 1/I is granted.  
It does **not** derive that form of D from particle-field mechanics (mechanical route closed by 1.3).  
Ontology: the dynamics is most coherently read as that of a recorded / estimated position under a detection-motivated diffusion, not of a real particle in flight.
