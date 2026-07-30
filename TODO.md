# RTT Research Program TODO

**Principles:** Every claim must be backed by exact math or reproducible numerical data. No over-claiming. Prefer L¹/KL over correlation; executable algebra for key identities. Default AI status: unverified until checked.

**Current focus:** Phase 4 — paper packaging under the honest post-audit framing.

## Phase 1: Open Problem #1 — Equilibrium structure without pure insertion

- [x] 1.1 Consistency check: D∝1/I ⇒ ρ∞∝I. Restatement, not a derivation.
- [x] 1.2 Counting: rate∝I ⇒ recorded density∝I. **Solid record-side content.**
- [x] 1.3 Mechanical homogenization (negative): Kapitza/∇I-type; occupation does not lock to I. Mechanical route closed.
- [ ] 1.4 Score route — **demoted**. Mean Poisson score ≡0; previous sim circular. Not an independent derivation.
- [x] 1.5 Synthesis: ontology (measurement records) rests on 1.3 + 1.2. See docs/PHASE1_SYNTHESIS.md.

## Phase 2: Quantitative experimental prediction

- [x] 2.1 Explicit visibility kernels (geometric τ_c vs phase τ_φ). simulations/09_visibility_kernels.py
- [x] 2.2 Realistic 50–200 eV electron parameter tables.
- [x] 2.3 Competing effects + feasibility notes.

## Phase 3: Dynamics & simulations

- [x] 3.1 Locking + L¹ convergence under D∝1/I; negative control (constant D). simulations/10_locking_L1_convergence.py + results/RESULT_N10_locking_L1.md
- [x] 3.2 Finite-resolution gate averaging + triangle kernel checks. simulations/11_finite_resolution_averaging.py + results/RESULT_N11_finite_resolution.md
- [x] 3.3 run_all.sh includes 04–11; provenance notes N-10/N-11; verification layer live.

## Verification & reproducibility

- [x] Executable sympy derivations: poisson_score, kapitza_effective_potential, fp_stationary_diffusion
- [x] VERIFICATION_LOG.md, RESULT_TEMPLATE.md, requirements.txt, run_all.sh
- [x] Critical-review trail for 1.4 audit permanent in VERIFICATION_LOG
- [ ] Remaining provenance notes (N-05–N-09); optional CI

## Phase 4: Paper & packaging

- [ ] 4.1 Expand Core Edition to full article (Wallstrom / multi-particle flagged open)
- [ ] 4.2 Align README, LAYMANS_GUIDE, paper with transparent post-audit status
- [ ] 4.3 arXiv-ready version + submission plan

---

**One-line status:** Mechanical route closed (1.3); record-side reachability by counting (1.2); geometric τ_c visibility prediction in place; dynamics demos under assumed structure. Ontology = measurement records. Multi-particle/config-space untouched.

*Last updated: 2026-07-30 — Phase 1–3 complete under verifiability standard. Next: Phase 4.*
