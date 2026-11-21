import os
from dataclasses import dataclass

from dotenv import load_dotenv

from counter_os.infrastructure.persistence.repository_type import RepositoryType


@dataclass(frozen=True)
class ApplicationConfiguration:
    counter_repository_type: str

    @classmethod
    def from_environment(cls) -> ApplicationConfiguration:
        # Automatically load your .env file
        load_dotenv()

        return cls(
            counter_repository_type=os.getenv(
                "COUNTER_REPOSITORY_TYPE", RepositoryType.MEMORY
            )
        )
