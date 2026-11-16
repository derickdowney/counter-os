from dataclasses import dataclass


@dataclass(frozen=True)
class CounterResponse:
    count: int
