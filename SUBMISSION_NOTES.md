# Submission notes — RTT Core Edition 4.1

Practical notes for posting the working note to arXiv (or similar).

## What to upload

| File | Role |
|------|------|
| `paper/RTT_Core_Edition_4.1.tex` | Primary source |
| `paper/figures/*.pdf` | Figures (run `python paper/generate_figures.py` first) |
| Compiled `RTT_Core_Edition_4.1.pdf` | Reader target |
| Comments field: repo URL | Code + simulations + verification log |

Do **not** upload the legacy pointer `paper/RTT_Core_Edition_4.0.tex`.

## Recommended arXiv metadata

- **Primary category:** quant-ph
- **Secondary (optional):** physics.hist-ph
- **Title:** Resolution Time Theory: Core Edition 4.1 — An Obstruction, a Record-Side Reading, and a Test
- **Authors:** Joshua B. Girod
- **Comments line (copy-ready):** Independent research working note (8 pages). Single-particle equilibrium sector; multi-particle and Wallstrom issues stated open. Companion code: https://github.com/nentrapper-g-rod/Resolution-Time-Theory

## Step-by-step arXiv upload

1. **Account:** Log in at https://arxiv.org (create account if needed).
2. **Endorsement:** If arXiv asks for quant-ph endorsement, request it via the endorsement system or from a researcher who posts to quant-ph (foundations / stochastic mechanics / SED adjacent).
3. **Start new submission** → category **quant-ph**.
4. **Upload:**
   - Prefer: a single `.tar.gz` or `.zip` containing `RTT_Core_Edition_4.1.tex` + `figures/` PDFs, **or** upload the compiled PDF only (PDF-only is allowed; source preferred for TeX).
   - Local build:
     ```bash
     python paper/generate_figures.py
     cd paper && pdflatex RTT_Core_Edition_4.1.tex && pdflatex RTT_Core_Edition_4.1.tex
     ```
5. **Metadata:** paste title, author, abstract from the `.tex`, and the comments line above.
6. **Preview** carefully (abstract, PDF, no over-claims).
7. **Submit.** After announcement, note the arXiv id (e.g. `2607.xxxxx`).

## Endorsement (quant-ph)

First-time submitters in quant-ph often need an endorser.

1. Ask a researcher who already posts to quant-ph in foundations / stochastic mechanics / SED.
2. Use arXiv’s endorsement interface for quant-ph.
3. If delayed: the GitHub repo + PDF remain a citable working note (CITATION.cff; optional Zenodo DOI).

This note does **not** claim journal peer review.

## Honesty constraints (do not weaken before submit)

- Mechanical route is **closed** (negative result), not pending.
- Surviving equilibrium content is **counting / measurement records**, not a derived trajectory force.
- 1.4 score route is **demoted**; do not restore the circular Langevin claim.
- Wallstrom, configuration space, and preferred-frame issues remain **open**.

## Cover / comments paragraph (copy-ready)

> RTT is an independent research working note. Phase-1 analysis rules out pure high-frequency mechanical averaging as the origin of density proportional to intensity and identifies ordinary intensity-proportional counting as the record-side content that recovers the pattern. The primary novel, potentially falsifiable handle is a geometric resolution time tau_c ~ Delta L / v for pulsed-gate electron interferometry. Multi-particle and Wallstrom issues are explicitly open. Source, simulations, and verification log: https://github.com/nentrapper-g-rod/Resolution-Time-Theory

## After posting

- [ ] Add arXiv identifier to README and CITATION.cff
- [ ] Tag git release `v4.1.0`
- [ ] Optional: Zenodo archive of the repo for a DOI

*Last updated: 2026-07-30 — aligned to Core Edition 4.1*
