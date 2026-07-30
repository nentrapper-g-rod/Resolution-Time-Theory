# Phase 1 Synthesis — Open Problem #1 (Equilibrium without pure insertion)

**Date:** 30 July 2026  
**Status:** Phase 1 complete

## One-line conclusion

The mechanical route is closed. The log / inverse-intensity structure that produces single-particle Born-like equilibrium lives in the measurement record / finite-resolution estimate, not in the dynamics of a real particle under high-frequency classical forces.

## Scoreboard (honest weights)

| Item | Nature | Weight |
|------|--------|--------|
| 1.1 D ∝ 1/I | Consistency check / restatement of the target | Low |
| 1.2 Rates or Poisson counting ∝ I | Consistency check / restatement of the target | Low |
| **1.3 Mechanical homogenization** | **Negative result: Kapitza/ponderomotive ∇I-type terms; occupation does not lock to I** | **High — load-bearing** |
| **1.4 Forced-likelihood detector model** | **Ordinary intensity → Poisson event rate (λ = α I) forces the score to contain ∇ log I; the estimator locks to I** | **High** |

1.1 and 1.2 confirm reachability once intensity controls occupation. They do not derive that control.

1.3 rules out pure particle-field mechanics as the origin. The result is robust (additive noise; no Itô–Stratonovich artifact).

1.4 shows that a standard detector model (photodetection, MCP, etc.) converts classical intensity into Poisson counts. The resulting likelihood contains log I; the score of the position estimate therefore contains ∇ log I. Continuous filtering of that score produces a recorded density that tracks I. This is forced by ordinary detector physics, not free insertion of the Born rule.

## Ontology (now the framing)

Given 1.3 + 1.4:

> RTT’s single-particle equilibrium sector is a theory of **measurement records under finite temporal resolution**. The density that locks to the classical intensity I is the density of the *recorded / estimated* position after detection with gate width ~τ_c. It is not (on present evidence) a dynamical law governing the real trajectory of a particle while it is still in flight under high-frequency classical forces.

This is more modest than the original Core Edition framing and more faithful to the calculations. It remains a coherent research program: the experimental signature (τ_c ~ ΔL/v and pulsed-gate visibility) is still concrete and is unaffected by the clarification.

## What remains open

1. A still-deeper derivation that starts from a fully microscopic field + detector Hamiltonian and obtains the intensity → event-rate relation without any phenomenological input.
2. Multi-particle / configuration-space problem and Wallstrom-type single-valuedness. Everything in Phase 1 is single-particle and one-dimensional. Success here says nothing yet about whether the ontology can represent entanglement or a wavefunction on 3N-dimensional configuration space.
3. Quantitative visibility kernels (Phase 2) that turn the geometric τ_c proposal into a concrete, plottable prediction distinguishable from ordinary quantum phase averaging.

## Implication for the paper and submission

The Core Edition should be revised so that:
- the obstruction (1.3) is stated first and given its proper weight;
- the original V_eff = −κ log I postulate is re-interpreted as the score of a finite-resolution estimator under standard intensity-to-count conversion;
- the ontology is stated clearly as a theory of measurement records;
- the multi-particle limitation is flagged explicitly;
- the pulsed-gate experiment remains the primary novel, falsifiable claim.

Phase 1 is complete. The next high-leverage work is Phase 2 (quantitative visibility).

---
Supporting scripts: `simulations/05`–`08`.  
All claims are backed by exact theorems or the linked numerical checks.
