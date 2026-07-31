# A.3 — Explicit detector / event law

**Purpose:** Write the detection chain as equations, not philosophy. State whether the present RTT form differs from standard gated quantum intensity detection.

**Date:** 30 July 2026  
**Status:** Complete for the *present* postulate set.  
**Result:** The only written RTT event law is ordinary intensity-proportional counting. When \(I = I_{\mathrm{QM}}\), it is **equivalent** to the standard gated intensity model. A distinct functional \(\mathcal{F}\) remains **Missing**.

---

## 1. Chain (what must be specified)

```
Field (or intensity)
        ↓
Detector coupling
        ↓
Gate / temporal window G(t)
        ↓
Event-rate functional
        ↓
Threshold / Poisson draw
        ↓
Recorded event (location, time, bin)
```

Each arrow needs a formula.

---

## 2. Standard quantum comparator (gated intensity)

Let \(I_{\mathrm{QM}}(x,t)\) be the time-dependent intensity from the quantum state (or the equivalent partially coherent classical intensity that reproduces the same first-order fringes).

Detector gate \(G(t)\ge 0\) with \(\int G(t)\,dt = 1\) (or any fixed normalization).

**Expected counts in spatial bin \(B\):**

\[
\boxed{
\mathbb{E}\,[N_B]
=
\eta
\int_B\!dx
\int\!dt\;
G(t)\;
I_{\mathrm{QM}}(x,t)
}
\tag{QM}
\]

with efficiency \(\eta > 0\). Fluctuations: \(N_B \sim \mathrm{Poisson}(\mathbb{E}\,[N_B])\) in the simplest model (or multinomial given a fixed total).

This is the null detector model used in N-12.

---

## 3. Present RTT event law (what is actually written in the repo)

### 3.1 Intensity

Two readings appear in the program:

| Reading | Status |
|---------|--------|
| \(I\) from classical interference of a high-frequency field | **Assumed / native** as a classical picture |
| \(I = I_{\mathrm{QM}} = |\psi|^2\) (envelope) when comparing to QM experiments | **Imported** for the N-12 null model |

No independent derivation of \(I\) that differs from \(|\psi|^2\) while matching established fringe data is written.

### 3.2 Coupling and rate

The only explicit rate law in the repo is

\[
\boxed{
\lambda(x,t) = \alpha\, I(x,t)
}
\tag{RTT-rate}
\]

with \(\alpha > 0\) constant (or slowly varying efficiency). Status: **Assumed** (Claim Map §3).

### 3.3 Gate

Same class of gates as QM:

\[
\Lambda_G(x) = \int\!dt\; G(t)\;\lambda(x,t) = \alpha \int\!dt\; G(t)\; I(x,t).
\tag{RTT-gate}
\]

### 3.4 Recorded events

\[
\boxed{
N_B \sim \mathrm{Poisson}\!\left(
\int_B\!dx\;\Lambda_G(x)
\right)
}
\tag{RTT-record}
\]

Empirical density of recorded locations tracks \(I\) by the LLN when \(\lambda \propto I\) (N-06). Status: **Derived** from (RTT-rate).

---

## 4. Equivalence theorem (present form)

**Assumptions.**

1. \(I(x,t) = I_{\mathrm{QM}}(x,t)\) (imported intensity).
2. \(\lambda = \alpha I\) (RTT-rate).
3. Same gate \(G\) and same binning as the quantum detector model.
4. Poisson (or multinomial) sampling as above.

**Conclusion.**

\[
\mathbb{E}\,[N_B]^{\mathrm{(RTT)}}
=
\alpha
\int_B\!dx
\int\!dt\;
G(t)\;
I_{\mathrm{QM}}(x,t)
\;
\propto
\;
\mathbb{E}\,[N_B]^{\mathrm{(QM)}}.
\]

Normalized spatial distributions agree. Gated visibility agrees. This is the N-12 null model in equation form.

**Status:** **Derived** under the assumptions. Not a new prediction.

---

## 5. What a *distinct* RTT law would have to look like

A distinct law must break at least one assumption in §4. Schematically:

