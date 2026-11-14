import pytest

from counter_os.domain.entities.counter import Counter


def test_Counter_init_requires_Count_value_object():
    with pytest.raises(TypeError):
        Counter()
