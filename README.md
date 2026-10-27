# coordconvertergc

A Python package for converting geographic coordinates between degrees, minutes, seconds and decimal degrees.

Created by Gracious Chinguwo

## Installation
Install the package from PyPi using: 
pip install coordconvertergc

## Usage
1. Convert DMS to decimal degrees
Use to_decimal() to convert latitude and longitude from DMS to decimal degrees. Southern and western coordinates are returned as negative values.

from coordconvertergc import to_decimal
latitude = (15, 47, 0, "S")
longitude = (35, 0, 0, "E")

result = to_decimal(latitude, longitude)
print(result)

Output:
(-15.783333333333333, 35.0)

2. Convert decimal degrees to DMS
Use to_degree() to convert decimal-degree latitude and longitude to DMS coordinates.

from coordconvertergc import to_degree
latitude = -15.783333333333333
longitude = 35.0

result = to_degree(latitude, longitude)
print(result)

output:
((15, 47, 0.0, 'S'), (35, 0, 0.0, 'E'))

## Input Validation 
The functions validate coordinate ranges, DMS values, and compass directions. Invalid inputs raise a ValueError with an explanatory message.

Example 1: Invalid latitude

to_degree(95, 35)

This raises a ValueError because latitude must be between -90 and 90 degrees.

Example 2: Invalid longitude

to_degree(15, 200)

This raises a ValueError because longitude must be between -180 and 180 degrees.

These checks help ensure that only geographically valid coordinates are converted.

## Contributing

Contributions are welcome. Please read the contributing guidelines and code of conduct before contributing. 

## License

This project is licensed under the MIT License. See the LICENSE file for details. 

## Project links
- GitHub repository: Add your repository URL after publishing the code.

- PyPI package: https://pypi.org/project/coordconvertergc/

## Credits
This package was created using Cookiecutter and the py-pkgs-cookiecutter template
