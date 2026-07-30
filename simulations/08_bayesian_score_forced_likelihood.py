#!/usr/bin/env python3
"""
RTT Phase 1.4 — Honest status after audit (corrected)
====================================================
CRITICAL CORRECTION (Claude audit + verification, 30 July 2026)

The previous version of this script claimed that a standard intensity→Poisson
detection model forces a net ∇log I drift on a position estimator. That claim
was incorrect.

Exact Poisson score
-------------------
λ(x) = α · I(x),  k ~ Poisson(λ τ)

∂_x log p(k|x) = (k − λ) · (∂_x log I) = I' · (k/I − ατ)

Averaged over the data, E[k] = λ, therefore E[score] ≡ 0.
There is no net drift toward high-I regions coming from the mean score of the
detection model. The “score climbs the intensity” picture does not hold for
the average Poisson likelihood.

What remains solid
------------------
The inhomogeneous Poisson process itself produces an empirical density of
arrival locations that is proportional to I by the law of large numbers
(already demonstrated cleanly in Phase 1.2). That counting statement is
non-circular once the rate λ ∝ I is granted as ordinary detection physics.
It does not require a score-driven Langevin.

What this script now does (honest)
----------------------------------
1. Computes the exact Poisson score and shows its mean is zero.
2. Demonstrates the pure counting result: sample many events with rate ∝ I;
   the histogram of recorded positions tracks I (LLN).
3. Does *not* run a hard-coded ∇log I Langevin or claim an independent
   non-circular derivation of a net score drift.

Ontology implication (unchanged in substance)
---------------------------------------------
The mechanical route is closed (1.3). The record of detections with rate ∝ I
has density ∝ I by counting (1.2). The single-particle equilibrium sector is
therefore best framed as a theory of measurement records. The previous
over-claim about a forced net ∇log I estimator dynamics is withdrawn.

Requires: numpy
Run: python 08_bayesian_score_forced_likelihood.py
"""

import numpy as np

def I(x):
    return 0.10 + 0.95 * (
        np.exp(-((x + 1.25)**2) / (2 * 0.32**2))
        + np.exp(-((x - 1.25)**2) / (2 * 0.32**2))
    )

def main():
    print("RTT Phase 1.4 — Corrected after audit")
    print("=" * 60)
    print("Exact Poisson score for λ = α I, k ~ Poisson(λτ):")
    print("  ∂x log p(k|x) = (k − λ) · (∂x log I)")
    print("  E[k] = λ  ⇒  E[score] = 0")
    print("There is no net drift up the intensity from the mean score.")
    print()

    # Numerical confirmation of mean score ≈ 0
    rng = np.random.default_rng(7)
    x_grid = np.linspace(-3.5, 3.5, 400)
    Ix = I(x_grid)
    alpha_tau = 5.0
    lam = alpha_tau * Ix
    # sample many (x, k) pairs from the true process
    # first sample positions with density ∝ I (the counting process)
    pdf = Ix / np.trapezoid(Ix, x_grid)
    cdf = np.cumsum(pdf)
    cdf /= cdf[-1]
    n_samp = 20000
    u = rng.random(n_samp)
    x_samp = np.interp(u, cdf, x_grid)
    k_samp = rng.poisson(alpha_tau * I(x_samp))
    # score at each sample
    # numerical ∂logI
    dlogI = np.gradient(np.log(Ix + 1e-12), x_grid)
    dlogI_at = np.interp(x_samp, x_grid, dlogI)
    scores = (k_samp - alpha_tau * I(x_samp)) * dlogI_at
    print(f"Monte-Carlo mean score over {n_samp} events: {scores.mean():.4e}")
    print("(Consistent with analytic E[score] = 0)")
    print()

    # Pure counting demonstration (the solid result)
    hist, edges = np.histogram(x_samp, bins=50, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_c = I(centers)
    I_norm = I_c / np.trapezoid(I_c, centers)
    # L1 distance (preferred over correlation)
    L1 = np.trapezoid(np.abs(hist - I_norm), centers)
    corr = np.corrcoef(hist, I_norm)[0, 1]
    print("Counting result (inhomogeneous Poisson arrivals, rate ∝ I):")
    print(f"  Correlation of arrival histogram with I: {corr:.4f}")
    print(f"  L¹ distance to normalized I:             {L1:.4f}")
    print("  This is the law of large numbers for the detection process.")
    print("  It is already established in Phase 1.2; no additional score")
    print("  dynamics is required.")
    print()
    print("Honest status after correction:")
    print("  1.4 does not supply an independent non-circular derivation of a")
    print("  net ∇log I drift. The mean Poisson score is zero.")
    print("  The solid measurement-side content remains the counting statement")
    print("  (rate ∝ I ⇒ recorded density ∝ I). Combined with the negative")
    print("  mechanical result (1.3) this still supports the measurement-")
    print("  records framing of the single-particle equilibrium sector.")

if __name__ == "__main__":
    main()
