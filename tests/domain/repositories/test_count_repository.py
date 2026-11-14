import pytest

from counter_os.domain.repositories.counter_repository import CounterRepository


def test_CounterRepository_is_abstract():
    with pytest.raises(TypeError):
        CounterRepository()
