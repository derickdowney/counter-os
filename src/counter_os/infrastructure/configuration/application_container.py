from dataclasses import dataclass

from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.interfaces.presenters.counter_presenter import CounterPresenter


@dataclass
class ApplicationContainer:
    """Application container which wires together all components"""

    counter_repository: CounterRepository
    counter_presenter: CounterPresenter
