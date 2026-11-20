from dataclasses import dataclass

from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass
class ApplicationContainer:
    """Application container which wires together all components"""

    counter_repository: CounterRepository
