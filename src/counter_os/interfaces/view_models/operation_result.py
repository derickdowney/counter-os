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

    @classmethod
    def succeed(cls, value: T):
        return cls(success=value)
