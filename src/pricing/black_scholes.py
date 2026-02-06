import math
from utils.math_utils import normal_cdf, validate_inputs


def d1(S, K, T, sigma, r):
    return (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))


def d2(S, K, T, sigma, r):
    return d1(S, K, T, sigma, r) - sigma * math.sqrt(T)


def black_scholes_price(S, K, T, sigma, r):
    """
    Returns (call_price, put_price)
    """
    validate_inputs(S, K, T, sigma, r)

    d1_val = d1(S, K, T, sigma, r)
    d2_val = d2(S, K, T, sigma, r)

    call_price = S * normal_cdf(d1_val) - K * math.exp(-r * T) * normal_cdf(d2_val)
    put_price = K * math.exp(-r * T) * normal_cdf(-d2_val) - S * normal_cdf(-d1_val)

    return call_price, put_price


# explicit export (important for cloud execution)
__all__ = ["black_scholes_price"]
