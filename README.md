# Cryptocurrency Price Analyzer

#### Video Demo: <URL HERE>

A command-line tool that fetches and analyzes cryptocurrency price data using the CoinGecko API. This tool allows users to view price trends, generate visualizations, and save historical price data for popular cryptocurrencies like Bitcoin (BTC), Ethereum (ETH), Binance Coin (BNB), and Solana (SOL).

## Features

- Fetch real-time cryptocurrency price data
- Generate price analysis and statistics
- Create price trend visualizations
- Export data to CSV format
- Support for multiple time periods (last week, last month)
- Command-line interface for easy interaction

## Installation

1. Clone this repository:

```bash
git clone https://github.com/amir-mostafa-hs/cs50p-final-project.git
cd cs50p-final-project
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program using the command line with the following arguments:

```bash
python project.py --coin=COIN_SYMBOL --time=TIME_PERIOD
```

### Arguments:

- `--coin`: Cryptocurrency symbol (BTC, ETH, BNB, SOL)
- `--time`: Time period for analysis
  - `lw`: Last week
  - `lm`: Last month

### Example:

```bash
python project.py --coin=BTC --time=lw
```

This will:

1. Fetch Bitcoin's price data for the last week
2. Display price statistics
3. Save the data to a CSV file
4. Generate and save a price chart

## Project Structure

```
cryptocurrency-price-analyzer/
├── project.py              # Main application file
├── requirements.txt        # Project dependencies
├── utils/
│   ├── fetch_api.py       # API handling utilities
│   ├── time_interval_calculator.py  # Time calculation utilities
│   ├── cli_tool.py        # Command line interface tools
│   └── plot_prices.py     # Data visualization utilities
└── tests/
    └── test_project.py    # Test suite
```

## Dependencies

The project uses several Python libraries:

- **requests**: For making HTTP requests to the CoinGecko API
- **pandas**: For data manipulation and analysis
- **matplotlib**: For generating price charts and visualizations
- **pytest**: For running unit tests
- **datetime**: For handling date and time operations

## Testing

To run the tests:

```bash
python -m pytest test_project.py -v
```

## Functions

### Main Functions

1. `get_data_coingecko_API(coin, time)`:

   - Fetches cryptocurrency price data from CoinGecko API
   - Parameters: coin name and time period

2. `process_price_data(prices)`:

   - Processes raw price data into a pandas DataFrame
   - Converts timestamps to datetime format

3. `display_price_info(df, coin_name, time_period)`:

   - Displays daily prices and summary statistics
   - Shows highest, lowest, and average prices

4. `save_to_csv(df, coin_symbol)`:

   - Exports price data to a CSV file
   - Filename includes timestamp for uniqueness

5. `save_price_plot(df, coin_symbol, coin_name, time_period)`:
   - Generates and saves price trend visualization
   - Creates timestamped PNG files

## API Usage

This project uses the CoinGecko API v3, which is free and doesn't require authentication. The API endpoints used are:

- `/coins/{id}/market_chart/range`: For historical price data

## Output Files

The program generates two types of output files:

1. CSV files: `{COIN}_prices_{TIMESTAMP}.csv`
2. PNG files: `{COIN}_prices_{TIMESTAMP}.png`

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.
