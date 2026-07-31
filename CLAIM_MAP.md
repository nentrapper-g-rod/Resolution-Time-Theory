# RTT Claim Map

**Purpose:** One place that distinguishes what is established, imported, interpretive, new, withdrawn, or still missing.  
**Rule:** No new scientific claims. Seeded from Core Edition 4.1, VALIDATION.md, N-12, and the Phase-1 result notes.  
**Status tags used here:**

| Tag | Meaning |
|-----|--------|
| **Proven** | Standard physics or an exact theorem used as-is |
| **Derived** | Follows from stated premises by math or LLN |
| **Shown-numerically** | Supported by a committed simulation / derivation script |
| **Imported** | Taken from another theory; not derived inside RTT |
| **Assumed** | Postulated inside RTT; not derived |
| **Interpretation** | Ontology or framing choice; not forced uniquely by the math |
| **Speculation** | Suggestive, exploratory, or not yet constrained |
| **Withdrawn** | Previously claimed; later corrected or demoted |
| **Missing** | Required for a distinct prediction; not written yet |
| **Open** | Named limitation; not addressed |

---

## 1. Standard / imported physics (not uniquely RTT)

| Claim | Status | Evidence / note |
|-------|--------|----------------|
| Classical interference produces an intensity envelope \(I\) | **Proven** | Standard wave optics |
| Path difference \(\Delta L\) implies travel-time difference \(\Delta L/v\) | **Proven** | Kinematics |
| Source bandwidth defines a temporal coherence scale \(\tau_\phi \sim \hbar/\delta E\) | **Proven** | Standard coherence theory |
| A detector gate integrates or convolves a time-dependent signal | **Proven** | Standard detector modeling |
| Kapitza / ponderomotive high-frequency averaging yields forces related to amplitude gradients (\(\propto \nabla I\)-type) | **Proven** | Classical high-frequency limit; `derivations/kapitza_effective_potential.py` |
| Itô / Stratonovich conversion for \(D \propto I\) still produces \(\nabla I\)-type drift, not \(\nabla\log I\) | **Proven** | Stochastic calculus; Wong–Zakai |
| Inhomogeneous Poisson process with rate \(\lambda \propto I\) has recorded locations distributed \(\propto I\) | **Proven** / **Derived** | LLN / counting; ordinary photodetection |
| Nelson free-packet dispersion | **Imported** | Nelson (1966); not derived from the RTT field |

---

## 2. Negative technical results (RTT work product)

| Claim | Status | Evidence / note |
|-------|--------|----------------|
| Pure high-frequency mechanical averaging of the tested class does **not** lock occupation \(\rho\) to \(I\) | **Shown-numerically** | N-07; mechanical route **closed** for that model class |
| Fokker–Planck with \(F \propto \nabla I\) and \(D \propto I\) does **not** have stationary \(\rho \propto I\) | **Proven** / **Derived** | Standard FP structure |
| Mean Poisson score \(E[(k-\lambda)\nabla\log I] = 0\) | **Proven** | `derivations/poisson_score.py` (D-01) |
| Independent “score drives \(\nabla\log I\) lock” route | **Withdrawn** | First sim hard-coded the drift; collapses to counting (N-08) |

These are the strongest technical contributions so far. They constrain mechanisms; they do not by themselves supply a new observable law.

---

## 3. Record-side statements

| Claim | Status | Evidence / note |
|-------|--------|----------------|
| Event rate \(\lambda \propto I\) | **Assumed** | Ordinary detector physics; **not** derived from particle mechanics under the field |
| Given \(\lambda \propto I\), recorded density \(\propto I\) | **Derived** | Counting / LLN (N-06) |
| Zero-drift Itô diffusion with **assumed** \(D \propto 1/I\) reaches \(\rho \propto I\) | **Shown-numerically** | Consistency only (N-05, N-10); does **not** derive \(D\) from mechanics |
| Single-particle equilibrium density that tracks \(I\) is best read as a density of **measurement records** | **Interpretation** | Framing supported by 1.3 + 1.2; not uniquely forced |

---

## 4. Gate / visibility sector

