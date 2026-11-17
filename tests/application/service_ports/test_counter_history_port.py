import pytest

from counter_os.application.service_ports.counter_history_port import CounterHistoryPort


def test_CounterHistoryPort_is_abstract():
    with pytest.raises(TypeError):
        CounterHistoryPort()
