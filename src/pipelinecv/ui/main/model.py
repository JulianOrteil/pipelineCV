# -*- coding: utf-8 -*-

"""Manages the state data for the main window."""


from dataclasses import dataclass


__all__ = ['MainWindowModel']


@dataclass
class MainWindowModel:
    """Holds the window state and data settings."""
