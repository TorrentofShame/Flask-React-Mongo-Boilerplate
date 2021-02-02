# -*- coding: utf-8 -*-
"""
    server.__main__
    ~~~~~~~~~~~~~~~

    The main file, allows for easy starting of the backend server.

    Functions:

        main()

    Misc Variables:

        parser
        args
        app
"""
import argparse
from server import app

# Setup the Parser
parser = argparse.ArgumentParser()

# Define the arguments
parser.add_argument("--host", type=str, help="The host to listen on (default: 127.0.0.1)", default="127.0.0.1")
parser.add_argument("--port", type=int, help="The port to listen on (default: 5000)", default=5000)
args = parser.parse_args()

def main():
    app.run(host=args.host, port=args.port)
    print(f"Listening on: {args.host}:{args.port}")

if __name__ == "__main__":
    main()
