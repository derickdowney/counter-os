from unittest.mock import Mock

import pytest

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp
from counter_os.interfaces.operation_result import OperationError, OperationSuccess
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


def test_ClickCliApp_init_requires_ApplicationContainer():
    with pytest.raises(TypeError):
        ClickCliApp()


def test_ClickCliApp_display_counter_view_model(capsys):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    counter_vm = CounterViewModel(11)

    # Act
    click_cli_app._display_counter_view_model(counter_vm)

    # Assert
    assert capsys.readouterr().out == "Current count is: 11\n"


def test_ClickCliApp_display_error_view_model(capsys):
    # Arrange
    mock_app_container: ApplicationContainer = Mock()
    click_cli_app = ClickCliApp(mock_app_container)
    error_vm = ErrorViewModel("some error", "SOME_CODE")

    # Act
    click_cli_app._display_error_view_model(error_vm)

    # Assert
    assert capsys.readouterr().err == "Error: some error\nCode: SOME_CODE\n"


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


# def test_ClickCliApp_display_count(capsys, click_cli_app):
#     click_cli_app._display_current_count()
#     output: str = capsys.readouterr().out
#     assert output == "Current count is: 0\n"


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
#
# def test_ClickCliApp_run_displays_current_count(capsys, click_cli_app):
#     click_cli_app.run()
#     output: str = capsys.readouterr().out
#     assert output == "Current count is: 0\n"
#
#
# def test_ClickCliApp_increment_count(capsys, click_cli_app):
#     click_cli_app.run()
#     output: str = capsys.readouterr().out
#     assert output == "Current count is: 0\n"
#
#     click_cli_app._increment_count()
#     output = capsys.readouterr().out
#     assert output == "Current count is: 1\n"
#
#     click_cli_app._increment_count()
#     output = capsys.readouterr().out
#     assert output == "Current count is: 2\n"
#
#
# # def test_ClickCliApp_display_error(capsys, click_cli_app):
# #     op_error = OperationError(ErrorViewModel(message="some error message"))
# #     click_cli_app._display_error(op_error)
# #     error = capsys.readouterr().err
# #     assert error == "some error message\n"
#
#
# # def test_ClickCliApp_display_current_count_error_path(capsys):
# #     app_container: ApplicationContainer = Mock()
# #     op_error = OperationError(ErrorViewModel(message="some error"))
# #     app_container.counter_controller.handle_get.return_value = op_error
# #     click_cli_app = ClickCliApp(app_container)
# #     click_cli_app._display_current_count()
# #     err = capsys.readouterr().err
# #     assert err == "some error\n"
# #
# #
# # def test_ClickCliApp_increment_count_error_path(capsys):
# #     app_container: ApplicationContainer = Mock()
# #     op_error = OperationError(ErrorViewModel(message="another error"))
# #     app_container.counter_controller.handle_increment.return_value = op_error
# #     click_cli_app = ClickCliApp(app_container)
# #     click_cli_app._increment_count()
# #     err = capsys.readouterr().err
# #     assert err == "another error\n"
# #
#
#
# def test_ClickCliApp_decrement_count_success(capsys):
#     # Arrange
#     mock_app_container: ApplicationContainer = Mock()
#     mock_op_success = OperationSuccess(CounterViewModel(49))
#     mock_app_container.counter_controller.handle_decrement.return_value = (
#         mock_op_success
#     )
#     click_cli_app = ClickCliApp(mock_app_container)
#
#     # Act
#     click_cli_app._decrement_count()
#
#     # Assert
#     mock_app_container.counter_controller.handle_decrement.assert_called_once()
#     assert capsys.readouterr().out == "Current count is: 49\n"
#
#
# # def test_ClickCliApp_decrement_count_error(capsys):
# #     # Arrange
# #     mock_app_container: ApplicationContainer = Mock()
# #     mock_op_error = OperationError(ErrorViewModel("some error", "SOME_CODE"))
# #     mock_app_container.counter_controller.handle_decrement.return_value = mock_op_error
# #     click_cli_app = ClickCliApp(mock_app_container)
# #
# #     # Act
# #     click_cli_app._decrement_count()
# #
# #     # Assert
# #     mock_app_container.counter_controller.handle_decrement.assert_called_once()
# #     assert capsys.readouterr().err == "Error: some error\nCode: SOME_CODE"
