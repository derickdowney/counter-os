from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from counter_os.infrastructure.flask_web.flask_routes import bp


def test_route_health_check():
    # Arrange (without create_flask_app() factory dependency)
    flask_app = Flask(__name__)
    flask_app.register_blueprint(bp)
    client: FlaskClient = flask_app.test_client()

    # Act
    response: TestResponse = client.get("/health")

    # Assert
    assert response.status_code == 200
    assert response.get_data(as_text=True) == '{"status":"healthy"}\n'
    assert response.json == {"status": "healthy"}
    assert response.content_type == "application/json"
