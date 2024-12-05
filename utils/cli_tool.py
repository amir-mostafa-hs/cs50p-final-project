from argparse import ArgumentParser

def cli_tool(*args, description=""):
    parser = ArgumentParser(description=description)

    for arg in args:
        parser.add_argument(arg["name"], type=arg["type"], help=arg["help"])

    args = parser.parse_args()

    return args
