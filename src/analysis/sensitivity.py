import pandas as pd
from pricing.black_scholes import black_scholes_price


def option_price_surface(
    S: float,
    K: float,
    T: float,
    sigma: float,
    r: float,
    price_shocks,
    vol_shocks
) -> pd.DataFrame:
    """
    Computes a call price surface by shocking stock price and volatility.

    price_shocks: iterable of % changes in stock price (e.g. -0.2 to 0.2)
    vol_shocks: iterable of absolute changes in volatility (e.g. -0.1 to 0.1)
    """

    data = []

    for ds in price_shocks:
        for dv in vol_shocks:
            shocked_S = S * (1 + ds)
            shocked_sigma = sigma + dv

            if shocked_S <= 0 or shocked_sigma <= 0:
                continue

            call_price, _ = black_scholes_price(
                shocked_S, K, T, shocked_sigma, r
            )

            data.append({
                "price_shock": ds,
                "vol_shock": dv,
                "call_price": call_price
            })

    return pd.DataFrame(data)


def option_pnl_surface(
    S: float,
    K: float,
    T: float,
    sigma: float,
    r: float,
    purchase_price: float,
    price_shocks,
    vol_shocks
) -> pd.DataFrame:
    """
    Computes a P&L surface for a call option.
    """

    data = []

    for ds in price_shocks:
        for dv in vol_shocks:
            shocked_S = S * (1 + ds)
            shocked_sigma = sigma + dv

            if shocked_S <= 0 or shocked_sigma <= 0:
                continue

            call_price, _ = black_scholes_price(
                shocked_S, K, T, shocked_sigma, r
            )

            pnl = call_price - purchase_price

            data.append({
                "price_shock": ds,
                "vol_shock": dv,
                "pnl": pnl
            })

    return pd.DataFrame(data)
