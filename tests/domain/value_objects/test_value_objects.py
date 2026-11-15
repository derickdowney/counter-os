from dataclasses import FrozenInstanceError

import pytest

from counter_os.domain.value_objects.count import Count


def test_Count_init_requires_int():
    with pytest.raises(TypeError):
        Count()


def test_Count_is_immutable():
    count: Count = Count(1)
    with pytest.raises(FrozenInstanceError):
        count.value = 2


def test_Count_raises_ValueError_when_less_than_zero():
    with pytest.raises(ValueError):
        Count(-1)
