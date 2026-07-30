#!/usr/bin/env python3
"""
RTT Phase 2.1 — Explicit visibility kernels
Geometric τ_c ∼ ΔL / v  vs  quantum phase / coherence time τ_φ ∼ ℏ / δE

Purpose: produce concrete, reproducible numbers and functional forms for the
pulsed-gate visibility comparison proposed in Core Edition 4.0.

Models (kept simple and transparent):
- Geometric kernel: TOF difference δt = ΔL / v. For a rectangular gate of
  width τ_g the contrast reduction for a pure time-delay is |sinc(δt / τ_g)|
  (Fourier transform of the gate). This is pure kinematics.
- Phase kernel: energy bandwidth δE defines τ_φ = ℏ / δE. A simple Gaussian
  decay of visibility with gate width relative to τ_φ is used as a
  representative QM temporal-coherence model. (Real beams have more
  complicated longitudinal wave-packets; this is a baseline.)

Honest limits: these are phenomenological kernels, not a full 3-D
wave-packet + detector simulation. They illustrate where the geometric and
phase timescales separate and therefore where a gated experiment could
discriminate.

Run: python 09_visibility_kernels.py
"""

import numpy as np

hbar = 1.0545718e-34
h = 2 * np.pi * hbar
m_e = 9.109e-31
e = 1.602e-19

def electron_velocity(E_eV):
    return np.sqrt(2 * E_eV * e / m_e)

def de_broglie_nm(E_eV):
    v = electron_velocity(E_eV)
    return h / (m_e * v) * 1e9

def tau_c_fs(DeltaL_um, E_eV):
    v = electron_velocity(E_eV)
    return (DeltaL_um * 1e-6) / v * 1e15

def tau_phi_fs(deltaE_eV):
    return hbar / (deltaE_eV * e) * 1e15

def visibility_geometric(delta_t, tau_g):
    """|sinc(δt / τ_g)| for rectangular gate (np.sinc = sin(πx)/(πx))."""
    x = np.asarray(delta_t) / np.asarray(tau_g)
    return np.abs(np.sinc(x))

def visibility_phase_gaussian(tau_g, tau_phi):
    """Simple Gaussian model of temporal coherence decay."""
    return np.exp(-0.5 * (np.asarray(tau_g) / np.asarray(tau_phi))**2)

if __name__ == "__main__":
    print("RTT Phase 2.1 — Visibility kernels")
    print("=" * 60)
    print("Electron parameters")
    for E in [50, 100, 200]:
        v = electron_velocity(E)
        lam = de_broglie_nm(E)
        print(f"  E = {E:3d} eV   v = {v:.3e} m/s   λ = {lam:.3f} nm")

    print("\nGeometric τ_c = ΔL / v  (fs)")
    print("-" * 40)
    DeltaLs = [0.1, 0.5, 1.0, 2.0, 5.0]
    print(f"{'ΔL (μm)':>8}", end="")
    for E in [50, 100, 200]:
        print(f"  E={E}eV", end="")
    print()
    for dL in DeltaLs:
        print(f"{dL:8.1f}", end="")
        for E in [50, 100, 200]:
            print(f"  {tau_c_fs(dL, E):7.1f}", end="")
        print()

    print("\nPhase τ_φ = ℏ / δE  (fs)")
    print("-" * 40)
    for dE in [0.05, 0.1, 0.2, 0.5, 1.0]:
        print(f"  δE = {dE:.2f} eV  →  τ_φ = {tau_phi_fs(dE):.2f} fs")

    print("\nExample visibility comparison (E=100 eV, ΔL=1 μm → δt≈169 fs)")
    print("-" * 60)
    delta_t = tau_c_fs(1.0, 100) * 1e-15
    tau_phi = tau_phi_fs(0.2) * 1e-15   # representative 0.2 eV bandwidth
    print(f"{'τ_g (fs)':>10}  {'V_geom':>8}  {'V_phase':>8}")
    for tg_fs in [10, 20, 50, 100, 169, 200, 500, 1000]:
        tg = tg_fs * 1e-15
        Vg = visibility_geometric(delta_t, tg)
        Vp = visibility_phase_gaussian(tg, tau_phi)
        print(f"{tg_fs:10.0f}  {Vg:8.3f}  {Vp:8.3f}")

    print("\nNotes:")
    print("  - Geometric kernel depends only on apparatus ΔL and beam velocity.")
    print("  - Phase kernel depends on energy bandwidth of the beam.")
    print("  - Where the two curves separate, a gated measurement can in principle")
    print("    discriminate. Full wave-packet + detector Monte-Carlo is future work.")
    print("  - Competing effects (Coulomb, residual gas, detector jitter) must be")
    print("    controlled; see Phase 2.3 literature notes.")
