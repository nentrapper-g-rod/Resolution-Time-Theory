"""Canonical intensity envelope for RTT numerical checks.

Double-peak classical interference envelope:
  I(x) = I0 + A * (exp(-(x+x0)^2/(2σ^2)) + exp(-(x-x0)^2/(2σ^2)))

Used by locking / homogenization studies. Other scripts may use a
closely related double-peak form; prefer this helper for new work.
"""
import numpy as np

I0 = 0.12
A = 0.95
X0 = 1.3
SIGMA = 0.35

def I(x):
    x = np.asarray(x, dtype=float)
    return I0 + A * (
        np.exp(-((x + X0) ** 2) / (2 * SIGMA ** 2))
        + np.exp(-((x - X0) ** 2) / (2 * SIGMA ** 2))
    )
