import pytest

from counter_os.domain.entities.counter import Counter
from counter_os.domain.exceptions import CountCannotBeNegative
from counter_os.domain.value_objects.count import Count


def test_Counter_init_requires_Count_value_object():
    with pytest.raises(TypeError):
        Counter()


def test_Counter_is_mutable(counter):
    assert counter.count == Count(0)
    counter.count = Count(12345)
    assert counter.count == Count(12345)


def test_Counter_increment_counts_up_by_one(counter):
    counter.increment()
    assert counter.count == Count(1)


def test_Counter_decrement_counts_down_by_one():
    counter: Counter = Counter(Count(100))
    counter.decrement()
    assert counter.count == Count(99)


def test_Counter_decrement_below_zero_raises_CounterCannotDecrementBelowZero(counter):
    with pytest.raises(CountCannotBeNegative):
        counter.decrement()
