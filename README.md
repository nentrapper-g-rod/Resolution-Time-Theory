# Resolution Time Theory (RTT)

> **Independent, non-peer-reviewed research working note.**

**Author:** Joshua B. Girod  
**Version:** Core Edition **4.1** (30 July 2026)  
**Living TODO:** [TODO.md](TODO.md)  
**Verification:** [VERIFICATION_LOG.md](VERIFICATION_LOG.md)  
**Cite:** [CITATION.cff](CITATION.cff)  
**License:** [LICENSE](LICENSE) — MIT (code) / CC-BY-4.0 (paper & docs)  
**Changelog:** [CHANGELOG.md](CHANGELOG.md)  
**arXiv packaging:** [ARXIV_CHECKLIST.md](ARXIV_CHECKLIST.md) | [SUBMISSION_NOTES.md](SUBMISSION_NOTES.md)

**Paper (current):** [paper/RTT_Core_Edition_4.1.tex](paper/RTT_Core_Edition_4.1.tex)  
**Figures:** `python paper/generate_figures.py`  
**Plain language:** [docs/LAYMANS_GUIDE.md](docs/LAYMANS_GUIDE.md)  
**Phase-1 synthesis:** [docs/PHASE1_SYNTHESIS.md](docs/PHASE1_SYNTHESIS.md)

---

## Status & honest scoreboard

| | Status tag | Content |
|---|------------|---------|
| **Ruled out** | shown-numerically | Mechanical high-frequency averaging does **not** produce ρ ∝ I (Phase 1.3) |
| **Solid record-side** | shown-numerically / by construction | Rate ∝ I ⇒ recorded density ∝ I by counting / LLN (Phase 1.2) |
| **Demoted** | withdrawn as independent claim | Bayesian score route (1.4): mean Poisson score is zero; collapses to 1.2 |
| **Ontology** | assumed framing (supported by 1.3+1.2) | Single-particle equilibrium = **measurement records / finite-resolution estimation** |
| **Novel prediction** | assumed identification + analytic kernels | Geometric τ_c ∼ ΔL / v; visibility vs gate width (Phase 2) |
| **Scope** | explicit limit | Single-particle, effectively 1-D; multi-particle / config-space **open** |

**One line:** Mechanical route closed; equilibrium reachable via counting on the record side; ontology = measurement records; the one novel falsifiable handle is τ_c vs gate-width.

Executable checks: [`derivations/`](derivations/). Audit trail: [`VERIFICATION_LOG.md`](VERIFICATION_LOG.md).

---

## What this is

RTT proposes that some features of quantum statistics can be understood as **under-sampling high-frequency classical intensity** with detectors of finite time resolution (gate ∼ τ_c).

This is **not** a claim that quantum mechanics is wrong about experimental predictions. It is a candidate classical mechanism / research program.

---

## The central technical point

| From the high-frequency field | Result |
|-------------------------------|--------|
| Kapitza / ponderomotive averaging | Force ∝ ∇I |
| Multiplicative noise ∼ |Φ| | D ∝ I |
| Itô–Stratonovich conversion | Spurious drift still ∝ ∇I |

**None of these produces ∇log I or D ∝ 1/I from bare particle mechanics.** Born-rule equilibrium needs an extra principle. On present evidence that principle sits on the **detection / record** side (1.2), not in the particle dynamics under the field (1.3 closed).

---

## Repository contents

```
LICENSE, CITATION.cff, CHANGELOG.md, README.md, TODO.md
ARXIV_CHECKLIST.md, SUBMISSION_NOTES.md
VERIFICATION_LOG.md, RESULT_TEMPLATE.md, requirements.txt, run_all.sh
derivations/   poisson_score.py, kapitza_effective_potential.py, fp_stationary_diffusion.py
docs/          LAYMANS_GUIDE.md, NOTES_ON_EQUILIBRIUM_ROUTES.md, PHASE1_SYNTHESIS.md, ...
paper/         RTT_Core_Edition_4.1.tex (current), generate_figures.py, BUILD.md
results/       RESULT_N05 … RESULT_N11
simulations/   04..11
```

```bash
pip install -r requirements.txt
python paper/generate_figures.py
bash run_all.sh
```

---

## Geometric resolution time

    τ_c ∼ ΔL / v

100 eV electrons: 0.1 μm → ~17 fs; 1 μm → ~169 fs; 2 μm → ~337 fs. See `simulations/09_visibility_kernels.py`.

---

## Native vs imported / assumed / ruled out

| Element | Status tag |
|---------|------------|
| High-frequency intensity from classical interference | native |
| Under-sampling / finite-gate observation model | native |
| Mechanical averaging fails to give ρ ∝ I | **ruled out as origin** (1.3) |
| Counting: rate ∝ I ⇒ recorded density ∝ I | shown (1.2) |
| Log-potential or D ∝ 1/I as trajectory law | assumed (reachability only) |
| τ_c ∼ ΔL / v | native identification |
| Nelson free-packet dynamics | imported (1966) |
| Multi-particle / Wallstrom / config-space | **open** |

---

## Falsification (this sector)

- Gated visibility follows pure quantum phase averaging where the geometric kernel predicts a clear deviation (after ordinary decoherence is controlled)
- No effective resolution timescale of order ΔL / v appears in gated fringe data

---

## Open problems

1. Microscopic derivation of intensity → event-rate
2. Multi-particle / configuration-space / Wallstrom (**untouched**)
3. Nelson-type free dispersion from the same field
4. No-signaling / Lorentz constraints on any preferred-frame sector

---

## License

- **Code** (`simulations/`, `derivations/`, scripts): MIT
- **Paper and docs**: CC-BY-4.0  
Copyright (c) 2026 Joshua B. Girod — see [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff).

> J. B. Girod, *Resolution Time Theory: Core Edition 4.1*, 2026.  
> https://github.com/nentrapper-g-rod/Resolution-Time-Theory

## Contact

Joshua B. Girod — independent researcher, Battle Ground / Vancouver, WA  
GitHub: [@nentrapper-g-rod](https://github.com/nentrapper-g-rod)
