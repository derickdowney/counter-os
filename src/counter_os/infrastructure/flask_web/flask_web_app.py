from flask import Flask

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.infrastructure.flask_web.flask_app_factory import create_flask_app


class FlaskWebApp:
    app_config: ApplicationConfiguration
    flask_app: Flask

    def __init__(
        self, app_config: ApplicationConfiguration, app_container: ApplicationContainer
    ):
        self.app_config = app_config
        self.flask_app = create_flask_app(app_container)
