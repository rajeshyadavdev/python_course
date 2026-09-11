""" 
A file is opened using the open() function.

Syntax
  file = open("file_name", "mode")

With encoding:
  file = open("file_name", "mode", encoding="utf-8")

Explanation
1. open() opens a file.
2. The first argument is the file name or path.
3. The second argument is the file mode.
4. Encoding is commonly used for text files.
5. utf-8 is a common and recommended enco
"""
file = open("data.txt", "r", encoding="utf-8")
# This opens data.txt in read mode.
