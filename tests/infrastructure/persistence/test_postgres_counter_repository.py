from collections.abc import Generator

import pytest
import sqlalchemy
import sqlalchemy as sa
import sqlalchemy.orm
from testcontainers.community.postgres import PostgresContainer

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.persistence.postgres_counter_repository import (
    Base,
    PostgresCounter,
    PostgresCounterRepository,
)

############################################################
# UNIT TESTS
############################################################


def test_PostgresCounterRepository_cannot_init_without_args():
    with pytest.raises(TypeError):
        PostgresCounterRepository()


def test_Base_inherits_from_DeclarativeBase():
    base = Base()
    assert isinstance(base, sa.orm.DeclarativeBase)


def test_PostgresCounter_inherits_from_Base():
    postgres_counter = PostgresCounter()
    assert isinstance(postgres_counter, Base)


def test_PostgresCounter_has_count_arg():
    PostgresCounter(id=1, count=10)


def test_PostgresCounterRepository_returns_correct_repo_info(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        PostgresCounterRepository,
        "_configure_sql_alchemy",
        lambda *args, **kwargs: False,
    )
    counter_repository = PostgresCounterRepository("t:t@localhost:1234/t")
    assert counter_repository.repository_type() == "postgres_local"
    assert counter_repository.repository_location() == "t:t@localhost:1234/t"


############################################################
# INTEGRATION TESTS
############################################################


@pytest.fixture
# @pytest.fixture(scope="session")
def postgres_container() -> Generator[PostgresContainer]:
    with PostgresContainer("postgres:19-alpine", driver="psycopg") as container:
        yield container


@pytest.fixture
def dedicated_postgres_repo(
    postgres_container: PostgresContainer,
) -> Generator[PostgresCounterRepository]:
    # PostgresContainer.get_connection_url() returns e.g. "postgresql+psycopg2://user:pass@localhost:32768/test"
    # Strip the dialect prefix because PostgresCounterRepository prepends "postgresql+psycopg://"
    host = postgres_container.get_container_host_ip()
    port = postgres_container.get_exposed_port(5432)
    user = postgres_container.username
    pw = postgres_container.password
    dbname = postgres_container.dbname

    yield PostgresCounterRepository(f"{user}:{pw}@{host}:{port}/{dbname}")


@pytest.mark.integration
def test_PostgresCounterRepository_creates_session_factory(
    dedicated_postgres_repo,
):
    assert isinstance(dedicated_postgres_repo._session_factory, sa.orm.sessionmaker)


@pytest.mark.integration
def test_PostgresCounterRepository_inherits_from_CounterRepository(
    dedicated_postgres_repo,
):
    repo = dedicated_postgres_repo
    assert isinstance(repo, CounterRepository)


@pytest.mark.integration
@pytest.mark.usefixtures("dedicated_postgres_repo")  # use fixture but not an arg
def test_PostgresCounterRepository_init_ensures_database_has_row_1(
    postgres_container,
):
    engine = sa.create_engine(postgres_container.get_connection_url())
    with sa.orm.Session(engine) as session:
        record = session.get(PostgresCounter, 1)
        assert isinstance(record, PostgresCounter)
        assert record.count == 0


@pytest.mark.integration
def test_PostgresCounterRepository_get_returns_value_of_existing_row(
    postgres_container, dedicated_postgres_repo
):
    # Arrange
    engine = sa.create_engine(postgres_container.get_connection_url())
    Base.metadata.create_all(engine)
    with sa.orm.Session(engine) as session:
        record = session.get(PostgresCounter, 1)
        if record is not None:
            record.count = 42
        else:
            session.add(PostgresCounter(id=1, count=42))
        session.commit()

    # Act
    counter: Counter = dedicated_postgres_repo.get()

    # Assert
    assert counter.count.value == 42
    with sa.orm.Session(engine) as session:
        row_count = session.scalar(
            sa.select(sa.func.count()).select_from(PostgresCounter)
        )
        assert row_count == 1


@pytest.mark.integration
def test_PostgresCounterRepository_save_updates_database_file(
    postgres_container, dedicated_postgres_repo
):
    # Act
    dedicated_postgres_repo.save(Counter(Count(27)))

    # Assert
    engine = sa.create_engine(postgres_container.get_connection_url())
    Base.metadata.create_all(engine)
    with sa.orm.Session(engine) as session:
        record = session.get(PostgresCounter, 1)
        assert isinstance(record, PostgresCounter)
        assert record.count == 27

        row_count = session.scalar(
            sa.select(sa.func.count()).select_from(PostgresCounter)
        )
        assert row_count == 1
