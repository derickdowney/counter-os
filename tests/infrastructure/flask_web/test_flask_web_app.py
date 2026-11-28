from unittest.mock import Mock

import pytest
from flask import Flask

from counter_os.bootstrap.application_environment_type import ApplicationEnvironmentType
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


def test_FlaskWebApp_run_when_app_env_development(monkeypatch):
    # Arrange
    mock_app_config = Mock()
    mock_app_config.app_env = ApplicationEnvironmentType.DEVELOPMENT
    mock_app_container = Mock()
    mock_flask_app = Mock()
    monkeypatch.setattr(
        "counter_os.infrastructure.flask_web.flask_web_app.create_flask_app",
        lambda *args, **kwargs: mock_flask_app,
    )
    flask_web_app = FlaskWebApp(mock_app_config, mock_app_container)

    # Act
    flask_web_app.run()

    # Assert
    mock_flask_app.run.assert_called_once_with(debug=True)


def test_FlaskWebApp_run_when_app_env_production(monkeypatch):
    # Arrange
    mock_app_config = Mock()
    mock_app_config.app_env = ApplicationEnvironmentType.PRODUCTION
    mock_app_container = Mock()
    flask_web_app = FlaskWebApp(mock_app_config, mock_app_container)
    mock_gunicorn_run = Mock()
    monkeypatch.setattr(
        "counter_os.infrastructure.flask_web.flask_web_app.gunicorn_run",
        mock_gunicorn_run,
    )

    # Act
    flask_web_app.run()

    # Assert
    mock_gunicorn_run.assert_called_once_with(mock_app_config)
