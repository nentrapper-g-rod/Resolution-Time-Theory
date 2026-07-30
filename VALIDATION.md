# Validation notes — Resolution Time Theory

This file records the numerical checks behind each claim and any revisions made while developing them.

**Status tags:** proven-analytically / shown-numerically / assumed / withdrawn

---

## Revisions

### 2026-07-30 — Phase 1.4 (revised)

The first score-function simulation drove a Langevin process with a hard-coded ∇log I drift, which pre-assumed the result. The Poisson score has mean zero analytically (`derivations/poisson_score.py`), so that independent route was withdrawn. Equilibrium content rests on **1.2** (counting) and **1.3** (mechanics closed).

---

## Checks

| ID | Evidence | Status |
|----|----------|--------|
| D-01–D-03 | `derivations/` | proven-analytically |
| N-05 | results/RESULT_N05_… | shown-numerically (consistency) |
| N-06 | results/RESULT_N06_… | shown-numerically / by construction |
| N-07 | results/RESULT_N07_… | shown-numerically (**negative**) |
| N-08 | results/RESULT_N08_… | shown-numerically; independent score claim **withdrawn** |
| N-09 | results/RESULT_N09_… | shown-numerically / analytic kernels |
| N-10 | results/RESULT_N10_… | shown-numerically (consistency; residual from binning) |
| N-11 | results/RESULT_N11_… | shown-numerically |

Regenerate with `bash run_all.sh`. Canonical intensity helper: `simulations/intensity.py`.
