# -*- coding: utf-8 -*-

"""Manages the main window display objects."""


from typing import Optional
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QMainWindow, QWidget

from .builder import Ui_MainWindow


__all__ = ['MainWindowView']


class MainWindowView(QMainWindow, Ui_MainWindow):
    """Builds and displays the main window for the application."""

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        flags: Qt.WindowFlags = Qt.WindowFlags()
    ) -> None:
        super().__init__(parent=parent, flags=flags)

        self.setupUi(self)