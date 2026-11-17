from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorViewModel:
    """Represents an error with an optional error code."""

    message: str
    code: str | None = None
