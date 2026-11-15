import pytest

from counter_os.application.use_cases.count_up_use_case import CountUpUseCase
from counter_os.infrastructure.memory_counter_repository import MemoryCounterRepository


def test_CountUpUseCase_is_immutable(counter_repository):
    count_up_use_case: CountUpUseCase = CountUpUseCase(counter_repository)
    with pytest.raises(AttributeError):
        count_up_use_case.counter_repository = counter_repository
