import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import sys

def get_btc_prices_last_week():
    # CoinGecko API endpoint for historical prices
    base_url = "https://api.coingecko.com/api/v3"

    # Calculate dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    # Convert dates to Unix timestamps (required by CoinGecko)
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    # Prepare the API request
    endpoint = f"{base_url}/coins/bitcoin/market_chart/range"
    params = {
        'vs_currency': 'usd',
        'from': start_timestamp,
        'to': end_timestamp
    }

    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the response
        data = response.json()

        # Extract prices (comes as [timestamp, price] pairs)
        prices = data['prices']

        # Convert to DataFrame for easier handling
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])

        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Clean up the DataFrame
        df = df.drop('timestamp', axis=1)
        df = df.set_index('date')

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None




def plot_btc_prices(df, filename='bitcoin_prices.png'):
    """
    Create and save a plot of Bitcoin prices

    Args:
        df: DataFrame with price data
        filename: Name of the file to save the plot (default: 'bitcoin_prices.png')
    """
    # Create the plot
    plt.figure(figsize=(12, 6))

    # Plot the price data
    plt.plot(df.index, df['price'], color='blue', linewidth=2)

    # Customize the plot
    plt.title('Bitcoin Price Last 7 Days', fontsize=14, pad=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)

    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add thousand separator to y-axis
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot
    plt.savefig(filename, dpi=300, bbox_inches='tight')

    # Close the plot to free memory
    plt.close()

    return filename




def main():
    # Get the prices
    prices_df = get_btc_prices_last_week()

    if prices_df is not None:
        # Create and save the plot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'bitcoin_prices_{timestamp}.png'
        saved_file = plot_btc_prices(prices_df, filename)
        print(f"\nPlot saved as: {saved_file}")

    if prices_df is not None:
        prices_df.to_csv('btc_prices.csv')
        print("\nData saved to btc_prices.csv")

    if prices_df is not None:
        # Display the results
        print("\nBitcoin Prices (Last 7 Days):")
        print("-----------------------------")

        # Resample to daily data (taking the mean price for each day)
        daily_prices = prices_df.resample('D').mean()

        for date, row in daily_prices.iterrows():
            print(f"{date.strftime('%Y-%m-%d')}: ${row['price']:,.2f}")

        # Calculate some basic statistics
        print("\nSummary Statistics:")
        print(f"Highest Price: ${prices_df['price'].max():,.2f}")
        print(f"Lowest Price: ${prices_df['price'].min():,.2f}")
        print(f"Average Price: ${prices_df['price'].mean():,.2f}")
        print(f"Price Change: ${(prices_df['price'].iloc[-1] - prices_df['price'].iloc[0]):,.2f}")

if __name__ == "__main__":
    main()
