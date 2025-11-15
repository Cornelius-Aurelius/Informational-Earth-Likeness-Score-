# -*- coding: utf-8 -*-
"""
Informational Earth-Likeness Score (IELS)
Official Verification Script — Cornelius Aurelius (Omniscientrix-vOmega Framework)

This script computes the Informational Earth-Likeness Score (IELS),
a normalized metric evaluating how closely an informational system
resembles the stability, balance, and regenerative behavior characteristic of Earth-like systems.

IELS is computed from normalized indicators:
    S = stability index
    R = regenerative index
    C = coherence index
    E = entropy-balance index

With final score:
    IELS = (S * R * C * E)**(1/4)
"""

import numpy as np

def normalize(x):
    """Normalize array to [0,1]."""
    x = np.clip(x, 1e-15, None)
    return x / np.max(x)

def compute_IELS(S, R, C, E):
    """Compute the Informational Earth-Like Score."""
    return (S * R * C * E) ** 0.25

def generate_random_system(n=1000):
    """Generate a synthetic system with Earth-like tendencies."""
    rng = np.random.default_rng(42)
    S = normalize(rng.random(n))
    R = normalize(rng.random(n))
    C = normalize(rng.random(n))
    E = normalize(rng.random(n))
    return S, R, C, E

if __name__ == "__main__":
    print("\n=== Verification: Informational Earth-Likeness Score (IELS) ===\n")

    S, R, C, E = generate_random_system()
    score = compute_IELS(S.mean(), R.mean(), C.mean(), E.mean())

    print("Mean Stability (S):", S.mean())
    print("Mean Regenerative Index (R):", R.mean())
    print("Mean Coherence (C):", C.mean())
    print("Mean Entropy-Balance (E):", E.mean())
    print("\nIELS Score:", score)
    print("\nInterpretation:")
    print("IELS close to 1.0 = highly Earth-like informational balance.")
    print("IELS close to 0.0 = low Earth-likeness.")
