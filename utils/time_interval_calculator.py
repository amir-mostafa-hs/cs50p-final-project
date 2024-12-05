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
    # Get current date and time
    end_date = datetime.now()
    # Calculate start date by subtracting given number of days from end date
    start_date = end_date - timedelta(days=time)

    # Convert start date to Unix timestamp
    start_timestamp = int(start_date.timestamp())
    # Convert end date to Unix timestamp 
    end_timestamp = int(end_date.timestamp())

    # Return tuple of start and end timestamps
    return (start_timestamp, end_timestamp)
