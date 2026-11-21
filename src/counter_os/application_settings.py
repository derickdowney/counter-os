import os
from dataclasses import dataclass

from dotenv import load_dotenv

from counter_os.infrastructure.persistence.repository_type import RepositoryType


@dataclass(frozen=True)
class ApplicationSettings:
    counter_repository_type: str

    @classmethod
    def from_environment(cls) -> ApplicationSettings:
        # Automatically load your .env file
        load_dotenv()

        return cls(
            counter_repository_type=os.getenv(
                "COUNTER_REPOSITORY_TYPE", RepositoryType.MEMORY
            )
        )
