import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('log_returns.csv', parse_dates=['Date'])

stocks = ['AAPL', 'AMZN', 'MSFT', 'NVDA']
weights = [0.3115, 0.2707, 0.2424, 0.1754]

df['Portfolio'] = df[stocks].mul(weights).sum(axis=1)

plt.figure(figsize=(12,7))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for stock, color in zip(stocks, colors):
    sns.kdeplot(df[stock], label=stock, color=color, fill=True, alpha=0.3, linewidth=2)

sns.kdeplot(df['Portfolio'], label='Portfolio (Weighted)', color='black', fill=False, linewidth=3, linestyle='--')

plt.title('Distribution of Daily Log Returns: Stocks & Weighted Portfolio')
plt.xlabel('Log Return')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()