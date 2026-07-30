# Notes on Equilibrium Routes (Open Problem #1)

**Status:** Phase 1.1, 1.2 and 1.3 complete (30 July 2026)

## Goal
Obtain a stationary density ρ∞ ∝ I without simply inserting V_eff = −κ log I by hand.

## Route A — State-dependent diffusion (completed 1.1)

**Exact statement.**  
For the pure-diffusion Itô process

    dX = √(2 D(x)) dW

the Fokker–Planck equation admits the stationary solution

    ρ∞(x) ∝ 1 / D(x)

Choosing D(x) = D₀ / (I(x) + ε) therefore yields ρ∞ ∝ I exactly.

**Numerical check.**  
See `simulations/05_state_dependent_diffusion_equilibrium.py`.

**Motivation from resolution / detection.**  
Inside a finite gate window of duration ~τ_c, higher local intensity produces more detection events. More events tighten the position estimate → smaller effective diffusion of the *recorded* trajectory. This motivation lives on the measurement side of the theory.

**Honest limitation.**  
Achieves the density by design. Does **not** yet derive D ∝ 1/I from the underlying high-frequency classical field dynamics of the particle itself.

## Route B — Rate and counting models (completed 1.2)

1. Inhomogeneous Poisson process of detection events with intensity ∝ I(x): empirical density of recorded events ∝ I by the law of large numbers.
2. Lattice continuous-time Markov chain with rates chosen to satisfy detailed balance for π ∝ I: stationary distribution exactly ∝ I.

See `simulations/06_rate_and_counting_models.py` and related lattice script.

Logs appear naturally from rate ratios. Again, the intensity dependence of the rates is motivated from the detection/under-sampling side.

## Route C — Pure mechanical homogenization (completed 1.3 — negative result)

**Model.** Overdamped particle in a rapidly oscillating potential V(x,t) = A(x) cos(ω t), so the force is -A'(x) cos(ω t).

**Analytic (Kapitza).** High-frequency averaging produces an effective potential proportional to (A')^{2} / ω^{2}. The resulting effective force is therefore related to derivatives of intensity gradients (ponderomotive / Kapitza form ∝ ∇I-type), **not** to ∇log I.

**Numeric.** Long trajectories under the fast force show occupation that does *not* lock to the intensity pattern (correlation with I near zero). See `simulations/07_homogenization_fast_field.py`.

**Conclusion.** Pure high-frequency classical averaging recovers the known technical obstruction. It does not generate the structure needed for Born-rule equilibrium. This strengthens the case for locating the log / 1/I structure on the detection, rate, or estimation side of the theory rather than in the particle’s mechanical dynamics during flight.

## What remains open

- A full microscopic derivation of intensity-dependent detection rates or of D ∝ 1/I from a concrete field + detector model.
- Ontology: is the equilibrium structure a property of the real particle trajectories or of the density reconstructed after finite-resolution detection? The second option is currently better supported by the calculations above.
- Phase 1.4: Bayesian / score-function estimator (score ∇log likelihood where likelihood ∝ I).
- Phase 1.5: Consolidated status note for the paper.

## Next
1.4 Bayesian filter sketch.
1.5 Synthesis note.
Then Phase 2 (quantitative visibility prediction).
