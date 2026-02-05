import math
from pricing.black_scholes import d1
from utils.math_utils import normal_cdf


def normal_pdf(x: float) -> float:
    """
    Standard normal probability density function.
    """
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x ** 2)


def call_delta(S: float, K: float, T: float, sigma: float, r: float) -> float:
    """
    Delta of a European call option.
    """
    d1_val = d1(S, K, T, sigma, r)
    return normal_cdf(d1_val)


def gamma(S: float, K: float, T: float, sigma: float, r: float) -> float:
    """
    Gamma of a European option (same for calls and puts).
    """
    d1_val = d1(S, K, T, sigma, r)
    return normal_pdf(d1_val) / (S * sigma * math.sqrt(T))


def vega(S: float, K: float, T: float, sigma: float, r: float) -> float:
    """
    Vega of a European option.
    NOTE: Vega is returned per 1.0 change in volatility (not 1%).
    """
    d1_val = d1(S, K, T, sigma, r)
    return S * normal_pdf(d1_val) * math.sqrt(T)
