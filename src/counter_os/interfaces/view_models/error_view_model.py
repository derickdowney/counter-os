from dataclasses import dataclass


@dataclass
class ErrorViewModel:
    """Represents an error with an optional error code."""

    message: str
    code: str | None = None
