import pytest

from counter_os.application.dtos.counter_response import CounterResponse


def test_CounterResponse_cannot_init_with_no_args():
    with pytest.raises(TypeError):
        CounterResponse()
