import pytest

from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects import Count


def test_Counter_init_requires_Count_value_object():
    with pytest.raises(TypeError):
        Counter()


def test_Counter_is_mutable(counter):
    assert counter.count == Count(0)
    counter.count = Count(12345)
    assert counter.count == Count(12345)
