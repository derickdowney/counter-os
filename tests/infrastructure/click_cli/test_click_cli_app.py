from unittest.mock import Mock

import pytest

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.bootstrap.application_factory import create_application_container
from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp
from counter_os.interfaces.operation_result import OperationError
from counter_os.interfaces.presenters.click_counter_presenter import (
    ClickCounterPresenter,
)
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


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


def test_ClickCliApp_run_keyboard_interrupt(monkeypatch, capsys):
    click_cli_app = ClickCliApp(app_container=Mock())

    def simulate_interrupt():
        raise KeyboardInterrupt

    monkeypatch.setattr(click_cli_app, "_display_current_count", simulate_interrupt)
    exit_code: int = click_cli_app.run()
    capturred = capsys.readouterr()
    assert exit_code == 0
    assert capturred.err == "\nGoodbye!\n"


def test_ClickCliApp_run_displays_current_count(capsys, click_cli_app):
    click_cli_app.run()
    output: str = capsys.readouterr().out
    assert output == "Current count is: 0\n"


def test_ClickCliApp_increment_count(capsys, click_cli_app):
    click_cli_app.run()
    output: str = capsys.readouterr().out
    assert output == "Current count is: 0\n"

    click_cli_app._increment_count()
    output = capsys.readouterr().out
    assert output == "Current count is: 1\n"

    click_cli_app._increment_count()
    output = capsys.readouterr().out
    assert output == "Current count is: 2\n"


def test_ClickCliApp_display_error(capsys, click_cli_app):
    op_error = OperationError(ErrorViewModel(message="some error message"))
    click_cli_app._display_error(op_error)
    error = capsys.readouterr().err
    assert error == "some error message\n"


def test_ClickCliApp_display_current_count_error_path(capsys):
    app_container: ApplicationContainer = Mock()
    op_error = OperationError(ErrorViewModel(message="some error"))
    app_container.counter_controller.handle_get.return_value = op_error
    click_cli_app = ClickCliApp(app_container)
    click_cli_app._display_current_count()
    err = capsys.readouterr().err
    assert err == "some error\n"
