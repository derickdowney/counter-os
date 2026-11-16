from dataclasses import FrozenInstanceError
from unittest.mock import Mock

import pytest

from counter_os.application.common.result import Result
from counter_os.application.dtos.counter_response import CounterResponse
from counter_os.application.dtos.counter_set_request import CounterSetRequest
from counter_os.application.use_cases.counter_set_use_case import CounterSetUseCase
from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


def test_CounterSetUseCase_init_requires_counter_repository():
    with pytest.raises(TypeError):
        CounterSetUseCase()


def test_CounterSetUseCase_is_immutable(counter_repository):
    use_case: CounterSetUseCase = CounterSetUseCase(counter_repository)
    with pytest.raises(FrozenInstanceError):
        use_case.counter_repository = counter_repository


def test_CounterSetUseCase_sets_counter_to_requested_value():
    counter_repo: Mock = Mock(spec=CounterRepository)
    counter_repo.get.return_value = Counter(Count(0))

    use_case: CounterSetUseCase = CounterSetUseCase(counter_repo)
    request: CounterSetRequest = CounterSetRequest(50)
    result: Result = use_case.execute(request)
    assert result.is_success
    assert isinstance(result.value, CounterResponse)
    assert result.value.count == 50
