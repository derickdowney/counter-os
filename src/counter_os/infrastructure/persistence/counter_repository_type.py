from enum import StrEnum


class CounterRepositoryType(StrEnum):
    MEMORY = "memory"
    SQLITE_LOCAL = "sqlite_local"
    POSTGRES_LOCAL = "postgres_local"
