import pytest

from counter_os.interfaces.view_models.error_view_model import ErrorViewModel


def test_ErrorViewModel_init_requires_message():
    with pytest.raises(TypeError):
        ErrorViewModel()
