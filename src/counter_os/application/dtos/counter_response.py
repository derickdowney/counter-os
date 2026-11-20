from dataclasses import dataclass

from counter_os.application.dtos.success_response import SuccessResponse
from counter_os.domain.entities.counter import Counter


@dataclass(frozen=True)
class CounterResponse(SuccessResponse):
    _current_count: int

    def __post_init__(self):
        if type(self._current_count) != int:
            raise TypeError("count must be an integer")

    @classmethod
    def from_entity(cls, counter: Counter) -> CounterResponse:
        """Create a response from the passed-in Counter entity"""
        return cls(_current_count=counter.count.value)

    @property
    def current_count(self):
        return self._current_count
