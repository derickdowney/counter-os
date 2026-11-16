import pytest

from counter_os.application.dtos.counter_set_request import CounterSetRequest


def test_CounterSetRequest_cannot_init_with_no_args():
    with pytest.raises(TypeError):
        CounterSetRequest()
