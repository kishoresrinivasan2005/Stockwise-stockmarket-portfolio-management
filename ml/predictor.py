import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta

def predict_stock_price(symbol):
    try:
        # Fetch historical data (last 2 years)
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="2y")
        
        if df.empty or len(df) < 30:
            return None, "Not enough data for this stock symbol."
            
        # We will predict next day's close based on past closes (simple Moving Averages as features)
        df['SMA_5'] = df['Close'].rolling(window=5).mean()
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        
        # Next day's price is what we want to predict
        df['Target'] = df['Close'].shift(-1)
        
        # Drop NaN values
        df.dropna(inplace=True)
        
        # Features and Target
        X = df[['Close', 'SMA_5', 'SMA_20']]
        y = df['Target']
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Evaluate accuracy (R^2 score)
        accuracy = model.score(X_test, y_test)
        
        # Predict next day using the very last row's data
        last_row = df.iloc[-1]
        last_features = pd.DataFrame([{
            'Close': last_row['Close'], 
            'SMA_5': last_row['SMA_5'], 
            'SMA_20': last_row['SMA_20']
        }])
        
        predicted_price = model.predict(last_features)[0]
        
        return {
            'symbol': symbol,
            'current_price': float(last_row['Close']),
            'predicted_price': float(predicted_price),
            'accuracy': float(accuracy * 100),
            'trend': 'UP' if predicted_price > last_row['Close'] else 'DOWN',
            'change': float(predicted_price - last_row['Close']),
            'change_pct': float((predicted_price - last_row['Close']) / last_row['Close'] * 100)
        }, None
        
    except Exception as e:
        print(f"Prediction error for {symbol}: {e}")
        return None, f"An error occurred while predicting: {str(e)}"
