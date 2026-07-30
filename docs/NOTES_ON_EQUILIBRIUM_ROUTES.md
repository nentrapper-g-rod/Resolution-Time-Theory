# Notes on Equilibrium Routes (Open Problem #1)

**Status after critical review (30 July 2026)**

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

- The program therefore rests on whether a non-circular detection / estimation model can force the intensity dependence without inserting the answer.

## Route D (1.4) — the remaining live candidate

The Bayesian / score-function route is promising because it relocates the log to the detection side (where RTT claims the physics lives).  
**Bar for real content:** the likelihood p(data | x) must be forced to be proportional to I by a concrete detector + field model, not chosen because that is the desired target.  
A pure Langevin sampler of an inserted π = I is again only the D∇log identity in a new costume.  
If the detector model cannot hand us the likelihood without insertion, then 1.4 becomes a fourth restatement and the honest conclusion is that RTT’s density is epistemic — a statement about the recorded estimate after finite-resolution detection — not a dynamical law of a real trajectory.  
That is still a defensible, publishable position; it is simply not the ontology the original Core Edition most naturally suggested.

## Ontology (now the headline, not a footnote)

Given the negative mechanical result of 1.3, the structure is not in the particle dynamics.  
RTT is therefore most coherently framed as a theory about **measurement records / finite-resolution estimation**, not about the real trajectories of particles under high-frequency classical forces.  
The under-sampling / τ_c idea already points in this direction. The calculations make it the default conclusion rather than an optional interpretation.

## Remaining hard problems (untouched by Phase 1)

- Multi-particle / configuration-space problem and Wallstrom-type single-valuedness issues.  
  Everything above is single-particle 1-D. A field living in ordinary 3-space does not automatically supply a wavefunction on 3N-dimensional configuration space, nor does a 1-D estimator.  
  Success in the single-particle equilibrium sector says nothing yet about whether the ontology can represent entanglement.

- A microscopic derivation that forces the intensity dependence of rates, effective diffusion of the estimate, or likelihood from concrete field + detector physics without circularity.

## Implication for the research program

The original postulate can be re-interpreted as the score of a finite-resolution estimator or as the consequence of intensity-dependent detection statistics.  
This is more coherent with the under-sampling / resolution-time framing than treating the log as a new mechanical force.  
The experimental handle (τ_c ~ ΔL/v and pulsed-gate visibility) remains the most concrete novel prediction and is unaffected by the ontology clarification.

Phase 1 has done its job: it ruled out the mechanical route and clarified where the remaining work must live.  
Next concrete step is a carefully non-circular detector model for 1.4, followed by the quantitative visibility kernels of Phase 2.

---
All numerical claims are backed by the linked scripts in `simulations/`.  
Itô audit of 07 confirms the negative result is free of convention artifacts.
