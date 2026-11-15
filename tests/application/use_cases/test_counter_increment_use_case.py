import pytest

from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)


def test_CounterIncrementUseCase_is_immutable(counter_repository):
    count_up_use_case: CounterIncrementUseCase = CounterIncrementUseCase(
        counter_repository
    )
    with pytest.raises(AttributeError):
        count_up_use_case.counter_repository = counter_repository
