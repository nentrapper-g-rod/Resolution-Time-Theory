#!/usr/bin/env python3
"""
RTT Phase 1.1 — State-dependent diffusion route to Born-like equilibrium
=======================================================================
Zero-drift Itô process with D(x) ∝ 1/I(x) has exact stationary density ρ∞ ∝ I
by the Fokker–Planck theorem.

Motivation (detection / resolution side):
  Higher local intensity → more detection events inside a finite gate window
  → tighter localization of the inferred position → smaller effective diffusion
  of the recorded trajectory. This lives on the measurement side, consistent
  with the under-sampling / resolution-time framing of RTT.

This is NOT yet a derivation from the underlying high-frequency field dynamics.
It is an alternative, mathematically exact route to ρ ∝ I that may be easier
to motivate from detector statistics than a mechanical log-potential.

Run:
  python 05_state_dependent_diffusion_equilibrium.py

Requires: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

def intensity(x):
    """Simple 1-D interference-like intensity (periodic)."""
    return 0.2 + 0.8 * np.sin(2 * np.pi * x)**2

def simulate(n_particles=800, n_steps=30000, dt=0.0008, eps=0.05, seed=42):
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.0, 1.0, n_particles)
    for _ in range(n_steps):
        I = intensity(x)
        D = 1.0 / (I + eps)
        sigma = np.sqrt(2.0 * D * dt)
        x = x + sigma * rng.standard_normal(n_particles)
        x = np.mod(x, 1.0)
    return x

def main():
    print("RTT 05 — D ∝ 1/I equilibrium demonstration")
    print("=" * 50)
    positions = simulate()
    bins = np.linspace(0, 1, 61)
    hist, edges = np.histogram(positions, bins=bins, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_centers = intensity(centers)
    # Normalize I to density scale for visual comparison
    I_norm = I_centers / np.trapz(I_centers, centers)

    # Correlation as a simple quantitative check
    corr = np.corrcoef(hist, I_norm)[0, 1]
    print(f"Correlation (histogram vs normalized I): {corr:.4f}")
    print(f"Particles: {len(positions)}, steps: 30000")

    # Optional plot
    try:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(centers, hist, width=edges[1]-edges[0], alpha=0.6, label="Monte-Carlo density")
        ax.plot(centers, I_norm, "r-", lw=2, label="normalized I(x)")
        ax.set_xlabel("x")
        ax.set_ylabel("density")
        ax.set_title("Zero-drift + D ∝ 1/I  →  ρ∞ ∝ I")
        ax.legend()
        ax.set_xlim(0, 1)
        fig.tight_layout()
        fig.savefig("05_D_inv_I_equilibrium.png", dpi=150)
        print("Saved plot: 05_D_inv_I_equilibrium.png")
        plt.close()
    except Exception as e:
        print("Plot skipped:", e)

    print("Done. Exact stationary result follows from Fokker–Planck;")
    print("numerics are a consistency check only.")

if __name__ == "__main__":
    main()
