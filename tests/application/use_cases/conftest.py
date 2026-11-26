import copy
from dataclasses import dataclass

import pytest

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository


@pytest.fixture
def counter_repository(counter):
    @dataclass
    class TestCounterRepository(CounterRepository):
        _counter: Counter

        def save(self, counter: Counter):
            self._counter = copy.deepcopy(counter)

        def get(self) -> Counter:
            return self._counter

        def repository_type(self):
            pass

        def repository_location(self):
            pass

    return TestCounterRepository(counter)
