from unittest.mock import Mock

import click
import pytest

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp
from counter_os.interfaces.operation_result import OperationError, OperationSuccess
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


def test_ClickCliApp_init_requires_ApplicationContainer():
    with pytest.raises(TypeError):
        ClickCliApp()


"""

    DISPLAY

"""


def test_ClickCliApp_display_counter_view_model(capsys):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    counter_vm = CounterViewModel(11)

    # Act
    click_cli_app._display_counter_view_model(counter_vm)

    # Assert
    captured = capsys.readouterr()
    assert captured.out == "Current count is: 11\n\n"
    assert captured.err == ""


def test_ClickCliApp_display_error_view_model(capsys):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    error_vm = ErrorViewModel("some error", "SOME_CODE")

    # Act
    click_cli_app._display_error_view_model(error_vm)

    # Assert
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "Error: some error\nCode: SOME_CODE\n\n"


def test_ClickCliApp_display_instructions(capsys):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)

    # Act
    click_cli_app._display_instructions()

    # Assert
    captured = capsys.readouterr()
    assert captured.out == "[+] inc  [-] dec  [<num>] set  [q] quit\n"
    assert captured.err == ""


def test_ClickCliApp_display_invalid_command(capsys):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)

    # Act
    click_cli_app._display_invalid_command("some input")

    # Assert
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "Invalid command: 'some input'\n\n"


def test_ClickCliApp_display_counter_repository_info(capsys, monkeypatch):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_repository.repository_type.return_value = (
        "some_repository_type"
    )
    mock_app_container.counter_repository.repository_location.return_value = (
        "some_repository_location.db3"
    )
    click_cli_app = ClickCliApp(mock_app_container)

    # Act
    click_cli_app._display_counter_repository_info()

    # Assert
    captured = capsys.readouterr()
    expected_output = """Counter repository type: some_repository_type
Counter repository location: some_repository_location.db3

"""
    assert captured.out == expected_output
    assert captured.err == ""


"""

    RUN LOOP AND PROMPTS

"""


@pytest.mark.parametrize(
    "user_input",
    ["+", " +", "+ ", " + "],
)
def test_ClickCliApp_prompt_user_interaction_increment_count(
    user_input, monkeypatch
) -> None:
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._increment_count = Mock()
    monkeypatch.setattr(click, "prompt", Mock(return_value=user_input))

    # Act
    should_continue: bool = click_cli_app._prompt_user_interaction()

    # Assert
    click_cli_app._increment_count.assert_called_once()
    assert should_continue == True


@pytest.mark.parametrize(
    "user_input",
    ["-", " -", "- ", " - "],
)
def test_ClickCliApp_prompt_user_interaction_decrement_count(
    user_input, monkeypatch
) -> None:
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._decrement_count = Mock()
    monkeypatch.setattr(click, "prompt", Mock(return_value=user_input))

    # Act
    should_continue: bool = click_cli_app._prompt_user_interaction()

    # Assert
    click_cli_app._decrement_count.assert_called_once()
    assert should_continue == True


@pytest.mark.parametrize(
    "user_input",
    ["q", " q", "q ", " q "],
)
def test_ClickCliApp_prompt_user_interaction_quit(user_input, monkeypatch) -> None:
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    monkeypatch.setattr(click, "prompt", Mock(return_value=user_input))

    # Act
    should_continue: bool = click_cli_app._prompt_user_interaction()

    # Assert
    # click_cli_app.sys.exit.assert_called_once()
    assert should_continue == False


@pytest.mark.parametrize("user_input", ["0", " 1", "20 ", " 97 ", "1000000"])
def test_ClickCliApp_prompt_user_interaction_set_count_success(
    user_input, monkeypatch
) -> None:
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._set_count = Mock()
    monkeypatch.setattr(click, "prompt", Mock(return_value=user_input))

    # Act
    should_continue: bool = click_cli_app._prompt_user_interaction()

    # Assert
    click_cli_app._set_count.assert_called_once()
    assert should_continue == True


