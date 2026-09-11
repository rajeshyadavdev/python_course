""" 
Error                 Meaning
=====                 =======
FileNotFoundError     File does not exist
PermissionError       No permission
IsADirectoryError     Expected file but got folder
UnicodeDecodeError    Encoding issue
OSError               General operating system error
"""
try:
  with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
except FileNotFoundError:
  print("File not found")
else:
  print(content) # Welcome to python coding