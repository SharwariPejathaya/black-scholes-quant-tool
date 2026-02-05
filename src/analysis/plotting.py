import matplotlib.pyplot as plt
import seaborn as sns


def plot_call_price_heatmap(df):
    pivot = df.pivot(
        index="vol_shock",
        columns="price_shock",
        values="call_price"
    )

    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, cmap="viridis")
    plt.title("Call Price Sensitivity Heatmap")
    plt.xlabel("Stock Price Shock")
    plt.ylabel("Volatility Shock")
    plt.tight_layout()
    plt.show()

def plot_pnl_heatmap(df):
    pivot = df.pivot(
        index="vol_shock",
        columns="price_shock",
        values="pnl"
    )

    plt.figure(figsize=(10, 6))
    sns.heatmap(
        pivot,
        cmap="RdYlGn",
        center=0
    )
    plt.title("Option P&L Heatmap")
    plt.xlabel("Stock Price Shock")
    plt.ylabel("Volatility Shock")
    plt.tight_layout()
    plt.show()
    
    
