import pytest

from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.memory_counter_repository import MemoryCounterRepository


@pytest.fixture
def counter():
    return Counter(Count(0))


@pytest.fixture
def counter_repository(counter):
    return MemoryCounterRepository(counter)
