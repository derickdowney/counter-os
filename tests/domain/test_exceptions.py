from counter_os.domain.exceptions import (
    CountCannotBeGreaterThan100,
    CountCannotBeNegative,
    DomainError,
)


def test_CountCannotBeNegative_is_DomainError():
    assert isinstance(CountCannotBeNegative(), DomainError)


def test_CountCannotBeNegative_is_ValueError():
    assert isinstance(CountCannotBeNegative(), ValueError)


def test_CountCannotBeGreaterThan100_is_DomainError():
    assert isinstance(CountCannotBeGreaterThan100(), DomainError)


def test_CountCannotBeGreaterThan100_is_ValueError():
    assert isinstance(CountCannotBeGreaterThan100(), ValueError)
