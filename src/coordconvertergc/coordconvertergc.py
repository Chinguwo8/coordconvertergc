def to_decimal(latitude, longitude):
    """
    Convert latitude and longitude from degrees, minutes, and seconds
    (DMS) to decimal degrees.

    Parameters
    ----------
    latitude : tuple
        Latitude as (degrees, minutes, seconds, direction).
        Direction must be N or S.
    longitude : tuple
        Longitude as (degrees, minutes, seconds, direction).
        Direction must be E or W.

    Returns
    -------
    tuple
        A pair containing (latitude, longitude) in decimal degrees.
        South and west coordinates are negative.

    Raises
    ------
    ValueError
        If the coordinate format, values, or direction is invalid.

    Examples
    --------
    >>> to_decimal((15, 47, 0, "S"), (35, 0, 0, "E"))
    (-15.783333333333333, 35.0)
    """

    def validate_coordinate(coordinate, coordinate_type):
        if not isinstance(coordinate, (tuple, list)) or len(coordinate) != 4:
            raise ValueError(
                "Coordinate must contain (degrees, minutes, seconds, direction)."
            )

        degrees, minutes, seconds, direction = coordinate

        if any(
            isinstance(value, bool) or not isinstance(value, (int, float))
            for value in (degrees, minutes, seconds)
        ):
            raise ValueError("Degrees, minutes, and seconds must be numeric.")

        if not all(
            value == value and abs(value) != float("inf")
            for value in (degrees, minutes, seconds)
        ):
            raise ValueError("Coordinate values must be finite numbers.")

        if degrees < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Degrees, minutes, and seconds cannot be negative.")

        if minutes >= 60 or seconds >= 60:
            raise ValueError("Minutes and seconds must be less than 60.")

        direction = direction.upper() if isinstance(direction, str) else ""

        if coordinate_type == "latitude":
            if direction not in ("N", "S"):
                raise ValueError("Latitude direction must be N or S.")
            maximum = 90
        else:
            if direction not in ("E", "W"):
                raise ValueError("Longitude direction must be E or W.")
            maximum = 180

        if degrees > maximum or (
            degrees == maximum and (minutes != 0 or seconds != 0)
        ):
            raise ValueError(
                f"{coordinate_type.title()} cannot exceed {maximum} degrees."
            )

        return degrees, minutes, seconds, direction

    lat_deg, lat_min, lat_sec, lat_dir = validate_coordinate(
        latitude, "latitude"
    )
    lon_deg, lon_min, lon_sec, lon_dir = validate_coordinate(
        longitude, "longitude"
    )

    lat_decimal = lat_deg + (lat_min / 60) + (lat_sec / 3600)
    lon_decimal = lon_deg + (lon_min / 60) + (lon_sec / 3600)

    if lat_dir == "S":
        lat_decimal = -lat_decimal

    if lon_dir == "W":
        lon_decimal = -lon_decimal

    return lat_decimal, lon_decimal


def to_degree(latitude, longitude):
    """
    Convert decimal-degree latitude and longitude to DMS coordinates.

    Parameters
    ----------
    latitude : int or float
        Latitude in decimal degrees, from -90 to 90.
    longitude : int or float
        Longitude in decimal degrees, from -180 to 180.

    Returns
    -------
    tuple
        Two tuples in the format (degrees, minutes, seconds, direction).

    Raises
    ------
    ValueError
        If coordinates are not finite numbers or are outside valid ranges.

    Examples
    --------
    >>> to_degree(-15.783333333333333, 35.0)
    ((15, 47, 0.0, 'S'), (35, 0, 0.0, 'E'))
    """

    for value, name, maximum in (
        (latitude, "Latitude", 90),
        (longitude, "Longitude", 180),
    ):
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or value != value
            or abs(value) == float("inf")
        ):
            raise ValueError(f"{name} must be a finite number.")

        if not -maximum <= value <= maximum:
            raise ValueError(f"{name} must be between {-maximum} and {maximum}.")

    lat_direction = "N" if latitude >= 0 else "S"
    lon_direction = "E" if longitude >= 0 else "W"

    latitude = abs(latitude)
    longitude = abs(longitude)

    def decimal_to_dms(value, direction):
        degrees = int(value)
        minutes_full = (value - degrees) * 60
        minutes = int(minutes_full)
        seconds = round((minutes_full - minutes) * 60, 6)

        # Correct rounding that reaches 60 seconds or minutes.
        if seconds >= 60:
            seconds = 0.0
            minutes += 1

        if minutes >= 60:
            minutes = 0
            degrees += 1

        return degrees, minutes, seconds, direction

    return (
        decimal_to_dms(latitude, lat_direction),
        decimal_to_dms(longitude, lon_direction),
    )

