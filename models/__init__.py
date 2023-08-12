#!/usr/bin/python3
"""__init__ method for this directory to package or
Module for FileStorage autoinit."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
