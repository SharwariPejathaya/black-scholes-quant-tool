import sys
import os
sys.path.append(os.path.abspath("src"))

import math
from pricing.black_scholes import black_scholes_price


def test_black_scholes_known_values():
    S = 100
    K = 100
    T = 1
    sigma = 0.2
    r = 0.05

    call, put = black_scholes_price(S, K, T, sigma, r)

    assert round(call, 2) == 10.45
    assert round(put, 2) == 5.57


def test_put_call_parity():
    S = 120
    K = 100
    T = 0.5
    sigma = 0.25
    r = 0.03

    call, put = black_scholes_price(S, K, T, sigma, r)

    lhs = call - put
    rhs = S - K * math.exp(-r * T)

    assert abs(lhs - rhs) < 1e-6
