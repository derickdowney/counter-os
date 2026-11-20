from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


class TyperCounterPresenter(CounterPresenter):
    """Counter presenter for the Typer command-line interface"""

    def present_counter_response(
        self, counter_response: CounterResponse
    ) -> CounterViewModel:
        current_count: str = f"Current count is: {counter_response.current_count}"
        return CounterViewModel(current_count)

    def present_error_response(self, error_response: ErrorResponse) -> ErrorViewModel:
        return ErrorViewModel(error_response.message, error_response.code)
