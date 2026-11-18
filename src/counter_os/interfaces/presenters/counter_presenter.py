from abc import ABC, abstractmethod

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


class CounterPresenter(ABC):
    """Abstract base presenter for counter-related output."""

    @abstractmethod
    def present_counter_response(
        self, counter_response: CounterResponse
    ) -> CounterViewModel:
        pass

    @abstractmethod
    def present_error_response(self, error_response: ErrorResponse) -> ErrorViewModel:
        pass
