from dataclasses import dataclass

from counter_os.application.dtos.success_response import SuccessResponse
from counter_os.domain.entities.counter import Counter


@dataclass(frozen=True)
class CounterResponse(SuccessResponse):
    count: int

    @classmethod
    def from_entity(cls, counter: Counter) -> CounterResponse:
        """Create a response from the passed-in Counter entity"""
        return cls(count=counter.count.value)
