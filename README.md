# Resolution Time Theory (RTT)

**Author:** Joshua B. Girod · **Core Edition 4.1** (30 July 2026) · Independent research working note (non-peer-reviewed)

**Read this:** [paper/RTT_Core_Edition_4.1.pdf](paper/RTT_Core_Edition_4.1.pdf) · [source](paper/RTT_Core_Edition_4.1.tex) · [VALIDATION.md](VALIDATION.md) · [CITATION.cff](CITATION.cff) · [LICENSE](LICENSE)

---

## What it is

RTT investigates whether some quantum *equilibrium* statistics can be read as **finite-resolution under-sampling** of a rapidly varying classical intensity pattern. It does **not** claim that quantum mechanics is wrong about experimental predictions, and it does **not** claim to replace Schrödinger dynamics.

A physicist should care because the program isolates a precise obstruction (∇I vs ∇log I under high-frequency averaging), closes the pure-mechanical route numerically, and offers one apparatus-defined experimental handle (gate-width visibility vs τ_c ∼ ΔL/v).

---

## Scientific motivation

Quantum mechanics predicts interferometry and detection statistics with high accuracy. RTT asks a narrower question: given a classical intensity envelope I from interference, can finite detector resolution and ordinary intensity-proportional event rates account for an empirical recorded density ∝ I — and does particle mechanics under the high-frequency field already do that by itself?

---

## Experimental predictions

| Would support RTT | Would strain RTT |
|-------------------|------------------|
| Gated fringe visibility follows a geometric kernel tied to τ_c ∼ ΔL/v after decoherence is controlled | Visibility follows pure quantum phase averaging where the geometric kernel predicts a clear deviation |
| An effective resolution timescale of order ΔL/v appears in gated data | No resolution timescale of order ΔL/v appears |

For 100 eV electrons: ΔL = 0.1 μm → τ_c ≈ 17 fs; ΔL = 1 μm → τ_c ≈ 169 fs. See `simulations/09_visibility_kernels.py`.

---

## Current status

| | Tag | Content |
|---|-----|--------|
| **Ruled out** | shown-numerically | Mechanical high-frequency averaging does **not** produce ρ ∝ I |
| **Solid** | shown / by construction | Rate ∝ I ⇒ recorded density ∝ I (counting) |
| **Withdrawn** | withdrawn | Independent score-route derivation (mean Poisson score = 0) |
| **Ontology** | framing | Single-particle equilibrium = measurement records |
| **Novel handle** | assumed ID + kernels | τ_c ∼ ΔL/v; visibility vs gate width |
| **Scope** | limit | Single-particle 1-D; multi-particle **open** |

---

## Limitations (open)

- Multi-particle / configuration-space / entanglement
- Wallstrom single-valuedness
- Microscopic intensity → event-rate derivation beyond ordinary detector physics
- Lorentz / no-signaling for any preferred-frame sector (no Bell construction is given here)
- Nelson free dispersion is **imported**, not derived from the field

---

## Conceptual flow (assumed links marked)

```
Classical field → interference intensity I
       → [ASSUMED] event rate λ ∝ I
       → recorded event locations
       → empirical density ∝ I (by counting)
```

The λ ∝ I arrow is **postulated** (ordinary detector physics), not derived from particle mechanics under the field.

---

## Repository

| Path | Role |
|------|------|
| `paper/RTT_Core_Edition_4.1.pdf` | Primary read |
| `paper/RTT_Core_Edition_4.1.tex` | Source |
| `simulations/` | Numerical checks (04–11) |
| `derivations/` | Sympy exact claims |
| `results/` | Regenerated output notes N-05–N-11 |
| `docs/` | Layman guide + Phase-1 notes |
| `VALIDATION.md` | Status tags and revisions |
| `dev/` | Process docs (TODO, changelog, arXiv notes) |

```bash
pip install -r requirements.txt
python paper/generate_figures.py
bash run_all.sh
```

---

## License / citation / contact

- **Code:** MIT · **Paper & docs:** CC-BY-4.0 · Copyright (c) 2026 Joshua B. Girod
- Cite: [CITATION.cff](CITATION.cff)
- Joshua B. Girod — independent researcher, Battle Ground / Vancouver, WA · [@nentrapper-g-rod](https://github.com/nentrapper-g-rod)
