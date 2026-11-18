from dataclasses import dataclass

from counter_os.interfaces.view_models.success_view_model import SuccessViewModel


@dataclass(frozen=True)
class CounterViewModel(SuccessViewModel):
    """View-specific representation of a counter."""

    count: int
