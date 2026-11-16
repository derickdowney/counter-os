from dataclasses import dataclass
from typing import Any

from counter_os.domain.value_objects.count import Count


@dataclass(frozen=True)
class CounterSetRequest:
    count: int

    def __post_init__(self) -> None:
        """Validate request data"""
        if type(self.count) != int:
            raise ValueError("Count must be an integer")

    def to_execution_params(self) -> dict[str, Any]:
        """Convert validated request data to use_case parameters"""
        return {"count": Count(self.count)}
