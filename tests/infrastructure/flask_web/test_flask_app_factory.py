from unittest.mock import Mock

from flask import Flask

from counter_os.infrastructure.flask_web.flask_app_factory import create_flask_app
from counter_os.infrastructure.flask_web.flask_routes import bp


def test_create_flask_app_factory_returns_Flask_instance():
    mock_app_container = Mock()
    assert isinstance(create_flask_app(mock_app_container), Flask)


def test_create_flask_app_factory_stores_ApplicationContainer_arg():
    # Arrange
    mock_app_container = Mock()

    # Act
    flask_app = create_flask_app(mock_app_container)

    # Assert
    assert flask_app.config["APP_CONTAINER"] == mock_app_container


def test_create_flask_app_factory_registers_blueprint():
    # Arrange
    mock_app_container = Mock()

    # Act
    flask_app = create_flask_app(mock_app_container)

    # Assert
    assert bp.name in flask_app.blueprints
