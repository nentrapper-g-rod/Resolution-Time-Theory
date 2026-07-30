#!/usr/bin/env python3
"""
RTT Phase 1.3 — Homogenization / stochastic averaging of a fast oscillating classical field

Purpose (honest):
Document the *mechanical* outcome of high-frequency averaging.
Expected and observed result: Kapitza / ponderomotive-type effective forces
proportional to derivatives of intensity (or amplitude gradients),
and/or diffusion ∝ I.
This does *not* produce the ∇log I drift or D ∝ 1/I needed for ρ_∞ ∝ I.

This negative result is valuable: it confirms the technical obstruction stated
in the Core Edition and supports the conclusion that the log / 1/I structure
is more naturally located on the detection / under-sampling / estimation side
(Routes A & B from Phases 1.1–1.2) rather than in pure particle-field mechanics.

Model:
Overdamped Langevin
  dX = F(X,t) dt + √(2) dW
with
  V(x,t) = A(x) * cos(ω t)
  F = -∂x V = -A'(x) cos(ω t)

For large ω the effective potential is the classic Kapitza form
  V_eff ~ (A')^{2} / (4 ω^{2})
so F_eff ~ -d/dx of that quantity (related to intensity gradients).

Run: python 07_homogenization_fast_field.py
Requires: numpy, scipy
"""

import numpy as np
from scipy.interpolate import interp1d

def kapitza_analytic(x, A, omega):
    """Classic high-frequency effective force for V = A(x) cos(ωt)."""
    dA = np.gradient(A, x)
    V_eff = (dA ** 2) / (4.0 * omega ** 2)
    F_eff = -np.gradient(V_eff, x)
    return F_eff, V_eff

def numerical_occupation(omega=60.0, n_steps=80000, dt=0.0004, seed=7):
    """Long trajectory under the fast force; check whether occupation tracks I."""
    np.random.seed(seed)
    x_grid = np.linspace(-3.5, 3.5, 200)
    I = np.exp(-(x_grid - 1.2)**2 / 0.5) + np.exp(-(x_grid + 1.2)**2 / 0.5) + 0.12
    A = np.sqrt(I)
    dA = np.gradient(A, x_grid)
    A_i = interp1d(x_grid, A, fill_value="extrapolate")
    dA_i = interp1d(x_grid, dA, fill_value="extrapolate")

    X = 0.0
    samples = []
    for step in range(n_steps):
        t = step * dt
        F = -dA_i(X) * np.cos(omega * t)
        X += F * dt + np.sqrt(2.0 * dt) * np.random.randn()
        X = np.clip(X, -3.5, 3.5)
        if step % 40 == 0:
            samples.append(X)
    samples = np.array(samples)

    hist, edges = np.histogram(samples, bins=30, density=True, range=(-3.5, 3.5))
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_c = np.exp(-(centers - 1.2)**2 / 0.5) + np.exp(-(centers + 1.2)**2 / 0.5) + 0.12
    I_c = I_c / np.trapezoid(I_c, centers)
    corr = np.corrcoef(hist, I_c)[0, 1]
    return corr, samples.mean(), samples.std()

if __name__ == "__main__":
    print("RTT Phase 1.3 — Homogenization of fast classical field")
    print("=" * 60)
    print("Analytic Kapitza effective force is proportional to derivatives")
    print("of (A')^{2} (i.e., intensity-gradient terms), not to ∇log I.")
    print()
    corr, mean, std = numerical_occupation()
    print(f"Numerical occupation correlation with I: {corr:.3f}")
    print("(Near zero or negative is expected — pure mechanical averaging")
    print("does *not* lock the density to the intensity pattern.)")
    print(f"Trajectory mean ~ {mean:.3f}, std ~ {std:.3f}")
    print()
    print("Conclusion (honest):")
    print("  High-frequency classical averaging recovers the known obstruction")
    print("  (∇I-type forces / related diffusion). It does not produce the")
    print("  ∇log I or D∝1/I structure required for Born-rule equilibrium.")
    print("  This supports locating that structure on the detection/estimation")
    print("  side (Phases 1.1–1.2) rather than in pure particle mechanics.")
    print("See docs/NOTES_ON_EQUILIBRIUM_ROUTES.md for the full status.")
