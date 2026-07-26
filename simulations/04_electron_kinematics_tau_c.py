#!/usr/bin/env python3
"""
RTT Core Edition — Geometric tau_c from electron interferometer kinematics
==========================================================================
tau_c ~ Delta L / v
tau_phi ~ hbar / delta E

Run:  python 04_electron_kinematics_tau_c.py
"""

import numpy as np

hbar = 1.0545718e-34
h = 2 * np.pi * hbar
m_e = 9.109e-31
e = 1.602e-19


def electron_velocity(E_eV):
    return np.sqrt(2 * E_eV * e / m_e)


def main():
    print("Electron speed and de Broglie wavelength")
    print("-" * 50)
    for E in [50, 100, 200, 1000]:
        v = electron_velocity(E)
        lam_nm = h / (m_e * v) * 1e9
        print(f"  E={E:4d} eV   v={v:.3e} m/s   lambda={lam_nm:.3f} nm")

    print("\nGeometric resolution time  tau_c = Delta L / v")
    print("-" * 50)
    for E in [100, 200]:
        v = electron_velocity(E)
        for dL_um in [0.1, 0.5, 1.0, 2.0, 10.0]:
            dt_fs = (dL_um * 1e-6) / v * 1e15
            print(f"  E={E} eV  DeltaL={dL_um:4.1f} um  →  tau_c={dt_fs:8.1f} fs")

    print("\nQM phase time  tau_phi = hbar / delta E")
    print("-" * 50)
    for dE in [0.05, 0.1, 0.2, 0.5, 1.0]:
        tau_fs = hbar / (dE * e) * 1e15
        print(f"  deltaE={dE:.2f} eV  →  tau_phi={tau_fs:.2f} fs")

    print("\nExample comparison (E=100 eV, DeltaL=1 um, deltaE=0.2 eV)")
    v = electron_velocity(100)
    tau_c = 1e-6 / v * 1e15
    tau_phi = hbar / (0.2 * e) * 1e15
    print(f"  tau_c   ≈ {tau_c:.1f} fs")
    print(f"  tau_phi ≈ {tau_phi:.1f} fs")
    print(f"  ratio   ≈ {tau_c/tau_phi:.1f}")


if __name__ == "__main__":
    main()
