import pytest

from coordconvertergc import to_decimal, to_degree


def test_to_decimal():
    """Test conversion from DMS to decimal degrees."""
    result = to_decimal((15, 47, 0, "S"), (35, 0, 0, "E"))

    assert result == pytest.approx((-15.783333333333333, 35.0))


def test_to_degree():
    """Test conversion from decimal degrees to DMS."""
    result = to_degree(-15.783333333333333, 35.0)

    assert result == (
        (15, 47, 0.0, "S"),
        (35, 0, 0.0, "E"),
    )


def test_invalid_latitude():
    """Check that latitude outside the valid range raises an error."""
    with pytest.raises(ValueError):
        to_degree(95, 35)


def test_invalid_longitude():
    """Check that longitude outside the valid range raises an error."""
    with pytest.raises(ValueError):
        to_degree(15, 200)


def test_invalid_dms_minutes():
    """Check that DMS minutes of 60 are rejected."""
    with pytest.raises(ValueError):
        to_decimal((15, 60, 0, "S"), (35, 0, 0, "E"))


def test_invalid_direction():
    """Check that an invalid latitude direction is rejected."""
    with pytest.raises(ValueError):
        to_decimal((15, 47, 0, "W"), (35, 0, 0, "E"))

