from dataclasses import dataclass

from counter_os.application.use_cases.counter_decrement_use_case import (
    CounterDecrementUseCase,
)
from counter_os.application.use_cases.counter_get_use_case import CounterGetUseCase
from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)
from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.interfaces.controllers.counter_controller import CounterController
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


@dataclass
class ApplicationContainer:
    """Application container which wires together all components"""

    counter_repository: CounterRepository
    counter_presenter: CounterPresenter

    def __post_init__(self):
        """Wire up all use cases and controllers"""

        # Configure all use cases as local variables
        counter_increment_use_case = CounterIncrementUseCase(self.counter_repository)
        counter_decrement_use_case = CounterDecrementUseCase(self.counter_repository)
        counter_get_use_case = CounterGetUseCase(self.counter_repository)
        counter_set_use_case = CounterSetUseCase(self.counter_repository)

        # Configure all controllers
        self.counter_controller = CounterController(
            increment_use_case=counter_increment_use_case,
            decrement_use_case=counter_decrement_use_case,
            get_use_case=counter_get_use_case,
            set_use_case=counter_set_use_case,
            presenter=self.counter_presenter,
        )
