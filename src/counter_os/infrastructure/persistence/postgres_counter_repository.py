import sqlalchemy as sa
import sqlalchemy.orm

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count
from counter_os.infrastructure.persistence.repository_type import RepositoryType


class PostgresCounterRepository(CounterRepository):
    _session_factory: sa.orm.sessionmaker
    _repository_location: str

    def __init__(self, location: str):
        self._repository_location = location
        self._configure_sql_alchemy(location)

    def _configure_sql_alchemy(self, location: str):
        sa_engine_config_url = "postgresql+psycopg://" + location
        engine = sa.create_engine(sa_engine_config_url)
        Base.metadata.create_all(engine)
        self._session_factory = sa.orm.sessionmaker(bind=engine)
        with self._session_factory() as session:
            record = session.get(PostgresCounter, 1)
            if record is None:
                session.add(PostgresCounter(id=1, count=0))
                session.commit()

    def save(self, counter: Counter) -> None:
        with self._session_factory() as session:
            record = session.get(PostgresCounter, 1)
            if record is not None:
                record.count = counter.count.value
            else:
                session.add(PostgresCounter(id=1, count=counter.count.value))
            session.commit()

    def get(self) -> Counter:
        with self._session_factory() as session:
            record = session.get(PostgresCounter, 1)
            if record is not None:
                return Counter(Count(record.count))

            new_record = PostgresCounter(id=1, count=0)
            session.add(new_record)
            session.commit()
            return Counter(Count(new_record.count))

    def repository_type(self) -> str:
        return RepositoryType.POSTGRES_LOCAL

    def repository_location(self) -> str:
        return self._repository_location


class Base(sa.orm.DeclarativeBase):
    pass


class PostgresCounter(Base):
    """SQL Alchemy ORM class for "counters" table"""

    __tablename__ = "counters"

    id: sa.orm.Mapped[int] = sa.orm.mapped_column(primary_key=True)
    count: sa.orm.Mapped[int]