| Claim | Status | Evidence / note |
|-------|--------|----------------|
| Geometric identification \(\tau_c \sim \Delta L/v\) as a laboratory timescale | **Assumed** | Kinematic scale; not a new dynamical law |
| Under **imported** \(I = \|\psi\|^2\) and \(\lambda \propto I\), gated visibility depends only on \(r = \tau_c/\tau_\phi\) | **Derived** / **Shown-numerically** | N-12; analytic envelope \(\exp(-r^2/2)\) for Gaussian spectrum |
| At benchmark \(r \approx 51\), gated \(V_{\mathrm{QM}} \approx 0\) across wide \(\tau_g\) range | **Shown-numerically** | N-12 |
| Phenomenological sinc kernel \(V_{\mathrm{geom}} = \|\mathrm{sinc}((\tau_c/\tau_g)/\pi)\|\) as an RTT **prediction** | **Withdrawn** as prediction / **Speculation** as exploratory form | N-12: excluded under the stated premises at large \(r\); not derived from RTT postulates |
| Finite-resolution sampling of a classical carrier produces a response **different** from integrating standard quantum intensity | **Missing** | No explicit event law written that differs from \(\int G(t)\, I_{\mathrm{QM}}\,dt\) |

---

## 5. Ontology and program framing

| Claim | Status | Evidence / note |
|-------|--------|----------------|
| RTT is a candidate classical research program, not a claim that QM is wrong about experimental numbers | **Interpretation** | Program statement |
| Preferred frame / master clock for Bell-type correlations | **Speculation** | No construction given; comparison table must not claim an existing Bell model |
| Multi-particle / configuration-space account | **Open** / **Missing** | Explicitly untouched |
| Wallstrom single-valuedness resolved by RTT | **Open** | Sidestepped by 1-D single-particle scope; not solved |
| Lorentz / no-signaling analysis completed | **Open** | Named; not done |

---

## 6. The blank row (what would be uniquely RTT)

| Quantity | Standard QM | RTT as presently written |
|----------|-------------|-------------------------|
| \(\Delta L\), \(v\), \(\Delta L/v\) | yes | yes (kinematics) |
| Coherence time \(\tau_\phi\) | yes | yes (imported bandwidth) |
| Detector gate \(G(t)\) | yes | yes |
| Rate \(\lambda \propto I_{\mathrm{QM}}\) | standard photodetection | **Assumed** (same form) |
| **Distinct temporal event law** | — | **Missing** |
| **Independently derived intensity** | \(\|\psi\|^2\) | **Missing** (currently imported when comparing to QM) |

Until the blank row is filled by an equation standard QM would reject, the single-particle record sector remains **conditionally equivalent** to standard QM under the N-12 premises.

---

## 7. One-line summary by sector

| Sector | Verdict |
|--------|--------|
| Mechanical origin of \(\rho \propto I\) | **Ruled out** (tested class) |
| Record-side counting under \(\lambda \propto I\) | **Derived** from an **Assumed** rate |
| Score-function dynamical derivation | **Withdrawn** |
| Measurement-record ontology | **Interpretation** |
| Gate response under imported \(I\) + \(\lambda \propto I\) | **Degenerate with QM** (N-12, scoped) |
| Distinct RTT detector law | **Missing** |
| Multi-particle / Wallstrom / Lorentz | **Open** |

---

## 8. What this map does *not* do

- It does not add predictions.
- It does not promote Missing items to Assumed or Speculation by silence.
- It does not treat \(\tau_c \sim \Delta L/v\) as a parameter-free new law.
- It does not claim that “no RTT experiment can ever exist” — only that under present postulates the gated single-particle sector has not produced a distinct equation.

---

## 9. Next actions this map implies

1. **A.2** — Search for the first equation standard QM would reject; if none, record that as a result.
2. **A.3** — Write Field → coupling → threshold → event as equations; compare to \(\int G\, I_{\mathrm{QM}}\).
3. Keep phenomenological kernels out of the “derived” column until derived.

*Claim Map v1.0 — 30 July 2026 — seeded only from existing repo content.*
