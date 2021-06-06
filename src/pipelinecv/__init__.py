# -*- coding: utf-8 -*-

"""Stupid simple OpenCV pipeline prototyping."""


import os
import sys
from multiprocessing import freeze_support

from loguru import logger
from PySide6.QtCore import Signal  # pylint: disable=no-name-in-module
from PySide6.QtWidgets import QApplication  # pylint: disable=no-name-in-module

sys.path.append(os.path.abspath("./src"))

from pipelinecv.utils import configure_logging  # pylint: disable=wrong-import-position


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

    def exec(self) -> int:
        """Run the application. Same as `exec_()`.

        Returns:
            errcode (`int`):
                The error code return from Qt's `QApplication.exec()`.
        """

        # Emit the start signal. This signal is responsible for starting
        # the background loading processes.
        logger.trace("Emitting start signal")
        self._start.emit()

        # Run the main event loop and return the errcode on application
        # exit
        logger.debug("Entering application event loop")
        return super().exec()

    def exec_(self) -> int:
        """Run the application. Same as `exec()`.

        Returns:
            errcode (`int`):
                The error code return from Qt's `QApplication.exec()`.
        """

        return self.exec()


@logger.catch
def main() -> int:
    """The entry point method of PipelineCV.

    Launches and runs the application.

    Returns:
        errcode (`int`):
            The error code return from Qt's `QApplication`.
    """

    # Required by some multiprocessing modules and objects. Per the
    # docs, this SHOULD ALWAYS be the first thing executed in the main
    # function.
    freeze_support()

    # Configure logging first
    configure_logging()

    # Metadata logging
    logger.info(f"Launching PipelineCV v{__version__}")
    logger.info('-' * 100)
    logger.info(f"Current working directory: {os.path.dirname(sys.argv[0])}")
    logger.info(f"Logging file: {getattr(logger, 'logfile', 'N/A')}")
    logger.info(f"Developed by: {__maintainer__}")
    logger.info(f'Release Type: {__status__}')
    logger.info('-' * 100)
    logger.info("PIPELINECV IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR")
    logger.info("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
    logger.info("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
    logger.info("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER")
    logger.info("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,")
    logger.info("OUT OF OR IN CONNECTION WITH PIPELINECV OR THE USE OR OTHER DEALINGS IN THE")
    logger.info("SOFTWARE.")
    logger.info('_' * 100)

    # Create the application object. This object is what handles all of
    # the window, core and supporting events and processes.
    app = Application()
    app.setApplicationDisplayName("PipelineCV")
    app.setApplicationName("PipelineCV")
    app.setApplicationVersion(__version__)

    return app.exec()
