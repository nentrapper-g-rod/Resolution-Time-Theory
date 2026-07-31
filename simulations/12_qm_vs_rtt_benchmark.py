#!/usr/bin/env python3
"""
N-12 — Scoped QM vs RTT gate-model benchmark

Premises (explicit):
  1. Single interferometer geometry (two arms, path difference ΔL).
  2. Intensity identified with the standard quantum intensity (imported I = |ψ|² envelope).
  3. Event rate λ ∝ I (ordinary counting).

Under these premises the gated visibility collapses to a function of the single
ratio r = τ_c / τ_φ only. The phenomenological sinc kernel is excluded by the
same premises at large r.

Scoped result — not a universal claim about every possible RTT model.

Run: python simulations/12_qm_vs_rtt_benchmark.py
"""
from __future__ import annotations

import numpy as np
from pathlib import Path

HBAR_EV_FS = 0.6582119569  # eV·fs
M_E = 9.1093837e-31
Q_E = 1.60217662e-19

E_EV = 100.0
DELTA_E_EV = 0.2
DELTA_L_M = 1.0e-6

FIG_DIR = Path(__file__).resolve().parent.parent / "paper" / "figures"


def kinematics():
    v = np.sqrt(2.0 * E_EV * Q_E / M_E)
    tau_c_fs = (DELTA_L_M / v) * 1e15
    tau_phi_fs = HBAR_EV_FS / DELTA_E_EV
    r = tau_c_fs / tau_phi_fs
    return v, tau_c_fs, tau_phi_fs, r


def stationary_baseband(n: int, dt: float, delta_e: float, rng: np.random.Generator) -> np.ndarray:
    white = rng.normal(size=n) + 1j * rng.normal(size=n)
    freqs = np.fft.fftfreq(n, d=dt)
    omega = 2.0 * np.pi * freqs
    sigma_w = delta_e / HBAR_EV_FS
    spec = np.exp(-0.5 * (omega / sigma_w) ** 2)
    b = np.fft.ifft(np.fft.fft(white) * np.sqrt(spec))
    return b / np.sqrt(np.mean(np.abs(b) ** 2))


def gated_visibility(
    tau_c: float,
    tau_g: float,
    delta_e: float,
    n_real: int = 250,
    dt: float = 0.25,
    T: float = 4000.0,
    seed: int = 0,
) -> float:
    """Visibility from ensemble-averaged gated intensity vs phase."""
    rng = np.random.default_rng(seed)
    n = int(round(T / dt))
    t = np.arange(n) * dt
    sigma = tau_g / (2.0 * np.sqrt(2.0 * np.log(2.0)))
    gate = np.exp(-0.5 * ((t - 0.5 * T) / sigma) ** 2)
    gate = gate / (np.sum(gate) * dt + 1e-30)
    shift = int(round(tau_c / dt))
    phases = np.linspace(0.0, 2.0 * np.pi, 32, endpoint=False)
    S = np.zeros(len(phases))
    for _ in range(n_real):
        b = stationary_baseband(n, dt, delta_e, rng)
        delayed = np.roll(b, shift)
        for i, phi in enumerate(phases):
            field = b + np.exp(1j * phi) * delayed
            S[i] += np.sum(gate * np.abs(field) ** 2) * dt
    S /= n_real
    return float((S.max() - S.min()) / (S.max() + S.min() + 1e-30))


def repo_kernels(tau_c: float, tau_phi: float, tau_g: np.ndarray):
    v_geom = np.abs(np.sinc((tau_c / tau_g) / np.pi))
    v_phi = np.exp(-0.5 * (tau_g / tau_phi) ** 2)
    return v_geom, v_phi


