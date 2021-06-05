# -*- coding: utf-8 -*-

"""Stupid simple OpenCV pipeline prototyping."""


import os
import sys
from multiprocessing import freeze_support
from typing import NoReturn

from loguru import logger
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication

sys.path.append(os.path.abspath("./src"))


__all__ = ['main']

__author__ = "Julian_Orteil"
__copyright__ = "Copyright 2021, The PipelineCV Project"
__license__ = "MIT"
__version__ = "0.0.1-dev"
__maintainer__ = "Julian_Orteil"
__status__ = "Development"


class Application(QApplication):
    """The application object of PipelineCV.

    Executes all window, core and other processing events.
    """

    _start = Signal()

    def exec(self) -> NoReturn:
        raise NotImplementedError("use the start() method instead")

    def exec_(self) -> NoReturn:
        raise NotImplementedError("use the start() method instead")

    def start(self) -> int:
        """Start the application.

        Returns:
            errcode (`int`):
                The error code return from Qt's `QApplication.exec()`.
        """

        # Emit the start signal. This signal is responsible for starting
        # the background loading processes.
        self._start.emit()

        # Run the main event loop and return the errcode on application
        # exit
        return super().exec()


@logger.catch
def main() -> int:
    """The entry point method of PipelineCV.

    Launches and runs the application.

    Returns:
        errcode (`int`):
            The error code return from Qt's `QApplication`.
    """

    # Required by some multiprocessing modules and objects
    freeze_support()

    # Create the application object. This object is what handles all of
    # the window, core and supporting events and processes.
    app = Application()
    app.setApplicationDisplayName("PipelineCV")
    app.setApplicationName("PipelineCV")
    app.setApplicationVersion(__version__)

    return app.start()
