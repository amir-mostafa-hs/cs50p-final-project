from argparse import ArgumentParser

def cli_tool(*args, description=""):
    """
    Creates a command line interface tool using argparse.
    
    Args:
        *args: Variable length list of dictionaries containing argument specifications.
              Each dictionary should have 'name', 'type' and 'help' keys.
        description (str): Description of the command line tool. Defaults to empty string.
    
    Returns:
        Namespace: Parsed command line arguments.
    
    Example:
        args = cli_tool(
            {"name": "--input", "type": str, "help": "Input file path"},
            {"name": "--output", "type": str, "help": "Output file path"},
            description="A file processing tool")
    """
    parser = ArgumentParser(description=description)

    for arg in args:
        parser.add_argument(arg["name"], type=arg["type"], help=arg["help"])

    args = parser.parse_args()

    return args
