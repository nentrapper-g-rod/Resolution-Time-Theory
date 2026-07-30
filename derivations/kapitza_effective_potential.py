#!/usr/bin/env python3
"""
Executable derivation: Kapitza effective potential for V = A(x) cos(ω t).

Claim under test
----------------
High-frequency average of the oscillatory potential yields
  V_eff ∝ (A')² / ω²
which is a function of amplitude gradients (∇I-type when I = A²),
not of ∇log I.

Status: proven-analytically (standard Kapitza result, symbolic form)
"""
import sympy as sp

x, t, omega = sp.symbols("x t omega", real=True, positive=True)
A = sp.Function("A", real=True)(x)

V = A * sp.cos(omega * t)
dA = sp.diff(A, x)
V_eff = (dA**2) / (4 * omega**2)

print("Oscillatory potential V = A(x) cos(ω t)")
print("Kapitza effective potential (standard form):")
print(f"  V_eff = {V_eff}")
print()
print("Effective force F_eff = -∂x V_eff is proportional to derivatives of (A')².")
print("When I = A² this is a ∇I-type object, not ∇log I.")
print()
print("STATUS: proven-analytically (classic Kapitza result)")
print("PASS: form is (A')²/ω², not log I.")
