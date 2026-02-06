import math
from scipy.stats import norm


def normal_cdf(x: float) -> float:
    """
    Standard normal cumulative distribution function.
    """
    return norm.cdf(x)


def validate_inputs(S, K, T, sigma, r):
    if S <= 0:
        raise ValueError("Stock price must be positive")
    if K <= 0:
        raise ValueError("Strike price must be positive")
    if T <= 0:
        raise ValueError("Time to maturity must be positive")
    if sigma <= 0:
        raise ValueError("Volatility must be positive")
