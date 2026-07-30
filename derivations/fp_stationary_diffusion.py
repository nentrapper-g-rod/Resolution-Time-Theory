#!/usr/bin/env python3
"""
Executable derivation: Fokker–Planck stationary density for pure diffusion
Supports Phase 1.1 (consistency check: D ∝ 1/I ⇒ ρ∞ ∝ I under Itô)

Status: proven-analytically
"""

import sympy as sp

def main():
    x = sp.symbols('x', real=True)
    D = sp.Function('D', positive=True)(x)

    # Pure diffusion Itô SDE: dX = √(2D) dW   (zero ordinary drift)
    # Fokker–Planck: ∂t ρ = ∂xx (D ρ)
    # Stationary: ∂x (D ρ) = 0  ⇒  D ρ = const  ⇒  ρ ∝ 1/D

    print("Fokker–Planck stationary density for pure diffusion (Itô)")
    print("=" * 55)
    print("SDE: dX = √(2 D(x)) dW   (zero ordinary drift)")
    print()
    print("Fokker–Planck operator: ∂t ρ = ∂xx (D ρ)")
    print("Stationary condition: ∂x (D ρ) = 0")
    print("⇒ D ρ = constant")
    print("⇒ ρ∞(x) ∝ 1 / D(x)")
    print()
    print("Therefore choosing D(x) ∝ 1/I(x) yields ρ∞ ∝ I(x) exactly.")
    print("This is a consistency check / restatement of the target, not a derivation")
    print("of why D should be inverse to I from the field dynamics.")
    print()
    print("Status: proven-analytically")

if __name__ == "__main__":
    main()
