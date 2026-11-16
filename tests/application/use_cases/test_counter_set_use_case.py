from dataclasses import FrozenInstanceError

import pytest

from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase


def test_CounterSetUseCase_init_requires_counter_repository():
    with pytest.raises(TypeError):
        CounterSetUseCase()


def test_CounterSetUseCase_is_immutable(counter_repository):
    use_case: CounterSetUseCase = CounterSetUseCase(counter_repository)
    with pytest.raises(FrozenInstanceError):
        use_case.counter_repository = counter_repository


#
