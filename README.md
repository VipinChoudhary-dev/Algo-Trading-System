# Algo-Trading System

## Components:
- `data_fetcher.py`: Fetches stock data using Yahoo Finance
- `strategy.py`: RSI + DMA crossover trading strategy
- `backtester.py`: Backtests the strategy and calculates win ratio
- `ml_model.py`: Predicts next-day movement using Logistic Regression (to be added)
- `google_sheets_logger.py`: Logs trades and performance to Google Sheets (to be added)
- `telegram_notifier.py`: Sends alerts to Telegram (to be added)
- `main.py`: Runs the complete pipeline

## Setup:
```bash
pip install -r requirements.txt
python main.py
```