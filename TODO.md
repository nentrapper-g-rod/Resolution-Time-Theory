# RTT Research Program TODO

**Principles:** Every claim must be backed by exact math or reproducible numerical data. No over-claiming. Prefer L1/KL over correlation.

**Status:** Phase 1–3 + documentation packaging **complete**. Remaining items are human-only (PDF binary upload, arXiv account).

## Phase 1: Open Problem #1

- [x] 1.1 D∝1/I ⇒ ρ∝I (consistency only)
- [x] 1.2 Counting: rate∝I ⇒ recorded density∝I (**solid**)
- [x] 1.3 Mechanical homogenization (**negative** — route closed)
- [ ] 1.4 Score route — **demoted** (mean Poisson score = 0; not an independent derivation)
- [x] 1.5 Synthesis → measurement-record ontology on 1.3+1.2

## Phase 2–3

- [x] Visibility kernels + electron tables (Phase 2)
- [x] L1 locking + finite-resolution averaging (Phase 3)
- [x] run_all.sh + verification layer

## Verification & reproducibility

- [x] sympy derivations; VERIFICATION_LOG; RESULT_TEMPLATE
- [x] LICENSE, CITATION.cff, CHANGELOG.md
- [x] Provenance notes N-05–N-11 in `results/`
- [x] Optional CI: `.github/workflows/verify.yml`
- [ ] Compiled PDF under `paper/` — **manual** (see `paper/BUILD.md`; local artifact exists)

## Phase 4: Paper & packaging

- [x] 4.2 Public docs aligned (README, LAYMANS, paper 4.0.1, checklists)
- [x] Companion calculations section in paper
- [x] ARXIV_CHECKLIST.md + SUBMISSION_NOTES.md + paper/BUILD.md
- [ ] 4.1 Full article expansion with figures — **deferred** (optional; working note is sufficient)
- [ ] 4.3 arXiv submission — **human only**
  - [ ] quant-ph endorsement if required
  - [ ] Upload source + PDF
  - [ ] Write arXiv id back into README + CITATION.cff

---

**One-line status:** Research + verification + packaging complete for a working-note release. Ontology = measurement records (1.3+1.2). You upload the PDF and post to arXiv.

*Last updated: 2026-07-30 — CI added; TODO closed except human steps.*