def main():
    v, tau_c, tau_phi, r = kinematics()
    print("N-12 Scoped QM vs RTT gate-model benchmark")
    print("=" * 52)
    print(f"E = {E_EV} eV, δE = {DELTA_E_EV} eV, ΔL = {DELTA_L_M * 1e6:.0f} μm")
    print(f"v = {v:.6e} m/s")
    print(f"τ_c = {tau_c:.1f} fs")
    print(f"τ_φ = {tau_phi:.2f} fs")
    print(f"r = τ_c/τ_φ = {r:.1f}")
    print()
    print("Premises: single setup; imported I = |ψ|²; rate λ ∝ I.")
    print()

    print("Result 1 — ratio collapse (wide gate ≈ 600 fs)")
    print("-" * 52)
    print(f"{'r':>8}  {'V_QM':>8}  {'exp(-r²/2)':>12}")
    ratio_rows = []
    for r_target in [0.15, 0.61, 2.43, 9.72]:
        tau_c_i = 50.0
        delta_e_i = HBAR_EV_FS / (tau_c_i / r_target)
        v_qm = gated_visibility(tau_c_i, 600.0, delta_e_i, n_real=250, seed=0)
        analytic = float(np.exp(-0.5 * r_target ** 2))
        print(f"{r_target:8.2f}  {v_qm:8.3f}  {analytic:12.3f}")
        ratio_rows.append((r_target, v_qm, analytic))

    print()
    print("Result 2 — gated V_QM at benchmark r ≈ 51")
    print("-" * 52)
    tau_g_list = [1.0, 3.0, 10.0, 30.0, 100.0, 169.0, 300.0, 600.0, 1000.0]
    print(f"{'τ_g (fs)':>10}  {'V_QM':>8}  {'V_geom':>8}  {'V_φ':>8}")
    v_qm_rows = []
    for tg in tau_g_list:
        v_qm = gated_visibility(tau_c, tg, DELTA_E_EV, n_real=250, seed=0)
        vg, vp = repo_kernels(tau_c, tau_phi, np.array([tg]))
        print(f"{tg:10.1f}  {v_qm:8.3f}  {float(vg[0]):8.3f}  {float(vp[0]):8.3f}")
        v_qm_rows.append((tg, v_qm, float(vg[0]), float(vp[0])))

    print()
    print("Repo kernels at selected τ_g")
    for tg in [3.0, 169.0, 1000.0]:
        vg, vp = repo_kernels(tau_c, tau_phi, np.array([tg]))
        print(f"  τ_g={tg:7.1f}  V_geom={float(vg[0]):.3f}  V_φ={float(vp[0]):.3f}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        FIG_DIR.mkdir(parents=True, exist_ok=True)

        rs = np.array([row[0] for row in ratio_rows])
        vs = np.array([row[1] for row in ratio_rows])
        r_line = np.linspace(0.05, 12, 200)
        fig, ax = plt.subplots(figsize=(5.5, 3.8))
        ax.plot(r_line, np.exp(-0.5 * r_line ** 2), "k-", label=r"$\exp(-r^2/2)$")
        ax.plot(rs, vs, "o", label=r"gated $V_{\mathrm{QM}}$ (wide gate)")
        ax.set_xlabel(r"$r = \tau_c/\tau_\phi$")
        ax.set_ylabel("Visibility")
        ax.set_title("Ratio collapse under imported intensity + rate ∝ I")
        ax.legend(frameon=False)
        ax.set_ylim(-0.05, 1.05)
        fig.tight_layout()
        fig.savefig(FIG_DIR / "fig_n12_ratio_collapse.pdf")
        fig.savefig(FIG_DIR / "fig_n12_ratio_collapse.png", dpi=140)
        plt.close(fig)

        tgs = np.array([row[0] for row in v_qm_rows])
        vqs = np.array([row[1] for row in v_qm_rows])
        vgs = np.array([row[2] for row in v_qm_rows])
        vps = np.array([row[3] for row in v_qm_rows])
        fig, ax = plt.subplots(figsize=(5.5, 3.8))
        ax.semilogx(tgs, vqs, "o-", label=r"$V_{\mathrm{QM}}$ (r≈51)")
        ax.semilogx(tgs, vgs, "s--", label=r"$V_{\mathrm{geom}}$ (sinc)")
        ax.semilogx(tgs, vps, "^:", label=r"$V_\phi$")
        ax.set_xlabel(r"gate FWHM $\tau_g$ (fs)")
        ax.set_ylabel("Visibility")
        ax.set_title("Benchmark geometry: QM vs repo kernels")
        ax.legend(frameon=False)
        ax.set_ylim(-0.05, 1.05)
        fig.tight_layout()
        fig.savefig(FIG_DIR / "fig_n12_gate_scan.pdf")
        fig.savefig(FIG_DIR / "fig_n12_gate_scan.png", dpi=140)
        plt.close(fig)
        print()
        print(f"Figures written under {FIG_DIR}")
    except Exception as e:
        print("Figure generation skipped:", e)

    print()
    print("Scoped conclusion: under imported I and λ∝I, gated visibility")
    print("depends only on r = τ_c/τ_φ; the sinc kernel is excluded at large r.")
    print("Open boundary: a non-imported sampling rule, dispersive multi-path,")
    print("or multi-particle sector is not constrained by this benchmark.")


if __name__ == "__main__":
    main()
