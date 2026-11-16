import requests
import pandas as pd


def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,solana,binancecoin,ripple"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return pd.DataFrame(data)