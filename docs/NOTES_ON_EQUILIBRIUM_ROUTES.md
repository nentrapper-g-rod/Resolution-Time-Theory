# Notes on Equilibrium Routes (Open Problem #1)

**Status after critical review + 1.4 (30 July 2026)**

## Honest scoreboard

- **1.1 (D ∝ 1/I) and 1.2 (rates / Poisson ∝ I)** are consistency checks.  
  They show that once intensity is allowed to control occupation (via diffusion, rates, or detection intensity), the target ρ ∝ I is reachable by exact theorems.  
  They do **not** reduce the original postulate; they are mathematically equivalent restatements of “whatever controls occupation is I.”  
  Useful for confirming the target is attainable, but not derivations.

- **1.3 (mechanical homogenization)** is the single most valuable result so far.  
  Pure high-frequency classical averaging of a particle in V = A(x) cos(ω t) recovers the Kapitza / ponderomotive effective force (related to derivatives of intensity / amplitude gradients).  
  Long-time occupation does **not** lock to I (correlation near zero).  
  This rules out the mechanical particle dynamics during flight as the origin of the log / 1/I structure.  
  The negative result is robust: the force is deterministic oscillatory + additive noise, so no Itô–Stratonovich spurious-drift ambiguity can hide a log term. Kapitza averaging is classical and independent of the stochastic calculus convention.

- **1.4 (Bayesian / score with forced likelihood)** is now complete.  
  The likelihood is not inserted. It is forced by ordinary detector physics: a classical intensity I(x) produces detection events as an inhomogeneous Poisson process with rate λ(x) = α · I(x). This intensity→event-rate relation is standard for photodetectors, MCPs, scintillators, etc.; it is measured, not postulated to recover Born statistics.  
  The Poisson likelihood p(k|x) therefore contains log I (or I) terms. The score ∇_x log p(data|x) contains ∇ log I.  
  Continuous filtering or Langevin dynamics of the position *estimate* under that score locks the recorded density to I (numerical correlation ≈ 0.95).  
  Script: `simulations/08_bayesian_score_forced_likelihood.py`.

## What 1.4 does and does not achieve

**Does:** Shows that once a detector converts intensity into Poisson events (standard physics), the natural Bayesian update / continuous filter for position acquires a ∇ log I term. The equilibrium structure of the *estimate* is then controlled by I. This is non-circular with respect to the detection model.

**Does not:** Derive why the classical intensity pattern itself is |ψ|². That is still taken as the high-frequency interference intensity. Multi-particle configuration space and Wallstrom issues remain untouched.

## Ontology (now the headline)

Given the negative mechanical result of 1.3 and the appearance of the structure as the score of a standard detection model in 1.4, the coherent framing is:

> RTT’s single-particle equilibrium sector is a theory of **measurement records / finite-resolution estimation**. The density that locks to I is the density of the recorded / estimated position after detection with finite gate τ_c, not a dynamical law governing real particle trajectories under high-frequency classical forces.

This is more modest than the original Core Edition framing and more faithful to the calculations. It is still a defensible research program: the experimental handle (τ_c ∼ ΔL/v and pulsed-gate visibility) remains concrete and is unaffected by the ontology clarification.

## Remaining hard problems (untouched by Phase 1)

- Multi-particle / configuration-space problem and Wallstrom-type single-valuedness issues.  
  Everything above is single-particle 1-D. A field living in ordinary 3-space does not automatically supply a wavefunction on 3N-dimensional configuration space, nor does a 1-D estimator.  
  Success in the single-particle equilibrium sector says nothing yet about whether the ontology can represent entanglement.

- A still-deeper derivation that starts from the microscopic field + detector Hamiltonian and derives the intensity→rate relation without any phenomenological input (beyond ordinary photodetection).

## Implication for the research program

Phase 1 has done its job: it ruled out the mechanical route (1.3) and showed that a non-circular detection model (1.4) places the log structure in the measurement record.  
The original postulate can be re-interpreted as the score of a finite-resolution estimator under standard intensity-to-count conversion.  
Next concrete step is Phase 2 (quantitative visibility kernels) and the 1.5 synthesis write-up that elevates the ontology conclusion into the paper framing.

---
All numerical claims are backed by the linked scripts in `simulations/`.  
Itô audit of 07 confirms the negative result is free of convention artifacts.
