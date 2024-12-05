import pytest
import pandas as pd
from project import process_price_data, time_interval_calculator

def test_process_price_data():
    """Test if process_price_data correctly processes price data"""
    # Test data
    test_prices = [
        [1704495600000, 100.0],  # Some timestamp with price
        [1704582000000, 150.0]   # Another timestamp with price
    ]
    
    # Process the test data
    df = process_price_data(test_prices)
    
    # Test cases
    # Verify the return type is a pandas DataFrame
    assert isinstance(df, pd.DataFrame)
    # Check the DataFrame has the expected number of rows
    assert len(df) == 2
    # Verify the 'price' column exists in the DataFrame
    assert 'price' in df.columns
    # Check first price value matches input
    assert df['price'].iloc[0] == 100.0
    # Check second price value matches input
    assert df['price'].iloc[1] == 150.0


def test_time_interval_calculator():
    """Test if time_interval_calculator returns correct intervals"""
    # Test with 7 days
    start, end = time_interval_calculator(7)
    
    # Basic checks
    # Verify start and end are integers
    assert isinstance(start, int)
    assert isinstance(end, int)
    # Ensure end timestamp is after start timestamp
    assert end > start
    # Verify interval is at least 7 days (in seconds)
    assert end - start >= (7 * 24 * 60 * 60)


def test_process_price_data_empty():
    """Test process_price_data with empty input"""
    # Test with empty list input
    df = process_price_data([])
    # Verify empty DataFrame is returned
    assert len(df) == 0
    # Ensure return type is still DataFrame even when empty
    assert isinstance(df, pd.DataFrame)


def test_process_price_data_single():
    """Test process_price_data with single data point"""
    # Create test data with a single price point
    test_prices = [[1704495600000, 100.0]]
    # Process the single data point
    df = process_price_data(test_prices)
    
    # Verify DataFrame has exactly one row
    assert len(df) == 1
    # Check the price value matches input
    assert df['price'].iloc[0] == 100.0
