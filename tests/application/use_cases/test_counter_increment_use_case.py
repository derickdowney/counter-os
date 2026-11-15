from unittest.mock import Mock

import pytest

from counter_os.application.common.result import Result
from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


def test_CounterIncrementUseCase_is_immutable(counter_repository):
    count_up_use_case: CounterIncrementUseCase = CounterIncrementUseCase(
        counter_repository
    )
    with pytest.raises(AttributeError):
        count_up_use_case.counter_repository = counter_repository


def test_CounterIncrementUseCase_execute_success():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(0))

    use_case: CounterIncrementUseCase = CounterIncrementUseCase(counter_repo)
    result: Result = use_case.execute()

    assert result.is_success
    assert result.value == Counter(Count(1))
    counter_repo.save.assert_called_once_with(Counter(Count(1)))
