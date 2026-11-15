from counter_os.domain.exceptions import CountCannotBeNegative, DomainException


def test_CountCannotBeNegative_is_DomainException():
    assert isinstance(CountCannotBeNegative(), DomainException)


def test_CountCannotBeNegative_is_ValueError():
    assert isinstance(CountCannotBeNegative(), ValueError)
