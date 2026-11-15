from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.memory_counter_repository import MemoryCounterRepository


def test_MemoryCounterRepository_saves_to_and_gets_from_memory(counter):
    counter.count = Count(123)
    counter_repository: MemoryCounterRepository = MemoryCounterRepository(counter)
    counter_repository.save(counter)
    saved_counter: Counter = counter_repository.get()
    assert saved_counter.count == Count(123)

    # Ensure counter stored as deepcopy, not as reference
    counter.count = Count(456)
    assert saved_counter.count == Count(123)
