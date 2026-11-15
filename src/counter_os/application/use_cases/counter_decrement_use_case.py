from dataclasses import dataclass

from counter_os.application.common.error import Error
from counter_os.application.common.result import Result
from counter_os.domain.entities.counter import Counter
from counter_os.domain.exceptions import (
    CounterCannotDecrementBelowZero,
)
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CounterDecrementUseCase:
    counter_repository: CounterRepository

    def execute(self) -> Result:
        counter: Counter = self.counter_repository.get()
        try:
            counter.decrement()
            self.counter_repository.save(counter)
            return Result.success(counter)
        except CounterCannotDecrementBelowZero:
            return Result.failure(Error.counter_cannot_decrement_below_zero(counter))
