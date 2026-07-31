# RTT Research Program TODO

**Principles:** Exact math or reproducible numbers. No over-claiming. Prefer L¹ over correlation. Scope claims; never turn a scoped result into a universal one.

**One-line status:** Project is finding out what RTT *is* (not defending a finished theory). Next: Claim Map → first RTT-only equation → explicit detector law.

---

## Done (keep for the record)

- [x] Mechanical route closed (∇I vs ∇log I; N-07)
- [x] Counting reachability (rate ∝ I ⇒ recorded density ∝ I; N-06)
- [x] Score route demoted (mean Poisson score = 0; N-08 / D-01)
- [x] Ontology framing: single-particle equilibrium = measurement records
- [x] N-12 scoped gate benchmark: under imported I = |ψ|² and λ ∝ I, V depends only on r = τ_c/τ_φ; sinc kernel excluded
- [x] Core Edition 4.1 + VALIDATION.md + reproducible sims 05–12

---

## Phase A — Clean up the theory (highest priority)

- [ ] **A.1 Claim Map** ⭐⭐⭐⭐⭐
  - Create `CLAIM_MAP.md` (or `theory/CLAIM_MAP.md`)
  - Label every major statement: Proven | Derived | Imported | Assumed | Interpretation | Speculation | Withdrawn | Missing
  - Seed from paper scoreboard, VALIDATION.md, N-12 premises — no new claims
  - Make the missing detector law visible as **Missing**, not as a prediction

- [ ] **A.2 First RTT-only equation** ⭐⭐⭐⭐⭐
  - Ask: what is the first sentence/equation standard QM would reject?
  - Not preferred frame, master clock, or ΔL/v (those are standard or kinematic)
  - Use N-12 null model: imported I + λ ∝ I ⇒ equivalence — what must change to break it?
  - If none exists under present postulates, record that as a result (interpretive fork)

- [ ] **A.3 Explicit detector / event law** ⭐⭐⭐⭐⭐
  - Field → detector coupling → electronics/threshold → recorded event
  - As equations, not philosophy
  - Must state whether response differs from ∫ G(t) I_QM dt; if not, mark equivalent

---

## Phase B — Tighten the mathematics

- [ ] **B.1 Hostile gate-width re-test**
  - Goal: try to *destroy* residual RTT distinction under import assumptions
  - Spectra: Gaussian, Lorentzian, rectangular, chirped, correlated packets
  - Report whether every case collapses to standard coherence

- [ ] **B.2 Move phenomenological kernels**
  - Anything “looks reasonable” but not derived → `exploratory_models/`
  - Do not leave exploratory math beside derived math in the main narrative

- [ ] **B.3 Separate kinematics from new physics**
  - Table: ΔL, v, ΔL/v, coherence time, detector gate = standard
  - Fill the blank RTT-only row — or state that it is empty under current postulates

---

## Phase C — Repository structure (after Claim Map)

- [ ] **C.1** Fold docs into clear homes only *after* A.1 exists:
  - `theory/` · `negative_results/` · `investigations/` · `derived_results/` · `exploratory_models/` · `future_work/`
- [ ] **C.2** Commit compiled `paper/RTT_Core_Edition_4.1.pdf` + figures
- [ ] **C.3** Finish any remaining companion links for N-12 (README status row, VALIDATION entry, run_all) if not already live

---

## Phase D — One prediction or interpretive paper

- [ ] **D.1** After A–B: is there **one** distinct prediction left? (Not five.)
- [ ] **D.2** If yes: write it as a single falsifiable claim with apparatus parameters
- [ ] **D.3** If no: draft *RTT as an Interpretive Framework* (still publishable; identical predictions, different ontology)

---

## Explicitly deferred (do not work on until A.2 has an answer)

- Bell experiments / entanglement constructions
- Lorentz / preferred-frame / master-clock phenomenology
- Cosmology
- Large multi-particle simulations
- Detector engineering / full experimental apparatus design
- arXiv upload can wait until Claim Map + first-equation decision exist (optional packaging only)

---

## Personal priority order (evenings)

1. Claim Map
2. First RTT-only equation (or honest “none under present postulates”)
3. Explicit detector/event law
4. Hostile gate re-test
5. Repo organization
6. Remove exploratory kernels from main narrative
7. New experiments / simulations only after the blank row is filled or declared empty

*Last updated: 2026-07-30 — roadmap shifted from “prove RTT” to “reduce uncertainty about what RTT is.”*
