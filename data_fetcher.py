import yfinance as yf          # for fetching stock market data from yahoo finance
import pandas as pd            

def fetch_data(ticker, period="6mo", interval="1d"):     # takes in a stock ticker ex RELIANCE.NS data of past 6 months with interval 1 day means daily
    data = yf.download(ticker, period=period, interval=interval)     # this line will fetch historical stock data using yfinance

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.dropna(inplace=True)
    return data
