class SqliteCounterRepository:
    _relative_file_path: str

    def __init__(self, relative_file_path: str):
        if not isinstance(relative_file_path, str):
            raise TypeError("`relative_file_path` arg must be of type `str`")

        if relative_file_path == "":
            raise ValueError("`relative_file_path` arg cannot be empty string")

        invalid_chars: list[str] = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
        for invalid_char in invalid_chars:
            if invalid_char in relative_file_path:
                raise ValueError(
                    "`relative_file_path` arg cannot contain invalid character: "
                    + invalid_char
                )

        stripped_path: str = relative_file_path.strip()

        if " " in stripped_path:
            raise ValueError("`relative_file_path` arg cannot contain spaces")

        self._relative_file_path = stripped_path
