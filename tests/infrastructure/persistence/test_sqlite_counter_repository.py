import pytest

from counter_os.infrastructure.persistence.sqlite_counter_repository import (
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
