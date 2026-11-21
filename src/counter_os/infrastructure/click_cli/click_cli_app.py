import click

from counter_os.bootstrap.application_container import ApplicationContainer
from counter_os.interfaces.operation_result import OperationResult, OperationSuccess
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel


class ClickCliApp:
    def __init__(self, app: ApplicationContainer):
        self.app_container = app

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
        else:
            # TODO: Display error
            pass

    def _increment_count(self) -> None:
        result: OperationResult = (
            self.app_container.counter_controller.handle_increment()
        )
        if isinstance(result, OperationSuccess):
            self._display_current_count()
        else:
            # TODO: Display error
            pass
