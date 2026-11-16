from dataclasses import dataclass
from typing import Any

from counter_os.application.common.error import Error


@dataclass(frozen=True)
class Result:
    """Represents success or failure of a use case execution"""

    value: Any = None
    error: Error | None = None

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)

    @classmethod
    def success(cls, value: Any) -> Self:
        return cls(value=value)

    @property
    def is_success(self) -> bool:
        return self.error is None

    @property
    def is_failure(self) -> bool:
        return not self.is_success
