from Finance_pkg.monte_carlo_val_eu_op import monte_carlo_val_eu_call_option

def main():
    """
    Example script demonstrating the use of Monte Carlo simulation to value a European call option.

    This script imports the 'monte_carlo_val_eu_call_option' function from the Finance_pkg module
    and calculates the value of a European call option using the provided parameters.

    Parameters:
    - s: Current stock price
    - k: Strike price of the option
    - t: Time to maturity (in years)
    - r: Risk-free interest rate
    - sigma: Volatility of the underlying stock
    - Print: Optional parameter to enable printing the result (default is True)
    - currency: Currency type for the option price calculation (default is 'Euro')

    Returns:
    - mceco: Value of the European call option calculated using Monte Carlo simulation
    """
    s = 100
    k = 105
    t = 1
    r = 0.05
    sigma = 0.2

    # Calculate the value of the European call option using Monte Carlo simulation
    mceco = monte_carlo_val_eu_call_option(s, k, t, r, sigma, Print=True, currency='Euro')

    return mceco

# Execute the main function
if __name__ == "__main__":
    main()
