# Verification Log — Resolution Time Theory

**Principle:** A claim is verified only when a stranger can regenerate the number *and* see from committed evidence that the number supports the sentence.

**Status tags:** proven-analytically / shown-numerically / assumed / withdrawn

---

## Critical-review trail

### 2026-07-30 — Claude audit of Phase 1.4
- Previous sim 08 hard-coded ∇log I (circular). Mean Poisson score = 0. 1.4 demoted.

### 2026-07-30 — Provenance notes N-05–N-11
- Regenerated script output; committed results/RESULT_N05 … RESULT_N11.

### 2026-07-30 — Optional CI
- `.github/workflows/verify.yml` runs derivations, core sims, and checks provenance files exist.

---

## Artifact register

| ID | Evidence | Status |
|----|----------|--------|
| D-01–D-03 | `derivations/` | proven-analytically |
| N-05 | results/RESULT_N05_state_dependent_diffusion.md | shown-numerically (consistency) |
| N-06 | results/RESULT_N06_rate_and_counting.md | shown-numerically / by construction |
| N-07 | results/RESULT_N07_homogenization.md | shown-numerically (**negative**) |
| N-08 | results/RESULT_N08_score_corrected.md | shown-numerically; independent score claim **withdrawn** |
| N-09 | results/RESULT_N09_visibility_kernels.md | shown-numerically / analytic kernels |
| N-10 | results/RESULT_N10_locking_L1.md | shown-numerically (reachability) |
| N-11 | results/RESULT_N11_finite_resolution.md | shown-numerically |
| C-1.4 | old forced-score Langevin | **withdrawn** |

---

## Open verification work

- [x] Provenance notes N-05 … N-11
- [x] Optional CI (`.github/workflows/verify.yml`)
- [ ] Compiled PDF under paper/ (local artifact only; binary upload is manual — see paper/BUILD.md)

*Permanent record of what was believed, falsified, and checked.*
