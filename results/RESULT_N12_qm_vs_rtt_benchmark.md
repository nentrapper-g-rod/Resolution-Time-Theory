# Result note — N-12

**ID:** N-12  
**Artifact:** `simulations/12_qm_vs_rtt_benchmark.py`  
**Status:** shown-numerically / proven-analytically (ratio law); **scoped**

## Premises (explicit)

1. Single interferometer setup (two arms, fixed path difference ΔL).
2. Intensity identified with the standard quantum intensity (imported I = |ψ|² envelope).
3. Event rate λ ∝ I (ordinary counting).

This benchmark does **not** claim that no RTT experiment can ever exist. It constrains the gate response under the premises above.

## Benchmark parameters

| Quantity | Value |
|----------|-------|
| E | 100 eV |
| δE | 0.2 eV |
| ΔL | 1 μm |
| τ_c = ΔL/v | 168.6 fs |
| τ_φ = ℏ/δE | 3.29 fs |
| r = τ_c/τ_φ | 51.2 |
| Seed | `default_rng(0)` |

## Method

Stationary partially coherent complex baseband with Gaussian spectrum of width δE/ℏ. Two arms: b(t) and e^{iφ} b(t−τ_c). Gaussian gate of FWHM τ_g. Visibility from ensemble-averaged gated intensity vs phase (≥250 realizations). Repo kernels: V_geom = |sinc((τ_c/τ_g)/π)| (numpy convention); V_φ = exp(−½(τ_g/τ_φ)²).

## Result 1 — τ_c is the coherence ratio (proven-analytically + shown-numerically)

Under the premises, gated visibility depends only on r = τ_c/τ_φ. For a Gaussian spectrum the analytic envelope is exp(−r²/2).

| r | V_QM (wide gate) | exp(−r²/2) |
|---|------------------|------------|
| 0.15 | 0.988 | 0.989 |
| 0.61 | 0.831 | 0.830 |
| 2.43 | 0.061 | 0.052 |
| 9.72 | 0.005 | 0.000 |

## Result 2 — gated V ≈ 0 at r = 51 (shown-numerically)

| τ_g (fs) | V_QM | V_geom | V_φ |
|----------|------|--------|-----|
| 1 | 0.071 | 0.005 | 0.955 |
| 3 | 0.071 | 0.006 | 0.660 |
| 10 | 0.064 | 0.054 | 0.010 |
| 30 | 0.029 | 0.110 | 0.000 |
| 100 | 0.002 | 0.589 | 0.000 |
| 169 | 0.003 | 0.842 | 0.000 |
| 600 | 0.007 | 0.987 | 0.000 |
| 1000 | 0.004 | 0.995 | 0.000 |

Residuals ≲ 0.09 are finite-realization noise. V_QM stays near zero across the full gate scan.

## Result 3 — sinc kernel excluded by existing data

At this geometry the phenomenological V_geom rises toward 1 for τ_g ≳ τ_c, while the QM response remains dark. Existing broadband electron-interference practice is consistent with the ratio law, not with a gate that restores fringe contrast when path delay exceeds the coherence time.

## Structural degeneracy (conditional on premises)

If RTT imports the same I and uses λ ∝ I with the same gate, the expected count distribution matches the gated standard-quantum prediction. A distinct RTT prediction requires changing the intensity, the event-rate law, the temporal sampling rule, or the detector coupling.

## Scoped conclusion

Under the stated premises, the RTT gate model is degenerate with standard QM: visibility is fixed by r = τ_c/τ_φ, and the sinc kernel is excluded. This does **not** prove that no RTT experiment can exist.

## Open boundary — what would move the conclusion

- A non-imported intensity (derived independently of |ψ|²)
- A different event-rate functional (not λ ∝ I)
- A temporal sampling / coarse-graining rule distinct from integrating I
- Dispersive multi-path or multi-particle sectors not tested here

## How to regenerate

```bash
python simulations/12_qm_vs_rtt_benchmark.py
```

Figures: `paper/figures/fig_n12_ratio_collapse.pdf`, `paper/figures/fig_n12_gate_scan.pdf`.
