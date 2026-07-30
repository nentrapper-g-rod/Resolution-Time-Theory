# RTT Research Program TODO

**Principles:** Every claim must be backed by exact math or reproducible numerical data. No over-claiming. Update this file and the repo after each completed item. Keep status transparent.

**Current focus:** Exhaust honest progress on open problems before any external submission.

## Phase 1: Open Problem #1 — Equilibrium structure without pure insertion

- [x] 1.1 Analytic + numeric confirmation: zero-drift + D(x) ∝ 1/I yields ρ∞ ∝ I (Fokker–Planck + Monte-Carlo)
- [x] 1.2 Discrete lattice master-equation / counting models with rates or detection intensity ∝ local I; stationary / empirical density ∝ I
- [ ] 1.3 Homogenization numerical of overdamped particle in fast oscillating field (document the mechanical outcome, expected to give ∇I-type terms)
- [ ] 1.4 Bayesian / score-function sketch for finite-resolution estimator
- [ ] 1.5 Honest status note: what is now motivated vs still postulated; clarify ontology (real particle dynamics vs recorded / estimated density)

## Phase 2: Quantitative experimental prediction

- [ ] 2.1 Explicit visibility kernels (geometric τ_c vs phase τ_φ)
- [ ] 2.2 Plots for realistic 50–200 eV electron parameters
- [ ] 2.3 Competing effects + feasibility notes citing ultrafast electron-beam literature

## Phase 3: Dynamics & simulations

- [ ] 3.1 Full state-dependent diffusion (or log-drift) simulations showing locking + L¹ convergence
- [ ] 3.2 Finite-resolution trajectory averaging demos
- [ ] 3.3 Clean runnable notebooks / scripts + figures

## Phase 4: Paper & packaging

- [ ] 4.1 Expand Core Edition to full article (related work on Nelson/SED/Wallstrom, figures, bibliography)
- [ ] 4.2 Update README, LAYMANS_GUIDE, and paper with new results while keeping status transparent
- [ ] 4.3 arXiv-ready version + endorsement / submission plan

---

*Last updated: Phase 1.1 and 1.2 complete. See simulations/05_state_dependent_diffusion_equilibrium.py, simulations/06_rate_and_counting_models.py and docs/NOTES_ON_EQUILIBRIUM_ROUTES.md.*
