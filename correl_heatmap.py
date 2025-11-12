import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cov_matrix = np.array([
    [0.0003380914418, 0.0002433992579, 0.0002033293219, 0.000329590485 ],
    [0.0002433992579, 0.0004975034709, 0.0002554718529, 0.0004260068642],
    [0.0002033293219, 0.0002554718529, 0.0002777730608, 0.0003555665499],
    [0.000329590485 , 0.0004260068642, 0.0003555665499, 0.001085761668 ]
])

tickers = ['AAPL', 'AMZN', 'MSFT', 'NVDA']

std_devs = np.sqrt(np.diag(cov_matrix))
corr_matrix = cov_matrix / np.outer(std_devs, std_devs)

corr_df = pd.DataFrame(corr_matrix, index=tickers, columns=tickers)

plt.figure(figsize=(6, 5))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
plt.title("Correlation Heatmap: AAPL, AMZN, MSFT, NVDA")
plt.tight_layout()
plt.show()