#!/usr/bin/env python3
"""
Executable derivation: Poisson score for intensity-proportional detection
Supports the audit of Phase 1.4

Status: proven-analytically
"""

import sympy as sp

def main():
    x = sp.symbols('x', real=True)
    I = sp.Function('I', positive=True)(x)
    alpha, tau, k = sp.symbols('alpha tau k', positive=True)

    lam = alpha * I * tau
    # log p(k|x) = -λ + k log λ - log(k!)
    log_p = -lam + k * sp.log(lam)
    score = sp.diff(log_p, x).simplify()

    print("Poisson score for λ(x) = α I(x) τ")
    print("=" * 45)
    print("Exact score ∂x log p(k|x) =")
    print(" ", score)
    print()
    print("Equivalent form: (k − λ) · (I'/I) = (k − λ) ∇log I")
    print()

    mean_score = score.subs(k, lam).simplify()
    print("Mean score (k → E[k] = λ):")
    print(" ", mean_score)
    print()
    print("Conclusion: E[score] ≡ 0. There is no net drift up the intensity")
    print("from the average detection model. This is the fact that demoted 1.4.")
    print()
    print("Status: proven-analytically")

if __name__ == "__main__":
    main()
