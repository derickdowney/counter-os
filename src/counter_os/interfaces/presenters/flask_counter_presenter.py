from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel


class FlaskCounterPresenter(CounterPresenter):
    def present_counter_response(
        self, counter_response: CounterResponse
    ) -> CounterViewModel:
        return CounterViewModel(counter_response.current_count)

    def present_error_response(self, error_response: ErrorResponse) -> ErrorViewModel:
        pass
