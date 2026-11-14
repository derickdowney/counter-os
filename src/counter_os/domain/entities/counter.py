from dataclasses import dataclass

from counter_os.domain.value_objects import Count


@dataclass()
class Counter:
    count: Count
