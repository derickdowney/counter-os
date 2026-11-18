from unittest.mock import Mock

import pytest

from counter_os.application.common.result import ErrorCode, Failure, Result, Success
from counter_os.application.use_cases.counter_decrement_use_case import (
    CounterDecrementUseCase,
)
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


def test_CounterDecrementUseCase_is_immutable(counter_repository):
    use_case: CounterDecrementUseCase = CounterDecrementUseCase(counter_repository)
    with pytest.raises(AttributeError):
        use_case.counter_repository = counter_repository


def test_CounterDecrementUseCase_execute_success():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(1))

    use_case: CounterDecrementUseCase = CounterDecrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert isinstance(result, Success)
    assert result.success == Counter(Count(0))
    counter_repo.save.assert_called_once_with(Counter(Count(0)))


def test_CounterDecrementUseCase_execute_decrement_below_zero():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(0))

    use_case: CounterDecrementUseCase = CounterDecrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert isinstance(result, Failure)
    assert result.error is not None
    assert result.error.code == ErrorCode.COUNT_CANNOT_BE_NEGATIVE
    assert (
        result.error.message == "-1 is a negative value and count cannot be negative."
    )
