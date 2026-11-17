from dataclasses import dataclass


@dataclass
class CounterViewModel:
    """View-specific representation of a counter."""

    count: int
