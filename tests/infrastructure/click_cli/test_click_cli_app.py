import pytest

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.bootstrap.application_factory import create_application_container
from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)


@pytest.fixture
def click_cli_app() -> ClickCliApp:
    presenter = ClickCounterPresenter()
    app = create_application_container(presenter)
    click_cli_app = ClickCliApp(app)
    return click_cli_app


def test_ClickCliApp_init_requires_ApplicationContainer():
    with pytest.raises(TypeError):
        ClickCliApp()


def test_ClickCliApp_display_count(capsys, click_cli_app):
    click_cli_app._display_current_count()
    output: str = capsys.readouterr().out
    assert output == "Current count is: 0\n"
    assert click_cli_app.cached_current_count == 0
