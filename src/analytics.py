import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    return pd.read_csv("data/crypto_prices.csv")


def top_market_cap(df):
    top10 = df.nlargest(10, "market_cap").copy()

    # Conversion en milliards USD
    top10["market_cap_billions"] = (
        top10["market_cap"] / 1_000_000_000
    )

    plt.figure(figsize=(12, 6))

    ax = sns.barplot(
        x="market_cap_billions",
        y="name",
        hue="name",
        data=top10,
        palette="viridis",
        legend=False
    )

    plt.title(
        "Top Cryptocurrencies by Market Capitalization",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Market Cap (Billion USD)")
    plt.ylabel("")

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f",
            padding=3
        )
    
    plt.grid(axis="x", linestyle="--", alpha=0.4)
    plt.tight_layout()

    plt.savefig(
        "reports/top_marketcap.png",
        dpi=300
    )

    plt.close()


def top_gainers(df):
    top = df.nlargest(
        10,
        "price_change_percentage_24h"
    ).copy()

    plt.figure(figsize=(12, 6))

    ax = sns.barplot(
        x="price_change_percentage_24h",
        y="name",
        hue="name",
        data=top,
        palette="rocket",
        legend=False
    )

    plt.title(
        "Top 10 Gainers (24h)",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("24h Change (%)")
    plt.ylabel("")

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.2f%%",
            padding=3
        )

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.4
    )
    
    plt.tight_layout()

    plt.savefig(
        "reports/top_gainers.png",
        dpi=300
    )

    plt.close()


if __name__ == "__main__":
    df = load_data()

    top_market_cap(df)
    top_gainers(df)

    print("Reports generated successfully")