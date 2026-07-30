# Notes on Equilibrium Routes (Open Problem #1)

**Status:** Phase 1.1 complete (30 July 2026)

## Goal
Obtain a stationary density ρ∞ ∝ I without simply inserting V_eff = −κ log I by hand.

## Route A — State-dependent diffusion (completed)

**Exact statement.**  
For the pure-diffusion Itô process

    dX = √(2 D(x)) dW

the Fokker–Planck equation admits the stationary solution

    ρ∞(x) ∝ 1 / D(x)

(when reflecting or periodic boundaries are used and the process is ergodic).  
Choosing D(x) = D₀ / (I(x) + ε) therefore yields ρ∞ ∝ I exactly.

**Numerical check.**  
See `simulations/05_state_dependent_diffusion_equilibrium.py`.  
Long Monte-Carlo trajectories produce a histogram that tracks the target intensity (correlation typically > 0.95 for the parameters used).

**Motivation from resolution / detection.**  
Inside a finite gate window of duration ~τ_c, higher local intensity produces more detection events. More events tighten the position estimate, which can be modelled as a smaller effective diffusion of the *recorded* trajectory. This motivation lives on the measurement side of the theory and is therefore consonant with the original under-sampling idea.

**Honest limitation.**  
This construction achieves the desired stationary density by design. It does **not** yet derive D ∝ 1/I from the underlying high-frequency classical field dynamics of the particle itself. Whether the physical particle (as opposed to the estimator of its position) experiences reduced diffusion in bright regions remains an open modelling question.

## Next routes (still open)

- **1.2 Lattice master equation** with intensity-dependent transition rates (detailed balance → log ratios → ρ ∝ I).
- **1.3 Stochastic averaging / homogenization** of a fast oscillating field (expected to recover only ∇I-type forces; documenting the negative result is useful).
- **1.4 Bayesian filter / score-function** model in which ∇log I appears as the score of a finite-resolution estimator.

## Ontology decision still required
Is the equilibrium structure a property of the real particle trajectories or of the density reconstructed after finite-resolution detection? The second option is currently easier to motivate and closer to the camera-blur analogy; the first is stronger but harder.

---

*These notes will be updated after each Phase 1 item.*
