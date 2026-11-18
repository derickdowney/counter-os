from unittest.mock import Mock

import pytest

from counter_os.application.common.result import (
    Error,
    ErrorCode,
    Failure,
    Result,
    Success,
)
from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.counter_set_request import CounterSetRequest
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count
from counter_os.interfaces.controllers.counter_controller import CounterController
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel
from counter_os.interfaces.view_models.operation_result import OperationResult


@pytest.fixture
def mock_counter_increment_use_case():
    class MockCounterIncrementUseCase:
        def __init__(self):
            self.result = Success(CounterResponse.from_entity(Counter(Count(1))))

        def execute(self) -> Result:
            return self.result

    return MockCounterIncrementUseCase()


@pytest.fixture
def mock_counter_decrement_use_case():
    class MockCounterDecrementUseCase:
        def __init__(self):
            self.result = Success(CounterResponse.from_entity(Counter(Count(0))))

        def execute(self) -> Result:
            return self.result


@pytest.fixture
def mock_counter_set_use_case():
    class MockCounterSetUseCase:
        def execute(self, request: CounterSetRequest) -> Result:
            if request.count == -1:
                return Failure(Error.count_cannot_be_negative(-1))
            if request.count == 101:
                return Failure(Error.count_cannot_be_greater_than_100(101))
            return Success(request.count)


@pytest.fixture
def mock_counter_presenter():
    class MockCounterPresenter:
        def present_counter(self, counter_response: CounterResponse):
            return CounterViewModel(counter_response.count)

        def present_error(self, error_msg: str, code: str | None = None):
            return ErrorViewModel(error_msg, code)

    return MockCounterPresenter()


@pytest.fixture
def mock_counter_controller(
    mock_counter_increment_use_case,
    mock_counter_decrement_use_case,
    mock_counter_set_use_case,
    mock_counter_presenter,
):
    return CounterController(
        mock_counter_increment_use_case,
        mock_counter_decrement_use_case,
        mock_counter_set_use_case,
        mock_counter_presenter,
    )


def test_CounterController_init_requires_counter_use_cases():
    with pytest.raises(TypeError):
        CounterController()


def test_CounterController_handle_increment_success_path(mock_counter_controller):
    op_result: OperationResult[CounterViewModel] = (
        mock_counter_controller.handle_increment()
    )
    assert op_result.is_success
    assert isinstance(op_result.success, CounterViewModel)
    assert op_result.success.count == 1


def test_CounterController_handle_increment_error_greater_than_100_path(
    mock_counter_increment_use_case,
    mock_counter_decrement_use_case,
    mock_counter_set_use_case,
    mock_counter_presenter,
):
    # Arrange
    increment_error: Error = Error.count_cannot_be_greater_than_100(101)
    increment_fail_result: Result = Failure(increment_error)
    mock_counter_increment_use_case.result = increment_fail_result

    counter_controller: CounterController = CounterController(
        mock_counter_increment_use_case,
        mock_counter_decrement_use_case,
        mock_counter_set_use_case,
        mock_counter_presenter,
    )

    # Act
    op_result: OperationResult[CounterViewModel] = counter_controller.handle_increment()

    # Assert
    assert op_result.is_failure
    assert isinstance(op_result.error, ErrorViewModel)
    assert (
        op_result.error.message
        == "101 is greater than 100 and count cannot be greater than 100."
    )
    assert op_result.error.code == "COUNT_CANNOT_BE_GREATER_THAN_100"
