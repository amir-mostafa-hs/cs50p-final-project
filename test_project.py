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
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'price' in df.columns
    assert df['price'].iloc[0] == 100.0
    assert df['price'].iloc[1] == 150.0


def test_time_interval_calculator():
    """Test if time_interval_calculator returns correct intervals"""
    # Test with 7 days
    start, end = time_interval_calculator(7)
    
    # Basic checks
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert end > start
    assert end - start >= (7 * 24 * 60 * 60)  # At least 7 days difference


def test_process_price_data_empty():
    """Test process_price_data with empty input"""
    df = process_price_data([])
    assert len(df) == 0
    assert isinstance(df, pd.DataFrame)


def test_process_price_data_single():
    """Test process_price_data with single data point"""
    test_prices = [[1704495600000, 100.0]]
    df = process_price_data(test_prices)
    
    assert len(df) == 1
    assert df['price'].iloc[0] == 100.0