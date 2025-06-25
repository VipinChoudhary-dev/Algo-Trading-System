# 📈 Algo-Trading System with ML & Automation

A Python-based algorithmic trading bot that combines technical indicators and basic machine learning to analyze and automate stock trading signals. It fetches data, applies a strategy, evaluates performance, and logs results to Google Sheets — with Telegram alerts and ML prediction support.

---


## 🎥 Demo Video

Watch the complete working demo and explanation:

🔗 [Demo Video Folder (Google Drive)](https://drive.google.com/drive/folders/1oAbiveaGSjrWqYFZdPBEAeTIwIGDAzZL?usp=sharing)

---

## 🚀 Features

- ✅ **Data Ingestion**  
  Fetches historical stock data using [Yahoo Finance](https://finance.yahoo.com/) for selected NIFTY 50 stocks.

- 📊 **Trading Strategy Logic**  
  Implements a simple rule-based strategy:
  - Buy Signal: **RSI < 30** and **20-DMA > 50-DMA**

- 📈 **Backtesting**  
  Compares strategy performance vs. market (buy & hold)  
  Calculates cumulative returns and win ratio

- 🤖 **Machine Learning Automation (Bonus)**  
  Uses Logistic Regression to predict next-day price movement  
  Features: RSI, DMA, MACD, and Volume  
  Outputs model accuracy (for evaluation purposes only)

- 📉 **Technical Indicators Used**
  - RSI (Relative Strength Index)
  - 20-day and 50-day Moving Averages
  - MACD (Moving Average Convergence Divergence)

- 🧾 **Google Sheets Logging**  
  Logs:
  - Trade signals
  - Strategy vs. market return
  - Win ratio
  - ML prediction accuracy

- 📬 **Telegram Notifications**  
  Sends live summary alerts for each stock directly to Telegram

---

## 🧩 Project Structure

```
algo_trading_project/
│
├── data_fetcher.py          # Gets historical data using yfinance
├── strategy.py              # Applies trading logic using RSI + DMA crossover
├── backtester.py            # Calculates returns and win ratio
├── ml_model.py              # ML model to predict next-day movement
├── google_sheets_logger.py  # Logs output to Google Sheets
├── telegram_notifier.py     # Sends Telegram alerts
└── main.py                  # Full pipeline integration
```

---

## ⚙️ Setup Instructions

1. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Add Your Google Sheets Credentials**  
   Place `credentials.json` in the root folder.  
   Ensure sharing access to your service account on the Google Sheet.

3. **Set Telegram Bot Credentials**  
   In `main.py`, replace the placeholders with your Telegram Bot Token and Chat ID.

4. **Run the Bot**
   ```bash
   python main.py
   ```

---

## 🧠 Notes

- This is a prototype for educational purposes only.
- The ML model is not used for live trading — it only evaluates prediction accuracy.
- Make sure you don’t hit Google Sheets or Telegram API limits with repeated runs.

---

## 🙋‍♂️ Author

**Vipin Choudhary**  
Feel free to connect for queries or feedback.
Email - vipinchoudhary0911@gmail.com
