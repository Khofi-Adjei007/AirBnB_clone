#!/usr/bin/python3
"""Package Initialization"""
from models.engine.file_storage import FileStorage

# Instantiate the FileStorage class
storage = FileStorage()

# Load data using the reload method
storage.reload()
