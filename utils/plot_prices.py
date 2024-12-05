import matplotlib.pyplot as plt

def plot_prices(df, filename="prices.png", info={"coin":"", "time":""}):
    """
    Create and save a line plot of price data over time.

    Args:
        df (pandas.DataFrame): DataFrame containing price data with datetime index and 'price' column
        filename (str, optional): Output filename for the saved plot. Defaults to "prices.png"
        info (dict, optional): Dictionary containing plot info with keys 'coin' and 'time'. Defaults to {"coin":"", "time":""}

    Returns:
        str: The filename of the saved plot

    The function creates a line plot showing price over time with:
    - Blue line for price data
    - Grid lines
    - Formatted y-axis labels with dollar signs
    - Rotated x-axis date labels
    - Title showing coin name and time period
    """
    plt.figure(figsize=(12, 6))

    # Plot the price data as a blue line
    plt.plot(df.index, df["price"], color="blue", linewidth=2)

    # Set the plot title with coin name and time period
    plt.title(f"{info["coin"]} Price Last {info["time"]} Days", fontsize=14, pad=20)
    
    # Add x and y axis labels
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)

    # Add grid lines
    plt.grid(True, linestyle="--", alpha=0.7)

    # Rotate x-axis date labels 45 degrees
    plt.xticks(rotation=45)

    # Format y-axis labels with dollar signs
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot to file with high resolution
    plt.savefig(filename, dpi=300, bbox_inches="tight")

    # Close the plot to free memory
    plt.close()

    # Return the filename of the saved plot
    return filename
