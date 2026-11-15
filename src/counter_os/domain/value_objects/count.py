from dataclasses import dataclass

from counter_os.domain.exceptions import CountCannotBeNegative


@dataclass(frozen=True)
class Count:
    value: int

    def __post_init__(self) -> None:
        if type(self.value) != int:
            raise TypeError("Count must be an integer")
        if self.value < 0:
            raise CountCannotBeNegative("Count cannot be less than 0")
