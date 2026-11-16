from dataclasses import FrozenInstanceError

import pytest

from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.domain.entities.counter import Counter
from counter_os.domain.value_objects.count import Count


def test_CounterResponse_cannot_init_with_no_args():
    with pytest.raises(TypeError):
        CounterResponse()


def test_CounterResponse_is_immutable():
    response: CounterResponse = CounterResponse(1)
    with pytest.raises(FrozenInstanceError):
        response.count = 2


def test_CounterResponse_from_entity_class_method_captures_count():
    counter: Counter = Counter(Count(17))
    response: CounterResponse = CounterResponse.from_entity(counter)
    assert response.count == 17
