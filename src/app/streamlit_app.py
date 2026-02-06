import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(
    page_title="Black–Scholes Quant Tool",
    layout="wide"
)
st.title("📈 Black–Scholes Option Pricing & Risk Tool")
st.write("✅ App rendered successfully")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
import streamlit as st

from pricing.black_scholes import black_scholes_price
from pricing.greeks import call_delta, gamma, vega
from analysis.sensitivity import option_price_surface, option_pnl_surface
from analysis.plotting import plot_call_price_heatmap, plot_pnl_heatmap


st.set_page_config(page_title="Black–Scholes Quant Tool", layout="wide")

st.title("📈 Black–Scholes Option Pricing & Risk Tool")

# ---------------- INPUTS ----------------
st.sidebar.header("Option Parameters")

S = st.sidebar.number_input("Stock Price", value=100.0)
K = st.sidebar.number_input("Strike Price", value=100.0)
T = st.sidebar.number_input("Time to Maturity (years)", value=1.0)
sigma = st.sidebar.number_input("Volatility", value=0.2)
r = st.sidebar.number_input("Risk-Free Rate", value=0.05)

purchase_price = st.sidebar.number_input(
    "Option Purchase Price", value=10.0
)

# ---------------- PRICING ----------------
call_price, put_price = black_scholes_price(S, K, T, sigma, r)

st.subheader("Option Prices")
st.write(f"**Call Price:** {call_price:.4f}")
st.write(f"**Put Price:** {put_price:.4f}")

# ---------------- GREEKS ----------------
st.subheader("Greeks")
st.write(f"**Delta:** {call_delta(S, K, T, sigma, r):.4f}")
st.write(f"**Gamma:** {gamma(S, K, T, sigma, r):.6f}")
st.write(f"**Vega:** {vega(S, K, T, sigma, r):.4f}")

# ---------------- HEATMAPS ----------------
price_shocks = np.linspace(-0.2, 0.2, 25)
vol_shocks = np.linspace(-0.1, 0.1, 25)

st.subheader("Call Price Sensitivity")
price_df = option_price_surface(
    S, K, T, sigma, r, price_shocks, vol_shocks
)
fig_price = plot_call_price_heatmap(price_df)
st.pyplot(fig_price)


st.subheader("P&L Sensitivity")
pnl_df = option_pnl_surface(
    S, K, T, sigma, r, purchase_price, price_shocks, vol_shocks
)
fig_pnl = plot_pnl_heatmap(pnl_df)
st.pyplot(fig_pnl)

