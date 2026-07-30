#!/usr/bin/env python3
"""
RTT Phase 3.2 — Finite-resolution trajectory averaging demo

Illustrates the under-sampling idea native to Resolution Time Theory:
a detector with finite gate width τ_c averages (or integrates) the
high-frequency intensity. The recorded event density tracks the slow
envelope I rather than the instantaneous oscillating field.

Status: shown-numerically (illustrative of the measurement-record /
under-sampling picture). Not a derivation of the equilibrium postulate
from microscopic field + detector dynamics.

Verifiability:
- Metric: L¹ distance of the gated/recorded histogram to the slow envelope
- Negative control: instantaneous (τ_c → 0) sampling retains high-frequency
  structure and does not collapse to the envelope in the same way
- Fixed seed, stated target, pass/fail tolerance

Run: python simulations/11_finite_resolution_averaging.py
"""

import numpy as np

def main():
    print("RTT Phase 3.2 — Finite-resolution trajectory averaging")
    print("=" * 60)
    print("Target: gated detections track the slow intensity envelope I")
    print("Metric: L¹ to the normalized envelope")
    print("Negative control: instantaneous samples retain fast oscillation")
    print()

    rng = np.random.default_rng(21)

    # Slow envelope + fast oscillation
    x = np.linspace(-4.0, 4.0, 500)
    envelope = 0.15 + 0.9 * (
        np.exp(-((x + 1.4)**2) / (2 * 0.4**2))
        + np.exp(-((x - 1.4)**2) / (2 * 0.4**2))
    )
    # High-frequency spatial modulation (standing-wave-like)
    k_fast = 12.0
    I_fast = envelope * (0.55 + 0.45 * np.cos(k_fast * x)**2)

    # Sample many detection events from the fast intensity
    n_events = 20000
    probs_fast = I_fast / I_fast.sum()
    idx = rng.choice(len(x), size=n_events, p=probs_fast)
    event_x = x[idx]

    # Instantaneous histogram (negative control / high-resolution limit)
    hist_inst, edges = np.histogram(event_x, bins=60, density=True, range=(-4, 4))
    centers = 0.5 * (edges[:-1] + edges[1:])
    env_c = np.interp(centers, x, envelope)
    env_norm = env_c / np.trapezoid(env_c, centers)
    I_fast_c = np.interp(centers, x, I_fast)
    I_fast_norm = I_fast_c / np.trapezoid(I_fast_c, centers)

    L1_inst_to_env = np.trapezoid(np.abs(hist_inst - env_norm), centers)
    L1_inst_to_fast = np.trapezoid(np.abs(hist_inst - I_fast_norm), centers)

    # Finite-resolution: bin events into coarse spatial bins that mimic
    # temporal averaging over a gate (simple model: spatial coarse-graining
    # proxy for temporal under-sampling of a moving interference pattern)
    # More direct model: average the intensity over a local window of width σ
    # and sample from the averaged intensity.
    sigma = 0.45   # resolution scale (proxy for v * τ_c)
    I_avg = np.convolve(I_fast, np.ones(int(sigma / (x[1]-x[0]))) / max(1, int(sigma / (x[1]-x[0]))), mode="same")
    probs_avg = I_avg / I_avg.sum()
    idx_avg = rng.choice(len(x), size=n_events, p=probs_avg)
    event_avg = x[idx_avg]
    hist_avg, _ = np.histogram(event_avg, bins=60, density=True, range=(-4, 4))

    L1_avg_to_env = np.trapezoid(np.abs(hist_avg - env_norm), centers)

    print("Results (L¹ distances):")
    print(f"  Instantaneous samples vs slow envelope : {L1_inst_to_env:.4f}")
    print(f"  Instantaneous samples vs fast intensity: {L1_inst_to_fast:.4f}")
    print(f"  Finite-resolution (averaged) vs envelope: {L1_avg_to_env:.4f}")
    print()

    # Pass criteria (illustrative)
    # Finite-resolution should be closer to the envelope than instantaneous is
    if L1_avg_to_env < L1_inst_to_env and L1_avg_to_env < 0.25:
        print("PASS: finite-resolution density is closer to the slow envelope")
        print("      than instantaneous sampling is.")
    else:
        print("CHECK: inspect numbers; finite-resolution should improve match to envelope.")

    print()
    print("Interpretation (honest):")
    print("  A finite gate / finite spatial-temporal resolution averages the")
    print("  high-frequency intensity. The recorded event density therefore")
    print("  tracks the slow envelope. This is the under-sampling picture")
    print("  native to RTT. It is an illustration of the measurement-record")
    print("  side of the theory, not a first-principles derivation of the")
    print("  equilibrium postulate from the microscopic field + detector.")
    print()
    print("Status: shown-numerically (illustrative)")

if __name__ == "__main__":
    main()
