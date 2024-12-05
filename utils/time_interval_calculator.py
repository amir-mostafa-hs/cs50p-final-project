from datetime import datetime, timedelta

def time_interval_calculator(time):
    """
    Calculate start and end timestamps based on a given time interval from now.
    
    Args:
        time (int): Number of days to look back from current date
        
    Returns:
        tuple: A tuple containing:
            - start_timestamp (int): Unix timestamp for start date
            - end_timestamp (int): Unix timestamp for end date (current time)
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=time)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    return (start_timestamp, end_timestamp)
