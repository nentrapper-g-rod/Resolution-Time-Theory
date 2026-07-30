# Phase 1 Synthesis — Open Problem #1 (Equilibrium Structure)

**Date:** 30 July 2026  
**Status:** Complete

## One-paragraph summary

Pure mechanical high-frequency averaging of a classical particle in an oscillating field (Kapitza / ponderomotive regime) does **not** produce the drift or diffusion structure required for stationary density ρ ∝ I. That negative result is robust under the stochastic calculus conventions examined. The structure *does* appear as the score of a standard intensity-to-count detector model (Poisson process with rate λ ∝ I). Consequently, in its present form, the single-particle equilibrium sector of Resolution Time Theory is best understood as a theory of **measurement records / finite-resolution estimation** rather than a dynamical law governing real particle trajectories under classical high-frequency forces. The experimental proposal (geometric resolution time τ_c ∼ ΔL/v and pulsed-gate visibility) is unaffected by this clarification.

## Scoreboard of the five Phase-1 items

| Item | Character | Result |
|------|-----------|--------|
| 1.1 D ∝ 1/I | Consistency check / restatement | Exact stationary ρ ∝ I under Itô; useful reachability confirmation only |
| 1.2 Rates / Poisson counting ∝ I | Consistency check / restatement | Exact or LLN stationary / empirical density ∝ I; useful reachability confirmation only |
| **1.3 Mechanical homogenization** | **Load-bearing negative result** | Kapitza-type ∇I forces; occupation does **not** lock to I. Mechanical route closed. |
| **1.4 Forced-likelihood score** | **Positive, non-circular on the detection side** | Ordinary detector physics (λ = α I) forces log I into the likelihood; score contains ∇log I; estimator locks to I |
| 1.5 Synthesis | Framing | Ontology elevated to measurement records; remaining open problems stated without inflation |

## What is now motivated versus what remains postulated or open

**Motivated / derived within the single-particle sector**
- The mechanical particle + high-frequency field dynamics do not generate ρ ∝ I (1.3).
- Once a detector converts classical intensity into events with rate proportional to I (standard photodetection), the natural Bayesian score for position contains ∇log I and the recorded density locks to I (1.4).
- The original equilibrium postulate can therefore be re-read as the score of a finite-resolution estimator under ordinary intensity-to-count conversion.

**Still postulated or phenomenological**
- The precise intensity-to-rate coefficient α and the detailed detector response function (beyond the leading Poisson term).
- Any residual mechanical contribution that might appear under a more complete field + particle + detector Hamiltonian.

**Completely open and harder**
- Multi-particle configuration space and Wallstrom-type issues. Everything above is single-particle. A classical field living in ordinary 3-space does not automatically supply a wave function on 3N-dimensional configuration space, nor does a one-particle estimator. Success in the single-particle equilibrium sector is silent on entanglement.
- Lorentz invariance / no-signaling once a preferred foliation is introduced for the Bell sector.
- Quantitative map from gravitational potential or velocity onto effective resolution timescales.

## Implication for the research program and the paper

The Core Edition should be revised so that the measurement-records framing is the **headline** of the equilibrium discussion, not a late status note. The original language that suggested a dynamical classical mechanism producing Born-rule equilibrium during flight should be tempered or removed. The experimental handle (τ_c and visibility-versus-gate-width) remains a concrete, apparatus-defined prediction and is independent of the ontology clarification.

Phase 1 has done the work it was asked to do: it closed the mechanical route and showed that a non-circular detection model places the log structure in the measurement record. The next concrete scientific step is Phase 2 — quantitative visibility kernels that can be compared with real pulsed-electron interferometry.

## Files that back the claims

- `simulations/05_state_dependent_diffusion_equilibrium.py`
- `simulations/06_lattice_master_equation_equilibrium.py` / `06_rate_and_counting_models.py`
- `simulations/07_homogenization_fast_field.py` (negative result + Itô audit)
- `simulations/08_bayesian_score_forced_likelihood.py`
- `docs/NOTES_ON_EQUILIBRIUM_ROUTES.md`

All numerical correlations and analytic statements are reproducible from the scripts above.
