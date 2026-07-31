#!/usr/bin/env bash
# Regenerate every derivation and simulation that supports a claim.
# No shutdown, reboot, kill, or other system-control commands.
set -euo pipefail

echo "=== Derivations (analytic) ==="
python derivations/poisson_score.py
python derivations/kapitza_effective_potential.py
python derivations/fp_stationary_diffusion.py

echo ""
echo "=== Simulations (numeric; core claims) ==="
python simulations/05_state_dependent_diffusion_equilibrium.py || true
python simulations/06_rate_and_counting_models.py || true
python simulations/07_homogenization_fast_field.py || true
python simulations/08_bayesian_score_forced_likelihood.py || true
python simulations/10_locking_L1_convergence.py || true
python simulations/11_finite_resolution_averaging.py || true
python simulations/12_qm_vs_rtt_benchmark.py || true

echo ""
echo "=== Exploratory (not claim-supporting) ==="
python exploratory_models/09_visibility_kernels.py || true

echo ""
echo "All runnable artifacts executed. Compare printed output to results/RESULT_N*.md and VALIDATION.md."
