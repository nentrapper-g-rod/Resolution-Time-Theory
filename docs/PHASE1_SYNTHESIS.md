# Phase 1 Synthesis — Open Problem #1 (Equilibrium without pure insertion)

**Date:** 30 July 2026 (updated after critical audit)
**Status:** Mechanical route closed; record-side reachability by counting established; estimator-score claim demoted

## One-line conclusion

The mechanical route is closed. The single-particle density that tracks classical intensity I is most coherently understood as the density of measurement records (detection events generated with rate ∝ I). This rests on the negative mechanical result (1.3) plus the counting statement (1.2). A dynamical score-driven estimator route does not currently supply an independent non-circular derivation.

## Scoreboard (honest weights, post-audit)

| Item | Nature | Weight |
|------|--------|--------|
| 1.1 D ∝ 1/I | Consistency check / restatement of the target | Low |
| **1.2 Rates / Poisson counting ∝ I** | **Counting: rate ∝ I ⇒ recorded event locations ∝ I (LLN)** | **High — solid record-side content** |
| **1.3 Mechanical homogenization** | **Negative result: Kapitza/ponderomotive ∇I-type terms; occupation does not lock to I** | **High — load-bearing** |
| 1.4 Bayesian / score route | **Demoted.** Real Poisson score = (k − λ) ∇log I has mean zero. Previous simulation hard-coded ∇log I (circular) and used a coefficient that produces I^{1.2}. Does not add an independent non-circular derivation. | Low / withdrawn as independent claim |

## Ontology (framing)

Given 1.3 + 1.2:

> RTT’s single-particle equilibrium sector is a theory of **measurement records**. Detection events generated with rate proportional to classical intensity I produce an empirical density of recorded locations that tracks I by the law of large numbers. Pure high-frequency classical mechanics does not produce this structure (1.3). The density of interest is therefore the density of the records, not a dynamical law of real trajectories under the high-frequency field.

This is more modest than the original Core Edition framing and more faithful to the calculations that survive scrutiny.

## What the Poisson score actually says (why 1.4 was demoted)

For λ(x) = α I(x) and k ~ Poisson(λ τ):

∂_x log p(k|x) = (k − λ) · (I'/I)

The expectation over k is exactly zero. There is no net drift that climbs the intensity landscape. A continuous filter or Langevin driven by the *mean* score therefore experiences no systematic force from the detection model. The previous claim that “the score contains ∇log I and therefore the estimator locks” conflated the fluctuation term with a mean drift and was implemented by hard-coding the desired drift. That error has been corrected; the script now demonstrates the mean-score-zero fact and the counting result.

## Remaining open

1. A still-deeper microscopic derivation of the intensity → event-rate relation.
2. Multi-particle / configuration-space problem and Wallstrom-type issues (completely untouched).
3. Quantitative visibility kernels and a concrete gated experiment (Phase 2 — already started).

## Implication for the paper

- State the obstruction (1.3) first and give it proper weight.
- Base the measurement-record ontology on the counting argument (1.2).
- Do not claim a non-circular dynamical score derivation from the Poisson model in its current form.
- Keep the pulsed-gate / geometric τ_c prediction as the primary novel, falsifiable claim.

Supporting scripts: `simulations/05`–`09` (08 corrected).  
All claims are backed by exact theorems or the linked numerical checks.
