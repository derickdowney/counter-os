class SqliteCounterRepository:
    _relative_file_path: str

    def __init__(self, relative_file_path: str):
        validate_relative_file_path_arg(relative_file_path)
        self._relative_file_path = relative_file_path


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

    if not relative_file_path.endswith(".db") and not relative_file_path.endswith(
        ".db3"
    ):
        raise ValueError("`relative_file_path` arg must end with `.db` or `.db3`")
