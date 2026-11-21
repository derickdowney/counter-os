import pytest

from counter_os.infrastructure.click_cli.click_cli_app import ClickCli


def test_ClickCli_init_requires_ApplicationContainer():
    with pytest.raises(TypeError):
        ClickCli()
