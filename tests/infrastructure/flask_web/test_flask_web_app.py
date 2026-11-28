from unittest.mock import Mock

import pytest
from flask import Flask

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_environment_type import ApplicationEnvironmentType
from counter_os.infrastructure.flask_web.flask_web_app import (
    FlaskWebApp,
    StandaloneGunicornApplication,
    gunicorn_run,
)


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


def test_FlaskWebApp_run_when_app_env_invalid(monkeypatch, capsys):
    # Arrange
    mock_app_config = Mock()
    mock_app_config.app_env = "test"
    mock_app_config.flask_host = "10.20.30.40"
    mock_app_config.flask_port = 43210
    mock_app_container = Mock()
    mock_flask_app = Mock()
    monkeypatch.setattr(
        "counter_os.infrastructure.flask_web.flask_web_app.create_flask_app",
        lambda *args, **kwargs: mock_flask_app,
    )
    flask_web_app = FlaskWebApp(mock_app_config, mock_app_container)

    # Act
    exitcode: int = flask_web_app.run()

    # Assert
    output = capsys.readouterr()
    assert output.out == ""
    assert (
        output.err
        == '"test" is not a valid APP_ENV\nStarting app with "development" application environment type\n'
    )
    mock_flask_app.run.assert_called_once_with(
        debug=True, host="10.20.30.40", port=43210
    )
    assert exitcode == 0


def test_FlaskWebApp_run_when_app_env_development(monkeypatch):
    # Arrange
    mock_app_config = Mock()
    mock_app_config.app_env = ApplicationEnvironmentType.DEVELOPMENT
    mock_app_config.flask_host = "1.2.3.4"
    mock_app_config.flask_port = 4321
    mock_app_container = Mock()
    mock_flask_app = Mock()
    monkeypatch.setattr(
        "counter_os.infrastructure.flask_web.flask_web_app.create_flask_app",
        lambda *args, **kwargs: mock_flask_app,
    )
    flask_web_app = FlaskWebApp(mock_app_config, mock_app_container)

    # Act
    exitcode: int = flask_web_app.run()

    # Assert
    mock_flask_app.run.assert_called_once_with(debug=True, host="1.2.3.4", port=4321)
    assert exitcode == 0


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
    exitcode: int = flask_web_app.run()

    # Assert
    mock_gunicorn_run.assert_called_once_with(mock_app_config, flask_web_app.flask_app)
    assert exitcode == 0


def test_gunicorn_run(monkeypatch):
    # Arrange
    mock_app_config: ApplicationConfiguration = Mock()
    mock_app_config.flask_host = "5.6.7.8"
    mock_app_config.flask_port = 111
    mock_flask_app: Flask = Mock()
    mock_gunicorn_app_instance: StandaloneGunicornApplication = Mock()
    mock_standalone_gunicorn_app = Mock(return_value=mock_gunicorn_app_instance)
    monkeypatch.setattr(
        "counter_os.infrastructure.flask_web.flask_web_app.StandaloneGunicornApplication",
        mock_standalone_gunicorn_app,
    )

    # Act
    gunicorn_run(mock_app_config, mock_flask_app)

    # Assert
    mock_standalone_gunicorn_app.assert_called_once_with(
        mock_flask_app, {"bind": "5.6.7.8:111", "workers": 2}
    )
    mock_gunicorn_app_instance.run.assert_called_once_with()
