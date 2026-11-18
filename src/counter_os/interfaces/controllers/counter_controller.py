from dataclasses import dataclass

from counter_os.application.common.result import Result, Success
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
            if isinstance(result, Success):
                success_vm: CounterViewModel = self.presenter.present_counter(
                    result.success
                )
                return OperationResult.succeed(success_vm)

            error_vm: ErrorViewModel = self.presenter.present_error(
                result.error.message, str(result.error.code.name)
            )
            return OperationResult.fail(error_vm.message, error_vm.code)

        # I think the only way this can get triggered is if we try to call
        # result.sucess or result.error on OperationResult and there is no
        # success or error. All other domain errors will be captured in the
        # error_vm above!
        except ValueError as e:
            error_vm: ErrorViewModel = self.presenter.present_error(
                str(e), "VALIDATION_ERROR"
            )
            return OperationResult.fail(error_vm.message, error_vm.code)
