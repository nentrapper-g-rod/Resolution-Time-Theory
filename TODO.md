# RTT Research Program TODO

**Principles:** Every claim must be backed by exact math or reproducible numerical data. No over-claiming. Update this file and the repo after each completed item. Keep status transparent.

**Current focus:** Exhaust honest progress on open problems before any external submission.

## Phase 1: Open Problem #1 — Equilibrium structure without pure insertion

- [x] 1.1 Consistency check: zero-drift + D(x) ∝ 1/I yields ρ∞ ∝ I (exact + Monte-Carlo). Restatement of the target, not a derivation.
- [x] 1.2 Consistency check: lattice rates / Poisson counting ∝ I yield stationary / empirical density ∝ I. Restatement of the target, not a derivation.
- [x] 1.3 Mechanical homogenization (negative result, load-bearing): pure high-frequency averaging recovers Kapitza/ponderomotive ∇I-type terms; occupation does **not** lock to I. Rules out particle mechanics as origin of the structure. (Itô audit: additive noise, result robust.)
- [x] 1.4 Bayesian / score-function route with **forced** likelihood: standard detector physics (event rate λ ∝ I) makes the log-likelihood contain log I; the score therefore contains ∇ log I. This is not free insertion. Combined with 1.3, the structure is located in the measurement record / estimate. See simulations/08_bayesian_score_forced_likelihood.py.
- [x] 1.5 Synthesis: ontology conclusion (measurement records / epistemic framing) elevated to the headline. See docs/PHASE1_SYNTHESIS.md.

## Phase 2: Quantitative experimental prediction

- [x] 2.1 Explicit visibility kernels (geometric τ_c vs phase τ_φ). See simulations/09_visibility_kernels.py.
- [ ] 2.2 Plots for realistic 50–200 eV electron parameters (data tables already in 09; figure generation next).
- [ ] 2.3 Competing effects + feasibility notes citing ultrafast electron-beam literature

## Phase 3: Dynamics & simulations

- [ ] 3.1 Full state-dependent diffusion (or log-drift) simulations showing locking + L¹ convergence
- [ ] 3.2 Finite-resolution trajectory averaging demos
- [ ] 3.3 Clean runnable notebooks / scripts + figures

## Phase 4: Paper & packaging

- [ ] 4.1 Expand Core Edition to full article (related work on Nelson/SED/Wallstrom, figures, bibliography). Note multi-particle/config-space remains open.
- [ ] 4.2 Update README, LAYMANS_GUIDE, and paper with new results while keeping status transparent
- [ ] 4.3 arXiv-ready version + endorsement / submission plan

---

*Last updated: Phase 2.1 complete. Explicit geometric vs phase visibility kernels with tables for 50–200 eV. Next: plots + feasibility notes.*
