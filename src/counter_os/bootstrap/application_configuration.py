import os
from dataclasses import dataclass

from dotenv import load_dotenv

from counter_os.infrastructure.persistence.repository_type import RepositoryType


@dataclass(frozen=True)
class ApplicationConfiguration:
    counter_repository_type: str
    counter_repository_location_sqlite_local: str
    counter_repository_location_postgres_local: str

    @classmethod
    def from_environment(cls) -> ApplicationConfiguration:
        # Automatically load your .env file
        load_dotenv()

        return cls(
            counter_repository_type=os.getenv(
                "COUNTER_REPOSITORY_TYPE", RepositoryType.MEMORY
            ),
            counter_repository_location_sqlite_local=os.getenv(
                "COUNTER_REPOSITORY_LOCATION_SQLITE_LOCAL", "data.sqlite3"
            ),
            counter_repository_location_postgres_local=os.getenv(
                "COUNTER_REPOSITORY_LOCATION_POSTGRES_LOCAL",
                "user:password@localhost:5432/counter_os",
            ),
        )
