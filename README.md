# Resolution Time Theory (RTT)

**Author:** Joshua B. Girod  
**Status:** Core Edition 4.0 + research program (Phases 1–3 complete under post-audit framing)  
**Living TODO:** [TODO.md](TODO.md)  
**Verification:** [VERIFICATION_LOG.md](VERIFICATION_LOG.md)

**Paper:** [paper/RTT_Core_Edition_4.0.tex](paper/RTT_Core_Edition_4.0.tex)  
**Plain-language:** [docs/LAYMANS_GUIDE.md](docs/LAYMANS_GUIDE.md)  
**Phase-1 synthesis:** [docs/PHASE1_SYNTHESIS.md](docs/PHASE1_SYNTHESIS.md)

---

## One-line status (30 July 2026)

Mechanical route closed (1.3). Record-side reachability by counting (1.2). Geometric τ_c visibility prediction in place. Dynamics demos under assumed structure. Ontology = **measurement records**. Multi-particle / configuration-space issues untouched.

---

## What this is

Resolution Time Theory proposes that some features of quantum statistics can be understood as the result of **under-sampling high-frequency classical fields** with detectors that have finite time resolution.

This repository is a **research program / working note**, not a claim that quantum mechanics is wrong about experimental predictions. It sits in the lineage of stochastic mechanics, stochastic electrodynamics, and pilot-wave theories, with:

1. A precise technical obstruction (mechanical averaging does not produce ρ ∝ I)
2. Candidate closures of the single-particle equilibrium sector (now understood as measurement-record side)
3. A geometric timescale for a pulsed-electron visibility test
4. Clear falsification conditions and open problems
5. An explicit verifiability standard (executable algebra, L¹ metrics, negative controls, audit trail)

---

## The central technical point (post-audit)

A classical high-frequency field produces intensity I by interference. Standard results give:

| From the high-frequency field | Result |
|-------------------------------|--------|
| Kapitza / ponderomotive averaging | Force ∝ ∇I |
| Multiplicative noise / Itô–Stratonovich | Still ∇I-type |

**None of these produces a drift ∝ ∇log I or D ∝ 1/I from pure particle mechanics.** Simulation 07 confirms occupation does not lock to I.

**Solid content after audit:**

- **1.3** Mechanical route is closed (negative result).
- **1.2** If detection rate ∝ I, the recorded event density ∝ I by counting (LLN).
- Therefore the single-particle equilibrium sector is best framed as a theory of **measurement records** under finite resolution, not a dynamical law of real trajectories in flight.

A previous claim that the Poisson score supplies a net ∇log I dynamical drift was incorrect (mean score ≡ 0) and has been withdrawn (Phase 1.4 demoted).

---

## Experimental handle (still primary)

The resolution timescale is identified with the interferometer path-difference transit time:

```math
\tau_c \sim \frac{\Delta L}{v}
```

For electrons at 100 eV (v ≈ 5.9×10⁶ m/s):

| ΔL | τ_c |
|----|-----|
| 0.1 µm | ≈ 17 fs |
| 1 µm | ≈ 170 fs |
| 2 µm | ≈ 340 fs |

Quantum phase timescale τ_φ ∼ ℏ/δE is typically a few femtoseconds. Both are fixed by the apparatus, so a visibility-versus-gate-width comparison is in principle parameter-free. See `simulations/09_visibility_kernels.py`.

---

## Repository map

```
TODO.md                          Living prioritized list
VERIFICATION_LOG.md              Status tags + critical-review trail
RESULT_TEMPLATE.md               Provenance stub for every claim
derivations/                     Executable sympy identities
  poisson_score.py               E[score] = 0 (caught the 1.4 error)
  kapitza_effective_potential.py V_eff ∝ (A')²/ω²
  fp_stationary_diffusion.py     ρ∞ ∝ 1/D
simulations/
  05–08                          Phase 1 equilibrium routes (08 corrected)
  09                             Visibility kernels + eV tables
  10                             L¹ locking under D∝1/I + negative control
  11                             Finite-resolution averaging demo
docs/
  PHASE1_SYNTHESIS.md            Ontology framing (post-audit)
  NOTES_ON_EQUILIBRIUM_ROUTES.md
  LAYMANS_GUIDE.md
paper/
  RTT_Core_Edition_4.0.tex
run_all.sh                       One-command regeneration
requirements.txt
```

### Run everything

```bash
bash run_all.sh
```

Requires Python 3 with `numpy`, `matplotlib`, `sympy`.

---

## What is native vs imported / assumed

| Element | Status |
|---------|--------|
| High-frequency intensity from classical interference | Native |
| Under-sampling / finite-gate observation model | Native |
| Mechanical homogenization does **not** give ρ ∝ I | Shown (1.3) |
| Rate ∝ I ⇒ recorded density ∝ I | Counting / LLN (1.2) |
| D ∝ 1/I or log-drift closures | Assumed structure (reachability only) |
| τ_c ∼ ΔL / v | Native identification |
| Pulsed-gate visibility comparison | Native |
| Multi-particle / Wallstrom / configuration space | **Open / untouched** |

---

## Falsification (this sector)

RTT would be strained or ruled out here if:

- In a pulsed interferometer with known ΔL, v, and δE, visibility vs gate width follows pure quantum phase averaging where the geometric resolution kernel predicts a clear deviation (after ordinary decoherence is controlled)
- No effective resolution timescale of order ΔL/v appears in gated fringe data

---

## Open problems

1. Deeper derivation of the intensity → event-rate relation from a microscopic field + detector Hamiltonian
2. Multi-particle configuration-space problem and Wallstrom-type single-valuedness (completely open)
3. Nelson-type free dispersion from the same ontology
4. No-signaling / Lorentz constraints on any preferred-frame sector

---

## Citation

> J. B. Girod, *Resolution Time Theory: Core Edition 4.0*, 2026.  
> https://github.com/nentrapper-g-rod/Resolution-Time-Theory

---

## Contact

Joshua B. Girod — independent researcher, Battle Ground / Vancouver, WA  
GitHub: [@nentrapper-g-rod](https://github.com/nentrapper-g-rod)