@pytest.mark.parametrize(
    "user_input",
    ["hello", " 1b", "@ ", " ] "],
)
def test_ClickCliApp_prompt_user_interaction_set_count_invalid(
    user_input, monkeypatch
) -> None:
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_invalid_command = Mock()
    monkeypatch.setattr(click, "prompt", Mock(return_value=user_input))

    # Act
    click_cli_app._prompt_user_interaction()

    # Assert
    click_cli_app._display_invalid_command.assert_called_once()


def test_ClickCliApp_run_loops_until_keyboard_interrupt(monkeypatch, capsys) -> None:
    # Arrange
    mock_app_container: Mock = Mock()
    click_cli_app: ClickCliApp = ClickCliApp(mock_app_container)

    # Arrange - _display_counter_repository_info()
    display_counter_repository_info_calls: int = 0

    def fake_counter_repo_info() -> None:
        nonlocal display_counter_repository_info_calls
        display_counter_repository_info_calls += 1

    monkeypatch.setattr(
        click_cli_app, "_display_counter_repository_info", fake_counter_repo_info
    )

    # Arrange - _get_count()
    get_count_calls: int = 0

    def fake_get_count() -> None:
        nonlocal get_count_calls
        get_count_calls += 1

    monkeypatch.setattr(click_cli_app, "_get_count", fake_get_count)

    # Arrange - _display_instructions()
    display_instructions_calls: int = 0

    def fake_display_instructions() -> None:
        nonlocal display_instructions_calls
        display_instructions_calls += 1

    monkeypatch.setattr(
        click_cli_app, "_display_instructions", fake_display_instructions
    )

    # Arrange - _prompt_user_interaction()
    prompt_user_calls: int = 0

    def fake_prompt_user() -> bool:
        nonlocal prompt_user_calls
        prompt_user_calls += 1
        if prompt_user_calls >= 3:
            raise KeyboardInterrupt
        return True

    monkeypatch.setattr(
        click_cli_app,
        "_prompt_user_interaction",
        fake_prompt_user,
    )

    # Act
    exit_code: int = click_cli_app.run()

    # Assert
    assert exit_code == 0
    assert get_count_calls == 1
    assert display_counter_repository_info_calls == 1
    assert display_instructions_calls == 3
    assert prompt_user_calls == 3
    captured = capsys.readouterr()
    assert captured.err == "\nGoodbye!\n"


"""

    GET COUNT

"""