\[
\boxed{
\lambda_{\mathrm{RTT}}(x,t)
=
\mathcal{F}\bigl[\Phi,\, G;\, x,t\bigr]
}
\tag{RTT-distinct}
\]

where \(\Phi\) is an underlying field (or hidden state), and

\[
\mathcal{F}\bigl[\Phi,\, G\bigr]
\;\not\equiv\;
\alpha\, I_{\mathrm{QM}}[\Phi]
\]

as functionals (after the same coarse-graining), *or* \(I\) itself is not identified with \(|\psi|^2\).

Examples of structure (illustrative only — **not** adopted as postulates here):

- Threshold on instantaneous amplitude: \(\mathcal{F} \propto \Theta(|\Phi|-\Phi_0)\) with rate of crossings.
- Nonlinear response: \(\mathcal{F} \propto |\Phi|^{2n}\), \(n\neq 1\).
- History-dependent kernel: \(\mathcal{F} = \int ds\, K(t-s)\, |\Phi(s)|^2\) with \(K \neq G\) in a way that does not reduce to gated \(I_{\mathrm{QM}}\).
- Phase-sensitive coupling that survives ensemble averaging differently from \(I_{\mathrm{QM}}\).

**None of these is written as an RTT postulate in the repo.** Status: **Missing**.

Any candidate \(\mathcal{F}\) must still:

1. Recover established interference results where they are solid.
2. State limits \(\Delta L \to 0\), \(\tau_g \to 0\), \(\tau_g \to \infty\), narrowband / broadband.
3. Be confronted with existing single-particle data (N-12-style benchmark).

---

## 6. Mechanical sector (not a detector law)

For clarity: particle mechanics under a high-frequency field with Kapitza / multiplicative-noise structure was tested and **does not** supply \(\rho \propto I\) (N-07). That negative result is about trajectories, not about the detector functional \(\mathcal{F}\). It does not fill §5.

---

## 7. Score function (not a detector law)

The Poisson score

\[
\partial_x \log p(k\mid x) = (k-\lambda)\,\partial_x\log I
\]

has mean zero (D-01). It does not define a new event rate. The earlier dynamical use of \(\nabla\log I\) as a forced drift was **Withdrawn**.

---

## 8. One-line verdict for the Claim Map

| Object | Equation | Status |
|--------|----------|--------|
| Present RTT rate | \(\lambda = \alpha I\) | **Assumed** |
| Present RTT record | Poisson gated \(\lambda\) | **Derived** from rate |
| Equivalence to gated QM when \(I=I_{\mathrm{QM}}\) | §4 | **Derived** |
| Distinct \(\mathcal{F}\) with \(P_{\mathrm{RTT}}\neq P_{\mathrm{QM}}\) | (RTT-distinct) | **Missing** |

---

## 9. Implication for the fork

- **Fork 1 (research program):** Propose a specific \(\mathcal{F}\) in (RTT-distinct), derive limits, run an N-12-style comparison, and accept falsification if \(\Delta P = 0\) in all tested regimes or if established fringes break.
- **Fork 2 (interpretive framework):** Keep (RTT-rate)–(RTT-record) as a reconstruction of equilibrium statistics; do not claim a distinct single-particle prediction; center the paper on the negative mechanical result + record ontology.

A.3 does not choose the fork. It removes the option of implying a distinct detector law that has not been written.

---

## 10. Minimal checklist for any future distinct law

- [ ] Write \(\mathcal{F}\) explicitly.
- [ ] Prove or disprove reduction to \(\alpha I_{\mathrm{QM}}\) under ensemble + gate.
- [ ] Limits: \(\Delta L\to 0\), \(\tau_g\to 0\), \(\tau_g\to\infty\), narrowband, broadband.
- [ ] Numerical \(P_{\mathrm{RTT}}-P_{\mathrm{QM}}\) on a single interferometer (extend N-12).
- [ ] Update Claim Map: move (RTT-distinct) from Missing to Assumed/Derived only after the above exist.

*A.3 complete — 30 July 2026.*
