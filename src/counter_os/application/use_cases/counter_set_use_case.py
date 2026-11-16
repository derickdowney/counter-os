from dataclasses import dataclass
from typing import Any

from counter_os.application.common.error import Error
from counter_os.application.common.result import Result
from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.counter_set_request import CounterSetRequest
from counter_os.domain.entities.counter import Counter
from counter_os.domain.exceptions import (
    CountCannotBeGreaterThan100,
    CountCannotBeNegative,
)
from counter_os.domain.repositories.counter_repository import CounterRepository


@dataclass(frozen=True)
class CounterSetUseCase:
    counter_repository: CounterRepository

    def execute(self, request: CounterSetRequest) -> Result:
        counter: Counter = self.counter_repository.get()

        try:
            params: dict[str, Any] = request.to_execution_params()
            counter.count = params["count"]
            return Result.success(CounterResponse.from_entity(counter))
        except CountCannotBeNegative:
            return Result.failure(Error.count_cannot_be_negative(request.count))
