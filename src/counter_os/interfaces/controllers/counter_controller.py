from dataclasses import dataclass

from counter_os.application.use_cases.counter_decrement_use_case import (
    CounterDecrementUseCase,
)
from counter_os.application.use_cases.counter_increment_use_case import (
    CounterIncrementUseCase,
)
from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase


@dataclass
class CounterController:
    counter_increment_use_case: CounterIncrementUseCase
    counter_decrement_use_case: CounterDecrementUseCase
    counter_set_use_case: CounterSetUseCase
