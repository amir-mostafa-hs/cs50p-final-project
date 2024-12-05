import requests
import pandas as pd
from datetime import datetime

from utils.fetch_api import fetch_api
from utils.time_interval_calculator import time_interval_calculator
from utils.cli_tool import cli_tool
from utils.plot_prices import plot_prices


def main():
    allOfArgs = [
        {
            "name":"--coin",
            "type":str,
            "help":"Cryptocurrency symbol. For example: BTC (Bitcoin), ETH (Ethereum)"
        },
        {
            "name":"--time",
            "type":str,
            "help":"Analyse time. For example: lw (last week), lm (last month)"
        },
    ]

    args = cli_tool(*allOfArgs, description="Simple cryptocurrency analysis")

    listOfCoin = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "BNB": "binancecoin",
        "SOL": "solana"
    }

    listOfTime = {
        "lw": 7,
        "lm": 30,
    }

    prices = get_data_coingecko_API(listOfCoin[args.coin], listOfTime[args.time])

    if prices is not None:
        # Convert to DataFrame for easier handling
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])

        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Clean up the DataFrame
        df = df.drop('timestamp', axis=1)
        df = df.set_index('date')

        # Display the results
        print(f"\n{listOfCoin[args.coin].title()} Prices (Last {listOfTime[args.time]} Days):")
        print("-----------------------------")

        # Resample to daily data (taking the mean price for each day)
        daily_prices = df.resample('D').mean()

        for date, row in daily_prices.iterrows():
            print(f"{date.strftime('%Y-%m-%d')}: ${row['price']:,.2f}")

        # Calculate some basic statistics
        print("\nSummary Statistics:")
        print(f"Highest Price: ${df['price'].max():,.2f}")
        print(f"Lowest Price: ${df['price'].min():,.2f}")
        print(f"Average Price: ${df['price'].mean():,.2f}")
        print(f"Price Change: ${(df['price'].iloc[-1] - df['price'].iloc[0]):,.2f}")

        print("\n-----------------------------")
        df.to_csv(f'{args.coin}_prices.csv')
        print(f"Data saved to {args.coin}_prices.csv")

        # Create and save the plot
        print("\n-----------------------------")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'{args.coin}_prices_{timestamp}.png'
        file_information = {
            "coin":listOfCoin[args.coin].title(),
            "time":listOfTime[args.time]
        }
        saved_file = plot_prices(df, filename, file_information)
        print(f"Plot saved as: {saved_file}")


def get_data_coingecko_API(coin, time):
    # CoinGecko API endpoint for historical prices
    base_url = "https://api.coingecko.com/api/v3"

    start, end = time_interval_calculator(time)

    # Prepare the API request
    endpoint = f"{base_url}/coins/{coin}/market_chart/range"
    params = {
        'vs_currency': 'usd',
        'from': start,
        'to': end
    }

    try:
        data = fetch_api(endpoint,params)

        # Extract prices (comes as [timestamp, price] pairs)
        prices = data['prices']

        return prices

    except requests.exceptions.RequestException as e:
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
    df = pd.DataFrame(data, columns=['timestamp', 'price'])

    # Convert timestamp column to datetime format using milliseconds as the unit
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    # Remove the original timestamp column since we now have the date column
    df = df.drop('timestamp', axis=1)
    # Set the date column as the index of the DataFrame
    df = df.set_index('date')

    return df



if __name__ == "__main__":
    main()
