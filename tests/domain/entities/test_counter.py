import pytest

from counter_os.domain.entities.counter import Counter


def test_Counter_init_requires_current_count():
    with pytest.raises(TypeError):
        Counter()
