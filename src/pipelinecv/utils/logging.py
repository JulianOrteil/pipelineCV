# -*- coding: utf-8 -*-

"""Setup and other helper functions for logging."""


from datetime import datetime
import os
import sys

from loguru import logger

from . import configurations


__all__ = ['configure_logging']


class Filter:
    """Filters logs on dynamically changing logging levels.

    Args:
        level (`str`):
            The name of a logging level. Look to loguru's
            `Logger.filter` function for more info.
    """

    _level: str

    def __init__(self, level: str = 'INFO') -> None:
        super().__init__()

        self._level = logger.level(level).no

    def __call__(self, record: dict) -> bool:
        return record["level"].no >= self._level


def configure_logging() -> None:
    """Configures the logger for the application.

    Edit the configuration files to change the behavior of the logger.
    """

    # Remove any default or existing handlers
    logger.remove()

    # Add the new handlers according to the configurations set by the
    # user
    if configurations.LoggingConfig.stderr.enabled:
        logger.add(
            sys.stderr,
            filter=Filter(configurations.LoggingConfig.stderr.level),
            enqueue=True  # Automatically enable support for threads and processes
        )
    if configurations.LoggingConfig.file.enabled:
        root = configurations.LoggingConfig.root
        filename = "{:%Y-%m-%d_%H-%M-%S_%f}.log".format(datetime.now())
        filepath = os.path.join(configurations.LoggingConfig.file.location, filename)
        filepath = filepath.replace(
            r'{root}',
            os.environ.get(root, 'TEMP') if not os.path.isabs(root) else root
        )
        logger.add(
            filepath,
            filter=Filter(configurations.LoggingConfig.file.level),
            enqueue=True  # Automatically enable support for threads and processes
        )
        setattr(logger, 'logfile', filepath)
