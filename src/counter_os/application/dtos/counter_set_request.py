from dataclasses import dataclass


@dataclass(frozen=True)
class CounterSetRequest:
    count: int
