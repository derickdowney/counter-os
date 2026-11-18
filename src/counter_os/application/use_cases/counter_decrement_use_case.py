from dataclasses import dataclass

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.error_response import ErrorResponse
from counter_os.application.result import Error, Result, Success
from counter_os.domain.entities.counter import Counter
from counter_os.domain.exceptions import CountCannotBeNegative
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CounterDecrementUseCase:
    counter_repository: CounterRepository

    def execute(self) -> Result:
        counter: Counter = self.counter_repository.get()
        try:
            counter.decrement()
            self.counter_repository.save(counter)
            return Success(CounterResponse.from_entity(counter))
        except CountCannotBeNegative:
            attempted_count: int = counter.count.value - 1
            return Error(ErrorResponse.count_cannot_be_negative(attempted_count))
