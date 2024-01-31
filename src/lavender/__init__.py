from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, getLogger

from lavender.lavender import setup

__version__ = "${pyproject.tool.poetry.version}"
__version__ = "${pyproject.tool.poetry.authors.0}"

__all__ = ("setup", "CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING", "getLogger")
