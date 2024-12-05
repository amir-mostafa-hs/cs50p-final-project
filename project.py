import requests
import pandas as pd
from datetime import datetime

from utils.fetch_api import fetch_api
from utils.time_interval_calculator import time_interval_calculator
from utils.cli_tool import cli_tool
from utils.plot_prices import plot_prices


def main():
    # Define command line arguments
    cli_args = [
        {
            "name": "--coin",
            "type": str,
            "help": "Cryptocurrency symbol. For example: BTC (Bitcoin), ETH (Ethereum)"
        },
        {
            "name": "--time", 
            "type": str,
            "help": "Analyse time. For example: lw (last week), lm (last month)"
        },
    ]

    args = cli_tool(*cli_args, description="Simple cryptocurrency analysis")

    # Define supported cryptocurrencies
    supported_coins = {
        "BTC": "bitcoin",
        "ETH": "ethereum", 
        "BNB": "binancecoin",
        "SOL": "solana"
    }

    # Define time period options
    time_periods = {
        "lw": 7,
        "lm": 30,
    }

    # Get price data
    prices = get_data_coingecko_API(supported_coins[args.coin], time_periods[args.time])

    if prices is not None:
        # Create and process dataframe
        df = process_price_data(prices)
        
        # Display price information
        display_price_info(df, supported_coins[args.coin], time_periods[args.time])
        
        # Save data to CSV
        save_to_csv(df, args.coin)
        
        # Generate and save price plot
        save_price_plot(df, args.coin, supported_coins[args.coin], time_periods[args.time])


def process_price_data(prices):
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df.drop("timestamp", axis=1)
    return df.set_index("date")


def display_price_info(df, coin_name, time_period):
    print(f"\n{coin_name.title()} Prices (Last {time_period} Days):")
    print("-----------------------------")

    daily_prices = df.resample("D").mean()
    for date, row in daily_prices.iterrows():
        print(f"{date.strftime('%Y-%m-%d')}: ${row['price']:,.2f}")

    print("\nSummary Statistics:")
    print(f"Highest Price: ${df['price'].max():,.2f}")
    print(f"Lowest Price: ${df['price'].min():,.2f}")
    print(f"Average Price: ${df['price'].mean():,.2f}")
    print(f"Price Change: ${(df['price'].iloc[-1] - df['price'].iloc[0]):,.2f}")
    print("\n-----------------------------")


def save_to_csv(df, coin_symbol):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{coin_symbol}_prices_{timestamp}.csv"
    df.to_csv(filename)
    print(f"Data saved to {filename}")


def save_price_plot(df, coin_symbol, coin_name, time_period):
    print("\n-----------------------------")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{coin_symbol}_prices_{timestamp}.png"
    file_information = {
        "coin": coin_name.title(),
        "time": time_period
    }
    saved_file = plot_prices(df, filename, file_information)
    print(f"Plot saved as: {saved_file}")


def get_data_coingecko_API(coin, time):
    """
    Fetch cryptocurrency price data from the CoinGecko API for a given coin and time period.

    Args:
        coin (str): The cryptocurrency identifier (e.g. "bitcoin", "ethereum")
        time (int): Number of days to fetch data for

    Returns:
        list: List of timestamp-price pairs if successful, None if request fails
            Each pair contains [timestamp in milliseconds, price in USD]

    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    # Base URL for the CoinGecko API
    base_url = "https://api.coingecko.com/api/v3"

    # Calculate start and end timestamps for the date range
    start, end = time_interval_calculator(time)

    # Construct the API endpoint URL for getting market chart data
    endpoint = f"{base_url}/coins/{coin}/market_chart/range"
    # Set up query parameters for the API request
    params = {
        "vs_currency": "usd",  # Get prices in USD
        "from": start,         # Start timestamp
        "to": end              # End timestamp
    }

    try:
        # Make the API request and get response data
        data = fetch_api(endpoint,params)

        # Extract just the price data from the response
        prices = data["prices"]

        return prices

    except requests.exceptions.RequestException as e:
        # Handle any API request errors by printing message and returning None
        print(f"Error fetching data: {e}")
        return None



def analyze_data(data):
    """
    Convert raw cryptocurrency price data into a formatted pandas DataFrame.

    Args:
        data (list): List of timestamp-price pairs from the CoinGecko API.

    Returns:
        pandas.DataFrame: DataFrame with datetime index and price column, with timestamp column dropped.
    """
    # Create a pandas DataFrame with timestamp and price columns from the input data
    df = pd.DataFrame(data, columns=["timestamp", "price"])

    # Convert timestamp column to datetime format using milliseconds as the unit
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    # Remove the original timestamp column since we now have the date column
    df = df.drop("timestamp", axis=1)
    # Set the date column as the index of the DataFrame
    df = df.set_index("date")

    return df



if __name__ == "__main__":
    main()
