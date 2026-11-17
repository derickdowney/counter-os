from abc import ABC, abstractmethod

from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count


class CounterHistoryPort(ABC):
    """Port for keeping track of counter history"""

    @abstractmethod
    def append_count_to_history(self, count: Count) -> None:
        pass

    @abstractmethod
    def get_count_history(self) -> list[Count]:
        pass

    @abstractmethod
    def reset_count_history(self):
        pass
