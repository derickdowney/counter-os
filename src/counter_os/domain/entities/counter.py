from dataclasses import dataclass

from counter_os.domain.value_objects.count import Count


@dataclass()
class Counter:
    count: Count

    def increment(self):
        self.count = Count(self.count.value + 1)

    def decrement(self):
        self.count = Count(self.count.value - 1)
