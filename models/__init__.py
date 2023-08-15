#!/usr/bin/python3

"""Entry point for package initialization."""

from models.engine.file_storage import FileStorage

# Initialize the FileStorage instance for data management
storage = FileStorage()

# Reload data from storage to populate the instance
storage.reload()i
