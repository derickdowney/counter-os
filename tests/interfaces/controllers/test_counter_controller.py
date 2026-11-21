import pytest

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.counter_set_request import CounterSetRequest
from counter_os.application.dtos.error_response import ErrorCode, ErrorResponse
from counter_os.application.result import (
    Error,
    Result,
    Success,
)
from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count
from counter_os.interfaces.controllers.counter_controller import CounterController
from counter_os.interfaces.operation_result import (
    OperationError,
    OperationResult,
    OperationSuccess,
)
from counter_os.interfaces.view_models.counter_view_model import CounterViewModel
from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


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

    return MockCounterDecrementUseCase()


@pytest.fixture
def mock_counter_get_use_case():
    class MockCounterGetUseCase:
        def execute(self) -> Result:
            return Success(CounterResponse(10))

    return MockCounterGetUseCase()


@pytest.fixture
def mock_counter_set_use_case():
    class MockCounterSetUseCase:
        def execute(self, request: CounterSetRequest) -> Result:
            if request.count == -1:
                return Error(ErrorResponse.count_cannot_be_negative(-1))
            if request.count == 101:
                return Error(ErrorResponse.count_cannot_be_greater_than_100(101))
            return Success(CounterResponse(request.count))

    return MockCounterSetUseCase()


@pytest.fixture
def mock_counter_presenter():
    class MockCounterPresenter:
        def present_counter_response(self, counter_response: CounterResponse):
            return CounterViewModel(counter_response.current_count)

        def present_error_response(self, error_response: ErrorResponse):
            return ErrorViewModel(error_response.message, error_response.code.name)

    return MockCounterPresenter()


@pytest.fixture
def counter_controller(
    mock_counter_increment_use_case,
    mock_counter_decrement_use_case,
    mock_counter_get_use_case,
    mock_counter_set_use_case,
    mock_counter_presenter,
):
    return CounterController(
        mock_counter_increment_use_case,
        mock_counter_decrement_use_case,
        mock_counter_get_use_case,
        mock_counter_set_use_case,
        mock_counter_presenter,
    )


def test_CounterController_init_requires_counter_use_cases():
    with pytest.raises(TypeError):
        CounterController()


def test_CounterController_handle_increment_success_path(counter_controller):
    op_result: OperationResult = counter_controller.handle_increment()
    assert isinstance(op_result, OperationSuccess)
    assert isinstance(op_result.success_vm, CounterViewModel)
    assert op_result.success_vm.current_count == 1


def test_CounterController_handle_increment_error_greater_than_100_path(
    counter_controller,
    mock_counter_increment_use_case,
):
    # Arrange
    result: Result = Error(ErrorResponse.count_cannot_be_greater_than_100(101))
    mock_counter_increment_use_case.result = result
    counter_controller.increment_use_case = mock_counter_increment_use_case

    # Act
    op_result: OperationResult = counter_controller.handle_increment()

    # Assert
    assert isinstance(op_result, OperationError)
    assert isinstance(op_result.error_vm, ErrorViewModel)
    assert (
        op_result.error_vm.message
        == "101 is greater than 100 and count cannot be greater than 100"
    )
    assert op_result.error_vm.code == "COUNT_CANNOT_BE_GREATER_THAN_100"


def test_CounterController_handle_decrement_success(counter_controller):
    op_result: OperationResult = counter_controller.handle_decrement()
    assert isinstance(op_result, OperationSuccess)
    assert isinstance(op_result.success_vm, CounterViewModel)
    assert op_result.success_vm.current_count == 0


def test_CounterController_handle_decrement_error_negative_value(
    counter_controller, mock_counter_decrement_use_case
):
    # Arrange
    result: Result = Error(ErrorResponse.count_cannot_be_negative(-1))
    mock_counter_decrement_use_case.result = result
    counter_controller.decrement_use_case = mock_counter_decrement_use_case

    # Act
    op_result: OperationResult = counter_controller.handle_decrement()

    # Assert
    assert isinstance(op_result, OperationError)
    assert isinstance(op_result.error_vm, ErrorViewModel)
    assert (
        op_result.error_vm.message
        == "-1 is a negative value and count cannot be negative"
    )
    assert op_result.error_vm.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE.name


def test_CounterController_handle_get_success(counter_controller):
    op_result: OperationResult = counter_controller.handle_get()
    assert isinstance(op_result, OperationSuccess)
    assert isinstance(op_result.success_vm, CounterViewModel)
    assert op_result.success_vm.current_count == 10


def test_CounterController_handle_set_success(counter_controller):
    op_result: OperationResult = counter_controller.handle_set(50)
    assert isinstance(op_result, OperationSuccess)
    assert isinstance(op_result.success_vm, CounterViewModel)
    assert op_result.success_vm.current_count == 50


def test_CounterController_handle_set_error_negative_value(counter_controller):
    op_result: OperationResult = counter_controller.handle_set(-1)
    assert isinstance(op_result, OperationError)
    assert isinstance(op_result.error_vm, ErrorViewModel)
    assert (
        op_result.error_vm.message
        == "-1 is a negative value and count cannot be negative"
    )
    assert op_result.error_vm.code == "COUNT_CANNOT_BE_NEGATIVE"


def test_CounterController_handle_set_error_greater_than_100(counter_controller):
    op_result: OperationResult = counter_controller.handle_set(101)
    assert isinstance(op_result, OperationError)
    assert isinstance(op_result.error_vm, ErrorViewModel)
    assert (
        op_result.error_vm.message
        == "101 is greater than 100 and count cannot be greater than 100"
    )
    assert op_result.error_vm.code == "COUNT_CANNOT_BE_GREATER_THAN_100"


def test_CounterController_handle_set_error_not_an_integer(counter_controller):
    op_result: OperationResult = counter_controller.handle_set("hello")
    assert isinstance(op_result, OperationError)
    assert isinstance(op_result.error_vm, ErrorViewModel)
    assert op_result.error_vm.message == "Count must be an integer"
    assert op_result.error_vm.code == "VALIDATION_ERROR"
