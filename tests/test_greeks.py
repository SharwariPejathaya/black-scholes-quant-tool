import sys
import os
import math

sys.path.append(os.path.abspath("src"))

from pricing.greeks import call_delta, gamma, vega
from pricing.black_scholes import black_scholes_price


def test_delta_bounds():
    delta = call_delta(100, 100, 1, 0.2, 0.05)
    assert 0 < delta < 1


def test_gamma_positive():
    g = gamma(100, 100, 1, 0.2, 0.05)
    assert g > 0


def test_vega_positive():
    v = vega(100, 100, 1, 0.2, 0.05)
    assert v > 0


def test_delta_finite_difference():
    S = 100
    eps = 1e-4

    call_up, _ = black_scholes_price(S + eps, 100, 1, 0.2, 0.05)
    call_down, _ = black_scholes_price(S - eps, 100, 1, 0.2, 0.05)

    numerical_delta = (call_up - call_down) / (2 * eps)
    analytical_delta = call_delta(100, 100, 1, 0.2, 0.05)

    assert abs(numerical_delta - analytical_delta) < 1e-3
