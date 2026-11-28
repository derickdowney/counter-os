import os
from dataclasses import dataclass

from dotenv import load_dotenv

from counter_os.bootstrap.application_environment_type import ApplicationEnvironmentType
from counter_os.infrastructure.frontend_type import FrontendType
from counter_os.infrastructure.persistence.counter_repository_type import (
    CounterRepositoryType,
)


@dataclass(frozen=True)
class ApplicationConfiguration:
    counter_repository_type: str
    counter_repository_location_sqlite_local: str
    counter_repository_location_postgres_local: str
    frontend_type: str
    app_env: str

    @classmethod
    def from_environment(
        cls,
        *,
        frontend_override: str | None = None,
        counter_repository_type_override: str | None = None,
    ) -> ApplicationConfiguration:
        # Automatically load your .env file
        load_dotenv()

        counter_repository_type: str
        if counter_repository_type_override is not None:
            counter_repository_type = counter_repository_type_override
        else:
            counter_repository_type = os.getenv(
                "COUNTER_REPOSITORY_TYPE", CounterRepositoryType.MEMORY
            )

        frontend: str
        if frontend_override is not None:
            frontend = frontend_override
        else:
            frontend = os.getenv("FRONTEND_TYPE", FrontendType.CLI)

        return cls(
            counter_repository_type=counter_repository_type,
            counter_repository_location_sqlite_local=os.getenv(
                "COUNTER_REPOSITORY_LOCATION_SQLITE_LOCAL", "data.sqlite3"
            ),
            counter_repository_location_postgres_local=os.getenv(
                "COUNTER_REPOSITORY_LOCATION_POSTGRES_LOCAL",
                "user:password@localhost:5432/counter_os",
            ),
            frontend_type=frontend,
            app_env=os.getenv("APP_ENV", ApplicationEnvironmentType.DEVELOPMENT),
        )
