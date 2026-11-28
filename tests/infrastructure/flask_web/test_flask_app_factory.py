from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from counter_os.infrastructure.flask_web.flask_app_factory import create_flask_app


def test_flask_app_variable_is_Flask_instance():
    assert isinstance(create_flask_app(), Flask)
