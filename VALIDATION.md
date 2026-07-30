# Validation notes — Resolution Time Theory

This file records the numerical checks behind each claim and any revisions I made while developing them.

**Status tags:** proven-analytically / shown-numerically / assumed / withdrawn

---

## Revisions

### 2026-07-30 — Phase 1.4 (revised)

My first version of the score-function simulation drove a Langevin process with a hard-coded ∇log I drift, which pre-assumed the result. On working out the Poisson score analytically it has mean zero (see `derivations/poisson_score.py`), so I withdrew that as an independent route. The equilibrium content rests on 1.2 (counting) and 1.3 (mechanics closed).

---

## Checks

| ID | Evidence | Status |
|----|----------|--------|
| D-01–D-03 | `derivations/` | proven-analytically |
| N-05 | results/RESULT_N05_state_dependent_diffusion.md | shown-numerically (consistency) |
| N-06 | results/RESULT_N06_rate_and_counting.md | shown-numerically / by construction |
| N-07 | results/RESULT_N07_homogenization.md | shown-numerically (**negative**) |
| N-08 | results/RESULT_N08_score_corrected.md | shown-numerically; independent score claim **withdrawn** |
| N-09 | results/RESULT_N09_visibility_kernels.md | shown-numerically / analytic kernels |
| N-10 | results/RESULT_N10_locking_L1.md | shown-numerically (consistency; residual from binning) |
| N-11 | results/RESULT_N11_finite_resolution.md | shown-numerically |
| C-1.4 | old forced-score Langevin | **withdrawn** |

---

## Open checks

- [x] Notes for N-05 … N-11
- [x] CI workflow runs numerical checks (`.github/workflows/verify.yml`)
- [ ] Compiled PDF under paper/ (see paper/BUILD.md)

*Record of what I checked, what I revised, and what remains assumed.*
