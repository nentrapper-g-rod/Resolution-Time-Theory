# A.2 — First RTT-only equation

**Question:** What is the smallest mathematical object that exists in RTT but not in standard quantum mechanics — the first equation standard QM would reject?

**Method:** List every major equation or structural claim in the present repo. For each, ask whether a textbook quantum physicist would reject it as false, or accept it as standard / kinematic / optional interpretation. Use the N-12 null model as the comparison baseline.

**Null model (N-12 premises):**
1. Single two-arm interferometer.
2. Intensity identified with standard quantum intensity (imported \(I = |\psi|^2\)).
3. Event rate \(\lambda \propto I\).

**Date:** 30 July 2026  
**Status:** Complete for the *present* postulate set. Result: **no RTT-only equation found** in the single-particle record sector.

---

## Candidates examined

### C1. \(\tau_c \sim \Delta L / v\)

| | |
|--|--|
| **What it is** | Travel time for path difference \(\Delta L\) at speed \(v\). |
| **Would QM reject it?** | **No.** It is ordinary kinematics / time-of-flight. |
| **Verdict** | **Not RTT-only.** Proven kinematics. |

### C2. \(\tau_\phi \sim \hbar / \delta E\)

| | |
|--|--|
| **What it is** | Coherence time from source bandwidth. |
| **Would QM reject it?** | **No.** Standard partial coherence. |
| **Verdict** | **Not RTT-only.** |

### C3. Kapitza / ponderomotive force \(F \propto \nabla I\)

| | |
|--|--|
| **What it is** | High-frequency classical averaging. |
| **Would QM reject it?** | **No** as classical electrodynamics / effective dynamics. QM does not use it as a substitute for Born-rule occupation, but the formula itself is standard classical physics. |
| **Verdict** | **Not RTT-only.** Used in RTT as a **negative** result: this force does **not** produce \(\rho \propto I\). |

### C4. \(\lambda(x,t) = \alpha\, I(x,t)\)

| | |
|--|--|
| **What it is** | Event rate proportional to intensity. |
| **Would QM reject it?** | **No.** Ordinary intensity-to-count conversion (photodetection). |
| **Verdict** | **Not RTT-only.** **Assumed** in RTT; same form as standard detector models. |

### C5. Recorded density \(\propto I\) given C4

| | |
|--|--|
| **What it is** | Law of large numbers on detection locations. |
| **Would QM reject it?** | **No.** Counting. |
| **Verdict** | **Derived** from C4; **not RTT-only.** |

### C6. Mean Poisson score \(E[(k-\lambda)\nabla\log I] = 0\)

| | |
|--|--|
| **What it is** | Exact identity for Poisson detection. |
| **Would QM reject it?** | **No.** Standard score of a Poisson likelihood. |
| **Verdict** | **Proven**; used to **withdraw** a bad RTT claim. Not a new law. |

### C7. \(V_{\mathrm{geom}} = \bigl|\mathrm{sinc}\bigl((\Delta L/v)/\tau_g\bigr)\bigr|\) (numpy-sinc form equivalent)

| | |
|--|--|
| **What it is** | Phenomenological gate-width visibility kernel. |
| **Would QM reject it as a general prediction?** | **Yes — as a universal fringe law at large path delay.** N-12: under imported \(I\) and \(\lambda\propto I\), visibility tracks the coherence ratio \(r = \tau_c/\tau_\phi\), not this sinc. At large \(r\), QM stays dark while the sinc rises toward 1 for large gates. |
| **Is it derived from RTT postulates?** | **No.** Exploratory / phenomenological. |
| **Verdict** | **Not a derived RTT-only equation.** Excluded as a prediction under N-12 premises. May remain only as an exploratory form. |

### C8. Measurement-record ontology

| | |
|--|--|
| **What it is** | The density tracking \(I\) is a density of records, not of trajectories under the high-frequency field. |
| **Would QM reject it?** | QM need not accept the ontology, but this is **not an equation**. It is an interpretation consistent with C4–C5 and the negative mechanical result. |
| **Verdict** | **Interpretation**, not an RTT-only dynamical law. |

