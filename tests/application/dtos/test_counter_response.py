from dataclasses import FrozenInstanceError

import pytest

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.success_response import SuccessResponse
from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count


def test_CounterResponse_cannot_init_with_no_args():
    with pytest.raises(TypeError):
        CounterResponse()


def test_CounterResponse_is_immutable():
    response = CounterResponse.from_entity(Counter(Count(1)))
    with pytest.raises(FrozenInstanceError):
        response.count = 2


def test_CounterResponse_is_in_class_SuccessResponse():
    response = CounterResponse.from_entity(Counter(Count(1)))
    assert isinstance(response, SuccessResponse)


def test_CounterResponse_from_entity_class_method_captures_count():
    response = CounterResponse.from_entity(Counter(Count(17)))
    assert response.count == 17
