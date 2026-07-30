#!/usr/bin/env python3
"""Generate Core Edition 4.1 figures into paper/figures/.

Run from repo root:
  python paper/generate_figures.py
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

def fig_counting():
    rng = np.random.default_rng(42)
    x = np.linspace(-5, 5, 80)
    I = np.exp(-((x - 1.5) ** 2) / 0.5) + np.exp(-((x + 1.5) ** 2) / 0.5) + 0.05
    I = I / I.sum()
    events = rng.choice(x, size=50000, p=I)
    hist, edges = np.histogram(events, bins=80, density=True, range=(-5, 5))
    centers = 0.5 * (edges[:-1] + edges[1:])
    I_cont = np.exp(-((centers - 1.5) ** 2) / 0.5) + np.exp(-((centers + 1.5) ** 2) / 0.5) + 0.05
    I_cont = I_cont / np.trapezoid(I_cont, centers)
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    ax.bar(centers, hist, width=edges[1] - edges[0], alpha=0.55, color="C0", label="recorded events (rate ∝ I)")
    ax.plot(centers, I_cont, "r-", lw=2, label="normalized I")
    ax.set_xlabel("x"); ax.set_ylabel("density")
    ax.set_title("Phase 1.2: counting recovers recorded density ∝ I")
    ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    fig.savefig(OUT / "fig_counting_density.pdf")
    fig.savefig(OUT / "fig_counting_density.png", dpi=160)
    plt.close()

def fig_kapitza():
    xg = np.linspace(-3.5, 3.5, 400)
    I = np.exp(-(xg - 1.2) ** 2 / 0.5) + np.exp(-(xg + 1.2) ** 2 / 0.5) + 0.12
    A = np.sqrt(I)
    dA = np.gradient(A, xg)
    V_eff = (dA ** 2) / (4.0 * 60.0 ** 2)
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    ax.plot(xg, I / I.max(), "r-", lw=2, label="intensity I (normalized)")
    ax.plot(xg, V_eff / (V_eff.max() + 1e-30), "k--", lw=1.8, label=r"Kapitza $V_{\mathrm{eff}}\propto(A')^2$")
    ax.set_xlabel("x"); ax.set_ylabel("normalized units")
    ax.set_title(r"Phase 1.3: mechanical $V_{\mathrm{eff}}$ is $\nabla I$-type, not $-\log I$")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "fig_kapitza_vs_I.pdf")
    fig.savefig(OUT / "fig_kapitza_vs_I.png", dpi=160)
    plt.close()

def fig_visibility():
    hbar = 1.0545718e-34
    m_e = 9.109e-31
    e = 1.602e-19
    def v_e(E):
        return np.sqrt(2 * E * e / m_e)
    def tau_c(dL, E):
        return (dL * 1e-6) / v_e(E) * 1e15
    def tau_phi(dE):
        return hbar / (dE * e) * 1e15
    delta_t = tau_c(1.0, 100) * 1e-15
    tphi = tau_phi(0.2) * 1e-15
    tg_fs = np.linspace(5, 1000, 400)
    tg = tg_fs * 1e-15
    Vg = np.abs(np.sinc(delta_t / tg))
    Vp = np.exp(-0.5 * (tg / tphi) ** 2)
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    ax.plot(tg_fs, Vg, lw=2, label=r"$V_{\mathrm{geom}}=|\mathrm{sinc}(\delta t/\tau_g)|$")
    ax.plot(tg_fs, Vp, lw=2, label=r"$V_\phi=\exp[-(\tau_g/\tau_\phi)^2/2]$")
    ax.axvline(tau_c(1.0, 100), color="gray", ls=":", lw=1.2, label=r"$\tau_c\approx 169$ fs")
    ax.set_xlabel(r"gate width $\tau_g$ (fs)")
    ax.set_ylabel("visibility")
    ax.set_title(r"Phase 2 kernels: 100 eV, $\Delta L=1\,\mu$m, $\delta E=0.2$ eV")
    ax.set_ylim(-0.05, 1.05)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "fig_visibility_kernels.pdf")
    fig.savefig(OUT / "fig_visibility_kernels.png", dpi=160)
    plt.close()

if __name__ == "__main__":
    fig_counting()
    fig_kapitza()
    fig_visibility()
    print("Wrote figures to", OUT)
