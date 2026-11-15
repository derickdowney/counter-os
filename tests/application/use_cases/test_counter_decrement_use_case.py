from unittest.mock import Mock

from counter_os.application.common.error_codes import ErrorCode
from counter_os.application.common.result import Result
from counter_os.application.use_cases.counter_decrement_use_case import (
    CounterDecrementUseCase,
)
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


def test_CounterDecrementUseCase_execute_success():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(1))

    use_case: CounterDecrementUseCase = CounterDecrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert result.is_success
    assert result.value == Counter(Count(0))
    counter_repo.save.assert_called_once_with(Counter(Count(0)))


def test_CounterDecrementUseCase_execute_decrement_below_zero():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(0))

    use_case: CounterDecrementUseCase = CounterDecrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert not result.is_success
    assert result.error is not None
    assert result.error.code == ErrorCode.COUNTER_CANNOT_DECREMENT_BELOW_ZERO
    assert (
        result.error.message
        == "Counter has a count value of 0 and cannot be decremented below zero."
    )
