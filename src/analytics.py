import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    return pd.read_csv("data/crypto_prices.csv")


def top_market_cap(df):
    top10 = df.nlargest(10, "market_cap")

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="market_cap",
        y="name",
        hue="name",
        data=top10,
        palette="viridis",
        legend=False
    )

    plt.title("Top 10 Cryptocurrencies by Market Cap")
    plt.xlabel("Market Cap")
    plt.ylabel("Cryptocurrency")
    plt.tight_layout()

    plt.savefig("reports/top_marketcap.png")
    plt.close()


def top_gainers(df):
    top = df.nlargest(
        10,
        "price_change_percentage_24h"
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x="price_change_percentage_24h",
        y="name",
        hue="name",
        data=top,
        palette="rocket",
        legend=False
    )

    plt.title("Top 10 Gainers (24h)")
    plt.xlabel("24h Change (%)")
    plt.ylabel("Cryptocurrency")
    plt.tight_layout()

    plt.savefig("reports/top_gainers.png")
    plt.close()


if __name__ == "__main__":
    df = load_data()
    top_market_cap(df)
    top_gainers(df)

    print("Reports generated successfully")