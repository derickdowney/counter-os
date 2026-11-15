from dataclasses import dataclass

from counter_os.application.common.result import Result
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CounterIncrementUseCase:
    counter_repository: CounterRepository

    def execute(self) -> Result:
        counter: Counter = self.counter_repository.get()
        counter.increment()
        self.counter_repository.save(counter)
        return Result.success(counter)
