#!/usr/bin/env python3
"""
RTT Phase 1.3 — Homogenization / stochastic averaging of a fast classical field
================================================================================
Overdamped Langevin dynamics in a rapidly oscillating potential

    V(x,t) = A(x) * cos(ω t)

with A(x) = sqrt(I(x)) (or similar), large ω, plus thermal noise.

Expected mechanical outcome (Kapitza / ponderomotive regime):
  The time-averaged force is *not* of the form ∇log I, and the long-time
  particle density does *not* lock to ρ ∝ I. Instead one recovers the classic
  high-frequency averaging results that produce the obstruction identified in
  the Core Edition (forces ~ ∇I or related derivatives, diffusion typically
  ∝ amplitude²).

This script demonstrates the negative result numerically: the long-time
histogram of particle positions has low (or negative) correlation with the
intensity profile I(x). The desired Born-like equilibrium is *not* generated
by pure mechanical under-sampling of the fast field.

This strengthens the case that any log or 1/I structure must live on the
detection / estimation / rate side of the theory rather than in the bare
particle + high-frequency field dynamics.

Run:
  python 07_homogenization_fast_field.py

Requires: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

def intensity(x):
    return 0.2 + 0.8 * np.sin(2 * np.pi * x)**2

def run_simulation(n_particles=400, n_steps=120000, dt=0.0004, omega=180.0, gamma=0.4, seed=7):
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.0, 1.0, n_particles)
    for step in range(n_steps):
        t = step * dt
        A = np.sqrt(intensity(x))
        # dA/dx for V = A cos(ωt) → F = - (dA/dx) cos(ωt)
        dA_dx = (0.8 * np.pi * np.sin(4 * np.pi * x)) / (A + 1e-8)
        F = -dA_dx * np.cos(omega * t)
        x = x + F * dt + np.sqrt(2 * gamma * dt) * rng.standard_normal(n_particles)
        x = np.mod(x, 1.0)
    return x

def main():
    print("RTT 07 — Homogenization of fast oscillating field (mechanical negative result)")
    print("=" * 70)
    positions = run_simulation()
    bins = np.linspace(0, 1, 51)
    hist, edges = np.histogram(positions, bins=bins, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    I = intensity(centers)
    I_norm = I / np.trapezoid(I, centers)
    corr = np.corrcoef(hist, I_norm)[0, 1]
    print(f"Particles: {len(positions)}")
    print(f"Long-time density vs normalized I correlation: {corr:.4f}")
    print("Expected: low or negative correlation (no locking to intensity peaks).")
    print("This is the classic obstruction: pure high-frequency mechanical averaging")
    print("does not produce ρ ∝ I.")

    try:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(centers, hist, width=edges[1]-edges[0], alpha=0.6, label="long-time particle density")
        ax.plot(centers, I_norm, "r-", lw=2, label="normalized I(x)")
        ax.set_xlabel("x")
        ax.set_ylabel("density")
        ax.set_title("Mechanical homogenization: density does NOT lock to I")
        ax.legend()
        ax.set_xlim(0, 1)
        fig.tight_layout()
        fig.savefig("07_homogenization_negative.png", dpi=150)
        print("Saved plot: 07_homogenization_negative.png")
        plt.close()
    except Exception as e:
        print("Plot skipped:", e)

    print("Done. Negative result documented.")

if __name__ == "__main__":
    main()
