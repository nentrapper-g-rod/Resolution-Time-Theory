# Validation notes — Resolution Time Theory

Numerical checks behind each claim, plus revisions made while developing them.

**Status tags:** proven-analytically / shown-numerically / assumed / withdrawn / exploratory

**Maps:** [CLAIM_MAP.md](CLAIM_MAP.md) · [investigations/A2_first_rtt_only_equation.md](investigations/A2_first_rtt_only_equation.md) · [investigations/A3_detector_event_law.md](investigations/A3_detector_event_law.md)

---

## Revisions

### 2026-07-30 — Phase 1.4 (revised)

The first score-function simulation drove a Langevin process with a hard-coded ∇log I drift, which pre-assumed the result. The Poisson score has mean zero analytically (`derivations/poisson_score.py`), so that independent route was withdrawn. Equilibrium content rests on **1.2** (counting) and **1.3** (mechanics closed).

### 2026-07-30 — N-09 reclassified

Geometric |sinc| visibility kernels moved to `exploratory_models/`. They are not a derived prediction. Gate claims rest on N-12.

### 2026-07-30 — A.2 / A.3

No RTT-only equation found under present postulates (single-particle record sector). Present detector law λ = α I is equivalent to gated I_QM when intensity is imported. Distinct functional F remains Missing.

---

## Checks

| ID | Evidence | Status |
|----|----------|--------|
| D-01–D-03 | `derivations/` | proven-analytically |
| N-05 | results/RESULT_N05_… | shown-numerically (consistency) |
| N-06 | results/RESULT_N06_… | shown-numerically / by construction |
| N-07 | results/RESULT_N07_… | shown-numerically (**negative**) |
| N-08 | results/RESULT_N08_… | shown-numerically; independent score claim **withdrawn** |
| N-09 | results/RESULT_N09_… · `exploratory_models/09_…` | **exploratory** (not a prediction) |
| N-10 | results/RESULT_N10_… | shown-numerically (consistency; residual from binning) |
| N-11 | results/RESULT_N11_… | shown-numerically |
| N-12 | results/RESULT_N12_… · `simulations/12_…` | shown-numerically / derived under premises (scoped QM equivalence; sinc excluded) |
| A.2 | investigations/A2_… | classification result: no RTT-only equation under present postulates |
| A.3 | investigations/A3_… | present law written; equivalence when I imported; distinct F Missing |

Regenerate with `bash run_all.sh`. Canonical intensity helper: `simulations/intensity.py`.
