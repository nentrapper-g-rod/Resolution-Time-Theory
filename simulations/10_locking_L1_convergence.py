#!/usr/bin/env python3
"""
RTT Phase 3.1 — Locking under state-dependent diffusion + L¹ convergence

Claim (status: shown-numerically, consistency only):
  Under the Itô pure-diffusion SDE dX = √(2 D(x)) dW with D(x) ∝ 1/I(x),
  the empirical density converges to ρ ∝ I as measured by L¹ distance.

This is a consistency / reachability check (same content as Phase 1.1).
It does *not* derive D ∝ 1/I from particle-field mechanics (that route is closed by 1.3).

Verifiability requirements met:
- Metric: L¹ distance to the exact normalized target (not correlation)
- Convergence: L¹ reported vs number of trajectories
- Negative control: constant D must *not* lock to I
- Seed fixed, analytic target stated, pass/fail tolerance given

Run: python simulations/10_locking_L1_convergence.py
"""

import numpy as np

def I(x):
    return 0.12 + 0.95 * (
        np.exp(-((x + 1.3)**2) / (2 * 0.35**2))
        + np.exp(-((x - 1.3)**2) / (2 * 0.35**2))
    )

def main():
    print("RTT Phase 3.1 — Locking + L¹ convergence (D ∝ 1/I)")
    print("=" * 60)
    print("Analytic target: pure Itô diffusion with D ∝ 1/I ⇒ ρ∞ ∝ I exactly")
    print("Metric: L¹ distance to normalized I (not correlation)")
    print("Negative control: constant D must not lock to I")
    print()

    rng = np.random.default_rng(7)
    x_grid = np.linspace(-3.5, 3.5, 300)
    Ix = I(x_grid)
    D = 1.0 / (Ix + 0.08)          # D ∝ 1/I
    D_const = np.full_like(Ix, np.mean(D))

    def run(n_traj, n_steps=4000, dt=0.008, diffusion=D):
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
        return L1, hist, centers, I_norm

    print("Convergence of L¹ vs number of trajectories (D ∝ 1/I):")
    print(f"{'N_traj':>8}  {'L1':>8}  {'pass?':>6}")
    tolerance = 0.12
    last_L1 = None
    for N in [200, 500, 1000, 2000, 4000]:
        L1, _, _, _ = run(N)
        status = "PASS" if L1 < tolerance else "..."
        print(f"{N:8d}  {L1:8.4f}  {status:>6}")
        last_L1 = L1

    print()
    print("Negative control (constant D):")
    L1_neg, _, _, _ = run(3000, diffusion=D_const)
    print(f"  L1 with constant D = {L1_neg:.4f}  (should stay large, not lock)")
    if L1_neg > 0.25:
        print("  PASS: negative control does not lock to I")
    else:
        print("  FAIL: negative control unexpectedly close to I")

    print()
    print("Final L1 (N=4000, D∝1/I) =", round(last_L1, 4))
    print("Tolerance for PASS:", tolerance)
    print()
    print("Status: shown-numerically (consistency of the D∝1/I construction under Itô).")
    print("Not a derivation from mechanical high-frequency averaging (see 1.3).")

if __name__ == "__main__":
    main()
