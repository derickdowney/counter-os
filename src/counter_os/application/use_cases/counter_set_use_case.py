from dataclasses import dataclass

from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CounterSetUseCase:
    counter_repository: CounterRepository
