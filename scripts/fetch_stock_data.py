import yfinance as yf
import pandas as pd
from time import sleep

def fetch_stock_data(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m")  # Get minute-level data
    df = pd.DataFrame(data)
    
    # Save data as CSV
    df.to_csv("data/stock_data.csv", index=False)
    print(f"✅ Fetched {ticker} stock data successfully.")

if __name__ == "__main__":
    fetch_stock_data()
 
