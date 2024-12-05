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

    plt.plot(df.index, df["price"], color="blue", linewidth=2)

    plt.title(f"{info["coin"]} Price Last {info["time"]} Days", fontsize=14, pad=20)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)

    plt.grid(True, linestyle="--", alpha=0.7)

    plt.xticks(rotation=45)

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

    plt.tight_layout()

    plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.close()

    return filename
