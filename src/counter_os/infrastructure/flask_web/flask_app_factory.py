from flask import Flask

from counter_os.bootstrap.application_container import ApplicationContainer


def create_flask_app(app_container: ApplicationContainer) -> Flask:
    flask_app = Flask(__name__)

    flask_app.config["APP_CONTAINER"] = app_container

    from . import flask_routes

    flask_app.register_blueprint(flask_routes.bp)

    return flask_app
