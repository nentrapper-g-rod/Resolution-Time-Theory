# Resolution Time Theory (RTT)

> **Independent, non-peer-reviewed research working note.**

**Author:** Joshua B. Girod  
**Version:** Core Edition 4.0.1 (30 July 2026)  
**Living TODO:** [TODO.md](TODO.md)  
**Verification:** [VERIFICATION_LOG.md](VERIFICATION_LOG.md)  
**Cite:** [CITATION.cff](CITATION.cff)  
**License:** [LICENSE](LICENSE) --- MIT (code) / CC-BY-4.0 (paper & docs)  
**Changelog:** [CHANGELOG.md](CHANGELOG.md)

**Paper (post-audit):** [paper/RTT_Core_Edition_4.0.1.tex](paper/RTT_Core_Edition_4.0.1.tex)  
**Plain language:** [docs/LAYMANS_GUIDE.md](docs/LAYMANS_GUIDE.md)  
**Phase-1 synthesis:** [docs/PHASE1_SYNTHESIS.md](docs/PHASE1_SYNTHESIS.md)

---

## Status & honest scoreboard

| | Status tag | Content |
|---|------------|---------|
| **Ruled out** | shown-numerically | Mechanical high-frequency averaging does **not** produce rho proportional to I (Phase 1.3) |
| **Solid record-side** | shown-numerically / by construction | Rate proportional to I implies recorded density proportional to I by counting / LLN (Phase 1.2) |
| **Demoted** | withdrawn as independent claim | Bayesian score route (1.4): mean Poisson score is zero; collapses to 1.2 |
| **Ontology** | assumed framing (supported by 1.3+1.2) | Single-particle equilibrium = **measurement records / finite-resolution estimation** |
| **Novel prediction** | assumed identification + analytic kernels | Geometric tau_c ~ Delta L / v; visibility vs gate width (Phase 2) |
| **Scope** | explicit limit | Single-particle, effectively 1-D; multi-particle / config-space **open** |

**One line:** Mechanical route closed; equilibrium reachable via counting on the record side; ontology = measurement records; the one novel falsifiable handle is tau_c vs gate-width.

Executable checks: [`derivations/`](derivations/). Audit trail: [`VERIFICATION_LOG.md`](VERIFICATION_LOG.md).

---

## What this is

RTT proposes that some features of quantum statistics can be understood as **under-sampling high-frequency classical intensity** with detectors of finite time resolution (gate ~ tau_c).

This is **not** a claim that quantum mechanics is wrong about experimental predictions. It is a candidate classical mechanism / research program.

---

## The central technical point

| From the high-frequency field | Result |
|-------------------------------|--------|
| Kapitza / ponderomotive averaging | Force proportional to grad I |
| Multiplicative noise ~ |Phi| | D proportional to I |
| Ito-Stratonovich conversion | Spurious drift still proportional to grad I |

**None of these produces grad log I or D proportional to 1/I from bare particle mechanics.** Born-rule equilibrium needs an extra principle. On present evidence that principle sits on the **detection / record** side (1.2), not in the particle dynamics under the field (1.3 closed).

---

## Repository contents

```
LICENSE, CITATION.cff, CHANGELOG.md, README.md, TODO.md
VERIFICATION_LOG.md, RESULT_TEMPLATE.md, requirements.txt, run_all.sh
derivations/   poisson_score.py, kapitza_effective_potential.py, fp_stationary_diffusion.py
docs/          LAYMANS_GUIDE.md, NOTES_ON_EQUILIBRIUM_ROUTES.md, PHASE1_SYNTHESIS.md, SYNTHESIS_PHASE1_EQUILIBRIUM.md
paper/         RTT_Core_Edition_4.0.tex, RTT_Core_Edition_4.0.1.tex
results/       RESULT_N10_locking_L1.md, RESULT_N11_finite_resolution.md
simulations/   04..11 (kinematics, equilibrium routes, homogenization, kernels, L1 locking, gate averaging)
```

```bash
pip install -r requirements.txt
bash run_all.sh
```

`run_all.sh` only regenerates outputs. No shutdown/reboot/kill/destructive commands.

---

## Geometric resolution time

    tau_c ~ Delta L / v

100 eV electrons: 0.1 um -> ~17 fs; 1 um -> ~170 fs; 2 um -> ~340 fs. Phase timescale tau_phi ~ hbar/delta E is typically a few femtoseconds. See `simulations/09_visibility_kernels.py`.

---

## Native vs imported / assumed / ruled out

| Element | Status tag |
|---------|------------|
| High-frequency intensity from classical interference | native |
| Under-sampling / finite-gate observation model | native |
| Mechanical averaging fails to give rho proportional to I | **ruled out as origin** (1.3) |
| Counting: rate proportional to I implies recorded density proportional to I | shown (1.2) |
| Log-potential or D proportional to 1/I as trajectory law | assumed (reachability only) |
| tau_c ~ Delta L / v | native identification |
| Nelson free-packet dynamics | imported (1966) |
| Multi-particle / Wallstrom / config-space | **open** |

---

## Falsification (this sector)

- Gated visibility follows pure quantum phase averaging where the geometric kernel predicts a clear deviation (after ordinary decoherence is controlled)
- No effective resolution timescale of order Delta L / v appears in gated fringe data

---

## Open problems

1. Microscopic derivation of intensity to event-rate
2. Multi-particle / configuration-space / Wallstrom (**untouched**)
3. Nelson-type free dispersion from the same field
4. No-signaling / Lorentz constraints on any preferred-frame sector

---

## License

- **Code** (`simulations/`, `derivations/`, scripts): MIT
- **Paper and docs**: CC-BY-4.0  
Copyright (c) 2026 Joshua B. Girod --- see [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff).

> J. B. Girod, *Resolution Time Theory: Core Edition 4.0*, 2026.  
> https://github.com/nentrapper-g-rod/Resolution-Time-Theory

## Contact

Joshua B. Girod --- independent researcher, Battle Ground / Vancouver, WA  
GitHub: [@nentrapper-g-rod](https://github.com/nentrapper-g-rod)
