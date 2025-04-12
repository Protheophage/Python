"""
File_Manipulation Package

This package provides utilities for performing various file operations, including:
- Finding files
- Removing files
- Counting files
- Searching files by content
- Changing file extensions

Modules:
- Find_Files: Provides functions to search for files based on patterns.
- Remove_Files: Allows deletion of files matching specific criteria.
- Get_FilesCount: Counts files matching specific patterns.
- Find_FilesByContent: Searches for files containing specific content.
- Set_FilesExtension: Changes the extensions of files.

Each module can be used independently or as part of the package.
"""

from .Find_Files import find_files
from .Remove_Files import remove_files
from .Get_FilesCount import get_filescount
from .Find_FilesByContent import find_filesbycontent
from .Set_FilesExtension import set_filesextension
