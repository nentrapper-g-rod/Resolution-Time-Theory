#!/usr/bin/env python3
"""
RTT Phase 3.1 — Locking under D ∝ 1/I with L¹ convergence
=========================================================
Status: shown-numerically (consistency / reachability only)

Claim
-----
For the pure-diffusion Itô process
    dX = √(2 D(x)) dW ,   D(x) = 1 / (I(x) + ε)
the stationary density is ρ∞ ∝ 1/D ∝ I (exactly, by Fokker–Planck).
This script demonstrates numerical locking measured by L¹ distance to the
normalized target I, shows improvement with more trajectories, and includes
a negative control (constant D) that must *not* lock to I.

This is a consistency check of the postulated structure, not a derivation
from high-frequency particle mechanics (see Phase 1.3 negative result).
Under the current ontology it is best read as dynamics of a recorded /
estimated position under intensity-dependent resolution.

Metric: L¹ distance (preferred). Correlation is reported only for reference
and is not used for pass/fail (it is blind to power-law distortion).

Run: python simulations/10_locking_L1_convergence.py
"""

import numpy as np

def I(x):
    return 0.12 + 0.92 * (
        np.exp(-((x + 1.3)**2) / (2 * 0.38**2))
        + np.exp(-((x - 1.3)**2) / (2 * 0.38**2))
    )

def run_ensemble(n_traj, n_steps, dt, D_func, seed):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-3.2, 3.2, size=n_traj)
    for _ in range(n_steps):
        D = D_func(x)
        x = x + np.sqrt(2.0 * D * dt) * rng.normal(size=n_traj)
        x = np.clip(x, -3.5, 3.5)
    return x

def L1_to_I(samples):
    hist, edges = np.histogram(samples, bins=50, density=True, range=(-3.5, 3.5))
    centers = 0.5 * (edges[:-1] + edges[1:])
    Ic = I(centers)
    Inorm = Ic / np.trapezoid(Ic, centers)
    L1 = np.trapezoid(np.abs(hist - Inorm), centers)
    corr = np.corrcoef(hist, Inorm)[0, 1]
    return L1, corr

def main():
    print("RTT Phase 3.1 — D ∝ 1/I locking with L¹ convergence")
    print("=" * 60)
    print("Analytic target: ρ∞ ∝ I  (exact for Itô pure-diffusion with D ∝ 1/I)")
    print("Metric: L¹ distance to normalized I (pass if L¹ decreases with N)")
    print()

    eps = 0.08
    def D_invI(x):
        return 1.0 / (I(x) + eps)

    def D_const(x):
        return np.full_like(x, 0.8)

    dt = 0.004
    n_steps = 12000

    print("Convergence study (D ∝ 1/I):")
    print(f"{'N_traj':>8}  {'L¹':>8}  {'corr (ref)':>10}")
    results = []
    for n_traj in [100, 300, 800, 2000]:
        samples = run_ensemble(n_traj, n_steps, dt, D_invI, seed=42 + n_traj)
        L1, corr = L1_to_I(samples)
        results.append((n_traj, L1, corr))
        print(f"{n_traj:8d}  {L1:8.4f}  {corr:10.3f}")

    # Negative control
    print()
    print("Negative control (constant D — must NOT lock to I):")
    samples_neg = run_ensemble(1500, n_steps, dt, D_const, seed=99)
    L1_neg, corr_neg = L1_to_I(samples_neg)
    print(f"  L¹ = {L1_neg:.4f}   corr = {corr_neg:.3f}")
    print("  (Expect L¹ larger / no systematic locking to the peaks of I)")

    # Simple pass criterion: L¹ decreases with N and final L¹ < negative-control L¹
    L1s = [r[1] for r in results]
    improving = all(L1s[i] >= L1s[i+1] - 0.02 for i in range(len(L1s)-1))  # allow small noise
    better_than_neg = L1s[-1] < L1_neg - 0.05
    print()
    if improving and better_than_neg:
        print("PASS: L¹ improves with N and is clearly better than constant-D control.")
    else:
        print("FAIL or marginal: check parameters / run longer.")
    print()
    print("Status: shown-numerically (consistency of D∝1/I → ρ∝I).")
    print("Not a derivation from mechanical high-frequency dynamics (see 1.3).")

if __name__ == "__main__":
    main()
