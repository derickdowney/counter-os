from flask import Flask

from counter_os.bootstrap.application_container import ApplicationContainer


def create_flask_app(app_container: ApplicationContainer) -> Flask:
    flask_app = Flask(__name__)

    flask_app.config["APP_CONTAINER"] = app_container

    return flask_app
