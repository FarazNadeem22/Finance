import yfinance as yf

def get_stock_info(ticker):
    """
    Retrieves stock information for a given ticker symbol.
    
    Args:
        ticker (str): The ticker symbol of the stock.
    
    Returns:
        tuple: A tuple containing the following stock information:
            (company_name, ticker_symbol, exchange, sector, industry, market_cap,
             previous_close_price, open_price, current_price, volume,
             fifty_two_week_high, fifty_two_week_low, eps)
             
            Returns None if an error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        company_name = info['longName']
        ticker_symbol = info['symbol']
        exchange = info['exchange']
        sector = info['sector']
        industry = info['industry']
        market_cap = info['marketCap']
        previous_close_price = info['previousClose']
        open_price = info['open']
        current_price = info['currentPrice']
        volume = info['volume']
        fifty_two_week_high = info['fiftyTwoWeekHigh']
        fifty_two_week_low = info['fiftyTwoWeekLow']
        eps = info['trailingEps']
        

        return (company_name, ticker_symbol, exchange, sector, industry, market_cap,
                previous_close_price, open_price, current_price, volume,
                fifty_two_week_high, fifty_two_week_low, eps)
    
    except Exception as e:
        print("Error:", e)  # Print detailed error message
        return None
    
def print_stock_info(info):
    """
    Prints the stock information.
    
    Args:
        info (tuple): A tuple containing the stock information.
    """
    if info:
        (company_name, ticker_symbol, exchange, sector, industry, market_cap,
         previous_close_price, open_price, current_price, volume,
         fifty_two_week_high, fifty_two_week_low, eps) = info
        
        # Format numerical values with commas
        market_cap_str = '{:,.0f}'.format(market_cap)
        previous_close_price_str = '{:,.2f}'.format(previous_close_price)
        open_price_str = '{:,.2f}'.format(open_price)
        current_price_str = '{:,.2f}'.format(current_price) if current_price is not None else 'N/A'
        volume_str = '{:,.0f}'.format(volume)
        fifty_two_week_high_str = '{:,.2f}'.format(fifty_two_week_high)
        fifty_two_week_low_str = '{:,.2f}'.format(fifty_two_week_low)
        eps_str = '{:,.2f}'.format(eps)
      
        
        print(f"Company Name: {company_name}")
        print(f"Ticker Symbol: {ticker_symbol}")
        print(f"Exchange: {exchange}")
        print(f"Sector: {sector}")
        print(f"Industry: {industry}")
        print(f"Market Cap: {market_cap_str}")
        print(f"Previous Close Price: {previous_close_price_str}")
        print(f"Open Price: {open_price_str}")
        print(f"Current Price: {current_price_str}")
        print(f"Volume: {volume_str}")
        print(f"EPS: {eps_str}")
        print(f"52 Week High: {fifty_two_week_high_str}")
        print(f"52 Week Low: {fifty_two_week_low_str}")
    else:
        print("Failed to retrieve stock information.")

def grahams_valuation(info):
    """
    Calculate Graham's valuation for a stock based on the provided information.

    Parameters:
    info (tuple): A tuple containing stock information including:
                  - Company name
                  - Ticker symbol
                  - Exchange
                  - Sector
                  - Industry
                  - Market capitalization
                  - Previous close price
                  - Open price
                  - Current price
                  - Volume
                  - 52-week high
                  - 52-week low
                  - Earnings per share

    Returns:
    float: Graham's valuation for the stock.

    """
    if info:
        # Unpack the tuple containing stock information
        (company_name, ticker_symbol, exchange, sector, industry, market_cap,
         previous_close_price, open_price, current_price, volume,
         fifty_two_week_high, fifty_two_week_low, eps) = info

        # Constants for the calculation
        AAA_bar = 0.044 * 100  # AAA corporate bond rate
        no_growth = 0.085 * 100  # No-growth rate

        try:
            # Prompt user to input expected growth rate
            g = float(input("What is your expected growth rate: "))
        except Exception as e:
            print(f'Error: {e}')

        try:
            # Prompt user to input current yield for a AAA corporate Bond
            Y = float(input("What the current yield for a AAA corporate Bond: "))
        except Exception as e:
            print(f'Error: {e}')

        # Calculate Graham's valuation
        V = (eps * (no_growth + 2 * g) * AAA_bar) / Y
        return V


def main():
    ticker = input("Enter the ticker symbol of the stock: ")
    info = get_stock_info(ticker.upper())
    print_stock_info(info)
    V = grahams_valuation(info=info)
    V = '{:,.2f}'.format(V)
    print(f'Grahams valuation for {ticker.upper()} = {V}')

if __name__ == "__main__":
    main()
