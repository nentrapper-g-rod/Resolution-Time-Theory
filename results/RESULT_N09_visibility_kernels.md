# Result Provenance — N-09

**ID:** N-09  
**Artifact:** `simulations/09_visibility_kernels.py`  
**Claim:** Explicit geometric τ_c = ΔL/v and phase τ_φ = ℏ/δE kernels with realistic 50–200 eV electron tables; visibility vs gate width can separate when timescales differ.  
**Status:** shown-numerically / analytic kernels (assumed geometric identification + phenomenological phase model)

## How to regenerate
```bash
python simulations/09_visibility_kernels.py
```
**Environment:** see requirements.txt (numpy only)

**Printed output (regenerated 2026-07-30, excerpt):**
```
E = 100 eV   v = 5.931e+06 m/s   λ = 0.123 nm

Geometric τ_c = ΔL / v  (fs)
 ΔL=0.1 μm → 16.9 fs;  ΔL=1 μm → 168.6 fs;  ΔL=2 μm → 337.2 fs  (at 100 eV)

Phase τ_φ: δE=0.2 eV → 3.29 fs

Example V_geom vs V_phase (E=100 eV, ΔL=1 μm):
  τ_g=50 fs  → V_geom=0.087  V_phase~0
  τ_g=500 fs → V_geom=0.823  V_phase~0
```

## Analytic target
V_geom = |sinc(δt/τ_g)| for rectangular gate; V_phase = exp(-½(τ_g/τ_φ)²) baseline.

## Metric used and why
Direct evaluation of closed-form kernels (no Monte-Carlo noise).

## Pass / Fail criterion
Tables match kinematics (τ_c = ΔL/v) within floating-point error → PASS.  
Discrimination is illustrative where curves separate.

## Notes / limitations
Phenomenological phase model; not full 3-D wave-packet + detector simulation. Competing decoherence must be controlled experimentally.
