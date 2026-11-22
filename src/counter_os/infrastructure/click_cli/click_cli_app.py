import click

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.interfaces.operation_result import (
    OperationError,
    OperationResult,
    OperationSuccess,
)
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


class ClickCliApp:
    def __init__(self, app_container: ApplicationContainer):
        self.app_container = app_container

    def _display_counter_view_model(self, counter_vm: CounterViewModel):
        click.echo(f"Current count is: {counter_vm.current_count}")

    def _display_error_view_model(self, error_vm: ErrorViewModel):
        click.echo(f"Error: {error_vm.message}", err=True)
        click.echo(f"Code: {error_vm.code}", err=True)

    def _display_unknown_result_type_error(self) -> None:
        click.echo("Something went wrong", err=True)
        click.echo("Operation resulted in neither success nor error", err=True)

    def _display_instructions(self) -> None:
        click.echo("[+] inc  [-] dec  [<num>] set  [q] quit")

    """

        USE CASES

    """

    def _get_count(self) -> None:
        op_result: OperationResult = self.app_container.counter_controller.handle_get()

        if isinstance(op_result, OperationSuccess):
            counter_vm: CounterViewModel = op_result.success_vm
            self._display_counter_view_model(counter_vm)
        elif isinstance(op_result, OperationError):
            error_vm: ErrorViewModel = op_result.error_vm
            self._display_error_view_model(error_vm)
        else:
            self._display_unknown_result_type_error()

    def _increment_count(self) -> None:
        op_result: OperationResult = (
            self.app_container.counter_controller.handle_increment()
        )

        if isinstance(op_result, OperationSuccess):
            counter_vm: CounterViewModel = op_result.success_vm
            self._display_counter_view_model(counter_vm)
        elif isinstance(op_result, OperationError):
            error_vm: ErrorViewModel = op_result.error_vm
            self._display_error_view_model(error_vm)
        else:
            self._display_unknown_result_type_error()

    def _decrement_count(self) -> None:
        op_result: OperationResult = (
            self.app_container.counter_controller.handle_decrement()
        )

        if isinstance(op_result, OperationSuccess):
            counter_vm: CounterViewModel = op_result.success_vm
            self._display_counter_view_model(counter_vm)
        elif isinstance(op_result, OperationError):
            error_vm: ErrorViewModel = op_result.error_vm
            self._display_error_view_model(error_vm)
        else:
            self._display_unknown_result_type_error()

    def _set_count(self, set_value: int) -> None:
        op_result: OperationResult = self.app_container.counter_controller.handle_set(
            set_value
        )

        if isinstance(op_result, OperationSuccess):
            counter_vm: CounterViewModel = op_result.success_vm
            self._display_counter_view_model(counter_vm)
        elif isinstance(op_result, OperationError):
            error_vm: ErrorViewModel = op_result.error_vm
            self._display_error_view_model(error_vm)
        else:
            self._display_unknown_result_type_error()

    # def run(self) -> int:
    #     try:
    #         self._display_current_count()
    #         return 0
    #     except KeyboardInterrupt:
    #         click.echo("\nGoodbye!", err=True)
    #         return 0

    # def _get_count(self) -> None:
    #     click.clear()
    #     result: OperationResult = self.app_container.counter_controller.handle_get()
    #     if isinstance(result, OperationSuccess):
    #         counter_vm: CounterViewModel = result.success_vm
    #         click.echo(f"Current count is: {counter_vm.current_count}")
    #     elif isinstance(result, OperationError):
    #         self._display_error(result)
    #     else:
    #         self._display_unknown_error()

    # def _increment_count(self) -> None:
    #     result: OperationResult = (
    #         self.app_container.counter_controller.handle_increment()
    #     )
    #     if isinstance(result, OperationSuccess):
    #         self._display_current_count()
    #     elif isinstance(result, OperationError):
    #         self._display_error(result)
    #     else:
    #         self._display_unknown_error()
    #
    # def _decrement_count(self) -> None:
    #     result: OperationResult = (
    #         self.app_container.counter_controller.handle_decrement()
    #     )
    #     if isinstance(result, OperationSuccess):
    #         counter_vm: CounterViewModel = result.success_vm
    #         self._display_counter_view_model(counter_vm)
    #     else:
    #         self._display_unknown_error()
