import pytest

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.result import Result, Success
from counter_os.application.use_cases.counter_get_use_case import CounterGetUseCase


def test_CounterGetUseCase_cannot_init_with_no_arguments():
    with pytest.raises(TypeError):
        CounterGetUseCase()


def test_CounterGetUseCase_init_requires_counter_repository(counter_repository):
    CounterGetUseCase(counter_repository)


def test_CounterGetUseCase_execute_returns_CounterResponse_with_current_count(
    counter_repository,
):
    use_case = CounterGetUseCase(counter_repository)
    result: Result = use_case.execute()
    assert isinstance(result, Success)
    assert isinstance(result.success_response, CounterResponse)
    assert isinstance(result.success_response.current_count, int)
    assert result.success_response.current_count == 0
