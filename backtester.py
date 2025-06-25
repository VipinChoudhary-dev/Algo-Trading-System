# this function will compare your trading strategy with the market actual performance and calculate the win ratio

def backtest(df):
    df["Returns"] = df["Close"].pct_change()
    df["Strategy_Returns"] = df["Returns"] * df["Signal"].shift(1)
    
    
    # performance if you follow the strategy
    cumulative_strategy_returns = (1 + df["Strategy_Returns"]).cumprod()  
    # performance if you just hold the stock
    cumulative_market_returns = (1 + df["Returns"]).cumprod()
    

    # how many times you made money after a buy signal
    win_trades = ((df["Strategy_Returns"] > 0) & (df["Signal"].shift(1) == 1)).sum()
    # total number of buy signal
    total_trades = (df["Signal"].shift(1) == 1).sum()
    # win ratio (success rate of your signals)
    win_ratio = win_trades / total_trades if total_trades > 0 else 0

    return cumulative_strategy_returns, cumulative_market_returns, win_ratio