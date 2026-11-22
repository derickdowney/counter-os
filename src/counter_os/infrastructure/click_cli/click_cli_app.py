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

    def run(self) -> int:
        try:
            self._display_current_count()
            return 0
        except KeyboardInterrupt:
            click.echo("\nGoodbye!", err=True)
            return 0

    def _display_current_count(self) -> None:
        click.clear()
        result: OperationResult = self.app_container.counter_controller.handle_get()
        if isinstance(result, OperationSuccess):
            counter_vm: CounterViewModel = result.success_vm
            click.echo(f"Current count is: {counter_vm.current_count}")
        elif isinstance(result, OperationError):
            self._display_error(result)
        else:
            self._display_unknown_error()

    def _increment_count(self) -> None:
        result: OperationResult = (
            self.app_container.counter_controller.handle_increment()
        )
        if isinstance(result, OperationSuccess):
            self._display_current_count()
        elif isinstance(result, OperationError):
            self._display_error(result)
        else:
            self._display_unknown_error()

    def _decrement_count(self) -> None:
        result: OperationResult = (
            self.app_container.counter_controller.handle_decrement()
        )
        if isinstance(result, OperationSuccess):
            counter_vm: CounterViewModel = result.success_vm
            self._display_counter_view_model(counter_vm)
        else:
            self._display_unknown_error()

    def _display_counter_view_model(self, counter_vm: CounterViewModel):
        click.echo(f"Current count is: {counter_vm.current_count}")

    def _display_error(self, op_error: OperationError) -> None:
        click.echo(op_error.error_vm.message, err=True)

    def _display_unknown_error(self) -> None:
        click.echo("Something went wrong", err=True)
