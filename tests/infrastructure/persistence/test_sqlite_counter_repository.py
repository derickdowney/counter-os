import pytest
import sqlalchemy as sa
import sqlalchemy.orm

from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.infrastructure.persistence.sqlite_counter_repository import (
    Base,
    SqliteCounter,
    SqliteCounterRepository,
)


def test_SqliteCounterRepository_cannot_init_without_args():
    with pytest.raises(TypeError):
        SqliteCounterRepository()


def test_SqliteCounterRepository_init_requires_relative_file_path():
    repo = SqliteCounterRepository("test.db3")
    assert isinstance(repo, SqliteCounterRepository)


def test_SqliteCounterRepository_cannot_init_with_non_string():
    with pytest.raises(TypeError):
        SqliteCounterRepository(1234)


def test_SqliteCounterRepository_relative_file_path_cannot_be_empty():
    with pytest.raises(ValueError):
        SqliteCounterRepository("")


@pytest.mark.parametrize(
    "invalid_char",
    ["\\", ":", "*", "?", '"', "<", ">", "|"],
)
def test_SqliteCounterRepository_relative_file_path_cannot_contain_invalid_chars(
    invalid_char,
):
    invalid_path: str = "test" + invalid_char + "file.db3"
    with pytest.raises(ValueError):
        SqliteCounterRepository(invalid_path)


def test_SqliteCounterRepository_relative_file_path_cannot_start_with_forward_slash():
    with pytest.raises(ValueError):
        SqliteCounterRepository("/test.db3")


def test_SqliteCounterRepository_relative_file_path_cannot_contain_spaces():
    with pytest.raises(ValueError):
        SqliteCounterRepository("test file.db3")


def test_SqliteCounterRepository_relative_file_path_must_end_with_db3_or_db():
    SqliteCounterRepository("test.db")
    SqliteCounterRepository("test.db3")
    with pytest.raises(ValueError):
        SqliteCounterRepository("test")
    with pytest.raises(ValueError):
        SqliteCounterRepository("test.d")


def test_SqliteCounterRepository_creates_session_factory():
    repo = SqliteCounterRepository("test.db3")
    assert isinstance(repo._session_factory, sa.orm.sessionmaker)


def test_Base_inherits_from_DeclarativeBase():
    base = Base()
    assert isinstance(base, sa.orm.DeclarativeBase)


def test_SqliteCounter_inherits_from_Base():
    sqlite_counter = SqliteCounter()
    assert isinstance(sqlite_counter, Base)


def test_SqliteCounter_has_count_arg():
    SqliteCounter(id=1, count=10)


def test_SqliteCounterRepository_inherits_from_CounterRepository():
    repo = SqliteCounterRepository("test.db3")
    assert isinstance(repo, CounterRepository)
