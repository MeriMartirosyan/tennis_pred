"""Core package for the Tennis Results Dashboard."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("tennis-results-dashboard")
except PackageNotFoundError:  # pragma: no cover - during local execution without install
    __version__ = "0.0.0"

__all__ = ["__version__"]
