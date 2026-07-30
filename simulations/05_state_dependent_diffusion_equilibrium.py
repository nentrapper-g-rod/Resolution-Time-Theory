#!/usr/bin/env python3
"""
RTT Phase 1.1 — State-dependent diffusion route to Born-like equilibrium
Zero-drift Itô process with D(x) ∝ 1/I(x) has exact stationary density ρ∞ ∝ I.
Consistency / reachability check only — not a derivation from field mechanics.
Run: python 05_state_dependent_diffusion_equilibrium.py
"""

import numpy as np
import matplotlib.pyplot as plt

def intensity(x):
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
    I_norm = I_centers / np.trapezoid(I_centers, centers)
    corr = np.corrcoef(hist, I_norm)[0, 1]
    L1 = np.trapezoid(np.abs(hist - I_norm), centers)
    print(f"Correlation (histogram vs normalized I): {corr:.4f}")
    print(f"L1 distance to normalized I: {L1:.4f}")
    print(f"Particles: {len(positions)}, steps: 30000")
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
