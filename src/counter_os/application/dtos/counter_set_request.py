from dataclasses import dataclass


@dataclass
class CounterSetRequest:
    count: int
