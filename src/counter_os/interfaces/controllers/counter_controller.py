from dataclasses import dataclass

from counter_os.application.result import Error, Result, Success
from counter_os.application.use_cases.counter_decrement_use_case import (
    CounterDecrementUseCase,
)
from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)
from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase
from counter_os.interfaces.operation_result import (
    OperationError,
    OperationResult,
    OperationSuccess,
)
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


@dataclass
class CounterController:
    increment_use_case: CounterIncrementUseCase
    decrement_use_case: CounterDecrementUseCase
    set_use_case: CounterSetUseCase
    presenter: CounterPresenter

    def handle_increment(self) -> OperationResult:
        result: Result = self.increment_use_case.execute()

        if isinstance(result, Success):
            success_vm: CounterViewModel = self.presenter.present_counter_response(
                result.success_response
            )
            return OperationSuccess(success_vm)

        if isinstance(result, Error):
            error_vm: ErrorViewModel = self.presenter.present_error_response(
                result.error_response
            )
            return OperationError(error_vm)

        raise TypeError(f"Unexpected result type: {type(result).__name__}")

    def handle_decrement(self) -> OperationResult:
        result: Result = self.decrement_use_case.execute()

        if isinstance(result, Success):
            success_vm: CounterViewModel = self.presenter.present_counter_response(
                result.success_response
            )
            return OperationSuccess(success_vm)

        if isinstance(result, Error):
            error_vm: ErrorViewModel = self.presenter.present_error_response(
                result.error_response
            )
            return OperationError(error_vm)

        raise TypeError(f"Unexpected result type: {type(result).__name__}")
