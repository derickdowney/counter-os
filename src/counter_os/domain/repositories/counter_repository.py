from abc import ABC, abstractmethod

from counter_os.domain.entities.counter import Counter


class CounterRepository(ABC):
    @abstractmethod
    def save(self, counter: Counter) -> None:
        pass

    @abstractmethod
    def get(self) -> Counter:
        pass

    @abstractmethod
    def repository_type(self) -> str:
        pass

    @abstractmethod
    def repository_location(self) -> str:
        pass
