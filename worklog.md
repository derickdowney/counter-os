# TODO
- Need to implement FileCounterRepository and add "COUNTER_NOT_FOUND" error
- Implement CounterHistoryPort in infrastructure using ORM database
- Need to implement an "optional service" into the CounterSetUseCase.
    - Give a feature to the web UI that the CLI doesn't have.
    - Use Sam Keen's "optional integration" on page 129


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

