from counter_os.infrastructure.flask_web.app import flask_app
from flask import Flask


def test_flask_app_variable_is_Flask_instance():
    isinstance(flask_app, Flask)
