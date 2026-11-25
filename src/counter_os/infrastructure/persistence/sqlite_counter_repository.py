import sqlalchemy as sa
import sqlalchemy.orm

from counter_os.domain.entities.counter import Counter
from counter_os.domain.repositories.counter_repository import CounterRepository
from counter_os.domain.value_objects.count import Count


class SqliteCounterRepository(CounterRepository):
    _session_factory: sa.orm.sessionmaker

    def __init__(self, relative_file_path: str):
        validate_relative_file_path_arg(relative_file_path)
        sa_engine_config_url = "sqlite+pysqlite:///" + relative_file_path
        engine = sa.create_engine(sa_engine_config_url)
        Base.metadata.create_all(engine)
        self._session_factory = sa.orm.sessionmaker(bind=engine)

    def save(self, counter: Counter) -> None:
        pass

    def get(self) -> Counter:
        with self._session_factory() as session:
            record = session.get(SqliteCounter, 1)
            if record is not None:
                return Counter(Count(record.count))

            new_record = SqliteCounter(id=1, count=0)
            session.add(new_record)
            session.commit()
            return Counter(Count(new_record.count))


def validate_relative_file_path_arg(relative_file_path: str):
    if not isinstance(relative_file_path, str):
        raise TypeError("`relative_file_path` arg must be of type `str`")

    if relative_file_path == "":
        raise ValueError("`relative_file_path` arg cannot be empty string")

    invalid_chars: list[str] = ["\\", ":", "*", "?", '"', "<", ">", "|"]
    for invalid_char in invalid_chars:
        if invalid_char in relative_file_path:
            raise ValueError(
                "`relative_file_path` arg cannot contain invalid character: "
                + invalid_char
            )

    if " " in relative_file_path:
        raise ValueError("`relative_file_path` arg cannot contain spaces")

    if not relative_file_path.endswith((".db", ".db3")):
        raise ValueError("`relative_file_path` arg must end with `.db` or `.db3`")

    if relative_file_path.startswith("/"):
        raise ValueError("`relative_file_path` arg cannot begin with `/`")


class Base(sa.orm.DeclarativeBase):
    pass


class SqliteCounter(Base):
    """SQL Alchemy ORM class for "counters" table"""

    __tablename__ = "counters"

    id: sa.orm.Mapped[int] = sa.orm.mapped_column(primary_key=True)
    count: sa.orm.Mapped[int]
