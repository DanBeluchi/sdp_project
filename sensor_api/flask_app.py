"""
Module for creating flask application.
"""

import os

from flask import Flask
from . import disk
from . import cpu
from . import cpu_error


def create_app(test_config=None):
    """
    Create flask application.
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Register disk usage
    app.register_blueprint(disk.disk)

    # register cpu temp
    app.register_blueprint(cpu.cpu)

    # register cpu error
    app.register_blueprint(cpu_error.cpu_error)

    return app
