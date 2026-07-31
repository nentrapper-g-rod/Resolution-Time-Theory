# RTT as an interpretive framework for equilibrium records

**Author:** Joshua B. Girod  
**Date:** 30 July 2026  
**Status:** Fork 2 write-up after a bounded Fork 1 attempt (F1) failed for the written intensity-proportional class.  
**This note does not claim a new single-particle prediction under the present postulates.**

---

## What this document is

A short, honest statement of what Resolution Time Theory (RTT) currently *is*, after the mechanical route was closed, the score route was withdrawn, the stationary gate sector was shown degenerate with standard intensity detection under imported \(I\), and a bounded search for a distinct non-stationary event law failed for the written sampling form.

It is an **interpretive framework** for single-particle equilibrium *records*, not a replacement dynamics for quantum mechanics.

---

## Four pillars (settled)

### 1. Mechanical negative

High-frequency classical field dynamics of the tested class produce Kapitza / ponderomotive structure of \(\nabla I\) type. They do **not** produce a stationary occupation \(\rho \propto I\) of the form required for Born-rule locking without an additional postulate (N-07; route closed).

Status: **shown-numerically** for the class checked; mechanical route to the equilibrium sector is closed, not deferred.

### 2. Record-side counting

If the event rate is taken to be proportional to intensity,

\[
\lambda = \alpha\, I,
\]

then recorded event locations follow \(I\) by ordinary counting (law of large numbers). This is **derived** from an **assumed** rate law. It is not a derivation of the Born rule from particle mechanics under the field (N-06; A.3).

Status: **derived** from **assumed** \(\lambda \propto I\).

### 3. Conditional equivalence (stationary imported intensity)

Under the premises of N-12 — imported \(I = |\psi|^2\), rate \(\lambda = \alpha I\), same temporal gate — the gated single-particle response is **degenerate with standard quantum intensity detection**. Visibility is fixed by the coherence ratio \(r = \tau_c / \tau_\phi\). The phenomenological geometric sinc kernel is **not** a prediction of the present law (N-12; exploratory kernels quarantined).

Status: **derived** / **shown-numerically** under those premises. Scope is explicit: not a universal “no experiment can exist.”

### 4. Bounded search for a distinct event law (F1)

A.2 found no RTT-only equation in the stationary imported-\(I\) sector. F1 asked the only remaining single-particle question left open by N-12 under the *written* sampling form: does non-stationarity of the field inside the resolution window generate a rate not equivalent to \(\alpha\langle I\rangle_G\)?

For

\[
\mathbb{E}[N] = \alpha \int G(t)\, I(t)\,\mathrm{d}t = \alpha\,\langle I\rangle_G,
\]

sampling and averaging commute for the mean; \(\lambda/I = \alpha\) is constant; no structural term outside gated intensity detection appears. Filter-then-square differs mathematically from square-then-average, but it is **not forced** by the written RTT postulate \(\lambda = \alpha I\). Adopting it would be a new coupling postulate, not a result of this program’s present axioms (F1).

Status: **shown-analytically (negative)** for the intensity-proportional class; distinct \(\mathcal{F}\) remains **Missing**.

---

## The sharpened line

We identified the exact missing ingredient for a distinct single-particle prediction: an event (or coupling) law that is **not** ordinary intensity-proportional sampling — including, if one exists, a non-stationary window functional forced by RTT’s own postulates rather than inserted to create a difference.

The present postulates were checked in the regime where such a term would have had to appear. They do not supply one.

That is not a failure of honesty. It is the content of the program as it stands.

---

## What RTT is, under present postulates

| Element | Role |
|---------|------|
| Classical interference intensity \(I\) | **Imported** / standard optics when identified with \(|\psi|^2\) |
| Finite detector resolution (gate \(G\), scale related to \(\Delta L/v\)) | Kinematic / apparatus scale; **not** a free fit parameter for contrast restoration against the ratio law |
| Event rate \(\lambda = \alpha I\) | **Assumed** (ordinary detector physics) |
| Recorded density \(\propto I\) | **Derived** by counting |
| Mechanical HF route to \(\rho \propto I\) | **Ruled out** (tested class) |
| Score / \(\nabla\log I\) dynamical derivation | **Withdrawn** |
| Distinct \(\mathcal{F}\not\equiv \alpha I\) | **Missing** |
| Ontology of the equilibrium sector | **Interpretation:** measurement records under finite resolution, not an extra classical force law |

---

## What this framework is not

- Not a claim that quantum mechanics is wrong about laboratory numbers.
- Not a completed derivation of the Born rule from classical field forces.
- Not a multi-particle / entanglement theory (configuration space remains open).
- Not a preferred-frame or Bell construction (none is given).
- Not a license to treat exploratory kernels (e.g. geometric sinc) as predictions.

---

## What would reopen research-program work (Fork 1 again)

Only an **explicitly adopted** new postulate, for example:

- a field-filter-then-square coupling (or other non-linear temporal functional) stated as an axiom, with limits and a confrontation against existing interference data; or
- an independently derived intensity not identified with \(|\psi|^2\), with the same discipline.

Until such a postulate is written and tested, the honest public status is this interpretive framework plus the recorded negatives.

---

## Primary references in this repository

| Item | Location |
|------|----------|
| Claim Map | `CLAIM_MAP.md` |
| Mechanical negative | `results/RESULT_N07_homogenization.md` |
| Counting | `results/RESULT_N06_rate_and_counting.md` |
| Score withdrawal | `results/RESULT_N08_score_corrected.md` |
| Gate equivalence | `results/RESULT_N12_qm_vs_rtt_benchmark.md` |
| Detector chain | `investigations/A3_detector_event_law.md` |
| No RTT-only equation (stationary) | `investigations/A2_first_rtt_only_equation.md` |
| Non-stationary intensity sampling (F1) | `investigations/F1_bounded_nonstationary_event_law.md` |
| Core working note | `paper/RTT_Core_Edition_4.1.tex` |
| Founding vision (frozen) | `origin/` |

---

*Fork 2 note — 30 July 2026 — no new predictions under present postulates.*
