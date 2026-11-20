from dataclasses import dataclass

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.result import Result, Success
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass
class CounterGetUseCase:
    counter_repository: CounterRepository

    def execute(self) -> Result:
        return Success(CounterResponse.from_entity(self.counter_repository.get()))
