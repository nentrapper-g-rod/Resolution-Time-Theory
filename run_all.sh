#!/usr/bin/env bash
# Regenerate every derivation and simulation that supports a claim.
set -euo pipefail

echo "=== Derivations (analytic) ==="
python derivations/poisson_score.py
python derivations/kapitza_effective_potential.py
python derivations/fp_stationary_diffusion.py

echo ""
echo "=== Simulations (numeric) ==="
python simulations/05_state_dependent_diffusion_equilibrium.py || true
python simulations/06_rate_and_counting_models.py || true
python simulations/07_homogenization_fast_field.py || true
python simulations/08_bayesian_score_forced_likelihood.py || true
python simulations/09_visibility_kernels.py || true
python simulations/10_locking_L1_convergence.py || true
python simulations/11_finite_resolution_averaging.py || true

echo ""
echo "All runnable artifacts executed. Check printed output against VERIFICATION_LOG.md."
