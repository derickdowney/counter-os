import pytest

from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase


def test_CounterSetUseCase_init_requires_counter_repository():
    with pytest.raises(TypeError):
        CounterSetUseCase()
