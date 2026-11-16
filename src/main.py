from extract import get_crypto_data
from analytics import top_gainers, top_losers

df = get_crypto_data()

columns = [
    "name",
    "symbol",
    "current_price",
    "market_cap",
    "total_volume",
    "price_change_percentage_24h",
    "last_updated"
]

df = df[columns]

df.to_csv(
    "data/crypto_prices.csv",
    index=False
)

print("\nTOP GAINERS")
print(
    top_gainers(df)[
        ["name", "price_change_percentage_24h"]
    ]
)

print("\nTOP LOSERS")
print(
    top_losers(df)[
        ["name", "price_change_percentage_24h"]
    ]
)