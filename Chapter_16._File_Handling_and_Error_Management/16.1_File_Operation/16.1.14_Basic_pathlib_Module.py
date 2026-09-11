""" 
pathlib is a modern way to work with file paths.

Syntax
  from pathlib import Path

1. pathlib works with paths as objects.It is cleaner than manually joining strings.
2. It is recommended for modern Python code.It works across operating systems.

Common pathlib Methods
======================
Code                  Meaning
----                  -------
Path("data.txt")      Creates path object
path.exists()         Checks if path exists
path.is_file()        Checks if path is file
path.is_dir()         Checks if path is folder
path.read_text()      Reads text file
path.write_text()     Writes text file
path.mkdir()          Creates folder
path.unlink()         Deletes file
"""