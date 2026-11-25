class SqliteCounterRepository:
    _relative_file_path: str

    def __init__(self, relative_file_path: str):
        if not isinstance(relative_file_path, str):
            raise TypeError("`relative_file_path` arg must be of type `str`")
