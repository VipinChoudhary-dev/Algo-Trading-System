from sklearn.linear_model import LogisticRegression  # It will be used to train a binary classification model which will predict 0 or 1
from sklearn.model_selection import train_test_split # this function will split the dataset into training and testing sets
from sklearn.metrics import accuracy_score           # this function will calculates the accuracy of the model by comparing predictions to actual values
import pandas as pd


def add_features(df):
    try:
        # this will calculates the percentage change in the stock's close price from the previous day
        df["Price_Change"] = df["Close"].pct_change()
        # if tomorrow’s price goes up → Target = 1
        # If it goes down or stays the same → Target = 0
        df["Target"] = (df["Price_Change"].shift(-1) > 0).astype(int)
    except Exception as e:
        print("Error adding features:", e)
    return df


# this will predict whether the price will rise tomorrow, based on today’s data
def train_model(df):
    
    # checks if all required columns are in the DataFrame
    required_cols = ["RSI", "20DMA", "50DMA", "MACD", "Volume", "Target"]
    print("\n📌 Columns in DF before ML training:", list(df.columns))

    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Skipping ML training due to missing columns: {missing_cols}")
        return None, 0.0
    
    df = df.dropna(subset=required_cols)
    
    # to check if enough data exists to train the model which is minimum 50 rows
    if df.empty or len(df) < 50:
        print("Not enough clean data for training. Skipping ML model.")
        return None, 0.0

    # prepare training and testing Data
    X = df[["RSI", "20DMA", "50DMA", "MACD", "Volume"]]
    y = df["Target"]

    try:
        # splits the data into: 80% training 20% testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LogisticRegression()
        model.fit(X_train, y_train)
        
        # compares predictions with actual values on test set
        # Returns an accuracy score between 0 and 1
        accuracy = accuracy_score(y_test, model.predict(X_test))

        # show predicted vs actual for the full data (tail of the DataFrame)
        df["Predicted"] = model.predict(X)
        df["Actual"] = y
        print("\n📊 Last 10 Predictions vs Actual:")
        print(df[["RSI", "20DMA", "50DMA", "MACD", "Volume", "Predicted", "Actual"]].tail(10))

        # it will return the ml model and it's accuracy that how well it works
        return model, accuracy
    
    except Exception as e:
        print("Model training failed:", e)
        return None, 0.0
