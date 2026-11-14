from abc import ABC, abstractmethod


class CounterRepository(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get(self):
        pass
