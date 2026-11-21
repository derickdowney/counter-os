import pytest

from counter_os.infrastructure.click_cli.click_cli_app import ClickCliApp


def test_ClickCliApp_init_requires_ApplicationContainer():
    with pytest.raises(TypeError):
        ClickCliApp()
