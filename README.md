# Monte Carlo Simulation for 95% Value-at-Risk (VaR) of a Four-Stock Portfolio

This project estimates the 1-day 95% Value-at-Risk (VaR) for a portfolio of four major US stocks: NVIDIA (NVDA), Microsoft (MSFT), Apple (AAPL), and Amazon (AMZN). Two methods are used:

- **Analytical (Parametric) VaR:** Assumes asset returns are normally distributed and uses the historical mean and covariance to compute VaR directly.
- **Monte Carlo Simulation:** Generates thousands or millions of possible future portfolio returns using correlated random draws (via Cholesky decomposition) to empirically estimate VaR.

## What is VaR?

**Value-at-Risk (VaR)** is a risk measure that estimates the maximum expected loss of a portfolio over a set period (here, 1 day) at a certain confidence level (here, 95%).

## Project Workflow

1. **Download historical price data** for the four stocks using Yahoo Finance.
2. **Calculate daily log returns** for each asset.
3. **Compute the mean vector and covariance matrix** for these returns.
4. **Calculate portfolio VaR analytically** using portfolio statistics.
5. **Run a Monte Carlo simulation** to generate correlated future returns and empirically estimate VaR.
6. **(Optional) Visualize VaR convergence** as simulation count increases.
