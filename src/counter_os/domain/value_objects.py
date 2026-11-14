from dataclasses import dataclass


@dataclass(frozen=True)
class Count:
    count: int

    def __post_init__(self):
        if self.count < 0:
            raise ValueError("Count cannot be less than 0")
