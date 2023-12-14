# Introduction to Options and Monte Carlo Simulation

## 1. European Call Options

### Definition
European call options are financial contracts that give the holder the right, but not the obligation, to buy an underlying asset at a specified price (strike price) on or before the expiration date. However, exercise can only occur at the expiration date.

### Characteristics
- The holder has the right to buy the asset at the strike price only on the expiration date.
- Payoff: Max(0, Stock Price - Strike Price) at expiration.

## 2. American Call Options

### Definition
American call options are similar to European options, but holders have the right to exercise the option at any time before or on the expiration date, not just on the expiration date.

### Characteristics
- The holder can exercise the option at any time until expiration.
- Payoff: Max(0, Stock Price - Strike Price) at exercise.

## 3. Monte Carlo Simulation

### Overview
Monte Carlo Simulation is a computational technique that uses random sampling to model and analyze complex systems or problems. In finance, it's used to estimate the value of options by simulating possible future prices of the underlying asset.

### Working Principle
- Generate multiple random scenarios of future stock prices based on the given parameters.
- Calculate the option value for each scenario.
- Take the average of these values to estimate the option's present value.

## 4. Functions Used in the Program

### monte_carlo_val_eu_call_option
This function is used to compute the value of a European call option using Monte Carlo simulation.

#### Parameters:
- `s`: Current stock price
- `k`: Strike price of the option
- `t`: Time to maturity (in years)
- `r`: Risk-free interest rate
- `sigma`: Volatility of the underlying stock
- `Print`: Optional parameter to enable printing the result (default is True)
- `currency`: Currency type for the option price calculation (default is 'Euro')

#### Returns:
- `mceco`: Value of the European call option calculated using Monte Carlo simulation

### (Add descriptions of other relevant functions used in the program if applicable)

