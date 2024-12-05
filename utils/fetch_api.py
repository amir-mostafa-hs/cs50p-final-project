import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

def fetch_api(endpoint, params):
    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the response
        return response.json()


    except HTTPError as http_err:
        # Handle HTTP errors (4XX and 5XX status codes)
        if response.status_code == 429:  # Rate limit exceeded
            raise RequestException("Rate limit exceeded. Please wait before trying again.")
        else:
            raise RequestException(f"HTTP error occurred: {http_err}")

    except ConnectionError as conn_err:
        # Handle connection errors
        raise RequestException(f"Error connecting to server: {conn_err}")

    except Timeout as timeout_err:
        # Handle timeout errors
        raise RequestException(f"Timeout error: {timeout_err}")

    except RequestException as req_err:
        # Handle other requests-related errors
        raise RequestException(f"An error occurred: {req_err}")
