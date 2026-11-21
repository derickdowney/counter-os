import copy
from dataclasses import dataclass

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


@dataclass
class InMemoryCounterRepository(CounterRepository):
    def __post_init__(self):
        self._counter = Counter(Count(0))

    def save(self, counter: Counter):
        self._counter = copy.deepcopy(counter)

    def get(self) -> Counter:
        return self._counter