### C9. Preferred frame / master clock

| | |
|--|--|
| **What it is** | Suggested for Bell-type sectors in earlier framing. |
| **Would QM reject it?** | Many interpretations reject preferred frames; but **no equation or construction is written** in this repo. |
| **Verdict** | **Speculation / Missing construction** — cannot count as an RTT-only equation that exists. |

### C10. Distinct temporal coarse-graining law

Something of the schematic form

\[
P_{\mathrm{RTT}}(\mathrm{event}\mid \text{field}, G)
\;\neq\;
P_{\mathrm{QM}}(\mathrm{event}\mid I_{\mathrm{QM}}, G)
\]

| | |
|--|--|
| **What it would be** | The first genuinely RTT-only object: a detector/event functional that differs from integrating standard quantum intensity. |
| **Does it exist in the repo?** | **No.** Claim Map marks it **Missing**. |
| **Verdict** | **Missing** — this is the blank row, not a filled equation. |

---

## Conditional equivalence (restated)

**Theorem (informal; N-12).**  
If RTT (i) imports \(I_{\mathrm{QM}}\), (ii) sets \(\lambda = \alpha I_{\mathrm{QM}}\), and (iii) uses the same gate \(G\) and efficiency as the quantum detector model, then the expected RTT count distribution matches the gated standard-quantum prediction (up to normalization).

**Corollary.** Under those premises there is **no** observational distinction in the single-particle gated sector, and therefore **no** equation that standard QM must reject *inside that sector*.

A distinct prediction requires changing at least one of: the intensity, the event-rate functional, the temporal sampling / coarse-graining rule, or the hidden dynamics — and writing that change as mathematics.

---

## Answer to A.2

**Under the present postulate set, no RTT-only equation was found in the single-particle record sector.**

What exists today:

- Standard kinematics and coherence (C1–C2)
- Standard classical averaging used as a **negative** result (C3)
- An **assumed** rate law shared with ordinary detection (C4)
- **Derived** counting (C5)
- A **withdrawn** score route (C6 misuse)
- An **excluded** phenomenological sinc kernel (C7)
- An **interpretation** of records (C8)
- A **Missing** distinct detector law (C10)

The first equation standard QM would reject is **not yet written**. The blank row in the Claim Map remains blank.

This is not a failure of the research program. It is a classification result:

> RTT, as presently formulated, does not yet contain a dynamical or detection law that is observationally distinct from standard quantum mechanics in the single-particle sector under its own working premises.

---

## The interpretive fork (forced by this result)

**Fork 1 — Fill the blank row (research program).**  
Write an explicit event law
\[
\lambda_{\mathrm{RTT}} = \mathcal{F}[\text{field}, G]
\]
with \(\mathcal{F}\) not equal to \(\alpha\, I_{\mathrm{QM}}\) (or an independently derived intensity not identified with \(|\psi|^2\)), derive its limits, and confront existing interference data.

**Fork 2 — Interpretive framework.**  
Accept conditional equivalence, keep the negative mechanical result and the record-side reading, and present RTT as an ontology / reconstruction of equilibrium statistics without a new single-particle prediction.

Both forks are legitimate. Neither is optional silence: the Claim Map and this note make the absence visible.

---

## What A.2 does *not* claim

- It does **not** claim that no RTT experiment can ever exist.
- It does **not** claim multi-particle or Lorentz sectors are settled.
- It does **not** promote the sinc kernel back to a prediction.
- It does **not** add a new postulate to fill the blank row by rhetoric.

---

## Next step (A.3)

Write the detector chain as equations even if the only honest present form is

\[
\lambda = \alpha I,\qquad
N(\mathrm{bin}) = \mathrm{Poisson}\Bigl(\int dt\, G(t)\,\lambda\Bigr),
\]

and mark explicitly that this is **equivalent** to the standard gated intensity model when \(I = I_{\mathrm{QM}}\). That makes the Missing status of any *distinct* \(\mathcal{F}\) impossible to miss.

*A.2 complete — 30 July 2026.*
