#!/usr/bin/env python3
"""
Executable derivation: Poisson score for intensity-proportional detection rate.

Claim under test
----------------
For λ(x) = α I(x), k ~ Poisson(λ τ),
  ∂x log p(k|x) = (k − λ) · (∂x log I)
and
  E_k[score | x] = 0   (exactly).

If this script prints anything other than mean score = 0, the algebraic
claim used in the prose is false.

Status: proven-analytically (symbolic identity)
"""
import sympy as sp

x = sp.symbols("x", real=True)
I = sp.Function("I", positive=True)(x)
alpha, tau, k = sp.symbols("alpha tau k", positive=True)

lam = alpha * I * tau
logp = -lam + k * sp.log(lam)   # drop log(k!) which is independent of x
score = sp.diff(logp, x).simplify()

print("Poisson score ∂x log p(k|x) =")
print(score)
print()

score_form = ((k - lam) * sp.diff(I, x) / I).simplify()
print("Equivalent form (k − λ) · (I'/I) =")
print(score_form)
print()

mean_score = score.subs(k, lam).simplify()
print("E_k[score | x]  (substitute k → λ) =")
print(mean_score)
print()

assert mean_score == 0, "FAIL: mean score is not identically zero"
print("PASS: mean score is identically zero.")
print("STATUS: proven-analytically")