def test_ClickCliApp_get_count_success():
    # Arrange
    mock_counter_vm = CounterViewModel(27)
    mock_op_success = OperationSuccess(mock_counter_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_get.return_value = mock_op_success
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_counter_view_model = Mock()

    # Act
    click_cli_app._get_count()

    # Assert
    mock_app_container.counter_controller.handle_get.assert_called_once()
    click_cli_app._display_counter_view_model.assert_called_once_with(mock_counter_vm)


def test_ClickCliApp_get_count_error():
    # Arrange
    mock_error_vm = ErrorViewModel("some error", "SOME_CODE")
    mock_op_error = OperationError(mock_error_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_get.return_value = mock_op_error
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_error_view_model = Mock()

    # Act
    click_cli_app._get_count()

    # Assert
    mock_app_container.counter_controller.handle_get.assert_called_once()
    click_cli_app._display_error_view_model.assert_called_once_with(mock_error_vm)


def test_ClickCliApp_get_count_unknown_error():
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_get.return_value = None
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_unknown_result_type_error = Mock()

    # Act
    click_cli_app._get_count()

    # Assert
    mock_app_container.counter_controller.handle_get.assert_called_once()
    click_cli_app._display_unknown_result_type_error.assert_called_once()


"""

    INCREMENT COUNT

"""


def test_ClickCliApp_increment_count_success():
    # Arrange
    mock_counter_vm = CounterViewModel(27)
    mock_op_success = OperationSuccess(mock_counter_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_increment.return_value = (
        mock_op_success
    )
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_counter_view_model = Mock()

    # Act
    click_cli_app._increment_count()

    # Assert
    mock_app_container.counter_controller.handle_increment.assert_called_once()
    click_cli_app._display_counter_view_model.assert_called_once_with(mock_counter_vm)


def test_ClickCliApp_increment_count_error():
    # Arrange
    mock_error_vm = ErrorViewModel("some error", "SOME_CODE")
    mock_op_error = OperationError(mock_error_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_increment.return_value = mock_op_error
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_error_view_model = Mock()

    # Act
    click_cli_app._increment_count()

    # Assert
    mock_app_container.counter_controller.handle_increment.assert_called_once()
    click_cli_app._display_error_view_model.assert_called_once_with(mock_error_vm)


def test_ClickCliApp_increment_count_unknown_error():
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_increment.return_value = None
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_unknown_result_type_error = Mock()

    # Act
    click_cli_app._increment_count()

    # Assert
    mock_app_container.counter_controller.handle_increment.assert_called_once()
    click_cli_app._display_unknown_result_type_error.assert_called_once()


"""

    DECREMENT COUNT

"""


def test_ClickCliApp_decrement_count_success():
    # Arrange
    mock_counter_vm = CounterViewModel(27)
    mock_op_success = OperationSuccess(mock_counter_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_decrement.return_value = (
        mock_op_success
    )
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_counter_view_model = Mock()

    # Act
    click_cli_app._decrement_count()

    # Assert
    mock_app_container.counter_controller.handle_decrement.assert_called_once()
    click_cli_app._display_counter_view_model.assert_called_once_with(mock_counter_vm)


def test_ClickCliApp_decrement_count_error():
    # Arrange
    mock_error_vm = ErrorViewModel("some error", "SOME_CODE")
    mock_op_error = OperationError(mock_error_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_decrement.return_value = mock_op_error
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_error_view_model = Mock()

    # Act
    click_cli_app._decrement_count()

    # Assert
    mock_app_container.counter_controller.handle_decrement.assert_called_once()
    click_cli_app._display_error_view_model.assert_called_once_with(mock_error_vm)


def test_ClickCliApp_decrement_count_unknown_error():
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_decrement.return_value = None
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_unknown_result_type_error = Mock()

    # Act
    click_cli_app._decrement_count()

    # Assert
    mock_app_container.counter_controller.handle_decrement.assert_called_once()
    click_cli_app._display_unknown_result_type_error.assert_called_once()


"""

    SET COUNT

"""


def test_ClickCliApp_set_count_success():
    # Arrange
    mock_counter_vm = CounterViewModel(50)
    mock_op_success = OperationSuccess(mock_counter_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_set.return_value = mock_op_success
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_counter_view_model = Mock()

    # Act
    click_cli_app._set_count(50)

    # Assert
    mock_app_container.counter_controller.handle_set.assert_called_once()
    click_cli_app._display_counter_view_model.assert_called_once_with(mock_counter_vm)


def test_ClickCliApp_set_count_error():
    # Arrange
    mock_error_vm = ErrorViewModel("some error", "SOME_CODE")
    mock_op_error = OperationError(mock_error_vm)
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_set.return_value = mock_op_error
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_error_view_model = Mock()

    # Act
    click_cli_app._set_count(-1)

    # Assert
    mock_app_container.counter_controller.handle_set.assert_called_once()
    click_cli_app._display_error_view_model.assert_called_once_with(mock_error_vm)


def test_ClickCliApp_set_count_unknown_error():
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    mock_app_container.counter_controller.handle_set.return_value = None
    click_cli_app = ClickCliApp(mock_app_container)
    click_cli_app._display_unknown_result_type_error = Mock()

    # Act
    click_cli_app._set_count(50)

    # Assert
    mock_app_container.counter_controller.handle_set.assert_called_once()
    click_cli_app._display_unknown_result_type_error.assert_called_once()


# def test_ClickCliApp_run_keyboard_interrupt(monkeypatch, capsys):
#     click_cli_app = ClickCliApp(app_container=Mock())
#
#     def simulate_interrupt():
#         raise KeyboardInterrupt
#
#     monkeypatch.setattr(click_cli_app, "_display_current_count", simulate_interrupt)
#     exit_code: int = click_cli_app.run()
#     capturred = capsys.readouterr()
#     assert exit_code == 0
#     assert capturred.err == "\nGoodbye!\n"
#
