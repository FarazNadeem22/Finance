# Stock Information and Valuation Calculator

This Python program retrieves stock information for a given ticker symbol using Yahoo Finance API and calculates Graham's valuation based on the provided information.

## Requirements

- Python 3.x
- yfinance library (`pip install yfinance`)

## Usage

1. Clone the repository or download the `stock_info_valuation.py` file.
2. Install the required library using `pip install yfinance`.
3. Run the `stock_info_valuation.py` file.
4. Enter the ticker symbol of the stock when prompted.
5. The program will retrieve and display the stock information including company name, ticker symbol, exchange, sector, industry, market cap, previous close price, open price, current price, volume, 52-week high, 52-week low, and earnings per share (EPS).
6. It will then prompt you to input the expected growth rate and the current yield for a AAA corporate bond.
7. Finally, it will calculate and display Graham's valuation for the stock.

## Functions

### `get_stock_info(ticker)`

Retrieves stock information for a given ticker symbol.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `tuple`: A tuple containing the stock information.
    - (company_name, ticker_symbol, exchange, sector, industry, market_cap, previous_close_price, open_price, current_price, volume, fifty_two_week_high, fifty_two_week_low, eps)

### `print_stock_info(info)`

Prints the stock information retrieved from Yahoo Finance.

- **Parameters:**
  - `info` (tuple): A tuple containing the stock information.
- **Returns:**
  - None

### `grahams_valuation(info)`

Calculates Graham's valuation for a stock based on the provided information.

- **Parameters:**
  - `info` (tuple): A tuple containing stock information.
- **Returns:**
  - `float`: Graham's valuation for the stock.

## Example
```bash
Enter the ticker symbol of the stock: AAPL
Company Name: Apple Inc.
Ticker Symbol: AAPL
Exchange: NMS
Sector: Technology
Industry: Consumer Electronics
Market Cap: $2,433,394,714,112
Previous Close Price: $149.62
Open Price: $149.76
Current Price: $149.71
Volume: 1,216,208,385
52 Week High: $180.60
52 Week Low: $114.70
EPS: $5.76

What is your expected growth rate: 10
What the current yield for a AAA corporate Bond: 3
Grahams valuation for AAPL = $444.77
```
