from flask import Flask

from counter_os.infrastructure.flask_web.flask_app_factory import create_flask_app


def test_create_flask_app_factory_returns_Flask_instance():
    assert isinstance(create_flask_app(), Flask)
