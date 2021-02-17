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
import os
import unittest
from flask.cli import FlaskGroup
from server import app

os.environ["FLASK_APP"] = "server.__main__:main()"


cli = FlaskGroup(app)


def main():
    return app


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover("test", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    cli()
