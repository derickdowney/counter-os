from unittest.mock import Mock

import pytest

from counter_os.application.result import ErrorCode, Failure, Result, Success
from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


def test_CounterIncrementUseCase_is_immutable(counter_repository):
    use_case: CounterIncrementUseCase = CounterIncrementUseCase(counter_repository)
    with pytest.raises(AttributeError):
        use_case.counter_repository = counter_repository


def test_CounterIncrementUseCase_execute_success():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(0))

    use_case: CounterIncrementUseCase = CounterIncrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert isinstance(result, Success)
    assert result.success == Counter(Count(1))
    counter_repo.save.assert_called_once_with(Counter(Count(1)))


def test_CounterIncrementUseCase_increment_above_100():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(100))

    use_case: CounterIncrementUseCase = CounterIncrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert isinstance(result, Failure)
    assert result.error.code == ErrorCode.COUNT_CANNOT_BE_GREATER_THAN_100
    assert (
        result.error.message
        == "101 is greater than 100 and count cannot be greater than 100."
    )
