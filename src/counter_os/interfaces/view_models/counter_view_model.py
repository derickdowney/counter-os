from dataclasses import dataclass


@dataclass(frozen=True)
class CounterViewModel:
    """View-specific representation of a counter."""

    count: int
