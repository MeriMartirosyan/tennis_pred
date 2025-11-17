from dataclasses import dataclass
import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    """Application settings loaded from environment variables."""

    sportradar_api_key: str
    sportradar_base_url: str


def _get_env_variable(name: str, default: Optional[str] = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        raise ValueError(f"Environment variable '{name}' is not set")
    return value


def get_settings() -> Settings:
    """Load settings from environment variables.

    The function relies on a local `.env` file (if present) for convenience in development.
    """

    return Settings(
        sportradar_api_key=_get_env_variable("SPORTRADAR_API_KEY", ""),
        sportradar_base_url=_get_env_variable("SPORTRADAR_BASE_URL", ""),
    )


settings = get_settings()
