from dataclasses import FrozenInstanceError
from typing import Any

import pytest

from counter_os.application.dtos.counter_set_request import CounterSetRequest
from counter_os.domain.exceptions import (
    CountCannotBeGreaterThan100,
    CountCannotBeNegative,
)


def test_CounterSetRequest_cannot_init_with_no_args():
    with pytest.raises(TypeError):
        CounterSetRequest()


def test_CounterSetRequest_is_immutable():
    request: CounterSetRequest = CounterSetRequest(1)
    with pytest.raises(FrozenInstanceError):
        request.count = 2


def test_CounterSetRequest_raises_ValueError_if_init_with_non_int():
    with pytest.raises(ValueError):
        CounterSetRequest("hello")


def test_CounterSetRequest_raises_when_count_is_negative():
    request: CounterSetRequest = CounterSetRequest(-1)
    with pytest.raises(CountCannotBeNegative):
        request.to_execution_params()


def test_CounterSetRequest_raises_when_count_is_greater_than_100():
    request: CounterSetRequest = CounterSetRequest(101)
    with pytest.raises(CountCannotBeGreaterThan100):
        request.to_execution_params()
