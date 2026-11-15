# TODO
- Need to implement FileCounterRepository and add "COUNTER_NOT_FOUND" error


# Project Setup Worklog
- Ran `uv init counter-os`
- Ran `source .venv/bin/activate`
- Ran `uv add pytest fastapi typer pytest-random-order pytest-xdist flask`
- Updated `pyproject.toml`description and added this to bottom:
```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
addopts = "--random-order -n auto"
```
-

