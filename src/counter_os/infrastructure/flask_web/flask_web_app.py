from dataclasses import dataclass

from counter_os.bootstrap.application_configuration import ApplicationConfiguration
from counter_os.bootstrap.application_container import ApplicationContainer


class FlaskWebApp:
    app_config: ApplicationConfiguration
    app_container: ApplicationContainer

    def __init__(
        self, app_config: ApplicationConfiguration, app_container: ApplicationContainer
    ):
        self.app_config = app_config
        self.app_container = app_container
