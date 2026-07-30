# Notes on Equilibrium Routes (Open Problem #1)

**Status after critical audit (30 July 2026)**

## Honest scoreboard (post-audit)

- **1.1 (D ∝ 1/I)** is a consistency check / restatement of the target. Useful for reachability, not a derivation.

- **1.2 (rates / Poisson counting ∝ I)** is the solid measurement-side content. Once the event rate is proportional to classical intensity I, the empirical density of recorded detection locations is proportional to I by the law of large numbers. This is by construction once the rate model is granted, and is correctly labeled as such.

- **1.3 (mechanical homogenization)** is the single most valuable result. Pure high-frequency classical averaging recovers the Kapitza / ponderomotive effective force (related to intensity gradients). Long-time occupation does **not** lock to I. The mechanical route is closed. The result is robust (additive noise; no Itô–Stratonovich artifact that could hide a log).

- **1.4 (Bayesian / score route)** is **demoted**. The exact Poisson score for λ = α I, k ~ Poisson(λτ) is

      ∂x log p(k|x) = (k − λ) · (∂x log I)

  The expectation over k is identically zero. There is no net drift that climbs the intensity. The previous simulation hard-coded ∇log I, never used the counts, and used a coefficient that produced ρ ∝ I^{1.2}. That claim has been withdrawn. The corrected script demonstrates the mean-score-zero fact and the counting result already present in 1.2. 1.4 does not supply an independent non-circular derivation of a dynamical score drift.

## Ontology (framing that survives)

Given the negative mechanical result (1.3) and the counting statement (1.2):

> RTT’s single-particle equilibrium sector is a theory of **measurement records**. Detection events generated with rate proportional to classical intensity produce an empirical density of recorded locations that tracks I. Pure high-frequency classical mechanics does not produce this structure. The density of interest is the density of the records.

This is more modest than the original Core Edition framing and more faithful to the calculations that survive scrutiny. The experimental handle (τ_c ∼ ΔL/v) remains intact.

## Remaining open

- Deeper microscopic derivation of the intensity → event-rate relation.
- Multi-particle / configuration-space / Wallstrom issues (completely untouched).
- Quantitative visibility discrimination (Phase 2).

## Supporting scripts

`simulations/05`–`09` (08 corrected after audit).  
All claims are backed by exact theorems or the linked numerical checks without circular insertion of the target drift.
