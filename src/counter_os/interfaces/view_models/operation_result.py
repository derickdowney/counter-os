from dataclasses import dataclass

from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


@dataclass
class OperationResult[T]:
    _success: T | None = None
    _error: ErrorViewModel | None = None

    def __init__(self, success: T | None = None, error: ErrorViewModel | None = None):
        if (success is None and error is None) or (
            success is not None and error is not None
        ):
            raise ValueError("Either success or error must be provided, but not both")
        self._success = success
        self._error = error

    @classmethod
    def succeed(cls, value: T) -> OperationResult:
        return cls(success=value)

    @classmethod
    def fail(cls, message: str, code: str | None = None) -> OperationResult:
        return cls(error=ErrorViewModel(message, code))

    @property
    def is_success(self) -> bool:
        return self._success is not None and self._error is None

    @property
    def is_failure(self) -> bool:
        return self._error is not None and self._success is None
