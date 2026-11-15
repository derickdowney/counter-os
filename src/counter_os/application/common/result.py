from dataclasses import dataclass

from counter_os.application.common.error import Error


@dataclass()
class Result:
    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)

    @property
    def is_success(self) -> bool:
        return True
