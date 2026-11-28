from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from counter_os.infrastructure.flask_web.app import flask_app


def test_flask_app_variable_is_Flask_instance():
    assert isinstance(flask_app, Flask)


def test_flask_app_health_check():
    client: FlaskClient = flask_app.test_client()
    response: TestResponse = client.get("/health")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == '{"status":"healthy"}\n'
    assert response.json == {"status": "healthy"}
    assert response.content_type == "application/json"
