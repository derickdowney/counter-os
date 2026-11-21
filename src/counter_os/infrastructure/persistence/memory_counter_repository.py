import copy
from dataclasses import dataclass

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass
class InMemoryCounterRepository(CounterRepository):
    def save(self, counter: Counter):
        self._counter = copy.deepcopy(counter)

    def get(self) -> Counter:
        return self._counter
