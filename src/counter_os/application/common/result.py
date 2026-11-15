from dataclasses import dataclass


@dataclass()
class Result:
    @property
    def is_success(self) -> bool:
        return True
