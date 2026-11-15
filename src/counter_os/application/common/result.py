from dataclasses import dataclass

from counter_os.application.common.error import Error


@dataclass(frozen=True)
class Result:
    """Represents success or failure of a use case execution"""

    error: Error | None = None

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)

    @property
    def is_success(self) -> bool:
        return True
