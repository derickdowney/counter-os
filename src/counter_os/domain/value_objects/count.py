from dataclasses import dataclass


@dataclass(frozen=True)
class Count:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Count cannot be less than 0")
