#!/usr/bin/env python3
"""
RTT Phase 1.2 — Rate and counting models that yield ρ ∝ I

Honest demonstration: when the detection intensity or the transition rates
scale with local intensity I, the recorded / stationary density tracks I
by construction (law of large numbers for inhomogeneous Poisson, or
detailed balance / rate construction for a continuous-time Markov chain).

These models live on the measurement / under-sampling side of RTT.
They do NOT yet derive the intensity-dependence from the high-frequency
classical particle-field mechanics. That remains open problem #1.

Run: python 06_rate_and_counting_models.py
Requires: numpy, scipy
"""

import numpy as np
from scipy.linalg import null_space

def poisson_counting_demo(n_bins=80, n_events=50000, seed=42):
    """Inhomogeneous Poisson: event rate density ∝ I(x) → empirical density ∝ I."""
    np.random.seed(seed)
    x = np.linspace(-5, 5, n_bins)
    I = np.exp(-((x - 1.5)**2) / 0.5) + np.exp(-((x + 1.5)**2) / 0.5) + 0.05
    I = I / I.sum()
    events = np.random.choice(x, size=n_events, p=I)
    hist, edges = np.histogram(events, bins=n_bins, density=True, range=(-5, 5))
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_cont = np.exp(-((centers - 1.5)**2) / 0.5) + np.exp(-((centers + 1.5)**2) / 0.5) + 0.05
    I_cont = I_cont / np.trapezoid(I_cont, centers)
    corr = np.corrcoef(hist, I_cont)[0, 1]
    L1 = np.trapezoid(np.abs(hist - I_cont), centers)
    return centers, hist, I_cont, corr, L1

def lattice_rate_demo(n=50):
    """CTMC lattice: rate i	o j ∝ I[j] (target intensity). Stationary exactly ∝ I."""
    x = np.linspace(-5, 5, n)
    I = np.exp(-((x - 1.5)**2) / 0.5) + np.exp(-((x + 1.5)**2) / 0.5) + 0.05
    I_norm = I / I.sum()
    Gamma = 1.0
    W = np.zeros((n, n))
    for i in range(n):
        for j in [i - 1, i + 1]:
            if 0 <= j < n:
                W[j, i] = Gamma * I[j]  # rate from i to j proportional to target I
        W[i, i] = -np.sum(W[:, i])
    ns = null_space(W)
    rho = np.abs(ns[:, 0].real)
    rho = rho / rho.sum()
    corr = np.corrcoef(rho, I_norm)[0, 1]
    L1 = np.sum(np.abs(rho - I_norm))
    return x, I_norm, rho, corr, L1

if __name__ == "__main__":
    print("=== Poisson counting process (detection rate ∝ I) ===")
    c, h, Ic, corr_p, L1_p = poisson_counting_demo()
    print(f"Correlation: {corr_p:.4f}")
    print(f"L1 distance: {L1_p:.4f}")

    print("\n=== Lattice CTMC with target-proportional rates ===")
    x, In, r, corr_l, L1_l = lattice_rate_demo()
    print(f"Correlation: {corr_l:.6f}")
    print(f"L1 distance: {L1_l:.2e}")

    print("\nBoth constructions produce ρ ∝ I by design once intensity enters the rates/detection measure.")
    print("See docs/NOTES_ON_EQUILIBRIUM_ROUTES.md for interpretation and remaining gaps.")
