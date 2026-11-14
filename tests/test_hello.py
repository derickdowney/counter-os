from counter_os.hello import hello


def test_hello():
    assert hello() == "hello!"
