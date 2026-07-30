#!/usr/bin/env python3
"""
RTT Phase 1.2 — Lattice master-equation and counting-process routes to ρ ∝ I
==============================================================================
1. Continuous-time Markov chain on a 1-D lattice.
   Transition rates into a site proportional to the local intensity I of the
   *target* site. This satisfies detailed balance with π ∝ I, so the unique
   stationary distribution is exactly proportional to I.

2. Pure inhomogeneous Poisson counting process: detections occur with rate
   density ∝ I(x). The empirical density of recorded events tracks I by the
   law of large numbers.

Motivation (detection / under-sampling):
  A finite-resolution detector registers events at a rate that tracks the local
  classical intensity. Modelling the recorded positions via intensity-dependent
  arrival rates or as a Poisson process therefore produces ρ ∝ I on the
  measurement side.

Honest limitation: by construction of the rates / intensity measure. The
physical derivation of why the microscopic rates should take this form from
the particle + high-frequency field dynamics remains open.

Run:
  python 06_lattice_master_equation_equilibrium.py

Requires: numpy, scipy, matplotlib
"""

import numpy as np
from scipy.linalg import null_space
import matplotlib.pyplot as plt

def main():
    print("RTT 06 — Lattice master equation + Poisson counting")
    print("=" * 60)
    N = 60
    x = np.linspace(0.0, 1.0, N, endpoint=False)
    I = 0.15 + 0.85 * np.sin(2 * np.pi * x)**2

    # Rate matrix W[j, i] = rate from i to j
    W = np.zeros((N, N))
    Gamma = 1.0
    for i in range(N):
        for dj in (-1, 1):
            j = (i + dj) % N
            W[j, i] = Gamma * I[j]
        W[i, i] = -np.sum(W[:, i])

    ns = null_space(W)
    pi = np.abs(ns[:, 0].real)
    pi /= pi.sum()
    I_norm = I / I.sum()

    corr = np.corrcoef(pi, I_norm)[0, 1]
    L1 = np.sum(np.abs(pi - I_norm))
    print(f"Lattice size N = {N}")
    print(f"Correlation (π vs normalized I): {corr:.6f}")
    print(f"L1 distance: {L1:.2e}")

    # Pure counting illustration (Poisson)
    n_events = 30000
    probs = I / I.sum()
    samples = np.random.choice(N, size=n_events, p=probs)
    hist, _ = np.histogram(samples, bins=np.arange(N+1), density=True)
    corr_poiss = np.corrcoef(hist, I_norm)[0, 1]
    print(f"Pure Poisson counting (n={n_events}) correlation: {corr_poiss:.4f}")

    try:
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        axes[0].plot(x, I_norm, "r-", lw=2, label="normalized I")
        axes[0].bar(x, pi, width=1.0/N, alpha=0.5, label="stationary π")
        axes[0].set_title("Master-equation stationary")
        axes[0].legend()
        axes[0].set_xlabel("x")

        axes[1].plot(x, I_norm, "r-", lw=2, label="normalized I")
        axes[1].bar(x, hist, width=1.0/N, alpha=0.5, label="Poisson samples")
        axes[1].set_title("Pure counting process")
        axes[1].legend()
        axes[1].set_xlabel("x")

        fig.tight_layout()
        fig.savefig("06_lattice_master_eq.png", dpi=150)
        print("Saved plot: 06_lattice_master_eq.png")
        plt.close()
    except Exception as e:
        print("Plot skipped:", e)

    print("Done. Stationary is exact by detailed balance construction.")

if __name__ == "__main__":
    main()
