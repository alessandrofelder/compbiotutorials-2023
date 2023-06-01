from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("compbiotutorials-2023")
except PackageNotFoundError:
    # package is not installed
    pass
