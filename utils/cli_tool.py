from argparse import ArgumentParser

def cli_tool(*args, description=""):
    """
    Creates a command line interface tool using argparse.
    
    Args:
        *args: Variable length list of dictionaries containing argument specifications.
              Each dictionary should have "name", "type" and "help" keys.
        description (str): Description of the command line tool. Defaults to empty string.
    
    Returns:
        Namespace: Parsed command line arguments.
    
    Example:
        args = cli_tool(
            {"name": "--input", "type": str, "help": "Input file path"},
            {"name": "--output", "type": str, "help": "Output file path"},
            description="A file processing tool")
    """
    # Create an ArgumentParser instance with the provided description
    parser = ArgumentParser(description=description)

    # Iterate through each argument specification and add it to the parser
    for arg in args:
        parser.add_argument(arg["name"], type=arg["type"], help=arg["help"])

    # Parse the command line arguments
    args = parser.parse_args()

    # Return the parsed arguments
    return args
