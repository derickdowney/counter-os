from flask import Flask

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

    def run(self):
        match self.app_config.app_env:
            case ApplicationEnvironmentType.DEVELOPMENT:
                self.flask_app.run(
                    host=self.app_config.flask_host,
                    port=self.app_config.flask_port,
                    debug=True,
                )
            case ApplicationEnvironmentType.PRODUCTION:
                gunicorn_run(self.app_config)
            case _:
                print("error")


def gunicorn_run(app_config: ApplicationConfiguration):
    pass
