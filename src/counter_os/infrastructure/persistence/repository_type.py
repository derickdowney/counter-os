from enum import StrEnum


class RepositoryType(StrEnum):
    MEMORY = "memory"
    SQLITE_LOCAL = "sqlite_local"
