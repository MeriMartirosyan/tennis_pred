## Tennis Results Dashboard

This project provides the scaffolding for a Tennis Results Dashboard, including:

- A `src/` directory containing the Python package and CLI entrypoint.
- A `tests/` folder pre-wired for `pytest`.
- A `config/` directory to hold runtime configuration (see `config/settings.toml`).
- Tooling for linting (`ruff`) and formatting (`black`).

### Getting started

```bash
pip install -e .[dev]
```

Run the hello-world CLI:

```bash
python -m tennis_results_dashboard
# or
tennis-results-dashboard
```

Code quality helpers:

```bash
ruff check .
black .
pytest
```
