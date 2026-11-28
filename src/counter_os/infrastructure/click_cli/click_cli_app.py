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

    """

        DISPLAYS

    """

    def _display_counter_view_model(self, counter_vm: CounterViewModel):
        click.echo(f"Current count is: {counter_vm.current_count}\n")

    def _display_error_view_model(self, error_vm: ErrorViewModel):
        click.echo(f"Error: {error_vm.message}", err=True)
        click.echo(f"Code: {error_vm.code}\n", err=True)

    def _display_unknown_result_type_error(self) -> None:
        click.echo("Something went wrong", err=True)
        click.echo("Operation resulted in neither success nor error", err=True)

    def _display_instructions(self) -> None:
        click.echo("[+] inc  [-] dec  [<num>] set  [q] quit")

    def _display_invalid_command(self, user_input: str) -> None:
        click.echo(f"Invalid command: '{user_input}'\n", err=True)

    def _display_counter_repository_info(self) -> None:
        click.echo(
            "Counter repository type: "
            + self.app_container.counter_repository.repository_type()
        )
        click.echo(
            "Counter repository location: "
            + self.app_container.counter_repository.repository_location()
            + "\n"
        )

    """

        RUN LOOP AND PROMPTS

    """

    def _prompt_user_interaction(self) -> bool:
        user_input = click.prompt("", type=str, show_default=False).strip().lower()

        if user_input == "q":
            return False

        if user_input == "+":
            click.clear()
            self._increment_count()
            return True

        if user_input == "-":
            click.clear()
            self._decrement_count()
            return True

        try:
            click.clear()
            number: int = int(user_input)
            self._set_count(number)
        except ValueError:
            self._display_invalid_command(user_input)
            self._get_count()

        return True

    def run(self) -> int:
        try:
            click.clear()
            self._display_counter_repository_info()
            self._get_count()
            while True:
                self._display_instructions()
                should_continue: bool = self._prompt_user_interaction()
                if not should_continue:
                    click.echo("\nGoodbye!")
                    return 0
        except KeyboardInterrupt:
            click.echo("\nGoodbye!", err=True)
            return 0

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
            self._get_count()
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
            self._get_count()
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
            self._get_count()
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
