from dataclasses import FrozenInstanceError

import pytest

from counter_os.application.dtos.counter_response import CounterResponse


def test_CounterResponse_cannot_init_with_no_args():
    with pytest.raises(TypeError):
        CounterResponse()


def test_CounterResponse_is_immutable():
    response: CounterResponse = CounterResponse(1)
    with pytest.raises(FrozenInstanceError):
        response.count = 2
