# -*- coding: utf-8 -*-

"""Processes user interactions and other display events from the app."""


from typing import Optional

from loguru import logger
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .model import MainWindowModel
from .view import MainWindowView


__all__ = ['MainWindow']


class MainWindow(MainWindowView, MainWindowModel):
    """The main window of the application.

    This is the primary window the user will interact with.
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        flags: Qt.WindowFlags = Qt.WindowFlags()
    ) -> None:
        logger.trace(f"Initializing {__name__}.{__class__.__name__}")
        super().__init__(parent=parent, flags=flags)
