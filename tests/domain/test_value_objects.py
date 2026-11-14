import pytest

from counter_os.domain.value_objects import Count


def test_Count_init_requires_int():
    with pytest.raises(TypeError):
        Count()
