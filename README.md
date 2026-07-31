# Resolution Time Theory (RTT)

**Author:** Joshua B. Girod · **Core Edition 4.1** (30 July 2026) · Independent research working note (non-peer-reviewed)

**Read this:** [paper/RTT_Core_Edition_4.1.pdf](paper/RTT_Core_Edition_4.1.pdf) · [source](paper/RTT_Core_Edition_4.1.tex) · [CLAIM_MAP.md](CLAIM_MAP.md) · [VALIDATION.md](VALIDATION.md) · [CITATION.cff](CITATION.cff) · [LICENSE](LICENSE)

---

## What it is

RTT investigates whether some quantum *equilibrium* statistics can be read as **finite-resolution under-sampling** of a rapidly varying classical intensity pattern. It does **not** claim that quantum mechanics is wrong about experimental predictions, and it does **not** claim to replace Schrödinger dynamics.

A physicist should care because the program isolates a precise obstruction (∇I vs ∇log I under high-frequency averaging), closes the pure-mechanical route numerically, and states honestly where the present detector law is still ordinary intensity-proportional counting.

---

## Scientific motivation

Quantum mechanics predicts interferometry and detection statistics with high accuracy. RTT asks a narrower question: given a classical intensity envelope I from interference, can finite detector resolution and ordinary intensity-proportional event rates account for an empirical recorded density ∝ I — and does particle mechanics under the high-frequency field already do that by itself?

---

## Experimental status (scoped)

Under the **present** written law (λ = α I) and **imported** intensity I = |ψ|², the gated single-particle response is **degenerate with standard QM**: visibility is fixed by the ratio r = τ_c/τ_φ (N-12). The phenomenological geometric |sinc| kernel is **not** a current prediction.

| Statement | Status |
|-----------|--------|
| Mechanical HF averaging produces ρ ∝ I | **Ruled out** (tested class) |
| λ ∝ I ⇒ recorded density ∝ I | **Derived** from an **Assumed** rate |
| Distinct event law $\mathcal{F} \not\equiv \alpha I_{\mathrm{QM}}$ | **Missing** |
| Gate response under imported I | **Equivalent to QM** (N-12, scoped) |

A distinct experimental prediction requires writing an event functional that does not reduce to gated I_QM (see [investigations/A3_detector_event_law.md](investigations/A3_detector_event_law.md)).

Kinematic scales for reference only (100 eV electrons): ΔL = 0.1 μm → τ_c ≈ 17 fs; ΔL = 1 μm → τ_c ≈ 169 fs.

---

## Current status

| | Tag | Content |
|---|-----|--------|
| **Ruled out** | shown-numerically | Mechanical high-frequency averaging does **not** produce ρ ∝ I |
| **Solid** | shown / by construction | Rate ∝ I ⇒ recorded density ∝ I (counting) |
| **Withdrawn** | withdrawn | Independent score-route derivation (mean Poisson score = 0) |
| **Ontology** | framing | Single-particle equilibrium = measurement records |
| **Gate (imported I)** | shown / derived under premises | Degenerate with QM (N-12); sinc kernel excluded as prediction |
| **Distinct detector law** | Missing | No $\mathcal{F} \not\equiv \alpha I_{\mathrm{QM}}$ written |
| **Scope** | limit | Single-particle 1-D; multi-particle **open** |

Full classification: [CLAIM_MAP.md](CLAIM_MAP.md).

---

## Limitations (open)

- Multi-particle / configuration-space / entanglement
- Wallstrom single-valuedness
- Microscopic intensity → event-rate derivation beyond ordinary detector physics
- Lorentz / no-signaling for any preferred-frame sector (no Bell construction is given here)
- Nelson free dispersion is **imported**, not derived from the field
- First RTT-only equation under present postulates: **none found** ([A.2](investigations/A2_first_rtt_only_equation.md))

---

## Conceptual flow (assumed links marked)

```
Classical field → interference intensity I
       → [ASSUMED] event rate λ ∝ I
       → recorded event locations
       → empirical density ∝ I (by counting)
```

The λ ∝ I arrow is **postulated** (ordinary detector physics), not derived from particle mechanics under the field. When I is identified with I_QM, this chain is equivalent to standard gated intensity detection ([A.3](investigations/A3_detector_event_law.md)).

---

## Repository

| Path | Role |
|------|------|
| `paper/RTT_Core_Edition_4.1.pdf` | Primary read |
| `paper/RTT_Core_Edition_4.1.tex` | Source |
| `CLAIM_MAP.md` | Proven / Assumed / Missing / Withdrawn labels |
| `investigations/` | A.2 first-equation search; A.3 detector law |
| `simulations/` | Numerical checks (05–08, 10–12) |
| `exploratory_models/` | Non-claim kernels (historical sinc tables) |
| `derivations/` | Sympy exact claims |
| `results/` | Regenerated output notes N-05–N-12 |
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
