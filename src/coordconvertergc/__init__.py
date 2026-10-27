# read version from installed package
from importlib.metadata import version
__version__ = version("coordconvertergc")
from .coordconvertergc import to_decimal, to_degree