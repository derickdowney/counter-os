from dataclasses import dataclass

from counter_os.application.common.error import Error
from counter_os.application.common.result import Result
from counter_os.domain.entities.counter import Counter
from counter_os.domain.exceptions import CountCannotBeGreaterThan100
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CounterIncrementUseCase:
    counter_repository: CounterRepository

    def execute(self) -> Result:
        counter: Counter = self.counter_repository.get()
        try:
            counter.increment()
            self.counter_repository.save(counter)
            return Result.success(counter)
        except CountCannotBeGreaterThan100:
            attempted_count: int = counter.count.value + 1
            return Result.failure(
                Error.count_cannot_be_greater_than_100(attempted_count)
            )
