from dataclasses import dataclass

from counter_os.domain.value_objects.count import Count


@dataclass()
class Counter:
    count: Count

    def increment(self):
        current_count: int = self.count.value
        new_count: int = current_count + 1
        self.count = Count(new_count)
