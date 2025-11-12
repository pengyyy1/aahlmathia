import numpy as np

mu_hat = np.array([0.000490, 0.000226, 0.000678, 0.002048])

# Cov Matrix
Sigma_hat = np.array([
    [0.0003381, 0.0002434, 0.0002033, 0.0003296],
    [0.0002434, 0.0004975, 0.0002555, 0.0004260],
    [0.0002033, 0.0002555, 0.0002778, 0.0003556],
    [0.0003296, 0.0004260, 0.0003556, 0.0010858]
])

# Weights
allocation = np.array([0.3115, 0.2707, 0.2424, 0.1754])

# V0
V0 = 100_000

# Stock Price (2025-08-29)
P_current = np.array([125.52, 172.55, 216.24, 13.33])

# Calculate how many shares of each stock we actually own
# (Money allocated to stock) ÷ (Price per share) = Number of shares
num_shares = (allocation * V0) / P_current

# Break down the covariance matrix so we can create correlated random moves
L = np.linalg.cholesky(Sigma_hat)

def monte_carlo_losses(N):
    # Set random seed so we get the same results each time
    np.random.seed(42)
    
    # Generate random numbers for our simulation
    # N = number of scenarios, 4 = number of stocks
    Z = np.random.randn(N, 4)
    
    # Make these random moves correlated like real stocks
    R_star = mu_hat + Z @ L.T
    
    # Calculate what prices would be after these moves
    P_future = P_current * np.exp(R_star)
    
    # Calculate new value of our portfolio
    V_sim = P_future @ num_shares
    
    # Calculate profit/loss compared to starting value
    PL = V_sim - V0
    
    # Convert to losses
    losses = -PL
    
    return losses

# Run N different scenarios
N = 10_000_000
losses_MC = monte_carlo_losses(N)

# 95th Percentile
VaR_95_MC = np.percentile(losses_MC, 95)

print(f"Monte Carlo 1-day 95% VaR: ${VaR_95_MC}")
print(f"Cholesky Decomposition: \n {L}")
