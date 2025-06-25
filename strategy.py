# for calculating RSI, 20DMA, 50DMA, and give an signal whether to buy or sell

import pandas as pd

def calculate_indicators(df):
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    df["20DMA"] = df["Close"].rolling(window=20).mean()
    df["50DMA"] = df["Close"].rolling(window=50).mean()

    # MACD calculation for ML model
    exp1 = df["Close"].ewm(span=12, adjust=False).mean()
    exp2 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = exp1 - exp2

    return df

# it only buys stock when it is cheap and short term growth is more
# RSI > 30 ( this means stock is being oversold and it is cheap )
# 20DMA > 50DMA _ short term trend is above long-term

def generate_signals(df):
    df["Signal"] = ((df["RSI"] < 30) & (df["20DMA"] > df["50DMA"])).astype(int)
    return df


