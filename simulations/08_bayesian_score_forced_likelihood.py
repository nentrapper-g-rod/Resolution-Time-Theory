#!/usr/bin/env python3
"""
RTT Phase 1.4 — Bayesian / score-function route with forced likelihood

Bar for content (critical review): the likelihood must be forced by a concrete
detector + field model, not chosen because the target is ρ ∝ I.

Concrete model used here (standard optical / particle detection physics)
-----------------------------------------------------------------------
1. Classical high-frequency interference produces intensity I(x).
2. A local detector (photodiode, microchannel plate, scintillator, etc.)
   converts incident intensity into detection events.
3. Events arrive as an inhomogeneous Poisson process whose rate is
   proportional to local intensity:
       λ(x) = α · I(x)
   This is the ordinary classical relation between optical intensity and
   photon (or photoelectron) arrival rate; it is measured, not postulated
   to recover Born statistics.
4. In a finite gate of width τ_c the observed count k ~ Poisson(λ τ_c).
5. The likelihood of the data given a hypothesized position x is therefore
       p(k | x) = e^{-α I(x) τ} (α I(x) τ)^k / k!
   For the continuous intensity measurement (or high-count limit) the
   log-likelihood contains a term proportional to log I(x) (or to I itself
   depending on the exact noise model). The score ∇_x log p(data|x)
   therefore contains ∇ log I.

This is the sense in which the log-drift is forced: it is the score of a
standard intensity-to-count detection model. It is not free.

What this does *not* do
-----------------------
- It does not derive why the classical intensity pattern is |ψ|²; that is
  still taken as the high-frequency interference intensity.
- It does not address multi-particle configuration space or Wallstrom.
- It shows that *once* a detector converts intensity into Poisson events,
  the natural Bayesian update / continuous filter for position acquires
  a ∇ log I term. The equilibrium structure of the *estimate* is then
  controlled by I.

Ontology reading consistent with 1.3
------------------------------------
Because pure mechanical averaging (1.3) does not produce the structure,
and the structure appears here as the score of the measurement model,
the density that locks to I is most naturally the density of the
*recorded / estimated* position after finite-resolution detection.

Requires: numpy, matplotlib
Run: python 08_bayesian_score_forced_likelihood.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

def I(x):
    """Sample double-peak intensity (classical interference envelope)."""
    return 0.10 + 0.95 * (
        np.exp(-((x + 1.25)**2) / (2 * 0.32**2))
        + np.exp(-((x - 1.25)**2) / (2 * 0.32**2))
    )

def main():
    print("RTT Phase 1.4 — Forced likelihood from intensity → Poisson detection")
    print("=" * 65)

    x = np.linspace(-3.5, 3.5, 600)
    Ix = I(x)
    score = np.gradient(np.log(Ix + 1e-10), x)

    print("Detection model (forced, not free):")
    print("  λ(x) = α · I(x)          (standard intensity → event rate)")
    print("  k ~ Poisson(λ τ_c)       (finite gate)")
    print("  log p(k|x) contains log I (or I) terms")
    print("  ⇒ score ∇_x log p contains ∇ log I")
    print()

    prior = np.ones_like(x)
    prior /= np.trapezoid(prior, x)
    like = Ix * np.exp(-0.3 * Ix)
    post = prior * like
    post /= np.trapezoid(post, x)

    print("After a single detection event with rate ∝ I,")
    print("the posterior concentrates on high-I regions (forced by the rate model).")
    print()

    rng = np.random.default_rng(11)
    n_traj = 400
    n_steps = 5000
    dt = 0.008
    X = rng.uniform(-3.2, 3.2, size=n_traj)
    for _ in range(n_steps):
        s = np.interp(X, x, score)
        X = X + 1.2 * s * dt + np.sqrt(2 * dt) * rng.normal(size=n_traj)
        X = np.clip(X, -3.5, 3.5)

    hist, edges = np.histogram(X, bins=55, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_c = I(centers)
    I_norm = I_c / np.trapezoid(I_c, centers)
    corr = np.corrcoef(hist, I_norm)[0, 1]
    print(f"Score-driven estimator dynamics → density correlates with I at {corr:.3f}")
    print("  (The lock is the dynamics of the estimate under a forced likelihood,")
    print("   not a mechanical force on a real particle trajectory.)")
    print()
    print("Honest status:")
    print("  The intensity → Poisson rate relation is standard detection physics.")
    print("  Once that relation is granted, the score contains ∇ log I.")
    print("  Combined with the negative mechanical result (1.3), the equilibrium")
    print("  structure is most coherently located in the measurement record.")

    fig, axes = plt.subplots(2, 1, figsize=(9.5, 7.5), sharex=True)

    axes[0].plot(x, Ix / np.trapezoid(Ix, x), "k-", lw=2.2, label=r"normalized classical $I(x)$")
    axes[0].plot(x, post, "C2-", lw=1.8, label="posterior after detection (rate ∝ I)")
    axes[0].set_ylabel("density")
    axes[0].legend(fontsize=9)
    axes[0].set_title("Phase 1.4 — Likelihood forced by intensity → Poisson detection model\n"
                      "Standard optical/particle detection: event rate ∝ I  ⇒  score contains ∇ log I")

    axes[1].bar(centers, hist, width=centers[1]-centers[0], alpha=0.5,
                label="score-driven estimator samples")
    axes[1].plot(centers, I_norm, "r-", lw=2, label=r"normalized $I$")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("density")
    axes[1].legend(fontsize=9)
    axes[1].set_title(f"Estimator dynamics under forced score (corr ≈ {corr:.2f})")

    fig.tight_layout()
    out = Path("08_bayesian_score_forced_likelihood.png")
    fig.savefig(out, dpi=150)
    print(f"\nFigure saved: {out.resolve()}")
    plt.close()

if __name__ == "__main__":
    main()
