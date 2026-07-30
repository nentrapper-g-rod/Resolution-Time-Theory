#!/usr/bin/env python3
"""
RTT Phase 1.4 (corrected) — Honest Poisson counting + score analysis

CRITICAL CORRECTION (30 July 2026 audit)
----------------------------------------
The previous version of this script hard-coded score = ∇log I and integrated
a Langevin dynamics. That was circular: it inserted the desired drift by hand
and never used actual Poisson counts. In addition the coefficient 1.2 produced
ρ ∝ I^{1.2}, not I, and correlation masked the bias.

The mathematically correct Poisson score for λ(x) = α I(x), k ~ Poisson(λ τ) is

    ∂x log p(k|x) = (k − λ) · (I'/I) = (k − λ) ∇log I

Averaged over the data, E[k] = λ, so the *mean* score is identically zero.
There is no net drift that climbs the intensity landscape from the average
detection model. The estimator does not spontaneously lock to high-I regions
via a score-driven force.

What remains solid (and is already in 1.2)
-----------------------------------------
If detection events are generated with rate ∝ I, the empirical density of
the *recorded event locations* is ∝ I by the law of large numbers. That is
pure counting. It does not require a dynamical score drift.

This corrected script therefore demonstrates only the honest facts:
1. Sample Poisson events from λ ∝ I and show the histogram of locations ∝ I.
2. Explicitly verify that the sample-mean score is consistent with zero.
3. Show a single Bayesian posterior update (likelihood ∝ I) concentrates, but
   that is still the counting/likelihood statement, not a continuous score
   dynamics of a particle.

Ontology implication (unchanged in substance)
---------------------------------------------
Combined with the negative mechanical result (1.3), the single-particle
equilibrium sector is about measurement records. The supporting argument is
the counting statement of 1.2, not an independent non-circular score derivation.

Run: python 08_bayesian_score_forced_likelihood.py
"""

import numpy as np
from pathlib import Path

def I(x):
    """Sample double-peak intensity (classical interference envelope)."""
    return 0.10 + 0.95 * (
        np.exp(-((x + 1.25)**2) / (2 * 0.32**2))
        + np.exp(-((x - 1.25)**2) / (2 * 0.32**2))
    )

def main():
    print("RTT Phase 1.4 (corrected) — Honest Poisson counting + score analysis")
    print("=" * 70)
    print("Correction: previous version hard-coded ∇log I. That was circular.")
    print("Real Poisson score = (k − λ) ∇log I; mean score ≡ 0.")
    print()

    rng = np.random.default_rng(42)
    x_grid = np.linspace(-3.5, 3.5, 400)
    Ix = I(x_grid)
    Ix_norm = Ix / np.trapezoid(Ix, x_grid)

    # 1. Generate detection events with rate ∝ I (inhomogeneous Poisson / thinning)
    #    Rejection sampling / discrete approximation on the grid
    n_events = 5000
    # Probability mass proportional to I
    probs = Ix / Ix.sum()
    event_idx = rng.choice(len(x_grid), size=n_events, p=probs)
    event_x = x_grid[event_idx]

    hist, edges = np.histogram(event_x, bins=40, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_c = I(centers)
    I_c_norm = I_c / np.trapezoid(I_c, centers)
    # Prefer L1 distance
    L1 = np.trapezoid(np.abs(hist - I_c_norm), centers)
    corr = np.corrcoef(hist, I_c_norm)[0, 1]
    print(f"1. Recorded event locations (rate ∝ I):")
    print(f"   L1 distance to normalized I: {L1:.4f}")
    print(f"   Correlation (for reference only): {corr:.3f}")
    print("   → Empirical density of detections ∝ I by construction / LLN.")
    print("   This is exactly the content of Phase 1.2 (counting).")
    print()

    # 2. Empirical mean score
    # For each event we can evaluate a realization of the score, but the
    # population mean is analytically zero. We demonstrate consistency.
    alpha_tau = 2.0  # arbitrary scale
    # Approximate local λ and sample k near each grid point for illustration
    mean_scores = []
    for _ in range(200):
        # Sample a location from the intensity, then a count, then the score
        idx = rng.choice(len(x_grid), p=probs)
        lam = alpha_tau * Ix[idx]
        k = rng.poisson(lam)
        # Numerical gradient of log I
        dlogI = np.gradient(np.log(Ix + 1e-12), x_grid)[idx]
        score = (k - lam) * dlogI
        mean_scores.append(score)
    mean_score_est = np.mean(mean_scores)
    print(f"2. Sample mean of Poisson score (k−λ)∇log I:")
    print(f"   Estimated mean score ≈ {mean_score_est:.4f}  (should be ~0)")
    print("   Analytic mean score is exactly zero. No net drift up the intensity.")
    print()

    # 3. Single Bayesian update (likelihood ∝ I) — still counting, not dynamics
    prior = np.ones_like(x_grid)
    prior /= np.trapezoid(prior, x_grid)
    # One observation with likelihood proportional to I (high-count or intensity measurement)
    like = Ix
    post = prior * like
    post /= np.trapezoid(post, x_grid)
    print("3. Single Bayesian posterior update with likelihood ∝ I:")
    print("   Posterior concentrates on high-I regions. This is the likelihood")
    print("   statement (again counting / rate model), not a continuous score")
    print("   dynamics that would produce a net force from mean-zero scores.")
    print()

    print("Honest status after correction:")
    print("  • The intensity → rate relation is ordinary detector physics.")
    print("  • Rate ∝ I ⇒ recorded event density ∝ I (Phase 1.2, by construction).")
    print("  • The Poisson score has mean zero; there is no net score-driven climb.")
    print("  • Combined with the negative mechanical result (1.3), the single-particle")
    print("    equilibrium sector is about measurement records via counting.")
    print("  • 1.4 does not supply an independent non-circular derivation of a")
    print("    dynamical ∇log I structure. It collapses back to 1.2.")

if __name__ == "__main__":
    main()
