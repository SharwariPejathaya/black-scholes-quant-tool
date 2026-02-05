import matplotlib.pyplot as plt
import seaborn as sns


def plot_call_price_heatmap(df):
    pivot = df.pivot(
        index="vol_shock",
        columns="price_shock",
        values="call_price"
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot, cmap="viridis", ax=ax)

    ax.set_title("Call Price Sensitivity Heatmap")
    ax.set_xlabel("Stock Price Shock")
    ax.set_ylabel("Volatility Shock")

    return fig


def plot_pnl_heatmap(df):
    pivot = df.pivot(
        index="vol_shock",
        columns="price_shock",
        values="pnl"
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot, cmap="RdYlGn", center=0, ax=ax)

    ax.set_title("Option P&L Heatmap")
    ax.set_xlabel("Stock Price Shock")
    ax.set_ylabel("Volatility Shock")

    return fig
