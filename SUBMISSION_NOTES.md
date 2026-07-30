# Submission notes --- RTT Core Edition 4.0.1

Practical notes for posting the working note (arXiv or similar).

## What to upload

| File | Role |
|------|------|
| `paper/RTT_Core_Edition_4.0.1.tex` | Primary source (post-audit) |
| Compiled PDF from that `.tex` | Reader target |
| Optional: this repo URL in comments | Code + simulations + verification log |

Do **not** upload the legacy pointer `paper/RTT_Core_Edition_4.0.tex` as the main manuscript.

## Recommended arXiv metadata

- **Primary category:** quant-ph
- **Secondary (optional):** physics.hist-ph
- **Title:** Resolution Time Theory: Core Edition 4.0 --- An Obstruction, a Record-Side Reading, and a Test
- **Authors:** Joshua B. Girod
- **Comments line (suggested):** Independent research working note. Single-particle equilibrium sector; multi-particle and Wallstrom issues stated open. Companion code: https://github.com/nentrapper-g-rod/Resolution-Time-Theory

## Endorsement (quant-ph)

First-time arXiv submitters in quant-ph often need an endorser. Options:

1. Ask a researcher who already posts to quant-ph and knows the work or adjacent literature (stochastic mechanics, SED, foundations).
2. Use arXiv's endorsement system: find an endorser in quant-ph with an appropriate subject class.
3. If endorsement is delayed, the GitHub repo + PDF still functions as a citable working note (use CITATION.cff / Zenodo DOI later if desired).

This note does not claim journal peer review.

## Honesty constraints (do not weaken before submit)

- Mechanical route is **closed** (negative result), not pending.
- Equilibrium content that survives is **counting / measurement records**, not a derived trajectory force.
- 1.4 score route is **demoted**; do not restore the circular Langevin claim.
- Wallstrom, configuration space, and preferred-frame issues remain **open**.

## Cover / comments paragraph (copy-ready)

> RTT is an independent research working note. Phase-1 analysis rules out pure high-frequency mechanical averaging as the origin of density proportional to intensity and identifies ordinary intensity-proportional counting as the record-side content that recovers the pattern. The primary novel, potentially falsifiable handle is a geometric resolution time tau_c ~ Delta L / v for pulsed-gate electron interferometry. Multi-particle and Wallstrom issues are explicitly open. Source, simulations, and verification log: https://github.com/nentrapper-g-rod/Resolution-Time-Theory

## After posting

- [ ] Add arXiv identifier to README and CITATION.cff
- [ ] Tag git release `v4.0.1`
- [ ] Optional: Zenodo archive of the repo for a DOI

*Last updated: 2026-07-30*
