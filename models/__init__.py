#!/usr/bin/python3
"""models package for storing objects"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
