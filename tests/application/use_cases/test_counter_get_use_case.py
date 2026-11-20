import pytest

from counter_os.application.use_cases.counter_get_use_case import CounterGetUseCase


def test_CounterGetUseCase_cannot_init_with_no_arguments():
    with pytest.raises(TypeError):
        CounterGetUseCase()


def test_CounterGetUseCase_init_requires_counter_repository(counter_repository):
    CounterGetUseCase(counter_repository)
