# Notes on Equilibrium Routes (Open Problem #1)

**Status:** Phase 1.1–1.3 complete; framing sharpened 30 July 2026

## Honest scoreboard

- **1.1** (D ∝ 1/I) and **1.2** (intensity-dependent rates / Poisson counting) are **consistency checks**.  
  They confirm that if the occupation-controlling object (diffusion profile or transition rates) is made proportional to I, then ρ∞ ∝ I follows exactly.  
  They do **not** derive the structure from the high-frequency field. They are mathematically equivalent restatements of the target (“whatever controls occupation is I”) wearing different costumes. Numerically verifying them is useful for reachability, but they leave the postulate intact.

- **1.3** (mechanical homogenization) is the **most valuable result so far**.  
  Pure high-frequency classical averaging of an oscillating potential recovers the standard Kapitza / ponderomotive form (effective forces related to intensity gradients, not ∇log I; long-time occupation does not lock to I).  
  The mechanical route is ruled out. This is a real finding, not a setback.

The program now rests on whether a concrete detector / estimation model can force the likelihood (or the rates, or the effective diffusion of the estimate) to track I without inserting the answer by hand.

## Route A — State-dependent diffusion (1.1)

Exact: pure-diffusion Itô process dX = √(2D(x)) dW has ρ∞ ∝ 1/D.  
Set D ∝ 1/I → ρ∞ ∝ I.  
Motivation attempted from detection statistics (more counts → tighter localization of the recorded position).  
Limitation: by construction; does not derive D ∝ 1/I from particle + field dynamics.

## Route B — Rate / counting models (1.2)

Poisson process with intensity ∝ I → empirical density of detections ∝ I by LLN.  
Lattice CTMC with target-proportional or detailed-balance rates for π ∝ I → exact stationary ∝ I.  
Limitation: again by construction of the rates / intensity measure.

## Route C — Pure mechanical homogenization (1.3 — negative)

Model: overdamped Langevin with deterministic force F = −A'(x) cos(ω t) + additive noise.  
Analytic Kapitza: V_eff ∼ (A')² / ω² → forces of ∇I-type.  
Numeric: long-time density correlation with I is near zero (or negative).  
No multiplicative noise → no Itô–Stratonovich conversion ambiguity that could hide a log term.  
Conclusion: the log / 1/I structure does **not** live in the bare particle mechanics under high-frequency averaging.

## Ontology implication (now the headline)

Given the negative mechanical result, the structure that produces ρ ∝ I is currently better supported as a property of the **recorded / estimated density after finite-resolution detection** than as a dynamical law of a real particle trajectory.  
RTT, as presently developed, is more coherent as a theory about measurement records under finite temporal resolution than as a hidden-variable mechanics that generates Born-rule equilibrium from classical field forces alone.  
This is a defensible and potentially interesting position; it is not the stronger claim the original Core Edition language sometimes suggested.

## What 1.4 must achieve to have content

A Bayesian / score-function route only reduces the postulate if the **likelihood itself is forced by a concrete detector + field model** to be proportional to I (or to have score ∇log I).  
Simply writing a Langevin sampler dX = D ∇log π dt + … with π chosen = I is another costume of the same assumption.  
The bar is: derive (or convincingly motivate from first principles of finite-time integration of the classical intensity / photon arrivals) that the likelihood takes that form.

## Completely open and harder

- Multi-particle / configuration-space problem and Wallstrom-type single-valuedness issues.  
  Success in the single-particle equilibrium sector (even a full derivation) says nothing yet about whether the ontology can represent entanglement.  
  These remain deferred but must be acknowledged as load-bearing open problems.

## Next steps

1.4 Carefully designed detector model that attempts to force the likelihood.  
1.5 Formal synthesis for the paper that states the above scoreboard without inflation.  
Then Phase 2 (quantitative visibility).
