# Verification Log — Resolution Time Theory

**Principle:** A claim is verified only when a stranger can regenerate the number *and* see from committed evidence that the number supports the sentence.

**Default status for AI-generated material:** `AI-generated-unverified` until an independent check (symbolic derivation, different method, or human audit) promotes it.

**Status tags:**
- `proven-analytically` — executable sympy (or equivalent) derivation exists and passes
- `shown-numerically` — reproducible simulation with stated metric, tolerance, and (where possible) convergence
- `assumed` — modelling assumption, not derived
- `AI-generated-unverified` — produced by AI, not yet independently checked
- `withdrawn` — previously claimed, later falsified or demoted

---

## Critical-review trail

### 2026-07-30 — Claude audit of Phase 1.4
- **Finding:** Previous `08_bayesian_score_forced_likelihood.py` hard-coded `score = ∇log I`, never sampled Poisson counts, used drift coefficient 1.2 → stationary ∝ I^1.2. Correlation hid the bias. Exact Poisson score has mean zero.
- **Action:** Script rewritten; 1.4 demoted in TODO and synthesis. Ontology retained on the footing of 1.3 + 1.2 only.
- **Lesson:** Reproducing a number is not enough; the number must be shown to support the prose claim. Correlation is an insufficient metric for density matching.

---

## Artifact register

| ID | Artifact | Claim | Status | Evidence |
|----|----------|-------|--------|----------|
| D-01 | `derivations/poisson_score.py` | E[Poisson score] = 0; score = (k−λ)∇log I | proven-analytically | Run the script |
| D-02 | `derivations/kapitza_effective_potential.py` | V_eff ∝ (A')²/ω² (∇I-type, not ∇log I) | proven-analytically | Run the script |
| D-03 | `derivations/fp_stationary_diffusion.py` | Pure diffusion (Itô, zero drift) ⇒ ρ∞ ∝ 1/D | proven-analytically | Run the script |
| N-05 | `simulations/05_...diffusion...` | D∝1/I ⇒ ρ∝I (consistency) | shown-numerically | Monte-Carlo; prefer L¹ |
| N-06 | `simulations/06_...` | Rate∝I ⇒ recorded density∝I (counting) | shown-numerically | LLN / histogram |
| N-07 | `simulations/07_homogenization...` | Mechanical averaging does **not** lock to I | shown-numerically | Negative result |
| N-08 | `simulations/08_...` (corrected) | Mean Poisson score ≈0; counting recovers density∝I | shown-numerically | Post-audit rewrite |
| N-09 | `simulations/09_visibility_kernels.py` | Geometric vs phase kernels, 50–200 eV tables | shown-numerically | Analytic forms + tables |
| N-10 | `simulations/10_locking_L1_convergence.py` | D∝1/I locks in L¹; constant-D control does not | shown-numerically | results/RESULT_N10_locking_L1.md |
| N-11 | `simulations/11_finite_resolution_averaging.py` | Finite-resolution samples track slow envelope better than instantaneous | shown-numerically | results/RESULT_N11_finite_resolution.md |
| S-01 | Phase-1 synthesis | Ontology = measurement records on 1.3+1.2 | assumed framing (supported by above) | docs/PHASE1_SYNTHESIS.md |

---

## Open verification work

- [ ] Provenance notes (RESULT_TEMPLATE filled) for N-05 … N-09
- [ ] Further convergence studies (dt, N, grid) for key sims
- [ ] Golden outputs + tighter run_all / Makefile
- [ ] Optional CI asserting tolerances

---

*This log is the permanent record of what was believed, what was falsified, and what has been independently checked.*
