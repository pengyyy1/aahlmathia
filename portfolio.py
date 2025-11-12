import numpy as np, pandas as pd, yfinance as yf
np.random.seed(42)

tickers = ["NVDA","MSFT","AAPL","AMZN"]
start = "2020-08-30"
end   = "2025-08-30"

raw = yf.download(tickers, start=start, end=end, auto_adjust=False, progress=False)
print("Raw columns:", raw.columns)

if isinstance(raw.columns, pd.MultiIndex):
    adj = raw["Adj Close"]
else:
    adj = raw[["Adj Close"]]
adj = adj.dropna()
print("Adj Close head:\n", adj.head())

logret = np.log(adj / adj.shift(1)).dropna()
print("Log returns head:\n", logret.head())

adj.to_csv("adj_close.csv")
logret.to_csv("log_returns.csv")