"""Tests for input validation module."""

import sys
from pathlib import Path

# Add parent to path for direct module import
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

from snow_flask_core.validation import (
    MAX_ADDRESS_LENGTH,
    MAX_NAME_LENGTH,
    ValidationError,
    validate_address,
    validate_name,
)


class TestValidateName:
    """Tests for validate_name function."""

    def test_valid_name(self) -> None:
        """Valid name passes validation."""
        assert validate_name("John Doe") == "John Doe"

    def test_name_with_special_chars(self) -> None:
        """Name with allowed special characters passes."""
        assert validate_name("O'Brien-Smith") == "O'Brien-Smith"

    def test_name_strips_whitespace(self) -> None:
        """Leading/trailing whitespace is stripped."""
        assert validate_name("  John  ") == "John"

    def test_empty_name_raises(self) -> None:
        """Empty name raises ValidationError."""
        with pytest.raises(ValidationError, match="Name is required"):
            validate_name("")

    def test_none_name_raises(self) -> None:
        """None name raises ValidationError."""
        with pytest.raises(ValidationError, match="Name is required"):
            validate_name(None)

    def test_whitespace_only_raises(self) -> None:
        """Whitespace-only name raises ValidationError."""
        with pytest.raises(ValidationError, match="Name is required"):
            validate_name("   ")

    def test_name_too_long_raises(self) -> None:
        """Name exceeding max length raises ValidationError."""
        long_name = "a" * (MAX_NAME_LENGTH + 1)
        with pytest.raises(ValidationError, match="characters or less"):
            validate_name(long_name)

    def test_name_at_max_length(self) -> None:
        """Name at exactly max length passes."""
        max_name = "a" * MAX_NAME_LENGTH
        assert validate_name(max_name) == max_name

    def test_invalid_characters_raises(self) -> None:
        """Name with invalid characters raises ValidationError."""
        with pytest.raises(ValidationError, match="invalid characters"):
            validate_name("John<script>")

    def test_sql_injection_blocked(self) -> None:
        """SQL injection attempt is blocked."""
        with pytest.raises(ValidationError, match="invalid characters"):
            validate_name("Robert'); DROP TABLE ADDRESSES;--")


class TestValidateAddress:
    """Tests for validate_address function."""

    def test_valid_address(self) -> None:
        """Valid address passes validation."""
        assert validate_address("123 Main St") == "123 Main St"

    def test_address_strips_whitespace(self) -> None:
        """Leading/trailing whitespace is stripped."""
        assert validate_address("  123 Main  ") == "123 Main"

    def test_empty_address_raises(self) -> None:
        """Empty address raises ValidationError."""
        with pytest.raises(ValidationError, match="Address is required"):
            validate_address("")

    def test_none_address_raises(self) -> None:
        """None address raises ValidationError."""
        with pytest.raises(ValidationError, match="Address is required"):
            validate_address(None)

    def test_address_too_long_raises(self) -> None:
        """Address exceeding max length raises ValidationError."""
        long_address = "a" * (MAX_ADDRESS_LENGTH + 1)
        with pytest.raises(ValidationError, match="characters or less"):
            validate_address(long_address)

    def test_address_at_max_length(self) -> None:
        """Address at exactly max length passes."""
        max_address = "a" * MAX_ADDRESS_LENGTH
        assert validate_address(max_address) == max_address
