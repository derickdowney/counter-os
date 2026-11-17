from dataclasses import dataclass

from counter_os.application.common.result import Result
from counter_os.application.use_cases.counter_decrement_use_case import (
    CounterDecrementUseCase,
)
from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)
from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel
from counter_os.interfaces.view_models.operation_result import OperationResult


@dataclass
class CounterController:
    increment_use_case: CounterIncrementUseCase
    decrement_use_case: CounterDecrementUseCase
    set_use_case: CounterSetUseCase
    presenter: CounterPresenter

    def handle_increment(self) -> OperationResult[CounterViewModel]:
        try:
            result: Result = self.increment_use_case.execute()
            if result.is_success:
                view_model: CounterViewModel = self.presenter.present_counter(
                    result.value
                )
                return OperationResult.succeed(view_model)

            error_vm: ErrorViewModel = self.presenter.present_error(
                result.error.message, str(result.error.code.name)
            )
            return OperationResult.fail(error_vm.message, error_vm.code)

        except ValueError as e:
            error_vm: ErrorViewModel = self.presenter.present_error(
                str(e), "VALIDATION_ERROR"
            )
            return OperationResult.fail(error_vm.message, error_vm.code)
