# RTT Research Program TODO

**Principles:** Every claim must be backed by exact math or reproducible numerical data. No over-claiming. Prefer L1/KL over correlation; executable algebra for key identities. Default AI status: unverified until checked.

**Current focus:** Phase 4 --- paper packaging under the honest post-audit framing.

## Phase 1: Open Problem #1 --- Equilibrium structure without pure insertion

- [x] 1.1 Consistency check: D proportional to 1/I implies rho proportional to I. Restatement, not a derivation.
- [x] 1.2 Counting: rate proportional to I implies recorded density proportional to I. **Solid record-side content.**
- [x] 1.3 Mechanical homogenization (negative): Kapitza/grad-I type; occupation does not lock to I. Mechanical route closed.
- [ ] 1.4 Score route --- **demoted**. Mean Poisson score is zero; previous sim circular. Not an independent derivation.
- [x] 1.5 Synthesis: ontology (measurement records) rests on 1.3 + 1.2. See docs/PHASE1_SYNTHESIS.md.

## Phase 2: Quantitative experimental prediction

- [x] 2.1 Explicit visibility kernels (geometric tau_c vs phase tau_phi). simulations/09
- [x] 2.2 Realistic 50--200 eV electron parameter tables.
- [x] 2.3 Competing effects + feasibility notes.

## Phase 3: Dynamics & simulations

- [x] 3.1 Locking + L1 convergence under D proportional to 1/I; negative control. simulations/10 + RESULT_N10
- [x] 3.2 Finite-resolution gate averaging. simulations/11 + RESULT_N11
- [x] 3.3 run_all.sh includes 04--11; verification layer live.

## Verification & reproducibility

- [x] Executable sympy derivations; VERIFICATION_LOG; RESULT_TEMPLATE; run_all.sh
- [x] LICENSE, CITATION.cff, CHANGELOG.md
- [ ] Remaining provenance notes (N-05--N-09); optional CI
- [ ] Compiled PDF committed under paper/ (local artifact exists)

## Phase 4: Paper & packaging

- [x] 4.2 Align public docs with post-audit status
  - [x] README scoreboard + disclaimer + full tree
  - [x] LAYMANS_GUIDE measurement-record rewrite
  - [x] paper/RTT_Core_Edition_4.0.1.tex (abstract, objections, bibliography)
  - [x] paper/RTT_Core_Edition_4.0.tex marked legacy pointer
  - [x] ARXIV_CHECKLIST.md + SUBMISSION_NOTES.md
  - [ ] Compiled PDF on GitHub (upload manually if needed)
- [ ] 4.1 Expand Core Edition toward full article (optional figures from sims)
- [ ] 4.3 arXiv submission
  - [x] Checklist + submission notes drafted
  - [ ] Endorsement / quant-ph path
  - [ ] Final PDF + source uploaded to arXiv
  - [ ] arXiv id written back to README and CITATION.cff

---

**One-line status:** Phase 1--3 complete. Ontology = measurement records (1.3 + 1.2). Phase 4.2 documentation alignment complete. Remaining: PDF on GitHub + arXiv upload / endorsement.

*Last updated: 2026-07-30 --- Phase 4.2 closed; SUBMISSION_NOTES added.*
