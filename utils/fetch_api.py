import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

def fetch_api(endpoint, params={}):
    """
    Fetches data from an API endpoint using GET request.

    Args:
        endpoint (str): The API endpoint URL to fetch data from.
        params (dict): Dictionary of query parameters to include in the request. Defaults to empty dict.

    Returns:
        dict: JSON response from the API.

    Raises:
        RequestException: If any error occurs during the API request:
            - Rate limit exceeded (HTTP 429).
            - Other HTTP errors.
            - Connection errors.
            - Timeout errors.
            - General request errors.
    """
    try:
        # Send GET request to endpoint with optional parameters
        response = requests.get(endpoint, params=params)
        # Raise exception for HTTP error status codes (4xx, 5xx)
        response.raise_for_status()  

        # Parse and return JSON response
        return response.json()


    except HTTPError as http_err:
        # Handle rate limit exceeded error (HTTP 429)
        if response.status_code == 429:  
            raise RequestException("Rate limit exceeded. Please wait before trying again.")
        else:
            # Handle other HTTP errors
            raise RequestException(f"HTTP error occurred: {http_err}")

    except ConnectionError as conn_err:
        # Handle connection errors (DNS failures, refused connections, etc)
        raise RequestException(f"Error connecting to server: {conn_err}")

    except Timeout as timeout_err:
        # Handle request timeout errors
        raise RequestException(f"Timeout error: {timeout_err}")

    except RequestException as req_err:
        # Handle any other request-related errors
        raise RequestException(f"An error occurred: {req_err}")
