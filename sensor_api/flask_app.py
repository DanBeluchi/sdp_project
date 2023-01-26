#!/usr/bin/env python3

"""
Module for creating flask application.
"""

# yapf: disable
import sys  # nopep8
import os  # nopep8

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # nopep8
sys.path.append(os.path.dirname(SCRIPT_DIR))  # nopep8
# yapf: enable

# pylint: disable=C0413
from flask import Flask, render_template

# pylint: disable=E0401
from sensor_api.disk import disk  # type: ignore
from sensor_api.cpu import cpu  # type: ignore
from sensor_api.cpu_error import cpu_error  # type: ignore

# pylint: enable=E0401
# pylint: enable=C0413


def create_app(test_config=None):
    """
    Create flask application.
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def hello():
        return render_template("index.html")

    # Register disk usage
    app.register_blueprint(disk)

    # register cpu temp
    app.register_blueprint(cpu)

    # register cpu error
    app.register_blueprint(cpu_error)

    return app
