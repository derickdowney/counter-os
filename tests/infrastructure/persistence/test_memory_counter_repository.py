from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.persistence.memory_counter_repository import (
    InMemoryCounterRepository,
)


def test_InMemoryCounterRepository_saves_to_and_gets_from_memory():
    counter = Counter(Count(50))
    counter_repository: InMemoryCounterRepository = InMemoryCounterRepository()
    counter_repository.save(counter)
    saved_counter: Counter = counter_repository.get()
    assert saved_counter.count == Count(50)

    # Ensure counter stored as deepcopy, not as reference
    counter.count = Count(100)
    assert saved_counter.count == Count(50)


def test_InMemoryCounterRepository_first_get_returns_counter_at_zero():
    counter_repository = InMemoryCounterRepository()
    assert counter_repository.get() == Counter(Count(0))
