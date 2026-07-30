# Resolution Time Theory (RTT)

**Author:** Joshua B. Girod  
**Status:** Research program / working note (Core Edition 4.0 + active updates)  
**Living TODO:** [TODO.md](TODO.md)  
**Verification:** [VERIFICATION_LOG.md](VERIFICATION_LOG.md)

**Paper:** [paper/RTT_Core_Edition_4.0.tex](paper/RTT_Core_Edition_4.0.tex)  
**Plain-language:** [docs/LAYMANS_GUIDE.md](docs/LAYMANS_GUIDE.md)  
**Phase-1 synthesis:** [docs/PHASE1_SYNTHESIS.md](docs/PHASE1_SYNTHESIS.md)

---

## One-line status (30 July 2026)

Mechanical route closed (1.3); record-side reachability by counting (1.2); geometric τ_c visibility prediction in place; dynamics demos under assumed structure. **Ontology = measurement records.** Multi-particle / configuration-space issues remain untouched.

---

## What this is

Resolution Time Theory proposes that some features of quantum statistics can be understood as the result of **under-sampling high-frequency classical intensity** with detectors that have finite time resolution (gate width ~τ_c).

This repository is **not** a claim that quantum mechanics is wrong about experimental predictions. It is a candidate classical mechanism / research program with:

1. A precise technical obstruction (mechanical averaging does not produce ρ ∝ I)
2. A solid counting argument on the measurement-record side
3. A geometric timescale for a pulsed-electron visibility test
4. Clear falsification conditions and open problems

---

## The central technical point

A classical high-frequency field produces intensity I by interference. Standard results give:

| From the high-frequency field | Result |
|-------------------------------|--------|
| Kapitza / ponderomotive averaging | Force ∝ ∇I |
| Multiplicative noise coupled to |Φ| | Diffusion D ∝ I |
| Itô / Stratonovich conversion | Spurious drift still ∝ ∇I |

**None of these produces a drift ∝ ∇log I or D ∝ 1/I from the bare particle mechanics.**  
Born-rule equilibrium (ρ ∝ I) therefore requires an extra principle. Phase-1 work shows that pure mechanical homogenization fails (negative result, load-bearing) while ordinary intensity-proportional counting recovers the recorded density by the law of large numbers.

### Honest Phase-1 scoreboard

| Item | Nature | Weight |
|------|--------|--------|
| 1.1 D ∝ 1/I | Consistency check | Low |
| **1.2 Rate / Poisson counting ∝ I** | **Recorded density ∝ I by LLN** | **High** |
| **1.3 Mechanical homogenization** | **Negative: does not lock to I** | **High (load-bearing)** |
| 1.4 Bayesian score route | **Demoted** (mean Poisson score ≡ 0; previous sim circular) | Withdrawn as independent claim |

**Ontology:** The single-particle equilibrium sector is a theory of **measurement records**. Detection events generated with rate ∝ I produce an empirical density of recorded locations that tracks I. Pure high-frequency classical mechanics does not produce this structure.

---

## Repository map

```
TODO.md                          # Living prioritized list
VERIFICATION_LOG.md              # Status tags + critical-review trail
derivations/                     # Executable sympy (Poisson score, Kapitza, FP)
simulations/
  05–08                          # Phase 1 equilibrium routes
  09                             # Visibility kernels (Phase 2)
  10                             # Locking + L¹ convergence (Phase 3.1)
  11                             # Finite-resolution averaging (Phase 3.2)
results/                         # Provenance notes (N-10, N-11, …)
paper/RTT_Core_Edition_4.0.tex
docs/PHASE1_SYNTHESIS.md
run_all.sh                       # One-command regeneration
requirements.txt
```

### Running everything

```bash
pip install -r requirements.txt
bash run_all.sh
```

---

## Geometric resolution time (primary experimental handle)

\[
\tau_c \sim \frac{\Delta L}{v}
\]

For electrons at 100 eV (v ≈ 5.9×10⁶ m/s):

| ΔL | τ_c |
|----|-----|
| 0.1 µm | ≈ 17 fs |
| 1 µm | ≈ 170 fs |
| 2 µm | ≈ 340 fs |

The quantum phase timescale τ_φ ~ ħ/δE is typically a few femtoseconds. Visibility versus gate width is in principle a parameter-free comparison (see simulations/09).

---

## What is native vs imported / assumed

| Element | Status |
|---------|--------|
| High-frequency intensity from classical interference | Native |
| Under-sampling / finite-gate observation model | Native |
| Mechanical averaging fails to give ρ ∝ I | Shown (1.3) |
| Counting: rate ∝ I ⇒ recorded density ∝ I | Shown (1.2) |
| Equilibrium closures (log-potential or D ∝ 1/I) | Assumed structure (reachability shown) |
| τ_c ∼ ΔL/v | Native identification |
| Multi-particle / Wallstrom / config-space | **Open** |

---

## Falsification (this sector)

RTT would be strained or ruled out here if:

- In a pulsed interferometer with known ΔL, v, and δE, visibility vs gate width follows pure quantum phase averaging where the geometric resolution kernel predicts a clear deviation (after ordinary decoherence is controlled)
- No effective resolution timescale of order ΔL/v appears in gated fringe data

---

## Open problems

1. Deeper microscopic derivation of the intensity → event-rate relation (beyond ordinary detection physics)
2. Multi-particle / configuration-space problem and Wallstrom-type issues
3. Derive Nelson-type free dispersion from the same field
4. No-signaling and Lorentz constraints on any preferred-frame sector

---

## Citation

> J. B. Girod, *Resolution Time Theory: Core Edition 4.0*, 2026.  
> https://github.com/nentrapper-g-rod/Resolution-Time-Theory

---

## Contact

Joshua B. Girod — independent researcher, Battle Ground / Vancouver, WA  
GitHub: [@nentrapper-g-rod](https://github.com/nentrapper-g-rod)
