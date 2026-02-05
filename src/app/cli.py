import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from pricing.black_scholes import black_scholes_price


def main():
    parser = argparse.ArgumentParser(
        description="Black-Scholes option pricing CLI"
    )

    parser.add_argument("--S", type=float, required=True, help="Current stock price")
    parser.add_argument("--K", type=float, required=True, help="Strike price")
    parser.add_argument("--T", type=float, required=True, help="Time to maturity (years)")
    parser.add_argument("--sigma", type=float, required=True, help="Volatility")
    parser.add_argument("--r", type=float, required=True, help="Risk-free interest rate")

    args = parser.parse_args()

    call_price, put_price = black_scholes_price(
        S=args.S,
        K=args.K,
        T=args.T,
        sigma=args.sigma,
        r=args.r
    )

    print("Black–Scholes Option Prices")
    print("---------------------------")
    print(f"Call Price: {call_price:.4f}")
    print(f"Put  Price: {put_price:.4f}")


if __name__ == "__main__":
    main()
