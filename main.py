from data_fetcher import fetch_data
from strategy import calculate_indicators, generate_signals
from backtester import backtest
from ml_model import add_features, train_model
from google_sheets_logger import connect_to_sheet, write_trade_log, write_summary, write_win_ratio
from telegram_notifier import send_telegram_message
import pandas as pd
import time

# Configs
TICKERS = ["INFY.NS", "TCS.NS", "BALKRISIND.NS","IRFC.NS", "RVNL.NS"]
SHEET_NAME = "Algo_Trading_Log"
CREDENTIALS_PATH = "credentials.json"
TELEGRAM_TOKEN = "8171862409:AAH3hxPvnAsfvYjSixuAkHOBjmdJ7NRmAgI"
CHAT_ID = "6393204093"

sheet = connect_to_sheet(CREDENTIALS_PATH, SHEET_NAME)

for ticker in TICKERS:

    df = fetch_data(ticker)
    if len(df) < 60:
        print(f"❗ Not enough data for {ticker}. Skipping...")
        continue

    df = calculate_indicators(df)
    df = generate_signals(df)

    strategy_returns, market_returns, win_ratio = backtest(df)
    df = add_features(df)

    required_cols = ["RSI", "20DMA", "50DMA", "MACD", "Volume", "Target"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"🚫 {ticker}: Missing columns {missing}, skipping ML.")
        accuracy = 0.0
    else:
        model, accuracy = train_model(df)

    trade_log = df[["Close", "RSI", "20DMA", "50DMA", "Signal"]].copy()
    write_trade_log(sheet, trade_log, tab_name=f"{ticker}_Log")
    time.sleep(2)  # prevent API quota error

    summary = {
        "Ticker": ticker,
        "Final Strategy Return": strategy_returns.iloc[-1],
        "Final Market Return": market_returns.iloc[-1],
        "Prediction Accuracy": accuracy
    }
    write_summary(sheet, summary, tab_name=f"{ticker}_P&L")
    time.sleep(2)  # prevent API quota error

    write_win_ratio(sheet, win_ratio, tab_name=f"{ticker}_Win_Ratio")
    time.sleep(2)  # prevent API quota error

    message = f"[{ticker}] Strategy Return: {strategy_returns.iloc[-1]:.2f}, Win Ratio: {win_ratio:.2f}, ML Accuracy: {accuracy:.2f}"
    send_telegram_message(TELEGRAM_TOKEN, CHAT_ID, message)
    time.sleep(1)  # minor delay between messages
