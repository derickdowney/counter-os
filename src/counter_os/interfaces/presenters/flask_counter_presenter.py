from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel


class FlaskCounterPresenter(CounterPresenter):
    def present_counter_response(
        self, counter_reponse: CounterResponse
    ) -> CounterViewModel:
        pass

    def present_error_response(self, error_reponse: ErrorResponse) -> ErrorViewModel:
        pass
