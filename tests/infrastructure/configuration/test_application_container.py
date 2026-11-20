import pytest

from counter_os.infrastructure.configuration.application_container import (
    ApplicationContainer,
)


def test_ApplicationContainer_init_requires_args():
    with pytest.raises(TypeError):
        ApplicationContainer()
