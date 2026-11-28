import sys

from flask import Flask
from gunicorn.app.base import BaseApplication as gunicorn_base

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.bootstrap.application_environment_type import ApplicationEnvironmentType
from counter_os.infrastructure.flask_web.flask_app_factory import create_flask_app


class FlaskWebApp:
    app_config: ApplicationConfiguration
    flask_app: Flask

    def __init__(
        self, app_config: ApplicationConfiguration, app_container: ApplicationContainer
    ):
        self.app_config = app_config
        self.flask_app = create_flask_app(app_container)

    def run(self) -> int:
        match self.app_config.app_env:
            case ApplicationEnvironmentType.DEVELOPMENT:
                self.flask_app.run(
                    host=self.app_config.flask_host,
                    port=self.app_config.flask_port,
                    debug=True,
                )
                return 0
            case ApplicationEnvironmentType.PRODUCTION:
                gunicorn_run(self.app_config, self.flask_app)
                return 0
            case _:
                print(
                    f'"{self.app_config.app_env}" is not a valid APP_ENV',
                    file=sys.stderr,
                )
                print(
                    'Starting app with "development" application environment type',
                    file=sys.stderr,
                )
                self.flask_app.run(
                    host=self.app_config.flask_host,
                    port=self.app_config.flask_port,
                    debug=True,
                )
                return 0


def gunicorn_run(app_config: ApplicationConfiguration, flask_app: Flask):
    options: dict[str, object] = {
        "bind": f"{app_config.flask_host}:{app_config.flask_port}",
        "workers": 2,
    }
    StandaloneGunicornApplication(flask_app, options).run()


class StandaloneGunicornApplication(gunicorn_base):
    def __init__(self, app: Flask, options: dict[str, object]):
        self.application = app
        self.options = options
        super().__init__()

    def load_config(self) -> None:
        assert self.cfg is not None
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self) -> Flask:
        return self.application
