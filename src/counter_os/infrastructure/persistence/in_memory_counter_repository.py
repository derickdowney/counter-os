import copy
from dataclasses import dataclass

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.persistence.repository_type import RepositoryType


@dataclass
class InMemoryCounterRepository(CounterRepository):
    def __post_init__(self):
        self._counter = Counter(Count(0))

    def save(self, counter: Counter):
        self._counter = copy.deepcopy(counter)

    def get(self) -> Counter:
        return self._counter

    def repository_type(self) -> str:
        return RepositoryType.MEMORY

    def repository_location(self) -> str:
        return "RAM"
