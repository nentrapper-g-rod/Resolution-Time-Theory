# arXiv packaging checklist — RTT Core Edition 4.0.1

**Category suggestion:** quant-ph  
**Type:** research working note / research program

## Content honesty (must pass before submit)

- [x] Abstract: finite-resolution under-sampling; grad-I vs grad-log-I obstruction
- [x] Abstract: mechanical route closed; counting recovers recorded density
- [x] Abstract: ontology = measurement records (not dynamical trajectory law)
- [x] Abstract: novel prediction tau_c ~ Delta L / v
- [x] Open problems named (intensity->rate; multi-particle; Wallstrom; preferred-frame)
- [x] No claim that Born rule is derived from pure classical particle mechanics
- [x] 1.4 score route not presented as independent derivation
- [x] Provenance notes N-05–N-11 committed under results/
- [x] CI workflow present (`.github/workflows/verify.yml`)

## Standard objections named in paper

- [x] Nelson (1966)
- [x] Wallstrom (1994) — **not solved**
- [x] Configuration-space / multi-particle — **open**
- [x] Preferred-frame / Lorentz tension — **open**

## Files for submission

- [x] Source: `paper/RTT_Core_Edition_4.0.1.tex`
- [ ] Compiled PDF in repo (compile via `paper/BUILD.md`; commit manually)
- [x] LICENSE (CC-BY-4.0 covers paper)
- [x] CITATION.cff

## arXiv process (human)

- [ ] Primary category: quant-ph
- [ ] Endorsement if first-time quant-ph submitter
- [ ] Author metadata matches CITATION.cff (Joshua B. Girod)
- [ ] Upload source + PDF
- [ ] After acceptance: write arXiv id into README + CITATION.cff

## Cover paragraph

RTT is an independent research working note. Phase-1 analysis rules out pure high-frequency mechanical averaging as the origin of density proportional to intensity and identifies ordinary intensity-proportional counting as the record-side content that recovers the pattern. The primary novel, potentially falsifiable handle is a geometric resolution time tau_c ~ Delta L / v for pulsed-gate electron interferometry. Multi-particle and Wallstrom issues are explicitly open. Companion code: https://github.com/nentrapper-g-rod/Resolution-Time-Theory

*Last updated: 2026-07-30*
