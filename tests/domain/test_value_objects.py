import pytest

from counter_os.domain.value_objects import Count


def test_Count_init_requires_int():
    with pytest.raises(TypeError):
        Count()


def test_Count_is_immutable():
    count: Count = Count(1)
    with pytest.raises(AttributeError):
        count.count = 2
