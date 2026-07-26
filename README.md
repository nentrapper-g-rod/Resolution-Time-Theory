# Resolution Time Theory (RTT)

**Author:** Joshua B. Girod  
**Status:** Core Edition 4.0 — research program / working note  

**View the paper:** [paper/RTT_Core_Edition_4.0.tex](paper/RTT_Core_Edition_4.0.tex)  
**Plain-language version:** [docs/LAYMANS_GUIDE.md](docs/LAYMANS_GUIDE.md)

---

## What this is

Resolution Time Theory proposes that some features of quantum statistics can be understood as the result of **under-sampling high-frequency classical motion** with detectors that have finite time resolution — analogous to a slow camera photographing a fast-moving object.

This repository is **not** a claim that quantum mechanics is wrong about experimental predictions. It is a **candidate classical mechanism** in the lineage of stochastic mechanics, stochastic electrodynamics, and pilot-wave theories, with:

1. A precise technical obstruction  
2. One explicit postulate that closes the equilibrium sector  
3. A geometric timescale for a pulsed-electron visibility test  
4. Clear falsification conditions and open problems  

---

## The central technical point

A classical high-frequency field produces intensity \(I\) by interference. Standard results give:

| From the high-frequency field | Result |
|-------------------------------|--------|
| Kapitza / ponderomotive averaging | Force \(\propto \nabla I\) |
| Multiplicative noise coupled to \(\|\Phi\|\) | Diffusion \(D \propto I\) |
| Itô / Stratonovich conversion | Spurious drift still \(\propto \nabla I\) |

**None of these produces a drift \(\propto \nabla \log I\).**  

Born-rule equilibrium (\(\rho \propto I\)) requires a drift of the form \(D\nabla\log I\) (or an engineered diffusion profile). That gap is where any high-frequency classical ontology must supply an extra principle.

RTT adopts the equilibrium postulate:

\[
V_{\mathrm{eff}} = -\kappa \log I
\]

which yields the Itô process

\[
\mathrm{d}X = D\,\partial_x\log I\,\mathrm{d}t + \sqrt{2D}\,\mathrm{d}W
\]

with stationary density \(\rho_\infty = I\) **exactly** (Fokker–Planck theorem). Numerics converge as \(L^1 \sim N^{-1/2}\).

---

## Repository contents

```
paper/
  RTT_Core_Edition_4.0.tex   # Technical note (LaTeX)
docs/
  LAYMANS_GUIDE.md           # High-school / plain-language explanation
simulations/
  04_electron_kinematics_tau_c.py
  README.txt
```

### Running the simulations

```bash
cd simulations
python 04_electron_kinematics_tau_c.py
```

Requires Python 3 with `numpy` and `matplotlib`.

---

## Geometric resolution time

The resolution timescale is identified with the interferometer path-difference transit time:

\[
\tau_c \sim \frac{\Delta L}{v}
\]

For electrons at \(100\,\mathrm{eV}\) (\(v \approx 5.9\times 10^6\,\mathrm{m/s}\)):

| \(\Delta L\) | \(\tau_c\) |
|--------------|------------|
| \(0.1\,\mu\mathrm{m}\) | \(\approx 17\,\mathrm{fs}\) |
| \(1\,\mu\mathrm{m}\) | \(\approx 170\,\mathrm{fs}\) |
| \(2\,\mu\mathrm{m}\) | \(\approx 340\,\mathrm{fs}\) |

The quantum phase timescale from energy spread is \(\tau_\phi \sim \hbar/\delta E\) (typically a few femtoseconds). Both are fixed by the apparatus, so a visibility-versus-gate-width comparison is in principle parameter-free.

---

## What is native vs imported

| Element | Status |
|---------|--------|
| High-frequency intensity from classical interference | Native |
| Under-sampling / \(\Delta t\) observation model | Native |
| Equilibrium postulate \(V = -\kappa\log I\) | Native (postulate) |
| Log-drift locking (\(\rho_\infty = I\) exact) | Follows from postulate |
| \(\tau_c \sim \Delta L / v\) | Native identification |
| Pulsed-gate visibility comparison | Native |
| Nelson free-packet dynamics | **Imported** (1966) |
| Preferred-foliation Bell construction | Construction; coordination inserted |

---

## Falsification (this sector)

RTT would be strained or ruled out here if:

- In a pulsed interferometer with known \(\Delta L\), \(v\), and \(\delta E\), visibility vs gate width follows pure quantum phase averaging where the geometric resolution kernel predicts a clear deviation (after ordinary decoherence is controlled)
- No effective resolution timescale of order \(\Delta L/v\) appears in gated fringe data
- The equilibrium postulate is shown incompatible with a more complete high-frequency dynamics required by the same ontology

---

## Open problems

1. Derive \(V_{\mathrm{eff}} = -\kappa\log I\) (or equivalent) from the high-frequency field without inserting it  
2. Derive Nelson-type free dispersion from the same field  
3. No-signaling and Lorentz constraints on the preferred-frame Bell sector  
4. Quantitative map from velocity / gravitational potential onto effective resolution  

---

## Relation to other programs

| Theory | Hidden variables | Preferred frame | Experimental handle (typical) |
|--------|------------------|-----------------|-------------------------------|
| Copenhagen | No | No | — |
| Bohmian mechanics | Yes | Often | Usually none |
| Nelson stochastic mechanics | Yes | No | Usually none |
| Stochastic electrodynamics | Yes | No | Spectral assumptions |
| **RTT** | Yes | Yes (master clock) | Gate-width visibility |

---

## Citation

If you use this material, please cite:

> J. B. Girod, *Resolution Time Theory: Core Edition 4.0*, 2026.  
> https://github.com/nentrapper-g-rod/Resolution-Time-Theory

---

## Contact

Joshua B. Girod — independent researcher, Battle Ground / Vancouver, WA  
GitHub: [@nentrapper-g-rod](https://github.com/nentrapper-g-rod)
