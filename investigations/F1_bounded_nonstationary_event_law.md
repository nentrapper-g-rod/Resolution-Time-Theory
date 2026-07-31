# F1 — Bounded attempt: non-stationary event law

**D.0 answer:** Fork 1 (bounded). Failure exit = Fork 2.  
**Relation to A.2:** Narrower retry in the regime A.2 / N-12 did not test. Does not reopen “none found” under stationary imported I.  
**Date:** 30 July 2026  
**Result:** **FAILURE (scoped)** for the class of event laws forced by the written RTT sampling form λ ∝ I (finite-window intensity sampling).

---

## Stopping rule (fixed before calculation)

One attempt. Success = F meeting all four conditions below. Failure = mean rate reduces to α⟨I⟩_G up to vanishing or α-rescaling terms for the class checked.

---

## Target regime

N-12 showed: under imported I and λ = α I with the same gate, gated statistics match standard QM when the intensity process is the usual partially coherent stationary construction.

Open gap named by N-12 / A.3: a temporal sampling rule that is not equivalent to integrating I. The only regime where a linear intensity law can still hide structure is **non-stationarity of the field (or of I) inside the resolution window**.

---

## Written RTT sampling form (not invented here)

From A.3 and the live postulate set:

\[
\lambda(t) = \alpha\, I(t), \qquad I(t) = |\phi(t)|^2,
\]

finite-window record:

\[
N = \mathrm{Poisson}\!\left(\int \mathrm{d}t\; G(t)\,\lambda(t)\right)
= \mathrm{Poisson}\!\left(\alpha \int \mathrm{d}t\; G(t)\, I(t)\right).
\tag{F1-A}
\]

Gate G ≥ 0, ∫ G = 1 without loss of generality (else α absorbs the norm).

This is the only event law **written** as a postulate. The camera-shutter metaphor in the founding vision is consistent with integrating intensity over an exposure.

---

## Mean rate under non-stationarity

Let I(t) be arbitrary (non-stationary). The expected count is

\[
\mathbb{E}[N] = \alpha \int G(t)\, I(t)\,\mathrm{d}t = \alpha\, \langle I \rangle_G.
\]

Define an effective rate against a reference intensity scale I_⋆ (e.g. peak or window-mean of a comparison model):

\[
\frac{\mathbb{E}[N]}{\langle I \rangle_G} = \alpha.
\]

**Commutation trap:** Sampling (multiply by α) and window-averaging commute for the mean:

\[
\int G(t)\,(\alpha I(t))\,\mathrm{d}t = \alpha \int G(t)\, I(t)\,\mathrm{d}t.
\]

No residual term that depends on τ_c except through the shape of G acting on I. That is ordinary gated intensity photodetection.

**Renormalization trap:** Any overall constant in G or α only rescales α. Invisible as new physics.

**Condition 3 test:** For the instantaneous law λ(t)/I(t) = α, the ratio is constant across the field by construction. Fail.

**Condition 1:** (F1-A) follows from the written postulate.  
**Condition 2:** τ_c → 0 with G → δ recovers instantaneous I; standard short-gate limit OK.  
**Condition 4:** No measurable difference beyond gated QM intensity when I is identified with I_QM.

**Verdict for (F1-A):** fails conditions 3 and 4. Not a distinct F.

---

## Candidate often suggested: filter-then-square

A different functional is the band-limited field measurement

\[
S_B = \left| \int H(t)\, \phi(t)\,\mathrm{d}t \right|^2,
\tag{F1-B}
\]

versus square-then-average

\[
S_A = \int G(t)\, |\phi(t)|^2\,\mathrm{d}t.
\tag{F1-A′}
\]

Numerically, for a non-stationary pulse φ(t) = e^{-t^2/(2σ^2)} e^{iωt} and rectangular unit-integral gate of width T=1:

| σ | ω | S_A | S_B | S_A/S_B |
|---|-----|------|------|--------|
| 0.3 | 0 | 0.522 | 0.463 | 1.13 |
| 0.3 | 5 | 0.522 | 0.094 | 5.56 |
| 0.3 | 20 | 0.522 | ~0 | ≫1 |
| 2.0 | 0 | 0.980 | 0.980 | 1.00 |
| 2.0 | 20 | 0.980 | 0.003 | ≫1 |

So S_A and S_B **differ** when the field oscillates or varies inside the window. That is real mathematics.

### Is (F1-B) forced by RTT’s written sampling postulate?

**No.** The written law is λ = α I with I = |φ|², which is the square-then-average chain (F1-A′), not filter-then-square. Adopting (F1-B) would be a **new** postulate about the detector coupling (linear filtering of the amplitude before the intensity nonlinearity).

That may be physically interesting as an ordinary electromagnetics model of a band-limited antenna. It is **not** derived from the present RTT postulate set. Inserting it to obtain a difference would violate the hard constraint (no F invented only to manufacture a prediction) and would fail Condition 1 as stated for this attempt (“follows from RTT’s sampling postulate”).

If a future Fork 1 were ever reopened, it would have to **promote** (F1-B) (or another coupling) to an explicit postulate and then confront existing interference data — that is a different program, not this bounded attempt.

---

## Analytic statement of failure (class tested)

**Class:** Event rates of the form λ(t) = α I(t) with I = |φ|², records Poisson with mean ∫ G λ, G a normalized resolution window, φ any complex waveform (stationary or not).

**Theorem (elementary):**
\[
\mathbb{E}[N] = \alpha \int G(t)\, I(t)\,\mathrm{d}t.
\]
Hence:

1. Sampling and averaging commute for the mean (trap 2).
2. λ(t)/I(t) = α constant (condition 3 fail).
3. When I = I_QM, predictions coincide with gated standard intensity detection (condition 4 fail).
4. Non-stationarity changes ⟨I⟩_G but does not produce a term outside the α⟨I⟩_G family (no new structural prediction).

**Scoped claim:** For this class, the present postulates do **not** supply a distinct event law in the non-stationary window regime. This does **not** prove that no distinct F can exist under some other postulate set.

---

## Four conditions — scorecard

| # | Condition | Outcome |
|---|-----------|--------|
| 1 | From RTT sampling postulate | (F1-A) yes; distinct alternatives not forced |
| 2 | τ_c → 0 recovers standard | yes for (F1-A) |
| 3 | Not equivalent to λ = αI | **fail** for (F1-A); (F1-B) not admitted |
| 4 | One measurable difference | **fail** for (F1-A) under imported I |

**Overall:** FAILURE (scoped).

---

## Handoff to Fork 2

Do not linger. Fork 2 write-up should center:

1. Negative mechanical result (N-07).
2. Record ontology from counting under assumed λ ∝ I.
3. Conditional equivalence (N-12) in the stationary imported-I sector.
4. Sharpened line: the missing ingredient for a distinct single-particle prediction was a non-stationary (or otherwise non–intensity-linear) event law; the present postulates were checked in that regime and do not supply one.

---

*F1 complete — 30 July 2026 — failure exit taken.*
