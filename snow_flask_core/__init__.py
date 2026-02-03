"""Snow Flask Core - shared functionality for snow-flask-whoami."""


def __getattr__(name: str):
    """Lazy import to avoid requiring all dependencies at import time."""
    if name == "create_app":
        from snow_flask_core.app import create_app

        return create_app
    if name == "get_db":
        from snow_flask_core.database import get_db

        return get_db
    if name == "SnowflakeDB":
        from snow_flask_core.database import SnowflakeDB

        return SnowflakeDB
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["create_app", "get_db", "SnowflakeDB"]
