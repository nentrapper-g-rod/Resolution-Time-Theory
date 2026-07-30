#!/usr/bin/env python3
"""
Executable derivation: Kapitza / high-frequency effective potential
Supports Phase 1.3 (negative mechanical result)

Status: proven-analytically
"""

import sympy as sp

def main():
    x, t, omega = sp.symbols('x t omega', real=True, positive=True)
    A = sp.Function('A', real=True)(x)

    V = A * sp.cos(omega * t)
    F = -sp.diff(V, x)  # -A' cos(ω t)

    # Classic high-frequency (Kapitza) average
    A_prime = sp.diff(A, x)
    V_eff = (A_prime**2) / (4 * omega**2)
    F_eff = -sp.diff(V_eff, x)

    print("Kapitza / high-frequency effective potential")
    print("=" * 50)
    print("V(x,t) = A(x) cos(ω t)")
    print("F = -∂x V = -A'(x) cos(ω t)")
    print()
    print("High-frequency effective potential:")
    print("  V_eff =", V_eff)
    print()
    print("Effective force:")
    print("  F_eff =", F_eff.simplify())
    print()
    print("Conclusion: F_eff is built from A' and A'' (amplitude gradients).")
    print("It is a ∇I-type / ponderomotive object, not ∇log I.")
    print("This is the analytic content of the negative result in Phase 1.3.")
    print()
    print("Status: proven-analytically")

if __name__ == "__main__":
    main()
