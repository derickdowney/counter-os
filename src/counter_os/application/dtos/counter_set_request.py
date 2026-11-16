from dataclasses import dataclass


@dataclass(frozen=True)
class CounterSetRequest:
    count: int

    def __post_init__(self) -> None:
        """Validate request data"""
        if type(self.count) != int:
            raise ValueError("Count must be an integer")
