import copy
from dataclasses import dataclass

import pytest

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


@pytest.fixture
def counter():
    return Counter(Count(0))
