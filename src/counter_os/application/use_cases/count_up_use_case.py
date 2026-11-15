from dataclasses import dataclass

from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CountUpUseCase:
    counter_repository: CounterRepository
