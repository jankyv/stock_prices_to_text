import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

from binance.client import Client

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

client = Client(api_key, api_secret)


def getBTCPrice():
    tickers = client.get_ticker(symbol='BTCUSDT')

    return round(float(tickers['lastPrice']), 2), round(float(tickers['priceChangePercent']), 2)


def getETHPrice():
    tickers = client.get_ticker(symbol='ETHUSDT')

    return round(float(tickers['lastPrice']), 2), round(float(tickers['priceChangePercent']), 2)
