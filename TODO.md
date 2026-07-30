# RTT Research Program TODO

**Principles:** Every claim must be backed by exact math or reproducible numerical data. No over-claiming. Update this file and the repo after each completed item. Keep status transparent.

**Current focus:** Exhaust honest progress on open problems before any external submission.

## Phase 1: Open Problem #1 — Equilibrium structure without pure insertion

- [x] 1.1 Consistency check: zero-drift + D(x) ∝ 1/I yields ρ∞ ∝ I (exact + Monte-Carlo). Restatement of the target, not a derivation.
- [x] 1.2 Consistency check: lattice rates / Poisson counting ∝ I yield stationary / empirical density ∝ I. Restatement of the target, not a derivation. **This is the solid record-side content.**
- [x] 1.3 Mechanical homogenization (negative result, load-bearing): pure high-frequency averaging recovers Kapitza/ponderomotive ∇I-type terms; occupation does **not** lock to I. Rules out particle mechanics as origin of the structure. (Itô audit: additive noise, result robust.)
- [ ] 1.4 Bayesian / score-function route — **demoted**. Previous claim that the Poisson score supplies a net ∇log I drift was incorrect (mean score ≡ 0). The corrected script demonstrates the mean-score-zero fact and the counting result already present in 1.2. Not an independent non-circular derivation.
- [x] 1.5 Synthesis: ontology conclusion (measurement records) rests on 1.3 + 1.2. See docs/PHASE1_SYNTHESIS.md (to be updated for the demotion).

## Phase 2: Quantitative experimental prediction

- [x] 2.1 Explicit visibility kernels (geometric τ_c vs phase τ_φ). See simulations/09_visibility_kernels.py.
- [x] 2.2 Data tables for realistic 50–200 eV electron parameters.
- [x] 2.3 Competing effects + feasibility notes (initial literature map).

## Phase 3: Dynamics & simulations

- [ ] 3.1 Full state-dependent diffusion (or log-drift) simulations showing locking + L¹ convergence
- [ ] 3.2 Finite-resolution trajectory averaging demos
- [ ] 3.3 Clean runnable notebooks / scripts + figures

## Phase 4: Paper & packaging

- [ ] 4.1 Expand Core Edition to full article (related work on Nelson/SED/Wallstrom, figures, bibliography). Note multi-particle/config-space remains open.
- [ ] 4.2 Update README, LAYMANS_GUIDE, and paper with new results while keeping status transparent
- [ ] 4.3 arXiv-ready version + endorsement / submission plan

---

*Last updated: Critical correction — 1.4 demoted after audit. Mean Poisson score is zero; previous Langevin was circular. Solid Phase-1 content is 1.3 (mechanics closed) + 1.2 (counting). Ontology still stands on that footing.*
