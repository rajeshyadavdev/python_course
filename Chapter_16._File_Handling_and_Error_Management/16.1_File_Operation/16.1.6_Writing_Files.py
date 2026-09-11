""" 
Writing means saving data into a file.

Syntax
  open("file_name", "w")

1. "w" means write mode.If the file does not exist, Python creates it.
2. If the file already exists, old content is removed.
3. New content is written from the beginning.

"""
with open(file="data.txt",mode="w",encoding="utf-8") as file:
  file.write("Welcome to python coding.")
  
''' 
This writes text into data.txt.
NOTE: Write mode overwrites old file content.
'''  