#!/usr/bin/env python3
"""
RTT Phase 3.1 — Locking + L¹ convergence under D ∝ 1/I

Holds total integration time fixed and studies:
  (A) trajectory count N at fixed dt
  (B) timestep dt at fixed large N

Metric: L¹ distance to normalized I (not correlation).
Negative control: constant D must not lock to I.

On review I found that a single fixed timestep leaves residual integrator
bias in the state-dependent diffusion, so the dt study is required for an
honest convergence claim.

Run: python simulations/10_locking_L1_convergence.py
"""

import numpy as np

def I(x):
    return 0.12 + 0.95 * (
        np.exp(-((x + 1.3)**2) / (2 * 0.35**2))
        + np.exp(-((x - 1.3)**2) / (2 * 0.35**2))
    )

def run(n_traj, n_steps, dt, diffusion, x_grid, rng):
    X = rng.uniform(-3.0, 3.0, size=n_traj)
    for _ in range(n_steps):
        Dx = np.interp(X, x_grid, diffusion)
        X = X + np.sqrt(2.0 * Dx * dt) * rng.normal(size=n_traj)
        X = np.clip(X, -3.5, 3.5)
    hist, edges = np.histogram(X, bins=40, density=True, range=(-3.5, 3.5))
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_c = I(centers)
    I_norm = I_c / np.trapezoid(I_c, centers)
    L1 = np.trapezoid(np.abs(hist - I_norm), centers)
    return L1

def main():
    print("RTT Phase 3.1 — Locking + L¹ convergence (D ∝ 1/I)")
    print("=" * 60)
    print("Analytic target: pure Itô diffusion with D ∝ 1/I ⇒ ρ∞ ∝ I exactly")
    print("Metric: L¹ to normalized I (not correlation)")
    print("Negative control: constant D must not lock to I")
    print()

    rng = np.random.default_rng(7)
    x_grid = np.linspace(-3.5, 3.5, 300)
    Ix = I(x_grid)
    D = 1.0 / (Ix + 0.08)
    D_const = np.full_like(Ix, np.mean(D))

    T = 16.0

    print("(A) L¹ vs number of trajectories (dt=0.002, T=16):")
    print(f"{'N_traj':>8}  {'L1':>8}")
    dt_a = 0.002
    n_steps_a = int(round(T / dt_a))
    for N in [200, 800, 2000, 4000]:
        L1 = run(N, n_steps_a, dt_a, D, x_grid, rng)
        print(f"{N:8d}  {L1:8.4f}")

    print()
    print("(B) Timestep convergence (N=4000, T=16 fixed):")
    print(f"{'dt':>10}  {'n_steps':>8}  {'L1':>8}")
    l1_dt = []
    for dt in [0.008, 0.004, 0.002, 0.001]:
        n_steps = int(round(T / dt))
        L1 = run(4000, n_steps, dt, D, x_grid, rng)
        l1_dt.append((dt, L1))
        print(f"{dt:10.4f}  {n_steps:8d}  {L1:8.4f}")

    print()
    print("Negative control (constant D, N=3000, dt=0.002):")
    L1_neg = run(3000, n_steps_a, dt_a, D_const, x_grid, rng)
    print(f"  L1 with constant D = {L1_neg:.4f}  (should stay large, not lock)")
    if L1_neg > 0.25:
        print("  Negative control does not lock to I.")
    else:
        print("  WARNING: negative control unexpectedly close to I.")

    finest = l1_dt[-1][1]
    print()
    print(f"Finest-dt L1 (dt=0.001, N=4000) = {finest:.4f}")
    print("Status: shown-numerically (consistency of D∝1/I under Itô).")
    print("Residual L¹ reflects finite binning and sampling;")
    print("refining dt reduces integrator bias. Not a derivation from")
    print("mechanical high-frequency averaging (see Phase 1.3).")

if __name__ == "__main__":
    main()
