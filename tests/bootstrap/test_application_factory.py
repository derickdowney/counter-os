from unittest.mock import Mock

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.bootstrap.application_factory import create_application_container


def test_create_application_container_factory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "counter_os.bootstrap.application_factory.create_repositories",
        lambda *args, **kwargs: (Mock(),),
    )
    app: ApplicationContainer = create_application_container(
        config=Mock(), counter_presenter=Mock()
    )
    assert isinstance(app, ApplicationContainer)
