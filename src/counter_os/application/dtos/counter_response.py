from dataclasses import dataclass


@dataclass(frozen=True)
class CounterResponse:
    count: int

    @classmethod
    def from_entity(cls, counter: Counter) -> Self:
        """Create a response from the passed-in Counter entity"""
        return cls(count=counter.count.value)
