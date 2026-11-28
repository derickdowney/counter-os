from unittest.mock import Mock

import pytest
from flask import Flask

from counter_os.infrastructure.flask_web.flask_web_app import FlaskWebApp


def test_FlaskWebApp_cannot_init_without_args():
    with pytest.raises(TypeError):
        FlaskWebApp()


def test_FlaskWebApp_init_requires_config_and_container():
    # Arrange
    mock_app_config = Mock()
    mock_app_container = Mock()

    # Act
    flask_web_app = FlaskWebApp(mock_app_config, mock_app_container)

    # Assert
    assert flask_web_app.app_config == mock_app_config
    assert flask_web_app.flask_app.config["APP_CONTAINER"] == mock_app_container


def test_FlaskWebApp_init_creates_flask_app():
    # Arrange
    mock_app_config = Mock()
    mock_app_container = Mock()

    # Act
    flask_web_app = FlaskWebApp(mock_app_config, mock_app_container)

    # Assert
    assert isinstance(flask_web_app.flask_app, Flask)
