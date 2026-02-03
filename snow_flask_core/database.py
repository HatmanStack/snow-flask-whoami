"""Database connection management for Snowflake."""

import logging
import os
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from snowflake import connector
from snowflake.connector import SnowflakeConnection
from snowflake.connector.errors import DatabaseError

logger = logging.getLogger(__name__)


class SnowflakeDB:
    """Manages Snowflake database connections with automatic reconnection."""

    _connection: SnowflakeConnection | None = None
    _key_file: str = "rsa_key.p8"

    @classmethod
    def set_key_file(cls, key_file: str) -> None:
        """Set the path to the private key file."""
        cls._key_file = key_file

    @classmethod
    def get_connection(cls) -> SnowflakeConnection:
        """Get or create a database connection."""
        if cls._connection is None:
            cls._connection = cls._create_connection()
        else:
            try:
                cls._connection.cursor().execute("SELECT 1").close()
            except DatabaseError:
                logger.warning("Connection stale, reconnecting")
                cls._connection = cls._create_connection()
        return cls._connection

    @classmethod
    def _create_connection(cls) -> SnowflakeConnection:
        """Create a new Snowflake connection."""
        return connector.connect(
            account=os.environ.get("SNOW_ACCOUNT"),
            user=os.environ.get("SNOW_USERNAME"),
            private_key_file=os.environ.get("SNOW_KEY_FILE", cls._key_file),
            private_key_file_pwd=os.environ.get("SNOW_PASSWORD"),
            warehouse="COMPUTE_WH",
            database="DEMO_DB",
            schema="PUBLIC",
            role="python_role",
            client_session_keep_alive=True,
        )

    @classmethod
    @contextmanager
    def cursor(cls) -> Iterator[Any]:
        """Context manager for database cursors."""
        cur = cls.get_connection().cursor()
        try:
            yield cur
        finally:
            cur.close()

    @classmethod
    def close(cls) -> None:
        """Close the database connection."""
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None


def get_db() -> type[SnowflakeDB]:
    """Get the database class for connection management."""
    return SnowflakeDB
