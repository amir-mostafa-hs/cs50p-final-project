import matplotlib.pyplot as plt

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
