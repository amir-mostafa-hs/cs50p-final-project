from datetime import datetime, timedelta


def time_interval_calculator(time):
    # Calculate dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=time)

    # Convert dates to Unix timestamps (required by CoinGecko)
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    return (start_timestamp, end_timestamp)
