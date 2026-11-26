import pytest
import sqlalchemy as sa
import sqlalchemy.orm

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.persistence.sqlite_counter_repository import (
    Base,
    SqliteCounter,
    SqliteCounterRepository,
)


@pytest.fixture
def sqlite_counter_repo(tmp_path, monkeypatch) -> SqliteCounterRepository:
    monkeypatch.chdir(tmp_path)
    return SqliteCounterRepository("test.db3")


def test_SqliteCounterRepository_cannot_init_without_args():
    with pytest.raises(TypeError):
        SqliteCounterRepository()


def test_SqliteCounterRepository_init_requires_relative_file_path(sqlite_counter_repo):
    repo = sqlite_counter_repo
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


def test_SqliteCounterRepository_relative_file_path_must_end_with_db3_or_db(
    tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)
    SqliteCounterRepository("test.db")
    SqliteCounterRepository("test.db3")
    with pytest.raises(ValueError):
        SqliteCounterRepository("test")
    with pytest.raises(ValueError):
        SqliteCounterRepository("test.d")


def test_SqliteCounterRepository_creates_session_factory(sqlite_counter_repo):
    repo = sqlite_counter_repo
    assert isinstance(repo._session_factory, sa.orm.sessionmaker)


def test_Base_inherits_from_DeclarativeBase():
    base = Base()
    assert isinstance(base, sa.orm.DeclarativeBase)


def test_SqliteCounter_inherits_from_Base():
    sqlite_counter = SqliteCounter()
    assert isinstance(sqlite_counter, Base)


def test_SqliteCounter_has_count_arg():
    SqliteCounter(id=1, count=10)


def test_SqliteCounterRepository_inherits_from_CounterRepository(
    sqlite_counter_repo,
):
    repo = sqlite_counter_repo
    assert isinstance(repo, CounterRepository)


def test_SqliteCounterRepository_creates_database_file(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.chdir(tmp_path)
    expected_db_file = tmp_path / "test.db3"
    assert not expected_db_file.is_file()

    # Act
    SqliteCounterRepository("test.db3")

    # Assert
    assert expected_db_file.is_file()


def test_SqliteCounterRepository_init_ensures_database_file_has_row_(
    tmp_path, monkeypatch
):
    # Arrange
    monkeypatch.chdir(tmp_path)

    # Act
    SqliteCounterRepository("test.db3")

    # Assert
    engine = sa.create_engine("sqlite+pysqlite:///test.db3")
    with sa.orm.Session(engine) as session:
        record = session.get(SqliteCounter, 1)
        assert isinstance(record, SqliteCounter)
        assert record.count == 0


def test_SqliteCounterRepository_get_returns_value_of_existing_row(
    tmp_path, monkeypatch
):
    # Arrange
    monkeypatch.chdir(tmp_path)
    engine = sa.create_engine("sqlite+pysqlite:///test.db3")
    Base.metadata.create_all(engine)
    with sa.orm.Session(engine) as session:
        session.add(SqliteCounter(id=1, count=42))
        session.commit()
    sqlite_counter_repo = SqliteCounterRepository("test.db3")

    # Act
    counter: Counter = sqlite_counter_repo.get()

    # Assert
    assert counter.count.value == 42
    with sa.orm.Session(engine) as session:
        row_count = session.scalar(
            sa.select(sa.func.count()).select_from(SqliteCounter)
        )
        assert row_count == 1


def test_SqliteCounterRepository_save_updates_database_file(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.chdir(tmp_path)
    sqlite_counter_repo = SqliteCounterRepository("test.db3")

    # Act
    sqlite_counter_repo.save(Counter(Count(27)))

    # Assert
    engine = sa.create_engine("sqlite+pysqlite:///test.db3")
    Base.metadata.create_all(engine)
    with sa.orm.Session(engine) as session:
        record = session.get(SqliteCounter, 1)
        assert isinstance(record, SqliteCounter)
        assert record.count == 27

        row_count = session.scalar(
            sa.select(sa.func.count()).select_from(SqliteCounter)
        )
        assert row_count == 1


def test_SqliteCounterRepository_returns_correct_repo_info(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    counter_repository = SqliteCounterRepository("some_location.db3")
    assert counter_repository.repository_type() == "sqlite_local"
    assert counter_repository.repository_location() == "some_location.db3"
