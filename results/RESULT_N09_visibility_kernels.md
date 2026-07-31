# Result note — N-09 (exploratory kernels)

**ID:** N-09  
**Artifact:** `exploratory_models/09_visibility_kernels.py` (moved from `simulations/` on 2026-07-30)  
**Status:** **exploratory / not a derived prediction**  
**Superseded for gate claims by:** N-12 (`simulations/12_qm_vs_rtt_benchmark.py`)

## What this file is

Closed-form tables of:

- geometric kernel $V_{\mathrm{geom}} = |\mathrm{sinc}(\delta t/\tau_g)|$ with $\delta t = \Delta L/v$
- phase baseline $V_\phi = \exp(-\tfrac12(\tau_g/\tau_\phi)^2)$

for 50–200 eV electrons. Useful as kinematics reference and as the historical form that N-12 tests against.

## What this file is not

It is **not** a derived RTT event law and **not** a current experimental prediction.  
N-12 shows that under imported $I = |\psi|^2$ and $\lambda \propto I$, visibility tracks $r = \tau_c/\tau_\phi$, and the sinc form is excluded as a prediction at large $r$.

## How to regenerate
```bash
python exploratory_models/09_visibility_kernels.py
```

## Notes

Kept for reproducibility of the Phase-2 discussion. Claim Map: sinc-as-prediction = Withdrawn; kinematics τ_c = ΔL/v = Assumed scale only.
